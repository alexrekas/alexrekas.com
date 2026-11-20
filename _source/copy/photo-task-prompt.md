# Prompt: turn my portfolio shot list into a task list

> Paste everything below into a new Claude chat. Attach **shot-list-preview.pdf** (same folder) so Claude can see the current images.

---

I'm Alex Rekas, a product designer rebuilding my portfolio site, alexrekas.com. The site is built and the copy is final. What's left is imagery. Below is an inventory of every image slot that needs work from me, with exactly what each image should show, the size to export and the filename to send it as. The attached PDF shows each of these slots with the image that's there now (or an empty placeholder), in the same order.

**Please turn this into a practical task list I can work through**, in this shape:

1. **Group tasks into work sessions by tool**, not by page, so I do all the similar work at once. Likely sessions:
   - **Figma and app exports:** raw screens and crops from my files (fastest, and several later tasks depend on them).
   - **Device renders:** laptops and phones at an angle, using one tool and one saved preset for all of them (Rotato or Shots.so).
   - **AI context photos plus compositing:** generate a scene with a blank screen, then place my real screenshot onto the screen in Photoshop or Figma.
   - **Upscaling and re-exports:** older images that are the right content but too small.
   - **Digging through archives:** things I may or may not still have.
2. **Order by dependency.** For example, the WorkRadar OK to Enter and STOP screens are used on the case study page, the Work tile and the homepage photo, so export them first. The same goes for the upscaled RegSearch screen.
3. **Within that, order by priority:** Priority 1 is the four featured projects (Enroll App, WorkRadar, RegSearch and CDC), the four homepage cards and the Work page tiles. Priority 2 is Vitae 27, TakeCare, the CRE project, IdeaCrew Rebrand and CrossFit. Priority 3 is older work.
4. **Each task is a checkbox** with: what to make (specific enough that I don't have to come back and ask), the source (which file, app or screen), the export size, the filename to send it as, and a rough time estimate.
5. **End with a "send to Claude" checklist:** every filename, so I can tick them off as I hand files over. My site Claude will place them, frame them and check them.
6. **Flag anything that needs a decision or permission** before I spend time on it. For example: client-owned photos, screenshots of an employer's CI, or a slot to remove if I can't find the material.

Keep it in plain language. Don't add new image ideas or new slots; work only from this list. If something in the list is ambiguous, say so in a short "questions" section at the top rather than guessing.

## How the site's images work

- The site is dark. Its tile color is **#1E2024**, and the page background is #0F1012.
- **Case study screens are exported raw:** just the UI, with no device, frame or background. The site draws the browser or phone frame and the tile around them, so everything matches. Don't bake in frames, shadows or colored canvases.
- **Device renders** (Work tiles and some heroes) use one device set: iPhone 16 Pro in Black Titanium, and MacBook Pro 14" in Space Black. Single device: three-quarter view, turned about 20° and tilted about 8°. Phone pairs: front-facing, slightly overlapping. Laptop plus phone: laptop behind at an angle, phone in front overlapping its corner. Soft light from the top left, a subtle rim light so dark devices separate from the dark background, and a soft contact shadow. The device fills 70–80% of the frame. Render on #1E2024 or as a transparent PNG. Save the angle and lighting as a preset so every render matches.
- **Homepage cards** are wide 3:2 photos (2400 × 1600). The project name, tagline and tags overlay the bottom-left third on a dark shade, so keep that area calm.
- **AI can't render my actual UI convincingly.** For context photos, generate the scene with a plain white screen, then place the real screenshot onto it (perspective warp, slight glare, match the room's brightness).
- **Sharpness rule:** every image must be at least twice as wide as it appears on a 1440 px screen. Raw desktop screens: about 2880 px wide. Raw phone screens: 780 × 1688.
- Use realistic but fake data, with one sample person per project (Enroll uses "Chris Smith").

## Rules that can't be broken

- The commercial real estate client stays unnamed: no client logo or name anywhere, including inside screenshots.
- WorkRadar never launched. Its photo is illustrative, so keep it ordinary, with no real company branding.
- The CDC homepage photo shows my evaluation work, not CDC branding: no seals or logos.
- No readable fake text in AI photos (papers, screens, signs).
- Client-owned material (Marriott photos, IdeaCrew CI screenshots) needs permission before it goes on a public site.

## AI photo prompts for the three remaining homepage cards

The Enroll App card is done (MacBook and iPhone renders).

