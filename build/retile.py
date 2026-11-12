"""Re-render screens exported on a flat light background onto the site's #1E2024 tile."""
import numpy as np
from PIL import Image, ImageDraw

TILE = np.array([30, 32, 36])


def retile(src, out, bg=(233, 238, 245)):
    im = Image.open(src).convert("RGB")
    a = np.asarray(im).astype(int)
    B = np.array(bg)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    # background + its drop shadows: bluish tint, no lighter than the background
    lum = a.mean(axis=-1)
    chrome = (np.abs(a - np.array([228, 232, 238])) <= 1).all(axis=-1)  # browser title bar
    cand = ((b - r) >= 5) & (a <= B + 1).all(axis=-1) & (lum >= 170) & ~chrome
    mask = Image.fromarray((cand * 255).astype(np.uint8)).copy()
    w, h = mask.size
    for seed in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]:
        if mask.getpixel(seed) == 255:
            ImageDraw.floodfill(mask, seed, 128, thresh=0)
    region = np.asarray(mask) == 128
    # keep shadows as a subtle darkening of the tile
    depth = (B - a).clip(0, None).mean(axis=-1, keepdims=True)
    new = (TILE - depth * 0.35).clip(0, 255)
    a = np.where(region[..., None], new, a)
    Image.fromarray(a.astype(np.uint8), "RGB").save(out, optimize=True)


def swap_flat(src, out, old=(30, 30, 30), tol=3):
    im = Image.open(src).convert("RGB")
    a = np.asarray(im).astype(int)
    near = (np.abs(a - np.array(old)) <= tol).all(axis=-1)
    a = np.where(near[..., None], TILE, a)
    Image.fromarray(a.astype(np.uint8), "RGB").save(out, optimize=True)
