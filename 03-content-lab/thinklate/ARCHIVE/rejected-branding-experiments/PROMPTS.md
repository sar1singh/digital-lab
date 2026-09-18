> # ⛔ SUPERSEDED 2026-09-13
> **Do not use this file.** Its prompts specify flat vector / enamel / geometric directions that were tried and rejected across eight rounds.
> **Canonical art direction and prompts: `ART-DIRECTION.md`.**
> Kept only as a record of what was tried and why it failed.

---

# ThinkLate — Branding Asset Prompts

**Revised:** 2026-09-13. **Supersedes the previous version of this file.**

---

## What changed and why

The earlier prompts asked for **an owl holding a signboard reading "hindsight."** Removed. Three reasons:

- **Text inside a mark dies small.** YouTube shows the avatar at 32–48 px in comments and search. A five-syllable word inside the artwork is a smudge there.
- **Redundant.** "ThinkLate" already means hindsight. Saying it twice is the same error as on-screen text repeating the narration.
- **Reads amateur.** Mascot-with-a-prop is clipart convention. Kurzgesagt's bird, Vox's V, Wendover's globe — all one shape, no props.

**"Hindsight" stays** — as the banner tagline and in the channel description, where it is large enough to read.

---

## The rule that governs everything below

**The mark is drawn, not generated.** `build_assets.py` outputs all four assets as SVG from ~40 lines of geometry.

| | AI generation | SVG geometry |
|---|---|---|
| Reproducible | No | **Identical every run** |
| Editable | Re-prompt and hope | **Change one number** |
| Readable at 32 px | Accidental | **Designed and tested** |
| Watermark risk | Real | **None** |
| Commercial licence | Tier-dependent | **Yours outright** |
| Cost | Credits | **₹0** |

**AI's only job here is shape exploration.** Generated images are reference for the geometry. **Nothing generated is ever uploaded to YouTube.** That single rule removes every watermark and licence problem you hit with OpenArt and Ideogram.

---

## Hard constraints for any branding prompt

1. **No text anywhere in the artwork** — no wordmark, no tagline, no signboard
2. **No props** — no banner, scroll, book, glasses, hat, branch, held object
3. **Owl head only.** Front-facing, symmetrical
4. **Exactly one accent** — amber, eyes only
5. **Flat.** No gradient, glow, 3D, shadow, rim light
6. **Must read at 32 px.** If it needs detail to be legible, it failed

---

## Prompt length limits — read first

**Bing Image Creator caps prompts at ~480 characters**, and reportedly produces its best output around **100–300**. Microsoft does not publish the number anywhere in the product, and users report truncation at varying lengths — so **treat 480 as a ceiling, not a guarantee.** Leonardo and Firefly are more generous, but short prompts beat long ones on all three: every extra clause dilutes the weight of the ones that matter.

**Rule: one sentence of subject, one of style, one of exclusions. Nothing else.**

| | Chars | Paste into |
|---|---|---|
| **A1** — owl, short | **260** | Bing (best), Leonardo, Firefly, Playground |
| **A2** — owl, fuller | **382** | Bing (near ceiling), Leonardo, Firefly |
| **B** — banner texture | **242** | Any |
| **C** — thumbnail device | **244** | Any |

---

## Prompt A1 — owl silhouette *(start here)*

```
Flat vector owl head icon, front-facing, symmetrical, minimal geometry. Off-white head on dark navy, round amber eyes, small triangular beak, two pointed ear tufts. Editorial press imprint style. No text, no props, no body. Flat colour, no gradient, no shadow.
```

## Prompt A2 — owl silhouette, more direction

Use if A1 returns mascots or cartoons.

```
Flat vector icon: single owl head, front-facing, symmetrical, minimal geometric shapes. Solid off-white head on dark navy square. Round amber eyes, small triangular beak, two pointed ear tufts. 1960s university press imprint, editorial, serious, not cute, not a mascot. No text, no signboard, no props, no body, no wings. Flat colour only, no gradient, no shadow, no 3D, no outline.
```

