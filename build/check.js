#!/usr/bin/env node
// Site checks: serves /docs under /alexrekas.com/ (like the GitHub Pages preview),
// then for every page: internal links resolve, no horizontal scroll at 1440 and 375px,
// images have alt, axe (WCAG 2.1 A/AA) has no violations. Screenshots go to $SHOTS if set.
// Usage: node build/check.js [page-url-substring ...]
const http = require("http");
const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");

const DOCS = path.resolve(__dirname, "..", "docs");
const BASE = "/alexrekas.com";
const SHOTS = process.env.SHOTS;
const TYPES = { ".html": "text/html", ".css": "text/css", ".js": "text/javascript", ".png": "image/png", ".jpg": "image/jpeg", ".webp": "image/webp", ".svg": "image/svg+xml", ".woff2": "font/woff2", ".pdf": "application/pdf", ".mp4": "video/mp4", ".txt": "text/plain", ".xml": "application/xml" };

function resolveFile(urlPath) {
  if (!urlPath.startsWith(BASE + "/")) return null;
  let rel = decodeURIComponent(urlPath.slice(BASE.length).split("?")[0].split("#")[0]);
  let f = path.join(DOCS, rel);
  if (!f.startsWith(DOCS)) return null;
  if (fs.existsSync(f) && fs.statSync(f).isDirectory()) f = path.join(f, "index.html");
  return fs.existsSync(f) ? f : null;
}

const server = http.createServer((req, res) => {
  const f = resolveFile(req.url);
  if (!f) { res.writeHead(404, { "content-type": "text/html" }); res.end(fs.readFileSync(path.join(DOCS, "404.html"), "utf8").toString?.() ?? ""); return; }
  res.writeHead(200, { "content-type": TYPES[path.extname(f)] || "application/octet-stream" });
  fs.createReadStream(f).pipe(res);
});

function allPages() {
  const out = [];
  (function walk(d) {
    for (const e of fs.readdirSync(d, { withFileTypes: true })) {
      const p = path.join(d, e.name);
      if (e.isDirectory()) { if (e.name !== "assets") walk(p); }
      else if (e.name.endsWith(".html")) {
        let rel = path.relative(DOCS, p).replace(/\\/g, "/");
        rel = rel === "index.html" ? "" : rel.replace(/index\.html$/, "");
        out.push(rel);
      }
    }
  })(DOCS);
  return out.sort();
}

(async () => {
  if (!fs.existsSync(path.join(DOCS, "404.html"))) fs.writeFileSync(path.join(DOCS, "404.html"), "Not found");
  await new Promise((r) => server.listen(0, r));
  const origin = `http://127.0.0.1:${server.address().port}`;
  const filters = process.argv.slice(2);
  const pages = allPages().filter((p) => !filters.length || filters.some((f) => p.includes(f)));
  const browser = await chromium.launch();
  const axeSrc = fs.readFileSync(require.resolve("axe-core/axe.min.js"), "utf8");
  let problems = 0;
  const checkedLinks = new Map();
  if (SHOTS) fs.mkdirSync(SHOTS, { recursive: true });

  for (const vp of [{ name: "desktop", width: 1440, height: 900 }, { name: "phone", width: 375, height: 812 }]) {
    const ctx = await browser.newContext({ viewport: { width: vp.width, height: vp.height }, deviceScaleFactor: 1, reducedMotion: "reduce" });
    const page = await ctx.newPage();
    const failed = [];
    page.on("response", (r) => { if (r.status() >= 400 && r.url().startsWith(origin)) failed.push(r.url()); });
    for (const p of pages) {
      failed.length = 0;
      const html = fs.readFileSync(path.join(DOCS, p.endsWith(".html") ? p : p + "index.html"), "utf8");
      const refresh = html.match(/http-equiv="refresh" content="0; url=([^"]+)"/);
      if (refresh) {
        // redirect stubs: only check the target exists
        const target = new URL(refresh[1], `${origin}${BASE}/${p}`).pathname;
        if (resolveFile(target)) console.log(`✓ [${vp.name}] /${p} → ${target.slice(BASE.length)}`);
        else { problems++; console.log(`✗ [${vp.name}] /${p} redirects to missing ${target}`); }
        continue;
      }
      const url = `${origin}${BASE}/${p}`;
      await page.goto(url, { waitUntil: "load" });
      // force lazy images to load
      await page.evaluate(async () => { document.querySelectorAll("img[loading=lazy]").forEach((i) => (i.loading = "eager")); for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise((r) => setTimeout(r, 60)); } window.scrollTo(0, 0); await Promise.all([...document.images].map((i) => i.decode().catch(() => {}))); });
      await page.waitForLoadState("networkidle");
      const issues = [];
      const overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
      // stray closing tags push content out of the centered wrapper
      const strays = await page.evaluate(() => [...document.querySelectorAll("main > :not(.wrap), body > :not(.skip-link):not(.site-header):not(main):not(.site-footer):not(script)")].map((e) => e.tagName + (e.className ? "." + e.className : "")));
      strays.forEach((s) => issues.push(`element outside the page wrapper: ${s}`));
      if (overflow > 0) issues.push(`horizontal overflow ${overflow}px`);
      const broken = await page.evaluate(() => [...document.images].filter((i) => !i.complete || i.naturalWidth === 0).map((i) => i.currentSrc || i.src));
      broken.forEach((b) => issues.push(`broken image ${b}`));
      failed.forEach((f) => issues.push(`404 ${f}`));
      if (vp.name === "desktop") {
        const links = await page.evaluate(() => [...document.querySelectorAll("a[href]")].map((a) => a.href));
        for (const l of links) {
          if (!l.startsWith(origin)) continue;
          const u = new URL(l);
          if (!checkedLinks.has(u.pathname)) checkedLinks.set(u.pathname, !!resolveFile(u.pathname));
          if (!checkedLinks.get(u.pathname)) issues.push(`broken link ${u.pathname}`);
          if (u.hash && u.pathname === new URL(url).pathname) {
            const ok = await page.evaluate((id) => !!document.getElementById(id), u.hash.slice(1));
            if (!ok) issues.push(`missing anchor ${u.hash}`);
          }
        }
        await page.addScriptTag({ content: axeSrc });
        const axe = await page.evaluate(async () => (await window.axe.run(document, { runOnly: { type: "tag", values: ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "best-practice"] } })).violations);
        axe.forEach((v) => issues.push(`axe ${v.id} (${v.impact}): ${v.help} — ${v.nodes.slice(0, 3).map((n) => n.target.join(" ")).join(" | ")}`));
      }
      if (SHOTS) await page.screenshot({ path: path.join(SHOTS, `${(p || "home").replace(/\//g, "_")}-${vp.name}.png`), fullPage: true });
      if (issues.length) { problems += issues.length; console.log(`✗ [${vp.name}] /${p}\n   ` + issues.join("\n   ")); }
      else console.log(`✓ [${vp.name}] /${p}`);
    }
    await ctx.close();
  }
  await browser.close();
  server.close();
  console.log(problems ? `\n${problems} problem(s)` : "\nAll checks passed");
  process.exit(problems ? 1 : 0);
})();
