# Case study copy deck

Approved copy for every project, written to match how gabrielvaldivia.com structures its case studies. Approved November 13, 2026 and applied to the site. Edit here first if the copy changes.

## How these are written

Every case study follows the same shape:

- **Tagline:** one line under the title.
- **Facts:** Years, the Company you worked for (and the Client, for agency work), Role and Services.
- **Overview:** what the product is, who it's for, what was wrong, your role, and the real result. Three to five sentences.
- **Sections named after parts of the product,** not process steps. Each says what that part does for the person using it, and one decision you made and why.
- **Images:** under each section, a list of what to show. This is the shot list for the imagery pass later.

Rules kept throughout: no invented numbers, quotes or outcomes; Enroll is a redesign, not a 0-to-1 build; WorkRadar never launched; no claims of managing people; code work is described as directing AI agents. Anything I couldn't confirm is a **(FILL IN: …)** with the question you need to answer.

Featured projects run about 450–650 words, like his main case studies. Smaller projects run 100–250 words.

---

## 1. Enroll App

**Tagline:** Health coverage enrollment, rebuilt mobile-first

**Facts**
- Years: 2020–present
- Company: IdeaCrew
- Role: Design Lead
- Services: Product design, Accessibility, Research, Design system

**Overview**
Enroll App runs the health insurance marketplaces for Washington, DC, Maine and Massachusetts. It's where people apply for coverage, find out what help they qualify for, and pick a plan, and where small businesses set up coverage for their employees. The app was built on Bootstrap 3 with no real mobile support, and an accessibility audit found problems serious enough to stop some people with disabilities from enrolling at all. I was design lead on a $1M+ modernization that moved the platform to Bootstrap 4 and 5, and I led the redesign of the enrollment experience on top of it: mobile-first, WCAG 2.1 AA and Section 508 compliant, and built on a new Figma design system. The redesign is live in Maine's Individual Market, and DC's migration is planned for 2026–2027.

**New employer sign-up**
Small businesses used to set up coverage on one long page: their own details, the company's details, office locations and notice preferences, all ending in a red Confirm button. I split it into three short steps, Personal Information, Business Information and Communication, with a progress rail that always shows where you are and what's left.

Each step asks about one thing, and Continue only unlocks once the required fields are done, so nobody reaches the end and finds a list of errors. Owners often need to stop and find a document like their FEIN, so Save & Exit lets them leave and pick up where they left off next time they log in. The last screen says plainly what happens next: a confirmation email once the account is approved.

*Images:* Personal Information (filled in) · Business Information with office location · Communication preferences · Complete screen · Before and after: the old single page beside the new first step

**Phone first**
A large share of marketplace users only have a phone, and the old app didn't work on one. Every step of the new flow was designed at phone width first, then expanded for desktop. Fields stack in a single column, the main action stays at the bottom of each step, and nothing needs horizontal scrolling.

*Images:* Three phones: Personal Information, Business Information, Communication · The full seven-screen mobile flow

