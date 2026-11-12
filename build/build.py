#!/usr/bin/env python3
"""Static site builder for alexrekas.com.

Reads page fragments from build/pages/**.html, wraps them in the shared layout,
generates responsive images, and writes the finished site into /docs.

Run from anywhere:  python3 -I build/build.py

Fragment format
---------------
The first thing in each fragment is an HTML comment holding JSON metadata:

    <!--{"url": "/portfolio/workradar/", "title": "...", "description": "...",
          "template": "case", ...}-->

Custom tags expanded by the builder:
    <x-img src="file.png" alt="..." [sizes="..."] [eager] [class="..."]>
    <x-todo>Description of the image still to add</x-todo>
    <x-video name="slug" label="What the recording shows" caption="..."></x-video>
Any "(FILL IN: ...)" text becomes a visible placeholder.
Absolute site paths in href/src ("/portfolio/") are rewritten to relative paths.
"""
import html
import json
import os
import re
import shutil
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"
DOCS = ROOT / "docs"
SRC_IMAGES = [BUILD / "img-src", ROOT / "_source" / "source-bundle" / "images"]
OUT_IMG = DOCS / "assets" / "img"
SITE_URL = "https://alexrekas.com"
PREVIEW = True  # set False at launch: removes noindex
# Where the site lives on its host. Only used by 404.html, which GitHub serves at any missing path.
BASE_PATH = "/alexrekas.com/" if PREVIEW else "/"

SOCIAL = {
    "LinkedIn": "https://www.linkedin.com/in/alexrekas",
    "Dribbble": "https://dribbble.com/alexrekas",
    "GitHub": "https://github.com/alexrekas",
    "Instagram": "https://www.instagram.com/aprekas",
    "X": "https://x.com/aprekas",
}

WIDTHS = [640, 1200, 2000]


# ---------------------------------------------------------------- images
def find_image(name):
    for d in SRC_IMAGES:
        p = d / name
        if p.exists():
            return p
    raise FileNotFoundError(f"image not found: {name}")


def fresh(out, src):
    return out.exists() and out.stat().st_mtime >= src.stat().st_mtime


def make_variants(name):
    """Return (webp_srcset_entries, fallback_relpath, width, height)."""
    src = find_image(name)
    stem = re.sub(r"[^a-z0-9]+", "-", src.stem.lower()).strip("-")
    im = Image.open(src)
    w, h = im.size
    has_alpha = im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info)
    widths = [x for x in WIDTHS if x < w] + [min(w, WIDTHS[-1])]
    widths = sorted(set(widths))
    OUT_IMG.mkdir(parents=True, exist_ok=True)
    entries = []
    loaded = None
    for tw in widths:
        out = OUT_IMG / f"{stem}-{tw}.webp"
        if not fresh(out, src):
            if loaded is None:
                loaded = im.convert("RGBA" if has_alpha else "RGB")
            th = round(h * tw / w)
            loaded.resize((tw, th), Image.LANCZOS).save(out, "WEBP", quality=84, method=6)
        entries.append((f"assets/img/{out.name}", tw))
    fw = widths[min(1, len(widths) - 1)]
    ext = "png" if has_alpha else "jpg"
    fout = OUT_IMG / f"{stem}-{fw}.{ext}"
    if not fresh(fout, src):
        if loaded is None:
            loaded = im.convert("RGBA" if has_alpha else "RGB")
        r = loaded.resize((fw, round(h * fw / w)), Image.LANCZOS)
        if has_alpha:
            r.save(fout, "PNG", optimize=True)
        else:
            r.save(fout, "JPEG", quality=84, optimize=True, progressive=True)
    return entries, f"assets/img/{fout.name}", w, h


def render_img(attrs):
    name = attrs["src"]
    alt = attrs.get("alt")
    if alt is None:
        raise ValueError(f"missing alt on {name}")
    sizes = attrs.get("sizes", "(min-width: 1248px) 1200px, calc(100vw - 32px)")
    eager = "eager" in attrs
    entries, fallback, w, h = make_variants(name)
    srcset = ", ".join(f"/{p} {tw}w" for p, tw in entries)
    cls = f' class="{attrs["class"]}"' if "class" in attrs else ""
    loading = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (
        f'<picture><source type="image/webp" srcset="{srcset}" sizes="{sizes}">'
        f'<img src="/{fallback}" alt="{html.escape(alt, quote=True)}" width="{w}" height="{h}" '
        f'{loading} decoding="async"{cls}></picture>'
    )


ATTR_RE = re.compile(r'([a-zA-Z-]+)(?:="([^"]*)")?')


def parse_attrs(s):
    return {k: html.unescape(v) if v is not None else "" for k, v in ATTR_RE.findall(s)}


