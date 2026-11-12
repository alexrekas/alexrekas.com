# Build

The published site is plain HTML in `/docs`. These scripts generate it.

```bash
cd build && npm install          # fonts, axe-core (one time)
python3 -I build/mono_logos.py    # one-color client logos (SVG)
python3 -I build/prep_images.py  # share images, re-rendered tiles
python3 -I build/build.py        # pages/ -> docs/ (+ responsive images)
node build/check.js              # links, phone/desktop overflow, axe
```

- `pages/` — one fragment per page; JSON metadata in the first comment.
- `static/` — CSS, JS, favicon, copied into `docs/` as-is.
- `img-src/` — derived images made by `prep_images.py`.
- At launch: set `PREVIEW = False` in `build.py`.

## Framed screenshots

Use `<x-shot>` for raw screen exports (no mockup, no background):

```html
<x-shot src="enroll-review.png" alt="..." frame="browser" caption="...">
<x-shot src="enroll-phone-1.png" alt="..." frame="phone" sizes="300px">
```

`frame` is `browser`, `phone` or `none`. Put raw exports in `build/img-src/`.
Desktop: 2x, about 1440px wide (2880px file), cropped to one moment. Phone: 2x at 390×844 (780×1688 file).
