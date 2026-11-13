# Imagery brief

How every image on alexrekas.com should look, why, and exactly what to produce for each project. Written November 13, 2026, after studying gabrielvaldivia.com's homepage, Work page and case studies with all images loaded.

---

## 1. Why the current images underperform

### The four homepage cards today

| Card | What's in it | What's wrong |
|---|---|---|
| **Enroll App** | A white form inside a line-drawn laptop outline, on dark gray | The UI fills about 40% of the card and the text is unreadable. The screen is mostly white space. The outline laptop reads as a wireframe, not a shipped product. It shows the least interesting screen (a blank-ish form), not the redesign's best moment. |
| **WorkRadar** | Two outline phones with the **old, white** result screens | Your most striking asset, the all-green OK To Enter and all-red STOP screens, isn't used. The phones fill about 35% of the card, with empty dark space on both sides. |
| **RegSearch** | A floating screenshot with a drop shadow | The source is only 1000px wide, so it's soft on modern screens, and the dense text is unreadable at card size. It looks like a 2016 product because it is one. |
| **CDC** | A stock photo of a child with the CDC logo | It shows the client's brand, not your work. It's a 400px image stretched to 586px, so it's blurry. It's also the only photo, so it breaks the set. |

**The common problems**
1. **The work is too small.** Product UI fills 25–45% of each card. In his, it fills 70–80%.
2. **No visual system.** Four cards, four treatments: line-art device, outline phones, floating screenshot, stock photo. His cards all follow one recipe, so the grid reads as one body of work.
3. **Low resolution.** Several sources are 400–1000px. Every image needs to be at least 2x its display size.
4. **No hero moment.** Each card should show the single most recognizable, most colorful screen from the project, the one you'd point to in an interview.
5. **Flat, drawn devices.** Outline devices look like wireframes. He uses photoreal devices with real materials, light and shadow.

### Why the current case study images have big backgrounds

That wasn't a design choice for this site. The images came from your old WordPress site, where they were made as presentation mockups: devices placed on a large colored canvas with generous margins, designed to sit on a white page. When I moved them to the dark site, I kept them as they were, and for Enroll I re-colored the canvas to match the dark tile. The margins are baked into the files, though, so the UI can never get bigger than its share of that canvas. For example, the WorkRadar dashboard images are 2400px wide, but the actual dashboard is only about half of that.

His approach is the opposite: **the canvas is the site's job, not the image's.** His exports are just the product: a device render or a raw screen. The page supplies one consistent tile, padding and frame around it. That's what the `x-shot` frame system on your site now does. Send raw screens, and the site frames them identically everywhere.

**A quick win I can do now, before new exports:** automatically trim the baked-in margins from the existing images (WorkRadar, Enroll, TakeCare and others), so the UI fills its space. It won't fix resolution or style, but it roughly doubles how big the work appears.

---

## 2. What he does

### Work page thumbnails
- **Tall cards (443 × 560 at 1440px)** on a light gray seamless background, with a **square image** inset 8px and the text below it.
- **One hero object per card:** a photoreal device render (iPhone, MacBook, iPad), or the physical product, **angled in 3D** (about 15–30° turn, slight tilt) with a soft contact shadow.
- **The object fills 70–80% of the card** and sometimes bleeds off an edge. No frame, no border, no second background; the object sits directly on the card color.
- **The screen shows the most colorful, recognizable state** of the product: a photo, a bright brand color, a big headline. Never a settings page.
- **Name and one-liner inside the card,** bottom left.