# ---------------------------------------------------------------- expansions
def expand(body):
    body = re.sub(r"<x-img\b([^>]*)>", lambda m: render_img(parse_attrs(m.group(1))), body)
    body = re.sub(
        r"<x-todo>(.*?)</x-todo>",
        lambda m: f'<div class="todo-box" role="note"><span class="todo-label">Image to add</span>{m.group(1)}</div>',
        body,
        flags=re.S,
    )
    body = re.sub(r"<x-video\b([^>]*)></x-video>", lambda m: render_video(parse_attrs(m.group(1))), body)
    body = re.sub(
        r"\(FILL IN: (.*?)\)(?![^<]*>)",
        lambda m: f'<mark class="fill">Fill in: {m.group(1)}</mark>',
        body,
        flags=re.S,
    )
    return body


def render_video(a):
    name = a["name"]
    vid = DOCS / "assets" / "video" / f"{name}.mp4"
    caption = a.get("caption", "")
    if not vid.exists():
        return (
            f'<figure class="video-slot"><div class="todo-box" role="note">'
            f'<span class="todo-label">Video to add</span>{a.get("label", "")}</div>'
            + (f"<figcaption>{caption}</figcaption>" if caption else "")
            + "</figure>"
        )
    poster = DOCS / "assets" / "video" / f"{name}.jpg"
    track = DOCS / "assets" / "video" / f"{name}.vtt"
    return (
        f'<figure class="video"><video muted loop playsinline controls preload="metadata" data-autoplay'
        + (f' poster="/assets/video/{name}.jpg"' if poster.exists() else "")
        + f' aria-label="{html.escape(a.get("label", ""), quote=True)}">'
        f'<source src="/assets/video/{name}.mp4" type="video/mp4">'
        + (f'<track kind="captions" src="/assets/video/{name}.vtt" srclang="en" label="English" default>' if track.exists() else "")
        + "</video>"
        + (f"<figcaption>{caption}</figcaption>" if caption else "")
        + "</figure>"
    )


def relativize(doc, url):
    if url == "/404.html":
        root = BASE_PATH
    else:
        depth = len([p for p in url.strip("/").split("/") if p])
        root = "../" * depth
    def fix_attr(m):
        attr, val = m.group(1), m.group(2)
        if attr == "srcset" or attr == "data-srcset":
            parts = [p.strip() for p in val.split(",")]
            return f'{attr}="' + ", ".join(fix_path(p, root) for p in parts) + '"'
        return f'{attr}="{fix_path(val, root)}"'
    return re.sub(r'\b(href|src|srcset|poster)="([^"]*)"', fix_attr, doc)


def fix_path(val, root):
    if val.startswith("/") and not val.startswith("//"):
        rest = val[1:]
        out = root + rest
        return out or "./"
    return val


# ---------------------------------------------------------------- layout
NAV = [("Work", "/portfolio/"), ("About", "/about/"), ("Resume", "/resume/")]


def header(url):
    items = []
    for label, href in NAV:
        cur = ' aria-current="page"' if url == href else (' aria-current="true"' if url.startswith(href) else "")
        items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    return (
        '<header class="site-header"><div class="wrap">'
        '<a class="brand" href="/"><svg class="brand-mark" viewBox="0 0 165.37 144" aria-hidden="true" focusable="false"><path fill="currentColor" d="M165.37,46.66A46.64,46.64,0,0,0,118.66,0H64L0,144H165.37L140.44,87.93A46.58,46.58,0,0,0,165.37,46.66ZM140.71,128H95.53L82.66,99.05,69.79,128H24.66L74.43,16h44.23A30.65,30.65,0,0,1,133,73.8l-13.23,7,6.08,13.67Z"/></svg><span class="visually-hidden">Alex Rekas, home</span></a>'
        f'<nav aria-label="Main"><ul>{"".join(items)}</ul></nav>'
        "</div></header>"
    )


def footer():
    links = []
    for label, href in SOCIAL.items():
        if href:
            links.append(f'<li><a href="{href}" rel="me">{label}</a></li>')
        else:
            links.append(f'<li><mark class="fill">Fill in: {label} URL</mark></li>')
    links.append('<li><a href="/privacy/">Privacy</a></li>')
    return (
        '<footer class="site-footer"><div class="wrap">'
        "<p>© 2026 Alex Rekas</p>"
        f'<ul class="footer-links">{"".join(links)}</ul>'
        "</div></footer>"
    )


