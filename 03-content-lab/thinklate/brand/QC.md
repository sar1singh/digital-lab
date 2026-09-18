# ThinkLate — Asset QC Rubric (4 verticals)

How to use: drop the asset in `brand/`, ask for "run QC on [file]". Scored 1–5 per line, **any score of 1 or 2 blocks publishing.**

**Honest capability statement** — what I can and cannot do:

| | |
|---|---|
| ✅ **Technical QC** | Fully. I can view the image, measure contrast ratios, check dimensions, file weight, safe areas, and render it at 32 / 98 / 128px to test legibility |
| ✅ **Expert heuristic QC** | Yes, against documented principles (Mayer's signalling and coherence, the 2–3 word CTR finding, the 69%-face headwind) |
| ✅ **Design-psychology QC** | Yes — research-grounded, sources cited |
| ⚠️ **Trend QC** | Only if I search first. Trend knowledge goes stale; I'll re-research at each review |
| ❌ **Non-tech audience QC** | **I can apply heuristics but I am not a naive viewer.** This vertical is a simulation, not data. **The real version costs nothing: show it to 5 people who don't know the brand and ask one question.** See V3 |

---

## V1 — TECHNICAL (objective, pass/fail)

| # | Check | Spec |
|---|---|---|
| 1.1 | Dimensions exact | Avatar 800×800 · watermark 150×150 · banner 2560×1440 · thumbnail 1280×720 |
| 1.2 | File weight | Banner <6 MB · thumbnail <2 MB · watermark <1 MB · avatar <15 MB |
| 1.3 | Banner safe area | All readable content inside 1235×338 centred |
| 1.4 | Forbidden by YouTube | No shadows, borders or frames on the banner file |
| 1.5 | Colour accuracy | Exact hex: `#1B2A4A` `#F4F1EA` `#D99A2B` `#A8741A` `#98A2B3`. *(palette unified on `#1B2A4A` 2026-09-13; `#111827` retired — `BRAND.md` → PART `02_BRAND` PALETTE ARCHITECTURE)* **`#111827` and `#6B7280` are retired — an asset using either FAILS this check** |
| 1.6 | **Contrast ratio** | Body text ≥4.5:1 · large text ≥3:1 (WCAG AA). **Amber `#D99A2B` on paper fails — must be `#A8741A`** |
| 1.7 | Avatar circle-safe | Nothing important outside the inscribed circle |
| 1.8 | Watermark survives light footage | Has outline ring or solid rim |
| 1.9 | Editable text | Not flattened into raster |
| 1.10 | End card zones reserved | 560×315 and 270×270 left clear |

## V2 — EXPERT UI/UX + CURRENT TREND

| # | Check | Criterion |
|---|---|---|
| 2.1 | **One accent rule** | Exactly one amber element. Two = fail (Mayer's signalling principle) |
| 2.2 | Type discipline | Max 2 families. Three is amateur |
| 2.3 | Hierarchy | One dominant element; eye path unambiguous in <1s |
| 2.4 | Negative space | Generous. Cramped reads cheap |
| 2.5 | Optical alignment | Not just mathematical — serif overshoots need correction |
| 2.6 | **2026–27 trend fit** | Serif-forward and editorial is *on* trend — AI companies moved en masse to serifs to read as human. Warmer colour systems and human texture are current. **Flat cold minimalism is going out** |
| 2.7 | **Trend risk to avoid** | Gradient layering, duotones, elastic/stretched letterforms and collage type are trending — **all wrong for a credibility brand.** Do not chase these |
| 2.8 | Controlled imperfection | Subtle paper grain / archival texture is on-trend AND on-brand. One of the few trends worth taking |
| 2.9 | Motion-ready | Layered, not flattened — 2026 identity systems are expected to animate |
| 2.10 | Scales across contexts | Works at 32px and on a TV. Ranges, not one fixed lockup |

## V3 — NON-TECH AUDIENCE

**I simulate this; I do not measure it.** Treat my score as a hypothesis.

| # | Check | Method |
|---|---|---|
| 3.1 | 3-second read | What is this channel about? Answerable from the asset alone |
| 3.2 | Category guess | Does a stranger place it as "serious explainer" not "crypto bro" or "kids channel"? |
| 3.3 | Trust read | Does it look like it knows things, or like it's selling something? |
| 3.4 | Owl recognition at 32px | Instantly an owl, or a blob? |
| 3.5 | Thumbnail: would you click | Beside 3 real competitors at feed size |
| 3.6 | Dark-mode survival | Most viewers browse in dark mode. Does it disappear? |

> **The real test, free:** send the avatar and one thumbnail to **five people who don't know the brand.** Ask exactly one question — *"What do you think this channel is about?"* Don't explain first. If 3+ get it roughly right, it works. That beats any score I give you.

## V4 — DESIGN PSYCHOLOGY (research-grounded)

| # | Check | Evidence |
|---|---|---|
| 4.1 | Signalling | Single accent directs attention — Mayer |
| 4.2 | Coherence | Nothing decorative competing with the message — Mayer |
| 4.3 | **Redundancy** | Text doesn't repeat what the narration will say — Mayer. Kicker cards are the usual offender |
| 4.4 | Cognitive load | ≤3 distinct elements per frame; working memory is the constraint |
| 4.5 | Face substitution | 69% of breakout thumbnails use a face (80% of top performers). Faceless = **contrast is mandatory compensation**, not styling |
| 4.6 | Curiosity gap | Thumbnail + title create an information gap, not a summary — Loewenstein 1994 |
| 4.7 | Fluency vs distinctiveness | Easy to process AND different from the feed around it. Fluent-but-generic loses |

---

## Output format when QC is run

```
ASSET: [file]  SIZE: [px]  WEIGHT: [kb]

V1 TECHNICAL      x/50   [blockers listed]
V2 UI/UX + TREND  x/50   [blockers listed]
V3 AUDIENCE       x/30   [simulated — verify with 5 humans]
V4 PSYCHOLOGY     x/35   [evidence cited]

VERDICT:  SHIP / FIX FIRST / REBUILD
BLOCKERS: [any 1-2 score, with the fix]
TOP 3 FIXES RANKED BY IMPACT
```

## Trend sources — re-check at each review

[Fontfabric — 10 design & typography trends 2026](https://www.fontfabric.com/blog/10-design-trends-shaping-the-visual-typographic-landscape-in-2026/) · [icons8 — design trends 2026–2027](https://icons8.com/blog/articles/design-trends-for-2027/) · [Hemisphere — 12 strategic brand shifts 2026](https://www.hemispheredm.com/graphic-design-trends-2026) · [Bigeye — 2027 design trends](https://www.bigeyeagency.com/insights/2027-design-trends-that-will-transform-consumer-brands) · [It's Nice That — graphic trends 2026](https://www.itsnicethat.com/features/forward-thinking-graphic-trends-2026-graphic-design-120126) · [Typography trends 2026–27](https://medium.com/design-bootcamp/typography-trends-2026-2027-when-letters-begin-to-breathe-8499fb6c5ef1)
