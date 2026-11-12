#!/usr/bin/env python3
"""Derived images that the site uses but the source bundle doesn't have as-is.

Writes into build/img-src/ (picked up by build.py) and docs/assets/share/.
Run: python3 -I build/prep_images.py
"""
from pathlib import Path

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_source" / "source-bundle" / "images"
OUT = ROOT / "build" / "img-src"
OUT.mkdir(parents=True, exist_ok=True)

LOGO_GRAY = (166, 168, 173)  # --muted


def gray_logo(src_name, out_name):
    """Logos arrive as a dark mark on a translucent white box. Keep only the mark,
    recolor it to one gray, crop tight, and scale to a common height."""
    im = Image.open(SRC / src_name).convert("RGBA")
    lum = im.convert("L")
    alpha = im.getchannel("A")
    # darkness × opacity → mask (dark pixels on the box become the logo)
    dark = lum.point(lambda v: max(0, min(255, int((200 - v) * 255 / 150))))
    mask = ImageChops.multiply(dark, alpha)
    bbox = mask.getbbox()
    mask = mask.crop(bbox)
    scale = 4  # upsample so the mark stays crisp on 2x screens
    mask = mask.resize((mask.width * scale, mask.height * scale), Image.LANCZOS)
    out = Image.new("RGBA", mask.size, LOGO_GRAY + (0,))
    out.putalpha(mask)
    out.save(OUT / out_name, optimize=True)
    return out.size


if __name__ == "__main__":
    for s, o in [
        ("trustedby-marriott2.png", "logo-marriott.png"),
        ("ar-trustedBrands-CDC.png", "logo-cdc.png"),
        ("trustedby-goodwill2.png", "logo-goodwill.png"),
        ("trustedby-dCS2.png", "logo-dcs.png"),
    ]:
        print(o, gray_logo(s, o))


# ---------------------------------------------------------------- share images
from PIL import ImageDraw, ImageFont, ImageOps

FONTS = ROOT / "build" / "node_modules" / "@fontsource"
SHARE = ROOT / "docs" / "assets" / "share"


def font(fam, w, size):
    return ImageFont.truetype(str(FONTS / fam / "files" / f"{fam}-latin-{w}-normal.woff2"), size)


def wrap(draw, text, f, width):
    lines, line = [], ""
    for word in text.split():
        t = f"{line} {word}".strip()
        if draw.textlength(t, font=f) <= width:
            line = t
        else:
            lines.append(line)
            line = word
    lines.append(line)
    return lines


def share_image(slug, title, image=None, subtitle=None):
    """1200×630 card: name kicker, title, and (optionally) a work image on a tile."""
    SHARE.mkdir(parents=True, exist_ok=True)
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), "#0F1012")
    d = ImageDraw.Draw(im)
    text_w = 1040 if image is None else 500
    if image:
        tile = (580, 0, 1160, 630)
        src = Image.open(find_src(image)).convert("RGB")
        tw, th = tile[2] - tile[0], tile[3] - tile[1]
        fitted = ImageOps.contain(src, (tw, th), Image.LANCZOS)
        fw, fh = fitted.size
        mask = Image.new("L", (fw, fh), 0)
        ImageDraw.Draw(mask).rounded_rectangle((0, 0, fw - 1, fh - 1), 16, fill=255)
        im.paste(fitted, (tile[0] + (tw - fw) // 2, tile[1] + (th - fh) // 2), mask)
    d.text((64, 72), "ALEX REKAS", font=font("ibm-plex-mono", 500, 22), fill="#A6A8AD")
    size = 64 if image is None else 52
    f = font("ibm-plex-sans", 500, size)
    y = 140
    for line in wrap(d, title, f, text_w):
        d.text((64, y), line, font=f, fill="#EDEDEE")
        y += int(size * 1.15)
    if subtitle:
        fs = font("ibm-plex-sans", 400, 26)
        y += 20
        for line in wrap(d, subtitle, fs, text_w):
            d.text((64, y), line, font=fs, fill="#C9CBCF")
            y += 38
    d.text((64, H - 90), "alexrekas.com", font=font("ibm-plex-mono", 400, 20), fill="#8FB4FF")
    im.save(SHARE / f"{slug}.jpg", "JPEG", quality=88, optimize=True)


def find_src(name):
    for d in (OUT, SRC):
        if (d / name).exists():
            return d / name
    raise FileNotFoundError(name)


SHARES = [
    ("default", "Alex Rekas", None, "Design Lead and Product Designer"),
    ("home", "Product design for complex, high-stakes software.", None, "Alex Rekas · Design Lead and Product Designer, Richmond, VA"),
    ("workradar", "WorkRadar", "workradar-00-hero-v2.png", "Daily check-ins for a safe return to the office"),
]

if __name__ == "__main__":
    for s in SHARES:
        share_image(*s)
        print("share", s[0])