**Eligibility results**
(FILL IN: This is the moment your cover photo shows, so it's worth a section if you can share it. Two or three sentences: what someone sees when their results come back, what was confusing about the old version, and one decision you made. For example how you explained what they qualify for, or what to do next.)

*Images:* Results screen on phone and desktop · The next step after results (plan choice or confirmation)

**Help on every screen**
People applying for coverage are often stressed, short on time, or reading in a second language. Every screen carries a language switch for English, Español and Amharic, and a help line with a TTY number, so help is never more than a glance away. An "I don't have a SSN" option keeps people without one from getting stuck at a required field, instead of abandoning the application.

*Images:* Language switch open · Help line and TTY in the footer · The "I don't have a SSN" option

**Accessible by default**
The audit found federal accessibility violations, so patching screens one at a time wasn't going to work. I built WCAG 2.1 AA and Section 508 requirements into the design system's foundations: color, type, components and every interaction state. Focus, error and disabled states all meet contrast requirements, so any new screen built from the system starts out accessible instead of being fixed later.

*Images:* Close-ups of focus, error and disabled field states · Color and type tokens

**Rolling it out**
I present designs directly to the state marketplaces and turn their feedback and policy requirements into product decisions. Alongside Maine's version, there's an unbranded reference version the other states can adopt with their own branding. DC, the platform's largest deployment, is next, with its migration planned for 2026–2027.

*Images:* The prototype recording (20–30 seconds) · Link: Open the prototype in Figma

---

## 2. WorkRadar

**Tagline:** Daily check-ins for a safe return to the office

**Facts**
- Years: 2020–2021
- Company: IdeaCrew
- Role: Design Lead
- Services: Product design, Brand, Mobile, Dashboard

**Overview**
WorkRadar helped employers decide when it was safe to bring people back to the office during COVID-19. Employees and guests answered a short daily health check-in, and managers saw local public-health data and their team's check-ins on one dashboard. I designed the employee app, the manager dashboard and the brand, from first concept through interactive prototype, in 2020–2021. It reached evaluation with a regional bank, then was shelved as restrictions eased.

**Daily check-in**
Every morning, employees answer two questions before coming in: have they been in close contact with someone with COVID-19 since their last screening, and do they have any of the listed symptoms. The questions are plain yes-or-no, based on CDC attestation guidance, and a summary lets people review and attest before they submit.

Not everyone fits the main path. Guests can screen without an account, and anyone not working that day can say so and pick a reason, so managers aren't left guessing about missing check-ins. I also wrote a user guide for each role, employees, guests and managers, to support rollout.

*Images:* Home (last screening and Begin) · Symptoms question · Review and attest · Guest check-in

**A result you can't misread**
A check-in is only useful if the answer is obvious from across a lobby. OK to Enter fills the screen in green with a checkmark and a QR code to show at the door. Stop fills it in red with an X, then turns to what to do next: CDC resources and a self-isolation date worked out for them.

*Images:* OK to Enter and Stop side by side

**Management dashboard**
Managers needed two pictures at once: what was happening in their community and what was happening on their own team. The dashboard pairs public-health trends for DC, Virginia and Maryland with the organization's screening results, and lists every employee's latest status with filters by facility, status and division.

Early on, the CEO wanted the employee list as cards. I pushed for a table instead, because managers needed to compare a lot of employees quickly, and a table makes that easy. Cards might have looked nicer, but this was a call to put UX above UI, and the table made it into the final design.

*Images:* Attestation and Public Health panels · Employee table with filters

**On the go**
Managers aren't always at a desk, so the same overview works on a phone: a response timeline and the day's totals for screenings, symptoms, exposures and no-responses, with the full employee list a tap away.

*Images:* Phone overview

**A brand for an anxious moment**
WorkRadar needed to feel calm and trustworthy at a time of real public anxiety. I created the name, logo, color palette and visual language from scratch, outside IdeaCrew's existing design system. The chevron in the wordmark points inward: a return to the workplace, to normalcy, to each other. OK Green and Stop Red carry the two results, so the brand and the product speak the same language.

*Images:* Brand board · Check-in prototype recording

---

## 3. Vitae 27

**Tagline:** One system for three state marketplace brands, built by directing an AI agent

**Facts**
- Years: (FILL IN: year started)–present
- Company: IdeaCrew
- Role: Design Lead
- Services: Product design, AI-assisted building, Accessibility

**Overview**
Vitae 27 is how IdeaCrew's Enroll platform themes three state brands, DC, Maine and Massachusetts, from one codebase. I built it by directing an AI coding agent: I made the design decisions and reviewed every result, and the agent wrote the code. One token set switches between the three brands in light and dark mode, and every change is checked for accessibility automatically before it reaches a state's marketplace.

**One system, three brands**
Each state has its own brand, but they all run the same product. Maintaining three sets of components would mean every fix happening three times, and the states slowly drifting apart. Instead, the brands differ only in their tokens for color, type and spacing. A fix made once shows up in every market, in light and dark mode.

*Images:* One component in each brand, light and dark (a 3×2 grid) · Token table per brand

**From Figma to production**
The system runs in one line from Figma to Storybook to the Rails components engineers ship. I directed the agent to build that pipeline and the components in it. My job was the part that needs a designer: deciding what each component should do, writing the rules, and reviewing every result against the Figma source before it shipped.

*Images:* A Figma component beside its Storybook page

**Accessibility on every change**
WCAG 2.1 AA checks and visual-regression tests run automatically in CI. If a change breaks contrast, focus states or layout in any brand, it's caught before it reaches a state. That turns accessibility from a review step into something the system enforces on its own.

*Images:* A CI run with checks passing · A visual-regression diff catching a change

**Directing the agent**
The agent was fast, but it filled gaps with assumptions instead of checking the source. It told me our buttons had 4px and 8px corners; production used 6px, and I had just moved them to pills. It turned a guideline, aim for one call to action per page, into an automated check that failed pages that genuinely needed two. The instruction I gave most often became: look first. Check the production code, the Figma file or Lookbook before deciding how Enroll looks or behaves.

My judgment mattered most where a check can't decide. In dark mode, the agent's blue turned the buttons almost gray. Of the options, I chose #24487A because it held up in a group of buttons, even though another looked better on its own. I kept bright green for call-to-action buttons only, and rather than add a border to make it work, we found the closest green to the logo that passes contrast with white text: #00884D.

**What's next**
Vitae 27 is moving into IdeaCrew's own repository, where it will be the foundation for every Enroll market. (FILL IN: update once the move is done.)

---

## 4. RegSearch

**Tagline:** Federal procurement regulations, actually searchable

**Facts**
- Years: 2016
- Company: Distributed Solutions, Inc.
- Role: Designer
- Services: Product design, UI design, Brand

**Overview**
RegSearch is a research tool for federal procurement regulations, used by people who spend their day inside hundred-page documents. It was a legacy app that only ran in Internet Explorer 7. I redesigned it into a responsive product, growing the reading pane from about a quarter of the screen to three quarters and adding search within search, document sets and sharing. It was built at Distributed Solutions with a team of five over eight months, and replaced the legacy tool across the client's organization.

**Designed for reading**
The old screen gave the document only a quarter of the space, squeezed under a checklist of documents and beside a list of sections. The redesign gives the document three quarters of the screen and moves everything else to the edges. Search hits use high-contrast highlights instead of red text buried in a block of black, so you can scan a long regulation for every match at a glance.

*Images:* Before and after: the search results screen

**Finding the right document**
Picking which documents to search used to mean working through a dense table of checkboxes. The new document browser is a clean list with currency and dates, a search field, and favorites, so people can get back to the regulations they use most without hunting for them.

*Images:* Before and after: document selection

**Two kinds of research**
Researchers dig deep into one topic across many documents. Case workers cross-check a specific rule under time pressure. Both used to copy text out or print whole documents to do their jobs. Search within search, document type filters, bookmarks, PDF export and shareable document sets now handle that work inside the tool.

*Images:* (FILL IN: any screens of search within search, bookmarks or document sets)

**Sign-in**
The old sign-in page was a small form surrounded by blocks of text on a yellow background. The new one asks only for what's needed, in a single centered card.

*Images:* Before and after: sign-in

**Brand**
I also designed a new RegSearch logo, repositioning it as a modern research tool rather than a legacy government utility. The mark set the color palette and icon language for the interface.

*Images:* The RegSearch wordmark

---

## 5. CDC Public Health Law

**Tagline:** A usability review of cdc.gov's Public Health Law section

**Facts**
- Years: 2020
- Company: Viscid
- Client: Centers for Disease Control and Prevention
- Role: Product & UX Designer (contract)
- Services: Heuristic evaluation, Information architecture, Visual review

**Overview**
In May 2020 I ran a two-week heuristic evaluation of the Public Health Law section of cdc.gov, working with the agency Viscid. The section runs on CDC's sitewide content management design system, so problems found here were likely repeated across the site. I rated every issue by severity, so CDC's team could fix the worst first.

**How I evaluated**
I reviewed each page against eight heuristics: consistency, standardization, cognitive load, navigational effort, aesthetic integrity, information architecture, recognition and linguistic clarity. Each finding got a low, moderate or high priority based on how much it got in the way of someone looking for public health law resources, not how hard it would be to fix.

**High priority: pages too dense to scan**
Long pages packed sections tightly together, with little space between a heading and the content around it, so it was hard to tell where one topic ended and the next began. Splitting long pages and adding space between headers and content would let people find what they came for faster.

*Images:* Annotated long pages

**Moderate priority: heavy modules**
On the About page, the office directory's heavy styling competed with the content it was meant to support, and numbers set as images would be hard to update.

*Images:* Annotated About page

**Low priority: small polish**
A CSS error left gaps in rounded card corners: a one-line fix with an outsized effect on how polished the site feels.

*Images:* Close-ups of the card corners

**Outcome**
I wasn't involved in implementation, so I can't confirm which recommendations were adopted. Revisiting cdc.gov later, many of the patterns I flagged, especially content density and visual hierarchy, appear to have been addressed. The full evaluation is available on request.

(FILL IN: Your resume also lists cdc.gov wireframes aligned with new federal design guidelines, and storyboards for digital content. Were those part of this engagement? If so, they could be a section here.)

---

## 6. TakeCare

**Tagline:** A wellness brand for Marriott's global workforce

**Facts**
- Years: 2019
- Company: Perphic
- Client: Marriott International
- Role: Product & UX Designer (contract)
- Services: Brand identity, Art direction, Brand system

**Overview**
TakeCare is Marriott International's employee health and wellness brand, and engagement was slipping as its workforce grew younger and more global. Working with the agency Perphic, I helped lead a full rebrand: logo, visual identity, photography direction and a brand system for every program under it. Marriott then brought the team back for more internal branding work.

**The mark**
The old logo, a green and blue starburst with the tagline "Go.Be.Happy.", read as corporate. The new identity trades that for a lifestyle brand's warmth, putting the weight on "Care." Its three dots stand for TakeCare's three pillars, Me, You+Me and We, and read as an ellipsis: more to come. Lockups work on their own and alongside the Marriott International wordmark, horizontally and stacked.

*Images:* Before and after · Lockups, including co-branded with Marriott

**Color and type**
A deep violet leads the palette, chosen for optimism and forward momentum, with yellow, magenta and teal for range and charcoal for text. Gotham carries the type, from light headlines to bold callouts.

*Images:* Palette · Type specimen

**One system, many programs**
TakeCare isn't one campaign; it's an umbrella over many programs. The system extends to two tiers of sub-brands: Hero Programs that run year after year, like Triathlon and Living Our Core Values, and Regular Programs for recurring events, like Unplugged. Each inherits TakeCare's language while keeping its own identity, so a new program can launch without a new brand.

*Images:* Program framework

**Imagery**
Photography mixes stock and associate images to reflect Marriott's global workforce, art-directed to stay warm and uncluttered.

*Images:* (FILL IN: three or four photos from the image library, cropped to one size)

**Brand book and templates**
A brand book, digital templates, an icon set and a curated image library let Marriott's teams make new materials without starting from scratch.

*Images:* Two brand book spreads · Icon set

---

## 7. Major CRE Firm

**Tagline:** Folding debt transactions into an enterprise CRM

**Facts**
- Years: 2019–2020
- Company: Main Digital
- Client: A major commercial real estate firm (confidential)
- Role: Product & UX Designer (contract)
- Services: Research, Workflow mapping, Interaction design

**Overview**
A major commercial real estate firm had just acquired a company that specialized in debt transactions, and needed that business's workflow inside its custom CRM, which was never built for it. Over five months with the consultancy Main Digital, I learned the debt process through interviews with stakeholders and the development team, then turned it into interactive wireframes and a prioritized backlog the team could build from.

**Learning a process nobody knew**
No one on the platform side had worked with debt transactions before, so the first job was understanding them. I interviewed the acquired company's stakeholders about how deals actually move, and the existing development team about what the CRM could already do. Every requirement went into one working document, so the business and the developers were reading from the same list.

*Images:* Requirements document

**Wireframes tied to the backlog**
I designed interactive wireframes inside the client's existing design system, and tagged every part of each screen with the backlog item that would build it. A developer could start from any requirement and find exactly where it lived in the design, and a stakeholder could see what each backlog item actually meant on screen.

*Images:* Tagged wireframe · The full set of debt wireframes

**Beyond the scope**
An experience audit of the existing CRM turned up usability problems outside the acquisition work. Those went into the backlog too, giving the client a roadmap for improvements beyond the immediate project.

**Outcome**
The client came away with a clear integration plan: a prioritized backlog backed by interactive wireframes, ready for development to build the debt workflow into the existing CRM.

---

## 8. IdeaCrew Rebrand

**Tagline:** Evolving the mark into a brand system

**Facts**
- Years: 2026
- Company: IdeaCrew
- Role: Design Lead
- Services: Brand identity, Visual system, Templates

**Overview**
In 2026 I led IdeaCrew's rebrand, from first concepts through launch. The company had grown, was rethinking how it positions itself, and had never had formal brand guidelines. The result is an evolved mark and a system around it: colors, type, patterns, document and slide templates, and a Claude skill that keeps AI-written documents on brand.

**Research**
I started by mapping themes the brand could draw on: light, development and technology, the ampersand, Washington, DC, the letters IC, and health care. Boards of reference marks showed how crowded the lightbulb space is, and which ideas felt like IdeaCrew rather than everyone else.

*Images:* Theme photos · Reference board

**Exploration**
Shape and font pairing ran through lightning bolts, brackets, interlocking letters and dozens of lightbulbs, each tested against different wordmarks. The strongest directions moved on to color themes, lockups and mockups on shirts, letterhead and mugs.

*Images:* Interlocking I and C marks · Bolts and brackets · Modern bulbs · Color lockups · Four finalist directions

**The decision**
Leadership's feedback was clear: keep the lightbulb. So the new mark is an evolution, not a revolution. The incandescent bulb, old technology, became a simpler modern outline, and the ampersand inside it became a plus that reads as both "and" and health care. Colors were darkened for higher contrast.

*Images:* Before and after · The mark on light and dark backgrounds

**The system**
Midnight Navy and Royal Blue carry the brand equally, with Deep Plum and Sky as accents in a 40/40/10/10 split. IBM Plex Serif Medium is the default typeface across nearly all marketing material. A family of patterns built from the plus gives documents and slides depth without competing with the content.

*Images:* Palette · Type specimen · A brand pattern

**In use**
The brand launched across marketing documents, document and slide templates, and a Claude skill, so documents written with AI come out on brand without anyone policing them.

*Images:* Marketing document spreads · T-shirt and mug

---

## 9. CrossFit Metropolis

**Tagline:** A simpler gym site for members and newcomers

**Facts**
- Years: 2015
- Client: CrossFit Metropolis, New York
- Company: Freelance
- Role: Designer
- Services: Web design, Content strategy, Art direction

**Overview**
In 2015 I redesigned the website for CrossFit Metropolis, a gym in New York City, working directly with its owners. The old site buried what people came for under a long, text-heavy homepage. I cut it down to the workout of the day, a short answer to "what is CrossFit?" and a simpler path to sign up, and built the look around professional photography.

**One homepage for two audiences**
Members check the site every day for the workout of the day; newcomers want to know what CrossFit is and how to start. I talked with the owners, took a class myself, and moved the most-used content into the hero and just below the fold. Old workouts went to an archive and low-traffic links moved to the footer.

*Images:* Before and after homepage · Desktop and phone

**Photography that sells the feeling**
Text alone couldn't carry the gym's culture, so the design leans on professional photography built around four themes: fitter New Yorkers, a program that works for me, a community a traditional gym doesn't offer, and health and happiness through fitness. The photography carried over into the gym's later marketing campaigns.

Members said the new homepage felt cleaner and made it easier to find what they needed, though some longtime members needed time to adjust to the change.

*Images:* (FILL IN: two or three photos from the shoot)

---

## 10. Extras

**Tagline:** Logos, print and other side work

**Overview**
Identity and print work for small businesses, nonprofits, events and friends, plus a few industrial design concepts.

**Logos**
Marks for local businesses, a biotech company, sports teams and events, plus the concepts I explored for IdeaCrew.

**Print**
Posters, save-the-dates and event pieces, from a hand-drawn chalkboard wreath to a Barcelona Pavilion exhibit poster.

**Other**
Packaging and product sketches, including soccer boot concepts I drew while applying for industrial design internships, to show I could draw.

---

## 11. SNOWATCH

**Tagline:** A ski watch that fits over your jacket

**Facts**
- Years: 2011
- Context: Industrial design concept
- Role: Designer

**Overview**
Checking the time on the mountain means pulling off a glove and digging under a sleeve. SNOWATCH is a waterproof sleeve that wraps over a ski jacket instead of sitting under it.

**Built for gloves and goggles**
A flexible e-ink display stays readable through goggles, and buttons sized for thick gloves mean you never have to take them off. A built-in RECCO reflector helps rescuers find you if something goes wrong.

*Images:* SNOWATCH on a jacket sleeve · Rendering with callouts

---

## 12. ERGO

**Tagline:** A running watch you can read mid-stride

**Facts**
- Years: 2011
- Context: Industrial design concept
- Role: Designer

**Overview**
To read a standard sports watch, runners twist their wrist and break stride. ERGO moves the face to the side of the wrist and tilts it toward the eyes.

**Reading on the run**
With the face where the eyes already are, the time reads at a glance with the arm in its natural running position. The buttons sit where the other hand can press them without strain.

*Images:* Prototype on the wrist · Diagram: twisting versus natural arm position

---

## 13. London

**Tagline:** A drinking fountain built for refilling bottles

**Facts**
- Years: 2010
- Context: Industrial design concept
- Role: Designer

**Overview**
Most drinking fountains make refilling a reusable bottle slow and awkward: you tilt the bottle, it never fills, and the stream is weak. LONDON is a concept fountain designed for refilling a bottle as well as taking a drink.

**From observation to form**
Most drinking fountains I saw in parks had no real way to refill a bottle. Parks would be a better experience if more fountains let people refill a reusable bottle as easily as they take a drink. The sketches worked toward a single fountain that does both, with a curved hood and room underneath for a bottle.

*Images:* Photos of people at fountains · Sketches · Final renderings

---

## 14. BEN

**Tagline:** A De Stijl bench, from idea to build

**Facts**
- Years: 2010
- Context: Industrial design, James Madison University
- Role: Designer and builder

**Overview**
BEN is a bench I designed and built in a week at the end of college, after years of thinking about it. It borrows the relaxed angles of an Adirondack chair and the reduced, floating forms of the Dutch De Stijl movement, sized for my 6'2" frame.

**Adirondack comfort, De Stijl form**
A beach-vacation Adirondack chair started the idea; a college studio on the Netherlands gave it a style. De Stijl stripped form down to essentials and let parts appear to float. An outer frame steadies the bench, physically and visually, while the seat floats inside it. A later version drops the frame so it sits lower and steadier.

*Images:* The bench in use · De Stijl inspiration · Sketches and studies · The outline turned into a logo
