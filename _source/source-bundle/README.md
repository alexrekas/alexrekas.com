# Source bundle for the new alexrekas.com

Reference material for building the site. None of this is published as-is. Exported November 12, 2026 from the WordPress drafts and the design mockup.

## content/
- `pages.json`: every page to build. Each entry has its WordPress id, title, final URL and source file.
- `*.wpbakery.txt`: the latest approved copy for each page, as WordPress (WPBakery) shortcodes and HTML. Treat it as content, not markup to keep:
  - `[vc_single_image image="N"]` is an image. Look up N in `media.json`.
  - `[vc_column width="1/2"]` means the images sit side by side.
  - Text inside `<strong style="background:#fff3bf">(FILL IN: …)</strong>` and dashed `IMAGE TO ADD:` boxes is a placeholder Alex still has to fill. Keep it visible on the preview, styled as a clear placeholder.
- `media.json`: media id → local file in `images/`, plus the original URL on alexrekas.com. Some large images were compressed for this bundle; use the original URL if quality looks off.

## mockup/
The approved visual design: `Main.html` (homepage), `EnrollApp.html`, `WorkRadar.html`, `RegSearch.html`, with images in `mockup/assets/`. These are exports of a design-tool canvas, so they contain `<x-dc>`, `<helmet>`, `<sc-for>` and `{{…}}` template tags. Use them for layout, type, color and spacing, not as finished code. Where the mockup copy differs from `content/`, the copy in `content/` wins.

Client logos for the homepage row: `images/trustedby-marriott2.png`, `images/trustedby-dCS2.png`, `images/ar-trustedBrands-CDC.png` and `images/trustedby-goodwill2.png`.
