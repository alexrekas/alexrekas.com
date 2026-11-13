#!/usr/bin/env node
// Minimal static server for /docs (local testing: Lighthouse, manual checks).
// Usage: node build/serve.js [port]   → http://127.0.0.1:8080/
const http = require("http");
const fs = require("fs");
const path = require("path");
const zlib = require("zlib");

const DOCS = path.resolve(__dirname, "..", "docs");
const PORT = Number(process.argv[2] || 8080);
const TYPES = { ".html": "text/html; charset=utf-8", ".css": "text/css", ".js": "text/javascript", ".png": "image/png", ".jpg": "image/jpeg", ".webp": "image/webp", ".svg": "image/svg+xml", ".woff2": "font/woff2", ".pdf": "application/pdf", ".txt": "text/plain", ".xml": "application/xml", ".webmanifest": "application/manifest+json" };

http.createServer((req, res) => {
  // also accept the preview's /alexrekas.com/ prefix, which 404.html uses for its assets
  let rel = decodeURIComponent(req.url.split("?")[0]).replace(/^\/alexrekas\.com(?=\/)/, "");
  let f = path.join(DOCS, rel);
  if (!f.startsWith(DOCS)) { res.writeHead(403); return res.end(); }
  if (fs.existsSync(f) && fs.statSync(f).isDirectory()) f = path.join(f, "index.html");
  if (!fs.existsSync(f)) { res.writeHead(404, { "content-type": TYPES[".html"] }); return fs.createReadStream(path.join(DOCS, "404.html")).pipe(res); }
  const type = TYPES[path.extname(f)] || "application/octet-stream";
  // GitHub Pages gzips text assets; mirror that so Lighthouse measures realistic sizes
  const gz = /text|javascript|svg|json|xml/.test(type) && /gzip/.test(req.headers["accept-encoding"] || "");
  res.writeHead(200, { "content-type": type, "cache-control": "max-age=600", ...(gz ? { "content-encoding": "gzip" } : {}) });
  const s = fs.createReadStream(f);
  gz ? s.pipe(zlib.createGzip()).pipe(res) : s.pipe(res);
}).listen(PORT, "127.0.0.1", () => console.log(`serving docs on http://127.0.0.1:${PORT}/`));