Use these as the starting prompt; place the real screen afterward.

**WorkRadar:** Candid photo of a man in his 30s in business-casual clothes standing just inside the glass entrance of a bright, modern office lobby in the morning, holding a smartphone up at chest height toward the camera, screen facing us, as if showing it at a door. Soft daylight through the glass, blurred reception desk and plants behind him. The phone screen is plain solid white, fully visible, sharp. Natural colors, shallow depth of field, 50mm lens. Wide 3:2, phone and hand in the right third, open space lower left. *Avoid:* masks or medical imagery, text on screen, logos, watermark, distorted hands, staged corporate look.

**RegSearch:** Candid photo of a woman in her 50s with reading glasses at a tidy government-office desk in soft afternoon light, leaning slightly toward an open laptop, focused. Beside the laptop: a thick printed binder open to a dense page, and a yellow highlighter. Muted, natural colors, shallow depth of field, 35mm. The laptop screen faces the camera at about 30 degrees, plain solid white, fully visible. Wide 3:2, laptop in the right half, calm lower left. *Avoid:* text on screen, logos, flags, watermark, distorted hands.

**CDC:** Overhead three-quarter photo of a clean wooden desk in soft daylight with an open laptop, a printed multi-page report with red pen marks, a few yellow sticky notes and a coffee cup. The laptop screen is plain solid white, fully visible, angled toward the camera. Calm, natural colors, shallow depth of field. Wide 3:2, laptop right of center, open space lower left. *Avoid:* readable text on screen or paper, logos, government seals, watermark, hands.

## The inventory

Status key: **Add** = empty slot; **Replace** = the current image is the wrong kind, make something new; **Sharper copy** = the right image, export it again bigger. Slots marked "Done", "Keep" or "Claude does it" (re-crops my site Claude will handle) are left out of both this list and the PDF.


### Homepage featured work (Priority 1)

- [ ] **Replace · Homepage card: WorkRadar**
  - What to make: Context photo: a man in his 30s in business-casual clothes just inside the glass entrance of a bright office lobby in the morning, holding his phone up toward the camera as if showing it at the door. The phone shows the all-green OK to Enter screen with the checkmark and QR code. Make the scene with a blank white phone screen, then place workradar-03-results-v2 (green half) onto it. Keep it ordinary: no masks, no real company branding. Today's image is a tall portrait image squeezed into a wide card, with empty dark bands on both sides.
  - Now: `workradar-tile-interim.png`, 1600 × 2000 px, shown 588 px wide
  - Send as: `workradar-home.jpg`
  - Size: Landscape 3:2, 2400 × 1600 JPG. Keep the bottom-left third calm: the project name, tagline and tags sit there on a dark shade.
- [ ] **Replace · Homepage card: RegSearch**
  - What to make: Context photo: a woman in her 50s with reading glasses at a tidy office desk in soft afternoon light, leaning toward an open laptop, a thick printed binder and a yellow highlighter beside it. The laptop shows the new RegSearch reading pane with yellow search highlights. Make the scene with a blank white laptop screen, then place the RegSearch screen onto it. The screen source is only 1000 px wide: upscale it first (Upscayl is free) or rebuild it in Figma at 2x. Today's image is that 1000 px screenshot fitted into the wide card, so it's soft and letterboxed.
  - Now: `regsearch-new3.png`, 1000 × 650 px, shown 588 px wide
  - Send as: `regsearch-home.jpg`
  - Size: Landscape 3:2, 2400 × 1600 JPG. Keep the bottom-left third calm: the project name, tagline and tags sit there on a dark shade.
- [ ] **Replace · Homepage card: CDC Public Health Law**
  - What to make: Context photo of the evaluation itself, not the CDC's brand: a three-quarter overhead view of a wooden desk in daylight with an open laptop, a printed report with red pen marks, yellow sticky notes and a coffee cup. The laptop shows one of your annotated cdc.gov pages with red callout circles (cdc-1). No readable text on paper, no government seals. Today's image is a 400 px stock photo of a child with the CDC logo, stretched to fill the card, so it's blurry and shows the client's brand instead of your work.
  - Now: `thumbnail400x400.png`, 400 × 400 px, shown 588 px wide
  - Send as: `cdc-home.jpg`
  - Size: Landscape 3:2, 2400 × 1600 JPG. Keep the bottom-left third calm: the project name, tagline and tags sit there on a dark shade.

### Work page tiles (Priority 1)

