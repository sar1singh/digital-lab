# ThinkLate — Scene Sheet: Narration to Visual, Line by Line

**Date:** 2026-09-13
**Gap this closes:** the other docs specify *what frame types exist* and *how many assets a video needs*, but never how to go from a finished script to a per-scene visual spec. This is that bridge — and it's the artifact you paste into an AI tool.

**Where it sits:** between Step 4 (script) and Step 6 (build assets) in `13_RUNBOOK.md`.

---

## 1. The format

One row per scene. A scene is a **visual state**, not a sentence — it holds 20–90 seconds while narration runs over it.

| Col | Meaning |
|---|---|
| `#` | Scene number |
| `TIME` | Start timecode |
| `HOLD` | Seconds this visual stays up |
| `NARRATION` | The actual words. Verbatim from the script |
| `SURFACE` | `ink` or `paper` |
| `FRAME` | Frame type from `08_DESIGN-SPEC-FOR-GENAI.md` §2 |
| `VISUAL` | Exactly what's on screen |
| `SOURCE` | Citation to display, or `—` |
| `LABEL` | Chain confidence, where the scene carries a link |
| `ASSET` | Where it comes from: `template` / `chart` / `archive` / `document` / `map` |
| `MOTION` | What moves |

**Target: 18–26 scenes for a 16-minute Standard video.** More than 30 means the script is over-illustrated and the asset budget will blow out.

---

## 2. Worked example — Video 1, first 3 minutes

*Is AI a Bubble? Ask the Railways.* **Draft narration, illustrative. Every figure marked `[VERIFY]` must be replaced with a checked primary source before this is built.**

| # | TIME | HOLD | NARRATION | SURFACE | FRAME | VISUAL | SOURCE | LABEL | ASSET | MOTION |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0:00 | 14s | "Somebody is building a data centre near you right now. It will use more electricity than the town it sits next to, and more water than the farms around it. Nobody asked you." | paper | archive base | Wide aerial of a data-centre construction site | Photo credit | — | archive | Slow push 2% |
| 2 | 0:14 | 20s | "In the next fifteen minutes you'll be able to see the shape of what's happening — and spot the next one of these before it arrives. Because this has happened before. Twice. And both times the thing being built was real." | paper | title card | **Is AI a Bubble? / Ask the Railways** | — | — | template | Text build, 0.4s stagger |
| 3 | 0:34 | 30s | "Here's the number that starts the argument. Roughly this much is being spent on AI infrastructure this year. Not on AI. On the buildings, the chips, the power." | ink | kicker/counter | `$___bn` counting up, label `ON AI INFRASTRUCTURE` | `[VERIFY]` primary | DOCUMENTED | chart | Count-up 2.2s, hold |
| 4 | 1:04 | 45s | "That spending is now large enough that it's holding up growth figures for entire economies. Which means the question isn't whether AI is useful. It's what happens to everything else if the spending slows." | ink | line chart | AI-related capex as share of GDP growth contribution | `[VERIFY]` S&P / national accounts | LIKELY | chart | Draw-on 5s, hold 40s |
| 5 | 1:49 | 8s | "So. Railways." | paper | chapter card | `01 / The thing that was actually real` | — | — | template | Cut |
| 6 | 1:57 | 40s | "In the 1840s Britain decided it needed railways. It was right. Railways were transformative, the demand was real, and the track that got laid is in many cases still carrying trains today." | paper | archive base | 1840s railway construction engraving | Library of Congress / Wikimedia — check item rights | DOCUMENTED | archive | Slow pan right, 3% |
| 7 | 2:37 | 35s | "Investors put in the equivalent of a substantial share of national income. Parliament authorised hundreds of new lines in a matter of years." | paper | document | Railway Act page excerpt, cropped tight | `[VERIFY]` Hansard / UK Parliament archive | DOCUMENTED | document | Highlight box draws on the key clause |
| 8 | 3:12 | 55s | "And then the credit tightened, and the share prices went to roughly this." | ink | line chart | Railway share index, 1840–1855, peak highlighted amber | `[VERIFY]` economic history source | DOCUMENTED | chart | Draw-on 5s, hold 45s |

Note the rhythm: 14s → 20s → 30s → 45s → **8s** → 40s → 35s → 55s. **The 8-second chapter card is doing work** — it breaks a run of long holds. Uniform pacing flattens attention, which is the same finding as sentence-length variance in `12_CRAFT-EVIDENCE.md`.

Note also the surface alternation: paper, paper, **ink**, ink, paper, paper, paper, **ink**.

---

## 3. Paste-ready prompt — script to scene sheet

Give an AI tool your finished script plus this. It returns the sheet.

