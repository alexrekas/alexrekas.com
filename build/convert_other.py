#!/usr/bin/env python3
"""One-time converter: WPBakery copy for the 'other work' pages -> build/pages fragments.

The copy comes verbatim from _source/content; alt text is written per image below.
Re-run only if the source copy changes (it overwrites the fragments).
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "_source" / "source-bundle" / "content"
MEDIA = json.loads((CONTENT / "media.json").read_text())
OUT = ROOT / "build" / "pages" / "portfolio"

ALT = {
    # CDC
    "5545": "Three tall cdc.gov Public Health Law pages side by side, with a red circle marking a dense block of text that runs together.",
    "5567": "The CDC About page with numbered callouts on its heavy, blue office-directory modules and numbers set as images.",
    "5553": "Close-ups of cdc.gov cards with callouts magnifying gaps in their rounded corners.",
    # CRE CRM
    "5518": "A spreadsheet of debt-workflow requirements with columns for each requirement, notes and status.",
    "5941": "A dark CRM wireframe with blue tags on each area naming the backlog item that builds it.",
    "5943": "A wireframing canvas showing the full set of debt-transaction screens laid out in rows.",
    # CrossFit Metropolis
    "4963": "The CrossFit Metropolis logo: distressed white lettering over a red circular mark.",
    "4916": "The redesigned CrossFit Metropolis site on a desktop monitor and a phone, led by a photo of an athlete lifting a barbell.",
    "5289": "The old CrossFit Metropolis homepage: a long, narrow column of text and small photos.",
    "5290": "The new homepage: a full-width photo of athletes headed “Health. Happiness. Fitness.” above the workout of the day and a short “What is CrossFit?” section.",
    # Pollen Productions
    "5250": "Peach roses and white snapdragons in a metal bucket against a wall of dark ivy.",
    "5221": "The Pollen Productions site on a laptop and a phone, with a photo of roses and snapdragons and a “Hello!” greeting.",
    "5220": "People taking notes at a wooden table with a laptop, notebooks and a glass of cold brew.",
    "5216": "A large numeral 1.",
    "5217": "A large numeral 2.",
    "5218": "A large numeral 3.",
    "5219": "A large numeral 4.",
    "5228": "The florist's hands arranging evergreen branches on a round wreath frame.",
    "5231": "A florist holding armfuls of peach, white and deep red flowers in front of an ivy-covered brick wall.",
    "5229": "A white and pink arrangement with peonies and greenery in a glass vase on a rustic wooden counter.",
    # How Much?
    "hmdawvc-header-text.png": "Script lettering reading “How much does a wedding video cost?”",
    "4950": "The quote tool on a laptop and a phone, with an illustrated question asking which wedding moments matter most.",
    # Extras
    "4499": "Herndon Farm to Table logo: line drawings of a sun, barn and place setting in white on weathered wood.",
    "5456": "Seneca Biopharma logo: a striped mark beside the word seneca.",
    "4528": "ClassWallet logo: a white rounded-square icon and wordmark on bright blue.",
    "5187": "Brand Talent logo for Marriott: a red and pink geometric mark beside the words Brand Talent.",
    "5457": "Champions in Action logo: a light blue C badge beside stacked lettering on navy.",
    "4529": "Gobblestone Paving logo: a turkey whose body is made of gray paving stones.",
    "5188": "Budget Referee logo: a pale green mark and lowercase wordmark on green stripes.",
    "5458": "Herndon hometown sticker: a black and red house outline on red.",
    "4532": "VRPS Leadership Training Institute logo over a sunrise above blue mountain ridges, with the line Learn, Transform, Inspire.",
    "5192": "Rampage F.C. crest: a black shield with blue stripes and the number 94.",
    "5191": "Sunset Taco logo: script lettering on a half-circle sunset gradient.",
    "5644": "Pizza King logo: a yellow crown shaped like a pizza slice above yellow italic lettering.",
    "5648": "Alex Rekas's personal monogram mark in white on black, with the mark shown on a cap and a T-shirt.",
    "5645": "The CDC logo in white on blue with the words Centers for Disease Control & Prevention.",
    "5646": "Four IdeaCrew wordmark variations in black and white.",
    "5402": "The RegSearch wordmark in white on deep purple.",
    "5647": "The WorkRadar wordmark in white on dark navy.",
    "5649": "The Enroll App logo: a blue EA monogram beside the words Enroll App.",
    "4504": "Amy & Alex save-the-date card: a hand-drawn leaf wreath on a chalkboard texture, Richmond, VA.",
    "4521": "Herndon Turkey Trot 2012 poster: a cartoon turkey in front of yellow and orange sunrays.",
    "4531": "Mies poster: white architectural plan lines and type on black for a Barcelona 1929 pavilion exhibit.",
    "4502": "Wreaths Across America invitation with three wreaths over a photo of a cemetery.",
    "4503": "Wreaths Across America sponsorship form with fields for a wreath order.",
    "5189": "Liz & Matt save-the-date card with a watercolor mountain lake, Glen Wild Lake, Bloomingdale, NJ.",
    "4538": "Three bottles of men's body wash and hair wash in yellow, teal and gray packaging.",
    "4537": "Pencil sketches of a process, with arrows showing materials pressed, rolled and cut.",
    "4535": "Rendered white soccer boots with a Nike swoosh, shown from the side and from below.",
    "4536": "Rendered black soccer boots with three white Adidas stripes, shown from the side and from below.",
    # BEN
    "168": "A student sitting on the BEN bench, a pale wooden bench with a floating seat inside an outer frame.",
    "5389": "A sheet of De Stijl centenary stamps with primary-color compositions and Mondrian-style grids.",
    "4223": "Sketches and orthographic drawings of the bench frame alongside photos of the wood joinery.",
    "4224": "A collage of bench studies, a rendering of the frame and seat, and the bench's outline turned into a logo.",
    # London
    "156": "A rendering of the LONDON fountain: a gray pedestal with a red curved hood, two grates and a red PUSH button.",
    "161": "A strip of photos of people struggling to drink from or fill bottles at public fountains.",
    "160": "A long strip of pencil sketches exploring fountain forms.",
    "162": "Line drawings developing the fountain's curved hood and bottle-filling spout.",
    "163": "A diagram of the fountain's parts and three silhouettes of its pedestal shape.",
    "154": "A rendering of the LONDON fountain from the side, showing the bottle-filling spout under the hood.",
    # SNOWATCH
    "4489": "The SNOWATCH sleeve wrapped around a jacket sleeve on a snowy slope, showing the time 10:20.",
    "4462": "A ski racer rounding a gate, and a ski patroller in a red jacket carrying a shovel.",
    "140": "A rendering of the SNOWATCH sleeve with labeled callouts for the RECCO reflector and fastening, beside a sketch of a snowboarder wearing it.",
    "4463": "Snowboarders standing on a snowy mountain ridge.",
    # ERGO
    "171": "The ERGO watch prototype worn on a wrist, its face tilted toward the wearer and showing 06:45.",
    "4217": "A runner looking at her watch mid-stride on a park path.",
    "4218": "A runner glancing at a TomTom GPS watch in a park.",
    "4219": "Line drawings comparing arm positions: A, a standard watch requires twisting the wrist; B, ERGO reads with the arm in its natural position.",
}

PAGES = {
    "cdc": dict(title="CDC Public Health Law", next=("Major CRE Firm", "/portfolio/cre-crm/"),
                desc="CDC Public Health Law: Alex Rekas ran a two-week heuristic evaluation of the Public Health Law section of cdc.gov, rating every issue by severity."),
    "cre-crm": dict(title="Major CRE Firm", next=("How Much?", "/portfolio/how-much/"),
                    desc="Major CRE Firm: Alex Rekas mapped a debt-transaction workflow into an enterprise CRM through stakeholder interviews, interactive wireframes and a prioritized backlog."),
    "how-much": dict(title="How Much?", next=("Pollen Productions", "/portfolio/pollen-productions/"),
                     desc="How Much?: a single-page wedding video quote tool for watchPVK, designed by Alex Rekas, where the price updates as you answer."),
    "pollen-productions": dict(title="Pollen Productions", next=("CrossFit Metropolis", "/portfolio/crossfit-metropolis/"),
                               desc="Pollen Productions: brand, art direction and a subscription store for a floral designer, by Alex Rekas."),
    "crossfit-metropolis": dict(title="CrossFit Metropolis", next=("Extras", "/portfolio/extras/"),
                                desc="CrossFit Metropolis: Alex Rekas redesigned a New York City gym's website around the workout of the day, a simple sign-up path and professional photography."),
    "extras": dict(title="Extras", next=("SNOWATCH", "/portfolio/snowatch/"),
                   desc="Extras: logos, print and other identity work by Alex Rekas for small businesses, nonprofits, events and friends."),
    "snowatch": dict(title="SNOWATCH", next=("ERGO", "/portfolio/ergo/"),
                     desc="SNOWATCH: an industrial design concept by Alex Rekas for a ski watch that wraps over your jacket, readable through goggles and usable in gloves."),
    "ergo": dict(title="ERGO", next=("London", "/portfolio/london/"),
                 desc="ERGO: an industrial design concept by Alex Rekas for a running watch you can read mid-stride without twisting your wrist."),
    "london": dict(title="London", next=("BEN", "/portfolio/ben/"),
                   desc="LONDON: a concept drinking fountain by Alex Rekas, designed for refilling a reusable bottle as well as taking a drink."),
    "ben": dict(title="BEN", next=("CDC Public Health Law", "/portfolio/cdc/"),
                desc="BEN: a bench Alex Rekas designed and built, borrowing an Adirondack chair's angles and the floating forms of De Stijl."),
}

SIZES = {
    1: None,
    2: "(min-width: 1248px) 584px, (min-width: 1000px) calc(50vw - 40px), calc(100vw - 32px)",
    3: "(min-width: 1100px) 384px, (min-width: 700px) calc(33vw - 32px), calc(100vw - 32px)",
    4: "(min-width: 1100px) 282px, (min-width: 700px) calc(25vw - 30px), calc(50vw - 28px)",
}


def clean(t):
    t = re.sub(r' style="[^"]*"', "", t)
    t = re.sub(r"\[/?vc_column_text[^\]]*\]", "", t)
    t = re.sub(r"\[/?vc_row[^\]]*\]", "", t)
    t = t.replace("[/vc_column]", "").replace("&nbsp;", "")
    t = re.sub(r' (img_size|alignment)="[^"]*"', "", t)
    return t


def fill(s):
    """<strong>(FILL IN: x)</strong> -> (FILL IN: x); <strong>REVIEW:</strong> x -> review mark."""
    s = re.sub(r"<strong>\s*(\(FILL IN:.*?\))\s*</strong>", r"\1", s, flags=re.S)
    s = re.sub(r"<p><strong>REVIEW:</strong>\s*(.*?)</p>", r'<p><mark class="fill review">Review: \1</mark></p>', s, flags=re.S)
    return s


def img(mid, n):
    name = MEDIA[mid]["file"].split("/")[-1]
    sizes = SIZES[n]
    s = f' sizes="{sizes}"' if sizes else ""
    return f'<x-img src="{name}" alt="{html.escape(ALT[mid], quote=True)}"{s}>'


def column_html(c, n):
    """A column: images get following <p>s as their caption; BEFORE/AFTER become kickers."""
    c = c.strip()
    parts = re.split(r'(\[vc_single_image image="\d+"[^\]]*\]|<div>IMAGE TO ADD:.*?</div>)', c)
    out, fig_open = [], False
    for p in parts:
        p = p.strip()
        if not p:
            continue
        m = re.match(r'\[vc_single_image image="(\d+)"', p)
        t = re.match(r"<div>IMAGE TO ADD:\s*(.*?)</div>", p, re.S)
        if m or t:
            if fig_open:
                out.append("</figure>")
            out.append("<figure>" + (img(m.group(1), n) if m else f"<x-todo>{t.group(1)}</x-todo>"))
            fig_open = True
            continue
        kick = re.fullmatch(r"<p>(BEFORE|AFTER)</p>", p)
        if kick:
            out.append(f'<p class="kicker">{kick.group(1).title()}</p>')
            continue
        if re.fullmatch(r"<h4>FLAGGED LOGOS</h4>", p):
            out.append('<h3 class="eyebrow">Flagged logos</h3>')
            continue
        p = re.sub(r"<p>(HIGH|MODERATE|LOW) PRIORITY</p>", lambda m: f'<p class="kicker">{m.group(1).title()} priority</p>', p)
        if fig_open:
            out.append(f"<figcaption>{strip_p(p)}</figcaption>")
        elif n == 1:
            out.append(f'<div class="section-text sub">{p}</div>')
        else:
            out.append(p)
    if fig_open:
        out.append("</figure>")
    return "".join(out)


def strip_p(p):
    ps = re.findall(r"<p>(.*?)</p>", p, re.S)
    return " ".join(ps) if ps else p


def convert(slug):
    raw = fill(clean((CONTENT / f"portfolio-{slug}.wpbakery.txt").read_text()))
    # raw <img> left in the copy -> responsive image with alt; its review note becomes the caption
    raw = re.sub(
        r'<div><img src="[^"]*/([^"/]+)"[^>]*></div><p>(<mark class="fill review">.*?</mark>)</p>',
        lambda m: f'<figure class="on-dark"><x-img src="{m.group(1)}" alt="{ALT[m.group(1)]}"><figcaption>{m.group(2)}</figcaption></figure>',
        raw, flags=re.S)
    raw = raw.replace("<h4>FLAGGED LOGOS</h4>", '<h3 class="eyebrow flagged">Flagged logos</h3>')
    # the image build already resizes and compresses everything
    raw = raw.replace(" (FILL IN: re-export this image smaller; it’s 776 KB)", "")
    rows = [r for r in raw.split("\n") if r.strip()]
    meta = PAGES[slug]
    first = rows.pop(0)
    intro = re.search(r"<p>(.*?)</p>", first, re.S).group(1)
    rowsmeta = []
    for label, val in re.findall(r"<tr><td>(.*?)</td><td>(.*?)</td></tr>", first, re.S):
        if label in ("Year",):
            label = "Years"
        if label == "Services":
            val = [v.strip() for v in val.split("·")]
            val = [v[0] + v[1:].lower() if not v.startswith("UX") and not v.startswith("UI") else v for v in val]
        rowsmeta.append([label, val])
    hero = None
    # a full-width, caption-less single image right after the intro is the hero
    if rows and re.fullmatch(r'\s*\[vc_column\]\[vc_single_image image="(\d+)"\]\s*', rows[0]):
        hero = re.search(r'image="(\d+)"', rows.pop(0)).group(1)

    body, section_open, text_open = [], False, False

    def close_text():
        nonlocal text_open
        if text_open:
            body.append("</div>")
            text_open = False

    sec_n = 0
    for r in rows:
        r = r.strip()
        cols = re.split(r'\[vc_column(?: width="([^"]+)")?\]', r)
        # cols = ['', width, content, width, content, ...]
        pieces = [(cols[i], cols[i + 1]) for i in range(1, len(cols), 2)]
        widths = [w for w, _ in pieces]
        if len(pieces) > 1 or (widths and widths[0]):
            n = len(pieces)
            close_text()
            cls = {2: "pair", 3: "triple", 4: "quad"}.get(n, "pair")
            inner = []
            for _, c in pieces:
                h = column_html(c, n)
                if not h:
                    continue
                if h.startswith("<figure>") and h.count("<figure>") == 1:
                    inner.append(h)
                else:
                    inner.append(f"<div>{h}</div>")
            ba = " before-after" if "kicker" in "".join(inner) else ""
            body.append(f'<div class="{cls}{ba}">' + "".join(inner) + "</div>")
            continue
        content = pieces[0][1] if pieces else r
        if content.startswith("<h2>"):
            close_text()
            if section_open:
                body.append("</section>")
            sec_n += 1
            h2 = re.match(r"<h2>(.*?)</h2>", content).group(1)
            rest = content[len(re.match(r"<h2>.*?</h2>", content).group(0)):]
            body.append(f'<section class="section" aria-labelledby="s{sec_n}"><div class="section-text"><h2 id="s{sec_n}">{h2}</h2>')
            text_open = True
            section_open = True
            # anything after the text (images) goes to figs
            m = re.search(r'\[vc_single_image|<div>IMAGE TO ADD', rest)
            if m:
                body.append(rest[: m.start()])
                close_text()
                body.append('<div class="figs">' + column_html(rest[m.start():], 1))
                body.append("</div>")
            else:
                body.append(rest)
            if section_open and not text_open:
                pass
            continue
        if content.startswith("<figure"):
            close_text()
            body.append(content)
            continue
        if "[vc_single_image" in content or "IMAGE TO ADD" in content:
            close_text()
            body.append(column_html(content, 1))
            continue
        # a plain text row: caption for a preceding grid, or closing text
        if body and body[-1].endswith("</div>") and not text_open and re.fullmatch(r"<p>.*</p>", content, re.S) and len(content) < 260 and not section_open_closed(body):
            body[-1] = wrap_grid_caption(body[-1], strip_p(content))
            continue
        close_text()
        body.append(f'<div class="section-text closing-text">{content}</div>')
    close_text()
    if section_open:
        body.append("</section>")
    # loose blocks before the first heading get section spacing
    first_sec = next((i for i, b in enumerate(body) if b.startswith("<section")), len(body))
    if first_sec:
        body = ['<div class="section">' + "".join(body[:first_sec]) + "</div>"] + body[first_sec:]
    page_meta = {
        "url": f"/portfolio/{slug}/",
        "template": "case",
        "title": meta["title"],
        "description": meta["desc"],
        "intro": intro,
        "rows": rowsmeta,
        "next": {"title": meta["next"][0], "url": meta["next"][1]},
    }
    if not hero and slug in ("cdc", "cre-crm"):
        page_meta["hero_todo"] = "Hero image for this project"
    if hero:
        page_meta["hero"] = MEDIA[hero]["file"].split("/")[-1]
        page_meta["hero_alt"] = ALT[hero]
    text = "<!--" + json.dumps(page_meta, ensure_ascii=False, indent=1) + "-->\n" + "\n".join(b for b in body if b) + "\n"
    (OUT / f"{slug}.html").write_text(text)


def section_open_closed(body):
    return False


def wrap_grid_caption(grid_html, caption):
    return f"<figure>{grid_html}<figcaption>{caption}</figcaption></figure>"


if __name__ == "__main__":
    for slug in PAGES:
        convert(slug)
        print("wrote", slug)
