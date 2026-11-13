// Mini golf on the 404 page: "Hole 404, par 3".
// Drag back from anywhere on the green to aim, release to putt.
// Keyboard: Left/Right to aim, Up/Down for power, Space or Enter to putt.
// Physics run in course units (800 × 400); on narrow screens the green is drawn
// rotated so it's tall instead of wide. Without JavaScript the game stays hidden
// and the page's links do the job.
(function () {
  var root = document.querySelector(".golf");
  if (!root || !root.querySelector("canvas").getContext) return;
  root.hidden = false;

  var canvas = root.querySelector("canvas");
  var ctx = canvas.getContext("2d");
  var strokesEl = root.querySelector(".golf-strokes");
  var powerEl = root.querySelector(".golf-power");
  var statusEl = root.querySelector(".golf-status");
  var resetBtn = root.querySelector(".golf-reset");

  var W = 800, H = 400, PAR = 3;
  var TEE = { x: 100, y: 300 };
  var HOLE = { x: 690, y: 110, r: 13 };
  var BALL_R = 7;
  var WALLS = [{ x: 400, y: 130, w: 22, h: 270 }];
  var SAND = [{ x: 545, y: 175, w: 95, h: 85, r: 34 }];
  var MAX_SPEED = 1150, MAX_DRAG = 170;

  var css = getComputedStyle(document.documentElement);
  var ACCENT = css.getPropertyValue("--accent").trim() || "#8FB4FF";

  var ball, strokes, sunk, aimAngle, aimPower, dragging, dragStart, showAim, sinkAnim;
  var layout = { portrait: false, s: 1, w: 0, h: 0 };

  function reset() {
    ball = { x: TEE.x, y: TEE.y, vx: 0, vy: 0 };
    strokes = 0; sunk = false; sinkAnim = 0;
    aimAngle = Math.atan2(HOLE.y - TEE.y, HOLE.x - TEE.x) - 0.35;
    aimPower = 0.55; dragging = false; showAim = false;
    strokesEl.textContent = "Strokes: 0";
    updatePower();
    statusEl.textContent = "";
  }

  function resize() {
    var w = root.querySelector(".golf-green").clientWidth;
    layout.portrait = w < 560;
    layout.s = layout.portrait ? w / H : w / W;
    if (layout.portrait) {
      // keep the tall green to about two-thirds of the screen so there's always room to scroll past it
      var maxH = Math.max(420, window.innerHeight * 0.66);
      layout.s = Math.min(layout.s, maxH / W);
      w = H * layout.s;
    }
    canvas.style.width = w + "px";
    layout.w = w;
    layout.h = layout.portrait ? W * layout.s : H * layout.s;
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.style.height = layout.h + "px";
    canvas.width = Math.round(w * dpr);
    canvas.height = Math.round(layout.h * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    draw();
  }

  // course units → screen pixels, and back
  function toScreen(x, y) {
    return layout.portrait ? { x: y * layout.s, y: layout.h - x * layout.s } : { x: x * layout.s, y: y * layout.s };
  }
  function toCourse(px, py) {
    return layout.portrait ? { x: (layout.h - py) / layout.s, y: px / layout.s } : { x: px / layout.s, y: py / layout.s };
  }
  function courseTransform() {
    var dpr = canvas.width / layout.w;
    if (layout.portrait) ctx.setTransform(0, -layout.s * dpr, layout.s * dpr, 0, 0, layout.h * dpr);
    else ctx.setTransform(layout.s * dpr, 0, 0, layout.s * dpr, 0, 0);
  }
  function screenTransform() { var dpr = canvas.width / layout.w; ctx.setTransform(dpr, 0, 0, dpr, 0, 0); }

  function roundRect(x, y, w, h, r) {
    ctx.beginPath();
    ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r);
    ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath();
  }

  function draw() {
    ctx.save();
    screenTransform();
    ctx.clearRect(0, 0, layout.w, layout.h);
    courseTransform();
    // green with mowing stripes
    roundRect(0, 0, W, H, 26); ctx.fillStyle = "#1B3A28"; ctx.fill();
    ctx.save(); ctx.clip();
    for (var i = 0; i < W; i += 80) { ctx.fillStyle = "rgba(255,255,255,0.03)"; ctx.fillRect(i, 0, 40, H); }
    ctx.restore();
    roundRect(1, 1, W - 2, H - 2, 25); ctx.strokeStyle = "rgba(255,255,255,0.10)"; ctx.lineWidth = 2; ctx.stroke();
    // sand
    SAND.forEach(function (s) {
      roundRect(s.x, s.y, s.w, s.h, s.r); ctx.fillStyle = "#5A4E36"; ctx.fill();
      ctx.fillStyle = "rgba(255,255,255,0.10)";
      for (var k = 0; k < 26; k++) { ctx.fillRect(s.x + 12 + ((k * 37) % (s.w - 24)), s.y + 10 + ((k * 23) % (s.h - 20)), 2, 2); }
    });
    // wall
    WALLS.forEach(function (w) {
      roundRect(w.x, w.y, w.w, w.h, 6); ctx.fillStyle = "#2E3035"; ctx.fill();
      ctx.strokeStyle = "rgba(255,255,255,0.12)"; ctx.lineWidth = 2; ctx.stroke();
    });
    // tee
    ctx.fillStyle = "rgba(255,255,255,0.35)";
    [[-14, -14], [-14, 14]].forEach(function (d) { ctx.beginPath(); ctx.arc(TEE.x + d[0], TEE.y + d[1], 3, 0, Math.PI * 2); ctx.fill(); });
    // hole
    ctx.beginPath(); ctx.arc(HOLE.x, HOLE.y, HOLE.r + 3, 0, Math.PI * 2); ctx.fillStyle = "rgba(255,255,255,0.08)"; ctx.fill();
    ctx.beginPath(); ctx.arc(HOLE.x, HOLE.y, HOLE.r, 0, Math.PI * 2); ctx.fillStyle = "#07080A"; ctx.fill();
    // aim line
    if (!sunk && atRest() && (showAim || dragging)) {
      var len = 30 + aimPower * 150;
      var ex = ball.x + Math.cos(aimAngle) * len, ey = ball.y + Math.sin(aimAngle) * len;
      ctx.setLineDash([8, 8]); ctx.lineWidth = 3; ctx.strokeStyle = ACCENT;
      ctx.beginPath(); ctx.moveTo(ball.x, ball.y); ctx.lineTo(ex, ey); ctx.stroke(); ctx.setLineDash([]);
      ctx.beginPath(); ctx.arc(ex, ey, 5, 0, Math.PI * 2); ctx.fillStyle = ACCENT; ctx.fill();
    }
    // ball
    var r = BALL_R * (sunk ? Math.max(0, 1 - sinkAnim) : 1);
    if (r > 0.3) {
      ctx.beginPath(); ctx.arc(ball.x + 2, ball.y + 3, r, 0, Math.PI * 2); ctx.fillStyle = "rgba(0,0,0,0.35)"; ctx.fill();
      ctx.beginPath(); ctx.arc(ball.x, ball.y, r, 0, Math.PI * 2); ctx.fillStyle = "#F4F4F5"; ctx.fill();
    }
    // flag, drawn upright in screen space
    screenTransform();
    var h = toScreen(HOLE.x, HOLE.y), pole = Math.max(34, 64 * layout.s);
    ctx.strokeStyle = "#EDEDEE"; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(h.x, h.y); ctx.lineTo(h.x, h.y - pole); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(h.x, h.y - pole); ctx.lineTo(h.x + pole * 0.5, h.y - pole * 0.82); ctx.lineTo(h.x, h.y - pole * 0.64); ctx.closePath();
    ctx.fillStyle = ACCENT; ctx.fill();
    // result
    if (sunk && sinkAnim >= 1) {
      ctx.fillStyle = "rgba(15,16,18,0.72)"; ctx.fillRect(0, 0, layout.w, layout.h);
      ctx.fillStyle = "#EDEDEE"; ctx.textAlign = "center";
      ctx.font = "500 " + Math.round(Math.min(44, layout.w / 9)) + "px 'IBM Plex Sans', system-ui, sans-serif";
      ctx.fillText(scoreName(strokes), layout.w / 2, layout.h / 2 - 6);
      ctx.fillStyle = "#A6A8AD"; ctx.font = "400 16px 'IBM Plex Sans', system-ui, sans-serif";
      ctx.fillText(strokes + (strokes === 1 ? " stroke" : " strokes") + " on a par " + PAR, layout.w / 2, layout.h / 2 + 26);
    }
    ctx.restore();
  }

  function scoreName(n) {
    return n === 1 ? "Hole in one!" : ({ "-1": "Birdie!", "-2": "Eagle!", "0": "Par.", "1": "Bogey.", "2": "Double bogey." })[n - PAR] || "In the hole.";
  }
  function atRest() { return Math.abs(ball.vx) + Math.abs(ball.vy) === 0; }
  function inside(p, r) { return p.x >= r.x && p.x <= r.x + r.w && p.y >= r.y && p.y <= r.y + r.h; }
  function updatePower() { powerEl.textContent = "Power " + Math.round(aimPower * 100) + "%"; }

  function putt() {
    if (sunk || !atRest() || aimPower < 0.04) return;
    var sp = aimPower * MAX_SPEED;
    ball.vx = Math.cos(aimAngle) * sp; ball.vy = Math.sin(aimAngle) * sp;
    strokes++; strokesEl.textContent = "Strokes: " + strokes;
    statusEl.textContent = "Stroke " + strokes + ".";
    loop();
  }

  var last = 0, running = false;
  function loop() { if (!running) { running = true; last = performance.now(); requestAnimationFrame(tick); } }
  function tick(now) {
    var dt = Math.min(0.05, (now - last) / 1000); last = now;
    var steps = 4, h = dt / steps;
    for (var i = 0; i < steps && !sunk; i++) step(h);
    if (sunk && sinkAnim < 1) sinkAnim = Math.min(1, sinkAnim + dt * 4);
    draw();
    if ((!atRest() && !sunk) || (sunk && sinkAnim < 1)) requestAnimationFrame(tick);
    else {
      running = false;
      if (sunk) statusEl.textContent = scoreName(strokes) + " " + strokes + (strokes === 1 ? " stroke" : " strokes") + ". Use the links above to get back to the site, or play again.";
    }
  }

  function step(h) {
    var inSand = SAND.some(function (s) { return inside(ball, s); });
    var k = inSand ? 4.5 : 1.15;
    var f = Math.exp(-k * h);
    ball.vx *= f; ball.vy *= f;
    var sp = Math.hypot(ball.vx, ball.vy);
    if (sp > 0) { var dec = Math.min(sp, 45 * h); ball.vx -= ball.vx / sp * dec; ball.vy -= ball.vy / sp * dec; }
    if (Math.hypot(ball.vx, ball.vy) < 10) { ball.vx = 0; ball.vy = 0; }
    ball.x += ball.vx * h; ball.y += ball.vy * h;
    // edges of the green
    var e = 0.62;
    if (ball.x < BALL_R) { ball.x = BALL_R; ball.vx = Math.abs(ball.vx) * e; }
    if (ball.x > W - BALL_R) { ball.x = W - BALL_R; ball.vx = -Math.abs(ball.vx) * e; }
    if (ball.y < BALL_R) { ball.y = BALL_R; ball.vy = Math.abs(ball.vy) * e; }
    if (ball.y > H - BALL_R) { ball.y = H - BALL_R; ball.vy = -Math.abs(ball.vy) * e; }
    // walls
    WALLS.forEach(function (w) {
      var cx = Math.max(w.x, Math.min(ball.x, w.x + w.w)), cy = Math.max(w.y, Math.min(ball.y, w.y + w.h));
      var dx = ball.x - cx, dy = ball.y - cy, d = Math.hypot(dx, dy);
      if (d < BALL_R) {
        var nx, ny;
        if (d === 0) { nx = ball.vx > 0 ? -1 : 1; ny = 0; } else { nx = dx / d; ny = dy / d; }
        ball.x = cx + nx * BALL_R; ball.y = cy + ny * BALL_R;
        var vn = ball.vx * nx + ball.vy * ny;
        if (vn < 0) { ball.vx -= (1 + e) * vn * nx; ball.vy -= (1 + e) * vn * ny; }
      }
    });
    // the cup: drops in if it's slow enough, lips out a little if it's not
    var hd = Math.hypot(ball.x - HOLE.x, ball.y - HOLE.y), speed = Math.hypot(ball.vx, ball.vy);
    if (hd < HOLE.r) {
      if (speed < 430) { sunk = true; ball.x = HOLE.x; ball.y = HOLE.y; ball.vx = ball.vy = 0; }
      else { ball.vx *= 0.9; ball.vy *= 0.9; }
    }
  }

  // pointer: drag back from anywhere, like pulling a putter back
  canvas.addEventListener("pointerdown", function (e) {
    if (sunk || !atRest()) return;
    canvas.setPointerCapture(e.pointerId);
    var r = canvas.getBoundingClientRect();
    dragStart = toCourse(e.clientX - r.left, e.clientY - r.top);
    dragging = true;
  });
  canvas.addEventListener("pointermove", function (e) {
    if (!dragging) return;
    var r = canvas.getBoundingClientRect(), p = toCourse(e.clientX - r.left, e.clientY - r.top);
    var dx = dragStart.x - p.x, dy = dragStart.y - p.y, d = Math.hypot(dx, dy);
    if (d > 4) { aimAngle = Math.atan2(dy, dx); aimPower = Math.min(1, d / MAX_DRAG); updatePower(); }
    draw();
  });
  function endDrag() { if (!dragging) return; dragging = false; putt(); draw(); }
  canvas.addEventListener("pointerup", endDrag);
  canvas.addEventListener("pointercancel", function () { dragging = false; draw(); });

  // keyboard
  canvas.addEventListener("focus", function () { showAim = true; draw(); });
  canvas.addEventListener("blur", function () { showAim = false; draw(); });
  canvas.addEventListener("keydown", function (e) {
    var handled = true;
    if (e.key === "ArrowLeft") aimAngle -= Math.PI / 36;
    else if (e.key === "ArrowRight") aimAngle += Math.PI / 36;
    else if (e.key === "ArrowUp") aimPower = Math.min(1, aimPower + 0.05);
    else if (e.key === "ArrowDown") aimPower = Math.max(0.05, aimPower - 0.05);
    else if (e.key === " " || e.key === "Enter") putt();
    else handled = false;
    if (handled) { e.preventDefault(); updatePower(); draw(); }
  });
  resetBtn.addEventListener("click", function () { reset(); draw(); canvas.focus(); });

  reset();
  resize();
  if (window.ResizeObserver) new ResizeObserver(resize).observe(root.querySelector(".golf-green"));
  else window.addEventListener("resize", resize);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(draw);
})();