```
You are producing a scene sheet for a faceless long-form YouTube explainer.

CHANNEL: ThinkLate — hindsight analysis of economics, geopolitics and
technology, landing on individual impact. Voice: friendly, direct, dry,
occasionally sarcastic, hard facts.

DESIGN SYSTEM
  Two surfaces, alternating — never one surface throughout:
    ink   #1B2A4A bg / #F4F1EA text / #D99A2B accent — charts, data, kickers
    paper #F4F1EA bg / #1A1A17 text / #A8741A accent — quotes, archive,
          documents, timelines, title cards
  Frame types: title card · chapter card · kicker/counter · quote card ·
    timeline · comparison table · lower third · source strip · end card ·
    archive base layer · chart · map · document excerpt

RULES
  - A scene is a VISUAL STATE holding 20-90 seconds, not one per sentence
  - Target 18-26 scenes for 16 minutes. Never exceed 30
  - VARY the hold durations deliberately. Put a short 6-10s card between
    long holds. Uniform pacing flattens retention
  - ALTERNATE surfaces. Never more than 3 consecutive scenes on one surface
  - Every scene showing a figure needs a SOURCE to display on screen
  - Label any scene carrying a causal-chain link:
    DOCUMENTED / LIKELY / PLAUSIBLE / SPECULATIVE
  - NO AI-generated illustrative imagery. NO fake archival photos.
    Real archive, real documents, real charts only
  - Every archival still gets a slow push or pan, 1-3% scale. Never static
  - Charts draw on over 4-6s then HOLD 30-60s. Never loop

OUTPUT a markdown table with columns:
  # | TIME | HOLD | NARRATION | SURFACE | FRAME | VISUAL | SOURCE | LABEL |
  ASSET | MOTION

Where ASSET is one of: template / chart / archive / document / map

Mark any figure I have not sourced as [VERIFY].
After the table, list: (a) every chart needed with its data requirement,
(b) every archival image needed with a suggested search term and which
public archive to try, (c) total unique asset count.

SCRIPT:
[paste script here]
```

---

## 4. Paste-ready prompt — scene to visual

Once the sheet exists, generate individual visuals from it.

```
Create the visual for one scene of a ThinkLate video.

SCENE
  Surface:     [ink | paper]
  Frame type:  [from the list]
  Visual:      [the VISUAL cell]
  Source line: [the SOURCE cell]
  Hold:        [seconds]
  Motion:      [the MOTION cell]

TOKENS
  [paste the token block from 08_DESIGN-SPEC-FOR-GENAI.md §1]

REQUIREMENTS
  - 1920x1080, 120px safe margin
  - Exactly ONE accent element
  - Source line bottom-left: mono, dim colour, caption size
  - Wordmark "ThinkLate" bottom-right: serif, dim, caption size
  - Legible on a television at ten feet
  - Text as editable layers, not baked into an image

DO NOT
  - Generate illustrative imagery, people, or anything resembling archive
  - Use gradients, glows, drop shadows or 3D
  - Add a second accent colour
```

---

## 5. Paste-ready prompt — archive sourcing

```
I need archival images for a documentary-style explainer on [TOPIC].

For each of these scenes, suggest 3 specific search strategies:
[paste the VISUAL cells needing archive]

For each, give me:
  - The exact search term to use
  - Which archive to try first: Wikimedia Commons, Library of Congress,
    US National Archives, NYPL Digital Collections, Europeana,
    Internet Archive, Getty Open Content, David Rumsey Maps, NASA
  - What rights status to expect, and what to check on the item page

Do NOT suggest generating images. I need real archival material only.
Do NOT assert that a specific item exists unless you are confident —
give me search strategies, not invented catalogue numbers.
```

That last line matters. AI tools will happily invent plausible-looking archive references. **Never trust a catalogue number you haven't opened.**

---

## 6. Filing

Keep one per video, beside the script:

```
videos/
  v01_ai-bubble-railways/
    script.md
    scene-sheet.md
    assets/
      charts/
      archive/
      documents/
    sources.md
```

`sources.md` *(you create this per video, in that video's own folder)* is the master citation list. It becomes the description's Sources block, and it's what a sponsor or a sceptical commenter will ask for.

---

## 7. Gates

Before building any assets, check the sheet:

- [ ] Scene count is 18–26 (never above 30)
- [ ] Hold durations vary — no run of four similar-length scenes
- [ ] Surfaces alternate — never more than 3 consecutive on one
- [ ] Every figure has a source to display
- [ ] Every chain link is labelled, and none above its real confidence
- [ ] No `[VERIFY]` remaining
- [ ] No scene requires a generated image
- [ ] Every archival still has motion assigned
- [ ] A value claim lands by 0:15
- [ ] The opening delivers the title's promise inside 30 seconds