- [ ] **Replace · Work tile: WorkRadar**
  - What to make: Two iPhones, front-facing in a slight fan: OK to Enter (all green, checkmark, QR code) in front, STOP (all red, X) behind and to one side. Both screens already exist in workradar-03-results-v2.png; export each one alone at 780 × 1688 and render. Today's tile is a tall 4:5 image fitted into the square, so it sits small with empty space around it.
  - Now: `workradar-tile-interim.png`, 1600 × 2000 px, shown 373 px wide
  - Send as: `workradar-tile.png`
  - Size: Square 1:1, 1600 × 1600. Device render on #1E2024 (the site's tile color) or a transparent PNG.
- [ ] **Add · Work tile: Vitae 27**
  - What to make: Three iPhones fanned out, the middle one forward, each showing the same Enroll screen in a different state brand: DC, Maine and Massachusetts. One layout with three color identities is the whole point of Vitae 27. Take the three screens from the Vitae Storybook or app at phone width (780 × 1688 each).
  - Now: empty placeholder
  - Send as: `vitae-tile.png`
  - Size: Square 1:1, 1600 × 1600. Device render on #1E2024 (the site's tile color) or a transparent PNG.
- [ ] **Replace · Work tile: RegSearch**
  - What to make: A MacBook at a three-quarter angle showing the new RegSearch reading pane: the slim table of contents on the left, the wide document with yellow search highlights, the purple header. Upscale or rebuild the 1000 px screen first. Today's tile is the 400 px purple wordmark tile from the old site.
  - Now: `regsearch-thumbnail.png`, 400 × 400 px, shown 373 px wide
  - Send as: `regsearch-tile.png`
  - Size: Square 1:1, 1600 × 1600. Device render on #1E2024 (the site's tile color) or a transparent PNG.
- [ ] **Replace · Work tile: CDC Public Health Law**
  - What to make: A MacBook at a three-quarter angle showing one of your annotated cdc.gov pages with the red callout circles (cdc-1 or cdc-2). Today's tile is the same blurry 400 px stock photo as the homepage card.
  - Now: `thumbnail400x400.png`, 400 × 400 px, shown 373 px wide
  - Send as: `cdc-tile.png`
  - Size: Square 1:1, 1600 × 1600. Device render on #1E2024 (the site's tile color) or a transparent PNG.
- [ ] **Replace · Work tile: Major CRE Firm**
  - What to make: A MacBook at a three-quarter angle showing the tagged CRM wireframe (cre-wireframe-tagged), with the blue backlog tags as the visual hook. Nothing that names the client. Today's tile is the old 400 px '[REDACTED]' over a photo of skyscrapers.
  - Now: `website-ProjectThumbnail-redacted.jpg`, 400 × 400 px, shown 373 px wide
  - Send as: `cre-tile.png`
  - Size: Square 1:1, 1600 × 1600. Device render on #1E2024 (the site's tile color) or a transparent PNG.
- [ ] **Replace · Work tile: CrossFit Metropolis**
  - What to make: An iPhone at an angle showing the new CrossFit Metropolis homepage hero (the athlete photo with 'Health. Happiness. Fitness.'), or a crop of one of your shoot photos with the phone in a hand. Today's tile is the 400 px gym logo on a grunge texture from the old site.
  - Now: `CFM1.png`, 400 × 400 px, shown 373 px wide
  - Send as: `crossfit-tile.png`
  - Size: Square 1:1, 1600 × 1600. Device render on #1E2024 (the site's tile color) or a transparent PNG.

### Enroll App (Priority 1)

- [ ] **Sharper copy · New employer sign-up**
  - Caption on the site: “Step one asks only for the account holder's details.”
  - What to make: Step one, Personal Information, filled in with the sample person Chris Smith. Re-export from Figma as a raw screen so the site can frame it; today's file has the frame baked in and is only 1060 px wide.
  - Now: `enroll-newemployer-01b-personal-dark.png`, 1060 × 774 px, shown 580 px wide
  - Send as: `enroll-01-personal.png`
  - Size: Raw desktop screen, about 2880 px wide (2x of 1440). No device, frame or background: the site adds the browser frame.
- [ ] **Sharper copy · New employer sign-up**
  - Caption on the site: “Legal name, FEIN, entity type and office locations get a step of their own.”
  - What to make: Step two, Business Information, with legal name, FEIN, entity type and one office location filled in. Raw re-export.
  - Now: `enroll-newemployer-02-business-dark.png`, 1060 × 774 px, shown 580 px wide
  - Send as: `enroll-02-business.png`
  - Size: Raw desktop screen, about 2880 px wide (2x of 1440). No device, frame or background: the site adds the browser frame.