### Homepage feature cards
- **A carousel of large, wide cards (about 3:2)**, each a **full-bleed lifestyle photo**: the product in a real setting (Daylight's tablet on a warm desk next to a keyboard), with moody natural light.
- Name, one-liner and tags overlaid bottom left; a client quote on frosted glass bottom right.

### Case study images
- **Desktop screens** in a minimal browser window, on a flat light-gray tile with even padding (about 3–5%). The screen fills the tile.
- **Phone screens** in matching device frames, in rows of 2–3 on the same tile.
- **Context photos:** at least one image per case study shows the product in a person's hands or on a desk. ORA shows an older adult creating a PIN on a laptop.
- **Covers** for brand-led projects: a bold brand image first (Twinsi's colorful hero, Kale's product photo).
- **Short screen recordings** (muted, looping) for key interactions.
- **One idea per image,** captioned in one plain line.

---

## 3. The visual system for alexrekas.com

Translate his recipe to your dark site, and apply it to every project so the grid reads as one body of work.

### Backgrounds
- **Thumbnails and heroes:** render the device on **exactly `#1E2024`** (the site's tile color), or export with a **transparent background** and I'll place it. Never bake in another color or a gradient canvas.
- **Case study screens:** export **raw screens only**: no device, no frame, no background. The site adds the tile and frame.

### Devices
- **Phone:** iPhone 15 or 16 Pro, Black Titanium. **Laptop:** MacBook Pro 14", Space Black. **Tablet** (only if a project needs one): iPad Pro, Space Black.
- Use **one device set for every project.** Mixing device models or colors breaks the system.

### Angle, light, shadow
- **Single device:** three-quarter view, turned about 20° and tilted about 8° toward the viewer. Use the same angle preset every time.
- **Phone pairs and trios:** front-facing, slightly overlapping, the front phone a little larger, or a gentle fan.
- **Laptop plus phone** (his ORA thumbnail): laptop open at an angle behind, phone in front and to one side, overlapping the laptop's corner.
- **Light:** soft key light from the top left, a subtle rim light so dark devices separate from the dark background, no harsh reflections.
- **Shadow:** soft contact shadow under the device, about 30–40% opacity.

### Framing
- The device fills **70–80% of the frame width.** It's fine to bleed off one edge.
- Keep a **safe area in the bottom 25%** of homepage cards, where the name and tags will overlay.

### Screen content
- **The hero moment:** the single screen you'd show first in an interview.
- **Realistic, fake data,** with one consistent sample person per project (for Enroll, "Chris Smith").
- Light-mode UI is fine and actually helps: bright screens pop against the dark tile.
- Export UI at **2x** before placing it on the device, so text stays crisp.

### Tools
- **Device renders:** [Rotato](https://rotato.app) (Mac app with consistent 3D angles and transparent export) or [Shots.so](https://shots.so) (web, quick). A Figma mockup plugin works too. Pick one and save your angle and lighting as a preset, so every render matches.
- **Context photos:** AI-generate the scene with a **plain white screen**, then place your real screenshot onto the screen in Photoshop or Figma (perspective warp, slight glare, match the room's brightness). AI can't render your actual UI convincingly, so never ask it to.

### File specs

| Slot | Shape | Export size | Notes |
|---|---|---|---|
| **Homepage card** (4 projects) | 3:2 landscape | 2400 × 1600 | Context photo, full bleed. Measured: 1215 × 810 at 1440px. Keep the bottom 30% calm; the name, tagline and tags sit there on a dark shade. |
| **Work page tile** (every project) | 1:1 square | 1600 × 1600 | Device render on `#1E2024` or transparent. Measured: his tile image is a square inset 8px inside a 40px-radius tile, with the text below it. |
| **Case study hero** | about 16:9 | 2400 × 1350 | The same render or photo as the card, wider. |
| **Desktop screen** | as designed | about 2880 wide (2x of 1440) | Raw UI, cropped to one moment. |
| **Phone screen** | 390 × 844 at 2x | 780 × 1688 | Raw UI, no device frame. |
| **Detail crop** | any | at least 1600 wide | A close-up of one component or state. |
| **Recording** | as designed | MP4, muted, 20–30 s, under 5 MB | Plus a poster frame (PNG). |

**Measured on November 13, 2026 and now built:** homepage cards are a 3:2 carousel (1215 × 810 at 1440px, 16px radius, 40px gap). Work tiles are 40px-radius cards with a **square** image inset 8px and the name and tagline below it, in a 3-column grid with 16px gaps. The interim 4:5 tile images are fitted into the square until 1:1 renders replace them.

---

## 4. Project by project

For each: the **homepage card** (featured four only), the **Work tile** (the "sexiest" image for that project), the **hero**, and the **case study shots**. Every placeholder box on the site matches an item here.

### Enroll App: *your most important project*

**Homepage card: context photo, someone getting good news.**
A woman in her early 40s at a kitchen table in early-evening window light, holding her phone, relieved, with a folder of paperwork beside her. On the phone: the **eligibility results** screen showing she can shop for plans and qualifies for financial help. This tells the whole story (stressful moment, clear answer) in one image.

> **Prompt:** Candid documentary-style photo, eye level, of a woman in her early 40s sitting at a kitchen table in the early evening, holding a smartphone in both hands and looking at the screen with quiet relief, a small genuine smile, shoulders relaxed. Warm natural window light from the left, soft shadows. Lived-in home details slightly out of focus behind her: a mug, a folder of paperwork, a child's drawing on the fridge. The phone faces the camera at a slight angle so the full screen is visible; the screen is plain solid white with no interface or text. Sharp focus on the phone and her hands, shallow depth of field. Muted, natural colors, no heavy grading. 35mm lens, f/2.0. Realistic skin texture, natural hands with five fingers. Wide 3:2 composition, the person and phone in the right half, calm open space in the lower left for text.
>
> **Avoid:** text on screen, UI, logos, watermark, extra fingers, distorted hands, glossy stock-photo look, posed smile, studio lighting.

**Work tile (the sexiest image): laptop plus phone, like his ORA thumbnail.**
MacBook open at an angle showing **New employer: Personal Information**, with the progress rail clearly visible on the left. In front, an iPhone showing the **eligibility results** screen. Light UI against the dark tile, the blue buttons the only accent color.

**Hero:** the same laptop-and-phone render, wider (16:9).

**Case study shots** (raw exports)
- New employer: Personal Information (filled), Business Information with office location, Communication, Complete. Desktop.
- Before and after: the old single-page form (you have this) beside the new step one.
- Phone trio: Personal, Business and Communication steps (rows of three).
- **Eligibility results:** results screen (phone and desktop) and the next step (plan choice).
- **Help on every screen:** language switch open; help line with TTY; the "I don't have a SSN" option.
- **Accessible by default:** close-ups of focus, error and disabled states; a color and type tokens page.
- **Recording:** 20–30 s of the new employer flow.

### WorkRadar

**Homepage card: context photo at the office door.**
An employee in a bright, modern office lobby in the morning, holding up a phone showing the **all-green OK To Enter** screen with its checkmark and QR code, the entrance blurred behind them. Green against the warm lobby is an instant read.

> **Prompt:** Candid photo of a man in his 30s in business-casual clothes standing just inside the glass entrance of a bright, modern office lobby in the morning, holding a smartphone up at chest height toward the camera, screen facing us, as if showing it at a door. Soft daylight through the glass, blurred reception desk and plants behind him, calm and ordinary. The phone screen is plain solid white with no interface or text, fully visible, sharp. Natural colors, shallow depth of field, 50mm lens. Wide 3:2 composition, phone and hand in the right third, open space lower left. Realistic hands, five fingers.
>
> **Avoid:** masks or medical imagery, text on screen, logos, watermark, distorted hands, staged corporate stock look.

**Work tile (the sexiest image): the two result screens.**
Two iPhones side by side, front-facing with a slight fan: **OK To Enter (all green, checkmark, QR)** in front and **STOP (all red, X)** behind. Nothing else you have is as bold or as instantly understood.

**Hero:** the dashboard on a MacBook at an angle, with the phone overview in front. Re-render the current hero as a proper device render, not a canvas with margins.

**Case study shots:** Home; symptoms question; review and attest; the two result screens; dashboard (Attestation and Public Health panels); employee table with filters; phone overview; brand board; check-in recording.

### Vitae 27

**Work tile: three phones fanned out, one per state brand.** The same Enroll screen in DC, Maine and Massachusetts colors, front-facing, overlapping, the middle one forward. One shared layout with three different color identities is the whole idea, and it's visually striking.

**Hero:** a 3 × 2 grid of the same component in each brand, light mode on top and dark mode below, on the dark tile. Clean, flat, no devices.

**Case study shots:** the 3 × 2 brand grid; token table per brand; a Figma component beside its Storybook page (two browser frames side by side); a CI run with checks passing; a visual-regression diff.

### RegSearch

**Homepage card: context photo, someone reading a long document.**
An acquisition specialist at an office desk in soft afternoon light, leaning in toward a laptop, a printed regulation and a highlighter beside it. This shows who the tool is for, which a 2016 screenshot can't.

> **Prompt:** Candid photo of a woman in her 50s with reading glasses at a tidy government-office desk in soft afternoon light, leaning slightly toward an open laptop, focused. Beside the laptop: a thick printed binder open to a dense page, and a yellow highlighter. Muted, natural colors, shallow depth of field, 35mm. The laptop screen faces the camera at about 30 degrees, plain solid white with no interface or text, fully visible. Wide 3:2 composition, laptop in the right half, calm lower left for text.
>
> **Avoid:** text on screen, logos, flags, watermark, distorted hands, staged look.

**Work tile: MacBook at an angle showing the new reading pane,** with yellow search highlights and the purple header. The source screenshots are only 1000px, so either rebuild the key screen in Figma at 2x or run the existing one through an AI upscaler (Topaz Gigapixel, or Upscayl, which is free) before placing it.

**Hero:** the same render, wider.

**Case study shots:** before and after for search, document browser and sign-in (you have these; upscale to at least 2000px wide); search within search, bookmarks and document sets if you can find them.

### CDC Public Health Law

**Homepage card: the evaluation itself, not the CDC's brand.**
An annotated cdc.gov page with your red callout circles and priority labels, on a laptop on a desk, with a printed report or sticky notes beside it. This shows your judgment, which is the actual deliverable.

> **Prompt:** Overhead three-quarter photo of a clean wooden desk in soft daylight with an open laptop, a printed multi-page report with red pen marks, a few yellow sticky notes and a coffee cup. The laptop screen is plain solid white with no interface or text, fully visible, angled toward the camera. Calm, focused, natural colors, shallow depth of field. Wide 3:2 composition, laptop right of center, open space lower left.
>
> **Avoid:** text on screen or paper that's readable, logos, government seals, watermark, hands.

Place your annotated cdc.gov screenshot on the laptop screen.

**Work tile:** a MacBook at an angle showing the annotated page with red callouts.

**Hero:** the annotated page in the browser frame, large.

**Case study shots:** the three annotated finding images you have (upscale or re-export at 2x if possible).

### TakeCare

**Work tile: the brand on violet.** The TakeCare wordmark in white, large, on the deep violet (`#5A3F98`), with the three dots. Optionally add one real application (a badge on a lanyard, a phone showing a program page) angled in the corner. Bold color makes this the most eye-catching tile in the grid.

**Hero:** a brand flat-lay on violet: the logo, a lanyard badge, a tote or poster, the icon set. If you don't have photos of real applications, use a brand mockup set (Figma community mockups for badges, posters and totes) rather than AI.

**Case study shots:** before and after logo; lockups; palette; type specimen; program framework; icon set; 3–4 image-library photos at one crop; two brand book spreads.

### Major CRE Firm

**Work tile: MacBook at an angle showing the tagged wireframe,** with the blue backlog tags as the visual hook. Keep everything client-free.

**Hero:** the same render, wider.

**Case study shots:** requirements document; tagged wireframe; full wireframe set (already cleaned of the client name).

### IdeaCrew Rebrand

**Work tile:** the white lockup on Midnight Navy (already on the site) works. A stronger option is the marketing document spread as a printed mockup, angled on the navy background.

**Hero:** before and after logos (already on the site), or the T-shirt and mug photo.

**Case study shots:** already built from your deck.

### CrossFit Metropolis

**Work tile:** an iPhone showing the new homepage hero photo ("Health. Happiness. Fitness."), angled on the dark tile, or a crop of a shoot photo with the phone in a hand.

**Hero:** the existing desktop-and-phone mockup, re-rendered on `#1E2024` and trimmed so it fills the frame.

**Case study shots:** before and after homepage (you have these); 2–3 photos from the shoot.

### Extras

**Work tile:** a 2 × 2 grid of your four strongest logos (Herndon Farm to Table, Champions in Action, Rampage F.C., Pizza King), each on its own color, instead of one logo.

### SNOWATCH, ERGO, London, BEN

These are physical products, so their own renders and photos are the right imagery, as with his hardware projects. They just need consistent framing.
- **Work tiles:** crop each hero tight so the product fills 70–80% of the tile: the SNOWATCH sleeve on the jacket, the ERGO prototype on the wrist, the London fountain render, BEN in use.
- **Optional:** re-photograph or re-render on a seamless background to match the set.

---

## 5. Order of work

1. **Enroll App:** the homepage photo, Work tile and raw screens. This is the pilot, and I'll rebuild its case study with the frames as soon as they arrive.
2. **WorkRadar Work tile** (the two result phones). It's the fastest big win, since the screens already exist.
3. **Homepage photos** for WorkRadar, RegSearch and CDC.
4. **Work tiles** for the rest, using the same device preset.
5. **Remaining case study shots,** project by project, following the placeholders on each page.

When files are ready, attach them in the chat with descriptive names (`enroll-tile.png`, `enroll-home.jpg`, `enroll-01-personal.png`…). I'll place them, update the card shapes, and send screenshots to review.