def head(meta):
    url = meta["url"]
    title = meta["title"]
    full_title = title if title == "Alex Rekas" or meta.get("title_exact") else f"{title} · Alex Rekas"
    desc = meta["description"]
    share = meta.get("share", "assets/share/default.jpg")
    e = lambda s: html.escape(s, quote=True)
    robots = '<meta name="robots" content="noindex">\n' if PREVIEW or meta.get("noindex") else ""
    canonical = f"{SITE_URL}{url}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
{robots}<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Alex Rekas">
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/{share}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(full_title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{SITE_URL}/{share}">
<meta name="theme-color" content="#0F1012">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/ibm-plex-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/ibm-plex-sans-latin-500-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css">
<script src="/assets/js/site.js" defer></script>
</head>
"""


def case_study(meta, body):
    rows = []
    pairs = meta.get("rows") or [(l, meta.get(l.lower())) for l in ("Role", "Company", "Team", "Services", "Years")]
    for label, v in pairs:
        if not v:
            continue
        if isinstance(v, list):
            v = '<ul class="tags">' + "".join(f"<li>{x}</li>" for x in v) + "</ul>"
        rows.append(f"<div><dt>{label}</dt><dd>{v}</dd></div>")
    hero = ""
    if meta.get("hero"):
        hero = f'<figure class="hero"><x-img src="{meta["hero"]}" alt="{html.escape(meta["hero_alt"], quote=True)}" eager></figure>'
    elif meta.get("hero_todo"):
        hero = f'<figure class="hero"><x-todo>{meta["hero_todo"]}</x-todo></figure>'
    nxt = meta.get("next")
    next_html = ""
    if nxt:
        next_html = (
            f'<nav class="next-project" aria-label="Next project"><a href="{nxt["url"]}">'
            f'<span class="kicker">Next project</span><span class="next-title">{nxt["title"]} <span aria-hidden="true">→</span></span></a></nav>'
        )
    return (
        '<article class="case">'
        f'<header class="case-intro"><h1>{meta["h1"] if "h1" in meta else meta["title"]}</h1>'
        f'<p class="lede">{meta["intro"]}</p></header>'
        f'<dl class="meta">{"".join(rows)}</dl>'
        f"{hero}{body}{next_html}</article>"
    )


def redirect_page(meta):
    to = meta["redirect"]
    return (
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="robots" content="noindex">\n'
        f'<title>Moved · Alex Rekas</title>\n<link rel="canonical" href="{SITE_URL}{to}">\n'
        f'<meta http-equiv="refresh" content="0; url={to}">\n</head>\n'
        f'<body><p>This project has been retired. <a href="{to}">See all work</a>.</p></body>\n</html>\n'
    )


def render(meta, body):
    if meta.get("redirect"):
        doc = relativize(redirect_page(meta), meta["url"])
        href = re.search(r'<a href="([^"]*)"', doc).group(1)
        return re.sub(r'content="0; url=[^"]*"', f'content="0; url={href}"', doc)
    if meta.get("template") == "case":
        body = case_study(meta, body)
    main_cls = f' class="{meta["main_class"]}"' if meta.get("main_class") else ""
    doc = (
        head(meta)
        + '<body>\n<a class="skip-link" href="#main">Skip to content</a>\n'
        + header(meta["url"])
        + f'\n<main id="main"{main_cls}><div class="wrap">\n{body}\n</div></main>\n'
        + footer()
        + "\n</body>\n</html>\n"
    )
    doc = expand(doc)
    return relativize(doc, meta["url"])


# ---------------------------------------------------------------- main
def copy_static():
    static = BUILD / "static"
    for p in static.rglob("*"):
        if p.is_file():
            out = DOCS / p.relative_to(static)
            out.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, out)
    fonts = DOCS / "assets" / "fonts"
    fonts.mkdir(parents=True, exist_ok=True)
    nm = BUILD / "node_modules" / "@fontsource"
    for fam, weights in (("ibm-plex-sans", (400, 500, 600)), ("ibm-plex-mono", (400, 500))):
        for w in weights:
            f = nm / fam / "files" / f"{fam}-latin-{w}-normal.woff2"
            shutil.copy2(f, fonts / f.name)


def output_path(url):
    if url.endswith(".html"):
        return DOCS / url.lstrip("/")
    return DOCS / url.strip("/") / "index.html"


def main():
    copy_static()
    pages = sorted((BUILD / "pages").rglob("*.html"))
    only = set(sys.argv[1:])
    built = []
    for p in pages:
        text = p.read_text()
        m = re.match(r"\s*<!--(.*?)-->", text, re.S)
        if not m:
            raise ValueError(f"{p}: missing metadata comment")
        meta = json.loads(m.group(1))
        if only and p.stem not in only:
            continue
        body = text[m.end():].strip()
        out = output_path(meta["url"])
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(meta, body))
        built.append(meta["url"])
    robots = DOCS / "robots.txt"
    if PREVIEW:
        robots.write_text("User-agent: *\nDisallow: /\n")
    (DOCS / ".nojekyll").touch()
    print(f"built {len(built)} pages")


if __name__ == "__main__":
    main()