## Prompt B — banner background texture *(optional)*

```
Faint engraved map graticule, thin latitude and longitude lines only, deep navy field, very low contrast, barely visible like a watermark on old paper. No text, no labels, no coastlines, no borders, no focal point. Uniform flat texture, 16:9.
```

**Drop to 3% opacity before compositing.** The current SVG grid at 5.5% already fights the wordmark.

## Prompt C — thumbnail visual zone

**Boundary first.** `CLAUDE.md` rule 6 bans AI imagery. That protects **editorial trust** — a viewer must never mistake a generated image for evidence. So AI is fine here **only** for an obviously abstract graphic, never for anything that could pass as a document, photo, chart or record.

| Thumbnail needs | Source |
|---|---|
| A chart, figure, data point | **`templates/charts.py`.** Always |
| A document, photo, map, newspaper | **Wikimedia Commons / public-domain archives.** Never generated |
| A screenshot | The real thing |
| An abstract device | Generated is fine |

```
Flat vector abstract graphic, 16:9: rising stepped bar form in off-white with one amber element, on paper-cream field. Three shapes maximum, large empty area on the right. No text, no numbers, no people, no photorealism. Flat colour, no shadow.
```

Swap the shape for `single long diagonal` or `concentric arcs` as the video needs.

## If a prompt still gets truncated

Cut in this order — first to go is least load-bearing:

1. The style reference (`1960s university press imprint...`)
2. The negatives you have not actually seen fail
3. Colour names — keep `off-white`, `navy`, `amber`; drop hex codes entirely, image models ignore them

**Never cut:** `flat vector`, `owl head`, `front-facing`, `symmetrical`, `no text`.

---

## Free-tier platform verdict

**Researched 2026-09-13. Confidence: moderate.** Almost all comparison content on this comes from affiliate blogs with no stated test methodology, and free tiers change without notice. **Check the platform's own terms page before relying on any row.**

| Platform | Free allowance | Watermark | Commercial use, free tier | Verdict |
|---|---|---|---|---|
| **Bing Image Creator** (DALL·E 3) | 15 fast/day + unlimited slow queue | **None** | Permitted | **First choice.** Best quality at ₹0 |
| **Leonardo AI** | ~150 tokens/day (≈30–50 images) | None | Permitted | **Highest volume.** Use when you want 30 variations |
| **Adobe Firefly** | 25 credits/month | None | Permitted — trained only on licensed + public-domain stock | **Most licence-safe.** Use if output gets near a shipped asset |
| **Playground AI** | ~100/day, to 1024² | None | Permitted | Volume backup. Quality is upper-stock |
| **Ideogram** | Limited daily credits | None | Permitted | Already exhausted. Its edge was text rendering — which you no longer need |
| **Recraft** | 30–50/day, SVG export | **Yes** | **PROHIBITED — free outputs are owned by Recraft and are public** | **Do not use.** The SVG export is the trap |
| **OpenArt** | — | **Yes, baked in** | — | **Do not use.** Confirmed watermarked |

---

## Order of operations

1. Run **Prompt A on Bing Image Creator** → 6 silhouettes
2. Want more range? Same prompt on **Leonardo**
3. Screenshot the grid, upload it in chat
4. I redraw the winner as SVG and rebuild all four assets
5. Run `QC.md` on the output

**Current status:** four assets already built from owl variant A and passing 32 px. Prompt A is only needed if you want a different head shape.

---

## What actually needs money

| | |
|---|---|
| Avatar, watermark, banner, thumbnail template | **₹0 — built, in SVG** |
| Fonts | **₹0** — Instrument Serif + IBM Plex are open-licensed. **Install locally**; sandbox renders fall back to sans and understate the wordmark |
| Archival imagery | **₹0** — Wikimedia Commons, public-domain archives |
| Charts | **₹0** — your own pipeline. The unfair advantage |
| A designer | **Not required.** Revisit only if the channel earns and the mark limits you |