- [ ] **Sharper copy · New employer sign-up**
  - Caption on the site: “Employers choose electronic, paper or both for official notices.”
  - What to make: Step three, Communication, with one notice option selected. Raw re-export.
  - Now: `enroll-newemployer-03-communication-dark.png`, 1060 × 774 px, shown 580 px wide
  - Send as: `enroll-03-communication.png`
  - Size: Raw desktop screen, about 2880 px wide (2x of 1440). No device, frame or background: the site adds the browser frame.
- [ ] **Sharper copy · New employer sign-up**
  - Caption on the site: “A clear finish: a confirmation email follows once the account is approved.”
  - What to make: The Complete screen. Raw re-export.
  - Now: `enroll-newemployer-04-complete-dark.png`, 1060 × 774 px, shown 580 px wide
  - Send as: `enroll-04-complete.png`
  - Size: Raw desktop screen, about 2880 px wide (2x of 1440). No device, frame or background: the site adds the browser frame.
- [ ] **Sharper copy · New employer sign-up**
  - Caption on the site: “One long form became three focused steps.”
  - What to make: The 'After' beside the old form: the new step one on a laptop. Today's file is only 600 px wide. A crop of the new hero render works, or the raw Personal Information screen and I'll frame it.
  - Now: `enroll-newemployer-desktop.png`, 600 × 400 px, shown 580 px wide
  - Send as: `enroll-after.png`
  - Size: At least 1600 px wide.
- [ ] **Sharper copy · Phone first**
  - Caption on the site: “The same three steps, designed for phone first.”
  - What to make: The three steps at phone width (Personal, Business, Communication). Send the three raw phone screens and I'll arrange them in a row; today's file is a 1604 px composite with baked-in phones.
  - Now: `enroll-newemployer-05-phones-dark.png`, 1604 × 978 px, shown 1200 px wide
  - Send as: `enroll-05-phone-personal.png, enroll-05-phone-business.png, enroll-05-phone-communication.png`
  - Size: Raw phone screen, 780 × 1688 (390 × 844 at 2x). No device frame: the site adds it. Three files.
- [ ] **Add · Eligibility results**
  - Caption on the site: “Results first, in plain language.”
  - What to make: The eligibility results screen at phone width, for Chris Smith: the result at the top in plain language (can shop for plans; qualifies for tax credits or other help), then one clear next-step button.
  - Now: empty placeholder
  - Send as: `enroll-06-results-phone.png`
  - Size: Raw phone screen, 780 × 1688 (390 × 844 at 2x). No device frame: the site adds it.
- [ ] **Add · Eligibility results**
  - Caption on the site: “One clear next step.”
  - What to make: The screen people land on after tapping the next-step button on the results screen: plan shopping, or a confirmation. Phone width.
  - Now: empty placeholder
  - Send as: `enroll-07-next-step.png`
  - Size: Raw phone screen, 780 × 1688 (390 × 844 at 2x). No device frame: the site adds it.
- [ ] **Add · Help on every screen**
  - What to make: The language switch opened, showing English, Español and Amharic. A crop around the header and the open menu is enough.
  - Now: empty placeholder
  - Send as: `enroll-08-language.png`
  - Size: Detail crop, at least 1600 px wide, no frame.
- [ ] **Add · Help on every screen**
  - What to make: The help line with the TTY number, cropped from the footer or help area.
  - Now: empty placeholder
  - Send as: `enroll-09-help.png`
  - Size: Detail crop, at least 1600 px wide, no frame.
- [ ] **Add · Help on every screen**
  - What to make: The SSN field with the 'I don't have an SSN' option visible, ideally checked so the field is shown as not required. Check the exact label in the app: the site quotes it as 'I don't have an SSN'; tell Claude if the app says something else.
  - Now: empty placeholder
  - Send as: `enroll-10-ssn.png`
  - Size: Detail crop, at least 1600 px wide, no frame.
- [ ] **Add · Accessible by default**
  - Caption on the site: “Focus, error and disabled states meet WCAG 2.1 AA contrast.”
  - What to make: One image showing a text field and a button in their default, focus, error and disabled states side by side, from the Figma design system, with the focus ring and error message visible.
  - Now: empty placeholder
  - Send as: `enroll-11-states.png`
  - Size: At least 2400 px wide, from Figma, on a plain background.
