# ThinkLate — Motion & Surface

**Date:** 2026-09-13
**Why:** the first template set was static full-screen cards. That is slide-deck grammar, not video grammar. This fixes it, and answers the dark-palette question.

---

## PART 1 — Why it read as a PPT

Five specific causes. None of them is "the design was wrong."

| Cause | Fix |
|---|---|
| **Nothing moved.** Static PNG on screen for 45s is a slide | Charts now animate — lines draw, bars grow, numbers count. `templates/animate.py`, built and tested |
| **One element filled the frame.** Slides do that; video layers | Compose: archival image as base layer, chart or text over it, lower-third for context |
| **No camera.** Even a still image should drift | Slow push or pan (Ken Burns) on every archival still. 1–3% scale over its duration |
| **No rhythm.** Every frame the same weight for the same time | Vary it: 3–6s kickers between 45–60s charts. Contrast creates pace |
| **One surface throughout.** 20 minutes of the same dark field flattens | Two surfaces, alternating. See Part 3 |

---

## PART 2 — Motion, now built

`templates/animate.py` renders MP4 (H.264, yuv420p, 30fps) straight into Resolve.

| Function | Motion | Duration |
|---|---|---|
| `line_draw()` | Lines draw left→right, ease-out. Series labels appear only in the last 20% so they don't track across the title | 5s draw + hold |
| `bars_grow()` | Bars grow **in sequence**, staggered 0.12s, with values counting up | 4s + stagger + hold |
| `counter()` | The kicker number counts up; the accent rule widens underneath | 2.2s + 2s hold |
| `share_fill()` | Stacked composition fills in over time | 5s + hold |

**Easing is ease-out cubic, deliberately.** Linear motion reads mechanical — like a chart animating because the software can, rather than because the argument needs it.

### Timing rule

> **Draw on over 4–6 seconds, then HOLD for 30–60.**

The motion earns attention; the hold is where comprehension happens. Do not loop, do not cut away at 3 seconds. That's short-form grammar and it destroys retention in long-form.

### What still needs doing in Resolve, not Python

- **Camera moves on stills** — 1–3% scale drift over the shot. Never static on an archival photo
- **Text builds** — reveal bullet lines as narration reaches them, not all at once
- **Map flows** — animated arrows along a shipping route. Fusion, or an animated GIF overlay
- **Highlight pulses** — draw a box or underline on a document excerpt as you cite it
- **Grain** — one adjustment layer over the whole timeline. `GRAIN = False` in `templates/frames.py` because SVG `feTurbulence` renders inconsistently across Affinity, Resolve and ImageMagick

### Layering — the single biggest visual upgrade

Stop thinking "which card is on screen." Think in three layers:

```
Layer 3   text / callout / source strip
Layer 2   chart, diagram or document excerpt
Layer 1   archival image or texture, dimmed 60-75%, slow drift
```

A chart floating over a dimmed 1840s railway photograph is video. The same chart full-screen on flat navy is a slide. Same asset, different grammar, near-zero extra work.

---

## PART 3 — The colour question

**Short answer: dark is right for data and wrong as the only surface. Use two.**

### Where dark is correct

- Charts and data read better on dark. Amber pops; gridlines recede
- It's the convention in this category — finance and data channels, terminals, Patrick Boyle
- It signals "analysis," which is the positioning

### Where dark actively hurts

- **20 minutes of one dark field is monotonous.** No rhythm, no contrast, and it flattens attention
- **Your topics are bubbles, collapses, chokepoints and crises. Dark + crisis = doom channel.** That conflicts directly with your stated voice — friendly, dry, sarcastic. Doom-mongering is a different brand with a different audience, and it's the most common failure in this niche
- **Archival material is paper-toned.** Documents, newspapers, 19th-century photographs, filings — forcing them onto dark navy fights the material
- **Thumbnails: most viewers browse in dark mode.** A dark thumbnail blends into the feed. A paper-dominant one cuts through. This is a practical distribution argument, not an aesthetic one

### The system

Two surfaces, defined in `templates/brand.py` as `SURFACES`:

| Surface | Background | Text | Accent | Use for |
|---|---|---|---|---|
| **ink** | `#1B2A4A` | `#F4F1EA` | `#D99A2B` | Charts, data, kickers, counters |
| **paper** | `#F4F1EA` | `#1A1A17` | `#A8741A` | Quotes, documents, archival, timelines, title cards |

Note the accent changes: `#D99A2B` fails contrast on paper, so the paper surface uses a darker ochre `#A8741A`. This is handled in `SURFACES` — don't override it by hand.

### Sequencing across a video

```
paper   title card
ink     kicker — the number that sets up the question
paper   archival photograph + document excerpt
ink     chart 1
paper   quote
ink     chart 2, chart 3
paper   timeline
ink     final chart
paper   end card
```

**Alternation is the point.** Each switch re-engages attention at zero production cost, and it makes a 20-minute video feel structured rather than long.

### Thumbnails

**Default to paper-dominant.** Ink for one specific case: when the subject image is itself dark (night satellite, dark archival photo) and forcing it onto paper would look pasted-on.

---

## PART 4 — Files

| File | Status |
|---|---|
| `templates/brand.py` | Extended with `SURFACES` |
| `templates/frames.py` | Static SVG frames. Being extended for surface switching |
| `templates/charts.py` | Static charts — still needed for thumbnails and stills |
| `templates/animate.py` | **New.** Animated charts → MP4 |
| `templates/surface_demo.py` | **New.** Renders the ink/paper comparison |
| `preview/anim_*.mp4` | Working motion samples |
| `templates/preview/_sheet_surfaces.png` | The ink vs paper comparison |
| `templates/preview/_sheet_thumbs.png` | Thumbnail comparison, both surfaces |

---

## PART 5 — Revised week-2 build list

- [ ] Decide surface split — recommend adopting the two-surface system as specified
- [ ] Rebuild `title_card`, `chapter_card`, `quote_card`, `timeline` on the **paper** surface
- [ ] In Resolve: build the three-layer composition as a template timeline (texture → content → text)
- [ ] In Resolve: Fusion titles for title/chapter/kicker so they're text-field swaps
- [ ] One grain adjustment layer over the whole timeline
- [ ] Collect 5–10 archival base-layer images to reuse as backgrounds across videos
- [ ] Test one 60-second segment end to end — motion, layering, surface switch — **before** scripting video 1

That last item matters most. One finished minute tells you more than another week of template work.
