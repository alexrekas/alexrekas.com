# Build

The published site is plain HTML in `/docs`. These scripts generate it.

```bash
cd build && npm install          # fonts, axe-core (one time)
python3 -I build/prep_images.py  # gray logos, share images, re-rendered tiles
python3 -I build/build.py        # pages/ -> docs/ (+ responsive images)
node build/check.js              # links, phone/desktop overflow, axe
```

- `pages/` — one fragment per page; JSON metadata in the first comment.
- `static/` — CSS, JS, favicon, copied into `docs/` as-is.
- `img-src/` — derived images made by `prep_images.py`.
- At launch: set `PREVIEW = False` in `build.py`.