- [ ] **Add · Accessible by default**
  - Caption on the site: “Accessibility rules live in the system, so new screens inherit them.”
  - What to make: The design system's color and type tokens page from Figma: swatches with names and hex values, and the type scale.
  - Now: empty placeholder
  - Send as: `enroll-12-tokens.png`
  - Size: At least 2400 px wide, from Figma.
- [ ] **Add · Rolling it out**
  - Caption on the site: “The new employer flow, from the interactive prototype.”
  - What to make: A screen recording of the new employer prototype in Figma, from Personal Information through Complete, at a steady pace with no cursor wandering.
  - Now: empty placeholder
  - Send as: `enroll-flow.mp4 + enroll-flow-poster.png`
  - Size: MP4 (H.264), 1920 × 1080 or larger, muted, 20–30 seconds, under 5 MB, plus a PNG of the first frame.

### WorkRadar (Priority 1)

- [ ] **Replace · Hero image (top of the page)**
  - What to make: A device render: the management dashboard on a MacBook at an angle, with the phone overview on an iPhone in front. Today's hero is a flat composite with margins baked in.
  - Now: `workradar-00-hero-v2.png`, 2008 × 1189 px, shown 1200 px wide
  - Send as: `workradar-hero.png`
  - Size: 16:9, 2400 × 1350, on #1E2024 or transparent.
