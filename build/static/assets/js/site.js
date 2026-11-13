// Autoplay muted case-study recordings only when the viewer hasn't asked for reduced motion.
// Videos always have controls, so they work (and can be paused) without this script.
(function () {
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce) return;
  document.querySelectorAll("video[data-autoplay]").forEach(function (v) {
    v.muted = true;
    var p = v.play();
    if (p && p.catch) p.catch(function () {});
  });
})();

// Work page filters. Without JavaScript the chips stay hidden and every project shows.
(function () {
  var bar = document.querySelector(".filters");
  if (!bar) return;
  var tiles = document.querySelectorAll(".work-tile");
  var status = document.getElementById("filter-status");
  bar.hidden = false;
  bar.addEventListener("click", function (e) {
    var btn = e.target.closest(".chip");
    if (!btn) return;
    var f = btn.getAttribute("data-filter");
    bar.querySelectorAll(".chip").forEach(function (c) { c.setAttribute("aria-pressed", String(c === btn)); });
    var shown = 0;
    tiles.forEach(function (t) {
      var match = f === "all" || (" " + t.getAttribute("data-tags") + " ").indexOf(" " + f + " ") > -1;
      t.hidden = !match;
      if (match) shown++;
    });
    if (status) status.textContent = shown + (shown === 1 ? " project" : " projects") + " shown";
  });
})();

// Phone menu: frosted panel from the top-right button. Without JavaScript the links stay inline.
(function () {
  var header = document.querySelector(".site-header");
  var btn = header && header.querySelector(".menu-button");
  var nav = header && header.querySelector("nav");
  if (!btn || !nav) return;
  btn.hidden = false;
  var phone = window.matchMedia("(max-width: 640px)");
  function setOpen(open, returnFocus) {
    header.classList.toggle("menu-open", open);
    btn.setAttribute("aria-expanded", String(open));
    btn.querySelector(".visually-hidden").textContent = open ? "Close menu" : "Menu";
    if (open) { var first = nav.querySelector("a"); if (first) first.focus(); }
    else if (returnFocus) btn.focus();
  }
  btn.addEventListener("click", function () { setOpen(btn.getAttribute("aria-expanded") !== "true"); });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && header.classList.contains("menu-open")) setOpen(false, true);
  });
  document.addEventListener("click", function (e) {
    if (header.classList.contains("menu-open") && !nav.contains(e.target) && !btn.contains(e.target)) setOpen(false);
  });
  nav.addEventListener("focusout", function (e) {
    if (phone.matches && header.classList.contains("menu-open") && !header.contains(e.relatedTarget)) setOpen(false);
  });
  (phone.addEventListener ? phone.addEventListener("change", function () { setOpen(false); }) : phone.addListener(function () { setOpen(false); }));
})();

// Homepage carousel: previous/next buttons, arrow keys, native swipe and scroll snap. No autoplay.
// Without JavaScript the track still scrolls sideways and the buttons stay hidden.
(function () {
  var track = document.getElementById("featured-track");
  if (!track) return;
  var controls = document.querySelector(".carousel-controls");
  var prev = controls.querySelector(".carousel-prev");
  var next = controls.querySelector(".carousel-next");
  var status = document.querySelector(".carousel-status");
  var slides = Array.prototype.slice.call(track.children);
  controls.hidden = false;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");

  var target = null; // the card we're scrolling to, so quick repeated clicks don't skip
  function current() {
    if (target !== null) return target;
    var left = track.getBoundingClientRect().left + parseFloat(getComputedStyle(track).paddingLeft);
    var best = 0, dist = Infinity;
    slides.forEach(function (s, i) { var d = Math.abs(s.getBoundingClientRect().left - left); if (d < dist) { dist = d; best = i; } });
    return best;
  }
  function update() {
    var maxScroll = track.scrollWidth - track.clientWidth;
    var i = current();
    // aria-disabled instead of disabled, so a focused button keeps focus at either end
    prev.setAttribute("aria-disabled", String(track.scrollLeft <= 2));
    next.setAttribute("aria-disabled", String(track.scrollLeft >= maxScroll - 2 || i === slides.length - 1));
  }
  function go(i, announce) {
    i = Math.max(0, Math.min(slides.length - 1, i));
    target = i;
    var pad = parseFloat(getComputedStyle(track).paddingLeft);
    track.scrollTo({ left: slides[i].offsetLeft - pad, behavior: reduce.matches ? "auto" : "smooth" });
    if (announce) status.textContent = "Project " + (i + 1) + " of " + slides.length + ": " + slides[i].querySelector(".feature-name").textContent;
  }
  prev.addEventListener("click", function () { if (prev.getAttribute("aria-disabled") !== "true") go(current() - 1, true); });
  next.addEventListener("click", function () { if (next.getAttribute("aria-disabled") !== "true") go(current() + 1, true); });
  track.addEventListener("keydown", function (e) {
    if (e.key !== "ArrowLeft" && e.key !== "ArrowRight") return;
    e.preventDefault();
    var i = current() + (e.key === "ArrowRight" ? 1 : -1);
    go(i, true);
    var link = slides[Math.max(0, Math.min(slides.length - 1, i))].querySelector("a");
    if (link) link.focus({ preventScroll: true });
  });
  var t;
  track.addEventListener("scroll", function () { clearTimeout(t); t = setTimeout(function () { target = null; update(); }, 150); }, { passive: true });
  window.addEventListener("resize", update);
  update();
})();
