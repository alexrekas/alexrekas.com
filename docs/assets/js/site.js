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
