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