- [ ] **Sharper copy · A result you can't misread**
  - Caption on the site: “Come in, or stay home. Nothing in between.”
  - What to make: The OK to Enter and STOP screens. Export each on its own from Figma (you'll need them for the Work tile and homepage anyway) and I'll place them side by side.
  - Now: `workradar-03-results-v2.png`, 1150 × 1052 px, shown 0 px wide
  - Send as: `workradar-ok.png, workradar-stop.png`
  - Size: Raw phone screen, 780 × 1688 (390 × 844 at 2x). No device frame: the site adds it. Two files.
- [ ] **Add · A brand for an anxious moment**
  - Caption on the site: “The employee check-in, from the interactive prototype.”
  - What to make: A recording of the employee check-in prototype at phone size: Home, the two questions, the summary, then the OK to Enter result.
  - Now: empty placeholder
  - Send as: `workradar-checkin.mp4 + poster PNG`
  - Size: MP4 (H.264), portrait phone size, muted, 20–30 seconds, under 5 MB, plus a PNG of the first frame.

### Vitae 27 (Priority 2)

- [ ] **Add · Hero image (top of the page)**
  - What to make: The same Enroll screen in the DC, Maine and Massachusetts brands, side by side. Send the three raw screens and I'll lay them out, or a finished composite.
  - Now: empty placeholder
  - Send as: `vitae-hero-dc.png, vitae-hero-me.png, vitae-hero-ma.png`
  - Size: Raw desktop screen, about 2880 px wide (2x of 1440). No device, frame or background: the site adds the browser frame. Three files.
- [ ] **Add · One system, three brands**
  - Caption on the site: “One token set, three brands, light and dark.”
  - What to make: One component (a card or a form block with a button) in each brand, in light and dark mode: six crops of the same size. I'll assemble the 3 × 2 grid.
  - Now: empty placeholder
  - Send as: `vitae-dc-light.png … vitae-ma-dark.png (6 files)`
  - Size: Same crop for all six, at least 1200 px wide each, from Storybook.
- [ ] **Add · One system, three brands**
  - Caption on the site: “Brands differ only in their tokens.”
  - What to make: A table of the token values per brand: color, type and spacing side by side. A screenshot of the token docs page in Storybook works.
  - Now: empty placeholder
  - Send as: `vitae-tokens.png`
  - Size: At least 2400 px wide.
- [ ] **Add · From Figma to production**
  - Caption on the site: “Figma is the source; Storybook shows what ships.”
  - What to make: The same component in Figma and on its Storybook page. Two raw screenshots; I'll frame and pair them.
  - Now: empty placeholder
  - Send as: `vitae-figma.png, vitae-storybook.png`
  - Size: Raw desktop screen, about 2880 px wide (2x of 1440). No device, frame or background: the site adds the browser frame. Two files.
- [ ] **Add · Accessibility on every change**
  - Caption on the site: “Every change is checked before it ships.”
  - What to make: A CI run with the accessibility and visual-regression jobs passing (green checks). Crop to the job list. Make sure nothing private shows (repo secrets, internal URLs, colleagues' names), and that IdeaCrew is OK with it being public.
  - Now: empty placeholder
  - Send as: `vitae-ci.png`
  - Size: Crop, at least 1600 px wide.
- [ ] **Add · Accessibility on every change**
  - Caption on the site: “Layout changes get flagged before they reach a state.”
  - What to make: A visual-regression report showing a caught change: before, after and the highlighted diff.
  - Now: empty placeholder
  - Send as: `vitae-diff.png`
  - Size: Crop, at least 1600 px wide.

### RegSearch (Priority 1)

- [ ] **Replace · Hero image (top of the page)**
  - What to make: The same MacBook render as the Work tile, composed wider. Today's hero is the 1000 px screenshot, so it can't fill the page width.
  - Now: `regsearch-new3.png`, 1000 × 650 px, shown 1000 px wide
  - Send as: `regsearch-hero.png`
  - Size: 16:9, 2400 × 1350.
- [ ] **Add · Two kinds of research**
  - What to make: Only if you can find them: screens of search within search, bookmarks or document sets. If you can't, tell Claude to remove this slot.
  - Now: empty placeholder
  - Send as: `regsearch-04-features.png`
  - Size: Any size you have; at least 1600 px wide if possible.
- [ ] **Sharper copy · Brand**
  - Caption on the site: “The new mark set the palette and icon language for the product.”
  - What to make: The RegSearch wordmark in white on deep purple, with the magnifying-glass loop in the G. Export it from your original logo file as an SVG, or a PNG at least 1600 px wide; today's copy is 400 px.
  - Now: `regsearch-thumbnail.png`, 400 × 400 px, shown 400 px wide
  - Send as: `regsearch-logo.svg`
  - Size: SVG, or PNG at least 1600 px wide.

### CDC Public Health Law (Priority 1)

- [ ] **Add · Hero image (top of the page)**
  - What to make: The strongest annotated cdc.gov page with your red callouts, large. If you still have the original evaluation file, re-export at 2x; otherwise send what you have and I'll upscale it.
  - Now: empty placeholder
  - Send as: `cdc-hero.png`
  - Size: At least 2400 px wide.
- [ ] **Sharper copy · High priority: pages too dense to scan**
  - Caption on the site: “Long, tightly packed pages made it hard to see where sections begin and end.”
  - What to make: Shows: Three tall cdc.gov Public Health Law pages side by side, with a red circle marking a dense block of text that runs together. It's 530 px wide but shown 530 px wide, so it's soft. Re-export the same image from the original evaluation file, if you still have it at 1060 px wide or more.
  - Now: `cdc-1.png`, 530 × 486 px, shown 530 px wide
  - Send as: `cdc-1.png`
  - Size: At least 1060 px wide.
- [ ] **Sharper copy · Moderate priority: heavy modules**
  - Caption on the site: “Heavy modules pulled attention away from the most important resource.”
  - What to make: Shows: The CDC About page with numbered callouts on its heavy, blue office-directory modules and numbers set as images. It's 500 px wide but shown 500 px wide, so it's soft. Re-export the same image from the original evaluation file, if you still have it at 1000 px wide or more.
  - Now: `cdc-3b.png`, 500 × 397 px, shown 500 px wide
  - Send as: `cdc-3b.png`
  - Size: At least 1000 px wide.
- [ ] **Sharper copy · Low priority: small polish**
  - Caption on the site: “A one-line CSS fix for a visible rendering bug.”
  - What to make: Shows: Close-ups of cdc.gov cards with callouts magnifying gaps in their rounded corners. It's 565 px wide but shown 565 px wide, so it's soft. Re-export the same image from the original evaluation file, if you still have it at 1130 px wide or more.
  - Now: `cdc-2.png`, 565 × 396 px, shown 565 px wide
  - Send as: `cdc-2.png`
  - Size: At least 1130 px wide.

### TakeCare (Priority 2)

- [ ] **Sharper copy · Hero image (top of the page)**
  - What to make: The wordmark sheet: violet and black on white, white on violet and on black. Re-export from the brand files at 2x. If you have real applications (badge, tote, poster), a flat-lay on violet would make a stronger hero.
  - Now: `takecare-logo-lockup1b.png`, 1157 × 714 px, shown 1157 px wide
  - Send as: `takecare-hero.png`
  - Size: At least 2400 px wide.
- [ ] **Sharper copy · The mark**
  - Caption on the site: “From a corporate wordmark to a warmer, lifestyle-brand mark.”
  - What to make: The new wordmark (the 'After'): TAKE in light capitals, CARE in bold, three violet dots. Export as an SVG from the brand files; today's copy is 531 px wide.
  - Now: `TakeCare-logo.png`, 531 × 64 px, shown 531 px wide
  - Send as: `takecare-wordmark.svg`
  - Size: SVG, or PNG at least 1200 px wide.
- [ ] **Add · Imagery**
  - What to make: Three or four photos from the TakeCare image library (stock and associate photos), all at the same crop. These are Marriott's images, so make sure you're OK to show them.
  - Now: empty placeholder
  - Send as: `takecare-photo-1.jpg … takecare-photo-4.jpg`
  - Size: Same 4:5 crop for each, at least 1200 px wide.
- [ ] **Add · Brand book and templates**
  - What to make: Two spreads from the TakeCare brand book, exported flat (not photographed).
  - Now: empty placeholder
  - Send as: `takecare-book-1.png, takecare-book-2.png`
  - Size: At least 2400 px wide each.
- [ ] **Sharper copy · Brand book and templates**
  - Caption on the site: “An icon set teams can build on.”
  - What to make: Shows: Fourteen violet TakeCare icons, including a piggy bank, globe, speech bubbles, a head with a gear, a lotus and a heart. It's 1500 px wide but shown 1200 px wide, so it's soft. Re-export the same image from the brand files at 2400 px wide or more.
  - Now: `takecare-iconset.png`, 1500 × 350 px, shown 1200 px wide
  - Send as: `takecare-iconset.png`
  - Size: At least 2400 px wide.

### Major CRE Firm (Priority 2)

- [ ] **Add · Hero image (top of the page)**
  - What to make: The same MacBook render as the Work tile (the tagged wireframe), composed wider. No client name anywhere.
  - Now: empty placeholder
  - Send as: `cre-hero.png`
  - Size: 16:9, 2400 × 1350.
- [ ] **Sharper copy · Learning a process nobody knew**
  - Caption on the site: “Requirements for the debt workflow, gathered into one working document.”
  - What to make: Shows: A spreadsheet of debt-workflow requirements with columns for each requirement, notes and status. It's 960 px wide but shown 960 px wide, so it's soft. Re-export the same image from the original wireframe file (keep the client name out) at 1920 px wide or more.
  - Now: `cre-requirements.png`, 960 × 550 px, shown 960 px wide
  - Send as: `cre-requirements.png`
  - Size: At least 1920 px wide.
- [ ] **Sharper copy · Wireframes tied to the backlog**
  - Caption on the site: “Each part of the wireframe is tagged with the backlog item that builds it.”
  - What to make: Shows: A dark CRM wireframe with blue tags on each area naming the backlog item that builds it. It's 1602 px wide but shown 1200 px wide, so it's soft. Re-export the same image from the original wireframe file (keep the client name out) at 2400 px wide or more.
  - Now: `cre-wireframe-tagged.png`, 1602 × 998 px, shown 1200 px wide
  - Send as: `cre-wireframe-tagged.png`
  - Size: At least 2400 px wide.

### IdeaCrew Rebrand (Priority 2)

- [ ] **Sharper copy · Hero image (top of the page)**
  - What to make: Shows: The old IdeaCrew logo, a lightbulb outline with an ampersand inside, beside the new one: a simpler bulb outline with a plus, and the same IDEACREW wordmark. It's 1684 px wide but shown 1200 px wide, so it's soft. Re-export the same image from the rebrand deck or Figma file at 2400 px wide or more.
  - Now: `ideacrew-before-after.png`, 1684 × 454 px, shown 1200 px wide
  - Send as: `ideacrew-before-after.png`
  - Size: At least 2400 px wide.
- [ ] **Sharper copy · Research**
  - Caption on the site: “Six themes to explore, from light to health care.”
  - What to make: Shows: Four photos for the themes explored: hanging lightbulbs, glowing circuitry, a large ampersand and the Washington Monument. It's 864 px wide but shown 580 px wide, so it's soft. Re-export the same image from the rebrand deck or Figma file at 1160 px wide or more.
  - Now: `ideacrew-themes.png`, 864 × 868 px, shown 580 px wide
  - Send as: `ideacrew-themes.png`
  - Size: At least 1160 px wide.
- [ ] **Sharper copy · Exploration**
  - Caption on the site: “Four finalist directions.”
  - What to make: Shows: Four IdeaCrew logo concepts: a blue open-circle mark with a geometric sans wordmark, a split-C mark with a serif wordmark, a lightbulb mark with a bold serif wordmark and an interlocking-bracket mark with a monospace wordmark. It's 1600 px wide but shown 1200 px wide, so it's soft. Re-export the same image from the rebrand deck or Figma file at 2400 px wide or more.
  - Now: `ideacrew-logo-concepts.png`, 1600 × 1200 px, shown 1200 px wide
  - Send as: `ideacrew-logo-concepts.png`
  - Size: At least 2400 px wide.
- [ ] **Sharper copy · The decision**
  - Caption on the site: “The evolved mark across light and dark backgrounds.”
  - What to make: Shows: The new IdeaCrew lockup and standalone mark shown in five color treatments, on white, navy and black. It's 581 px wide but shown 480 px wide, so it's soft. Re-export the same image from the rebrand deck or Figma file at 960 px wide or more.
  - Now: `ideacrew-reasoning-lockups.png`, 581 × 724 px, shown 480 px wide
  - Send as: `ideacrew-reasoning-lockups.png`
  - Size: At least 960 px wide.
- [ ] **Sharper copy · The system**
  - Caption on the site: “A 40/40/10/10 color split.”
  - What to make: Shows: The palette: large Midnight Navy and Royal Blue blocks, with smaller Deep Plum and Sky accents. It's 810 px wide but shown 580 px wide, so it's soft. Re-export the same image from the rebrand deck or Figma file at 1160 px wide or more.
  - Now: `ideacrew-colors.png`, 810 × 812 px, shown 580 px wide
  - Send as: `ideacrew-colors.png`
  - Size: At least 1160 px wide.
- [ ] **Sharper copy · The system**
  - Caption on the site: “IBM Plex Serif Medium as the default typeface.”
  - What to make: Shows: IBM Plex Serif Medium specimen with the alphabet and numerals. It's 788 px wide but shown 580 px wide, so it's soft. Re-export the same image from the rebrand deck or Figma file at 1160 px wide or more.
  - Now: `ideacrew-type.png`, 788 × 907 px, shown 580 px wide
  - Send as: `ideacrew-type.png`
  - Size: At least 1160 px wide.
- [ ] **Sharper copy · In use**
  - Caption on the site: “The mark on apparel and merchandise.”
  - What to make: Shows: A navy IdeaCrew T-shirt with the small bulb mark, and a white mug with the IdeaCrew lockup. It's 1330 px wide but shown 1200 px wide, so it's soft. Re-export the same image from the rebrand deck or Figma file at 2400 px wide or more.
  - Now: `ideacrew-in-use.png`, 1330 × 669 px, shown 1200 px wide
  - Send as: `ideacrew-in-use.png`
  - Size: At least 2400 px wide.

### CrossFit Metropolis (Priority 2)

- [ ] **Add · Photography that sells the feeling**
  - What to make: Two or three photos from the professional shoot, showing the four themes: fitter New Yorkers, a program that works for me, community, health and happiness.
  - Now: empty placeholder
  - Send as: `crossfit-photo-1.jpg … crossfit-photo-3.jpg`
  - Size: Landscape, at least 1600 px wide.

## Not for me (my site Claude handles these)

- Work page tiles: TakeCare. The white TakeCare wordmark and three dots on violet is right. It's a 4:5 file cropped to a square, so I'll re-lay it out as a true square myself. Optional upgrade from you: a real application (a lanyard badge or a phone showing a program page) angled in one corner.
- Work page tiles: Extras. The 2 × 2 logo grid (Herndon Farm to Table, Champions in Action, Rampage F.C., Pizza King) is right, but it's laid out 4:5 and fitted into the square. I'll rebuild it as a square from the logo files you already gave me.
- Work page tiles: SNOWATCH. A crop of the SNOWATCH hero. I can make a sharper square crop from the 2000 px hero myself.
- Work page tiles: ERGO. A crop of the ERGO hero. Sharp enough; I'll re-crop it as a true square.
- Work page tiles: London. A crop of the London fountain render. Sharp enough; I'll re-crop it as a true square.
- Work page tiles: BEN. A crop of the BEN bench photo. Sharp enough; I'll re-crop it as a true square.
