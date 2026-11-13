// Accessibility lens: shows a case study's images the way people with low vision or
// color blindness see them. Images only, so the text stays readable. Without
// JavaScript nothing is added.
//
// Color blindness uses the Machado, Oliveira & Fernandes (2009) matrices at full
// severity. SVG filters work in linear RGB by default, which is what those
// matrices expect.
(function () {
  var article = document.querySelector("article.case");
  if (!article) return;

  var MODES = [
    { id: "none", label: "Typical vision", note: "How most people see it." },
    { id: "low", label: "Low vision", note: "Blurred detail, as with uncorrected vision or cataracts. Small text and thin lines disappear first." },
    { id: "protan", label: "Protanopia", note: "Red-blind. Reds look dark and red and green look alike. Red-green color blindness affects about 1 in 12 men." },
    { id: "deutan", label: "Deuteranopia", note: "Green-blind. Red and green look alike. Red-green color blindness affects about 1 in 12 men." },
    { id: "tritan", label: "Tritanopia", note: "Blue-blind, and rare. Blue and green look alike, and yellow shifts toward pink." },
    { id: "achroma", label: "No color", note: "Achromatopsia, or a grayscale screen. Only contrast is left to carry meaning." }
  ];
  var MATRIX = {
    protan: "0.152286 1.052583 -0.204868 0 0  0.114503 0.786281 0.099216 0 0  -0.003882 -0.048116 1.051998 0 0  0 0 0 1 0",
    deutan: "0.367322 0.860646 -0.227968 0 0  0.280085 0.672501 0.047413 0 0  -0.011820 0.042940 0.968881 0 0  0 0 0 1 0",
    tritan: "1.255528 -0.076749 -0.178779 0 0  -0.078411 0.930809 0.147602 0 0  0.004733 0.691367 0.303900 0 0  0 0 0 1 0",
    achroma: "0.2126 0.7152 0.0722 0 0  0.2126 0.7152 0.0722 0 0  0.2126 0.7152 0.0722 0 0  0 0 0 1 0"
  };

  // SVG filter definitions
  var NS = "http://www.w3.org/2000/svg";
  var svg = document.createElementNS(NS, "svg");
  svg.setAttribute("aria-hidden", "true");
  svg.setAttribute("focusable", "false");
  svg.setAttribute("class", "lens-defs");
  var defs = document.createElementNS(NS, "defs");
  Object.keys(MATRIX).forEach(function (id) {
    var f = document.createElementNS(NS, "filter");
    f.setAttribute("id", "lens-" + id);
    var m = document.createElementNS(NS, "feColorMatrix");
    m.setAttribute("type", "matrix");
    m.setAttribute("values", MATRIX[id]);
    f.appendChild(m);
    defs.appendChild(f);
  });
  svg.appendChild(defs);
  document.body.appendChild(svg);

  // Control: a frosted pill that opens a panel of options
  var wrap = document.createElement("div");
  wrap.className = "lens";
  wrap.innerHTML =
    '<div class="lens-panel" id="lens-panel" role="dialog" aria-labelledby="lens-title" hidden>' +
      '<p class="lens-title" id="lens-title">See it like your users</p>' +
      '<p class="lens-sub">Changes how the images on this page look.</p>' +
      '<fieldset class="lens-options"><legend class="visually-hidden">Vision</legend>' +
        MODES.map(function (m) {
          return '<label class="lens-option"><input type="radio" name="lens" value="' + m.id + '"><span>' + m.label + "</span></label>";
        }).join("") +
      "</fieldset>" +
      '<p class="lens-note" aria-live="polite"></p>' +
    "</div>" +
    '<button class="lens-button" type="button" aria-expanded="false" aria-controls="lens-panel">' +
      '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 5C6.5 5 2.7 9.6 1.5 12c1.2 2.4 5 7 10.5 7s9.3-4.6 10.5-7C21.3 9.6 17.5 5 12 5Zm0 11.2A4.2 4.2 0 1 1 12 7.8a4.2 4.2 0 0 1 0 8.4Zm0-6.4a2.2 2.2 0 1 0 0 4.4 2.2 2.2 0 0 0 0-4.4Z" fill="currentColor"/></svg>' +
      '<span class="lens-label">Accessibility lens</span>' +
    "</button>";
  document.body.appendChild(wrap);

  var btn = wrap.querySelector(".lens-button");
  var panel = wrap.querySelector(".lens-panel");
  var label = wrap.querySelector(".lens-label");
  var note = wrap.querySelector(".lens-note");
  var radios = wrap.querySelectorAll("input[name=lens]");

  function store(v) { try { sessionStorage.setItem("lens", v); } catch (e) {} }
  function stored() { try { return sessionStorage.getItem("lens"); } catch (e) { return null; } }

  function apply(id, announce) {
    var mode = MODES.filter(function (m) { return m.id === id; })[0] || MODES[0];
    if (mode.id === "none") document.documentElement.removeAttribute("data-lens");
    else document.documentElement.setAttribute("data-lens", mode.id);
    radios.forEach(function (r) { r.checked = r.value === mode.id; });
    label.textContent = mode.id === "none" ? "Accessibility lens" : "Lens: " + mode.label;
    btn.classList.toggle("is-active", mode.id !== "none");
    if (announce !== false) note.textContent = mode.note;
    store(mode.id);
  }

  function setOpen(open, returnFocus) {
    panel.hidden = !open;
    btn.setAttribute("aria-expanded", String(open));
    if (open) {
      var checked = wrap.querySelector("input[name=lens]:checked") || radios[0];
      checked.focus();
    } else if (returnFocus) btn.focus();
  }

  btn.addEventListener("click", function () { setOpen(panel.hidden); });
  radios.forEach(function (r) { r.addEventListener("change", function () { apply(r.value); }); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && !panel.hidden) setOpen(false, true); });
  document.addEventListener("click", function (e) { if (!panel.hidden && !wrap.contains(e.target)) setOpen(false); });

  var start = stored();
  apply(start && start !== "none" ? start : "none", false);
  var current = MODES.filter(function (m) { return m.id === (start || "none"); })[0] || MODES[0];
  note.textContent = current.note;
})();
