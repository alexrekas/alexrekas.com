#!/usr/bin/env python3
"""Turn the client logo SVGs in _source/logos/ into one-color versions for the dark site.

"flat": every shape becomes the gray.
"knockout": colored shapes become the gray and white shapes are cut out of them
(so CDC's letters and Goodwill's smiling G show the page through, not white).
Run: python3 -I build/mono_logos.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_source" / "logos"
OUT = ROOT / "build" / "static" / "assets" / "logos"
GRAY = "#A6A8AD"

LOGOS = {
    # name: (mode, viewBox override or None)
    "marriott": ("flat", None),
    "dcs": ("flat", "0 0 104.177 64.248"),
    "cdc": ("knockout", None),
    "goodwill": ("knockout", "5.334 3.93 330.332 432.141"),  # crop to the box, without the ®
}

WHITE = r"(?:#fff(?:fff)?|white)"


def inner_and_viewbox(svg):
    svg = re.sub(r"<\?xml.*?\?>|<!DOCTYPE.*?>|<!--.*?-->", "", svg, flags=re.S)
    m = re.search(r"<svg\b([^>]*)>(.*)</svg>", svg, re.S)
    attrs, inner = m.group(1), m.group(2)
    vb = re.search(r'viewBox="([^"]+)"', attrs)
    return inner, vb.group(1) if vb else None


def clean(name, inner):
    inner = re.sub(r"<text\b.*?</text>", "", inner, flags=re.S)
    # Inkscape editor metadata (self-closing or with children)
    inner = re.sub(r"<sodipodi:namedview\b[^>]*?/>|<sodipodi:namedview\b.*?</sodipodi:namedview>", "", inner, flags=re.S)
    if name == "dcs":
        # the tagline group is exported twice at the same spot; keep the first
        inner = re.sub(r'<g id="Group_162".*?</g></g></g>', "", inner, flags=re.S)
    if name == "goodwill":
        # drop the trailing ® group
        inner = re.sub(r"<g>\s*<path d=\"M335\.913.*?</g>", "", inner, flags=re.S)
    return inner


def recolor(inner, white_to, other_to):
    def fix_style(m):
        st = m.group(1)
        st = re.sub(r"fill:\s*(#[0-9a-fA-F]{3,6}|white|black)", lambda f: "fill:" + (white_to if re.fullmatch(WHITE, f.group(1), re.I) else other_to), st)
        return f'style="{st}"'
    inner = re.sub(r'style="([^"]*)"', fix_style, inner)
    inner = re.sub(r'fill="(#[0-9a-fA-F]{3,6}|white|black)"', lambda f: f'fill="{white_to if re.fullmatch(WHITE, f.group(1), re.I) else other_to}"', inner)
    inner = re.sub(r'\sclass="cls-\d+"', "", inner)
    return inner


def build(name):
    mode, vb_override = LOGOS[name]
    inner, vb = inner_and_viewbox((SRC / f"{name}.svg").read_text())
    vb = vb_override or vb
    inner = clean(name, inner)
    x, y, w, h = vb.split()
    if mode == "flat":
        body = f'<g fill="{GRAY}">{recolor(inner, GRAY, GRAY)}</g>'
    else:
        masked = recolor(inner, "#000", "#fff")
        body = (
            f'<mask id="k-{name}" maskUnits="userSpaceOnUse" x="{x}" y="{y}" width="{w}" height="{h}">'
            f'<g fill="#fff">{masked}</g></mask>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{GRAY}" mask="url(#k-{name})"/>'
        )
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">{body}</svg>\n'
    svg = re.sub(r"\s+inkscape:[\w-]+=\"[^\"]*\"|\s+sodipodi:[\w-]+=\"[^\"]*\"", "", svg, flags=re.S)
    svg = re.sub(r">\s+<", "><", svg)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{name}.svg").write_text(svg)
    return float(w) / float(h), len(svg)


if __name__ == "__main__":
    for n in LOGOS:
        print(n, *build(n))
