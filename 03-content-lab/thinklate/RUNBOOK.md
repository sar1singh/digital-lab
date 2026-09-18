# ThinkLate — Runbook

**How to make one video, start to finish**

Everything about producing a video: the step sequence, the script format, the scene sheet, assets and which tool to use.

**Consolidated 2026-09-13** from 5 separate files. Originals preserved in `ARCHIVE/originals/`.

## Parts in this file

- **13_RUNBOOK** — was `13_RUNBOOK.md`
- **15_SCRIPT-FORMAT** — was `15_SCRIPT-FORMAT.md`
- **14_SCENE-SHEET** — was `14_SCENE-SHEET.md`
- **05_ASSETS-AND-PROMPTS** — was `05_ASSETS-AND-PROMPTS.md`
- **16_FREE-TOOL-STACK** — was `16_FREE-TOOL-STACK.md`


---

# PART — 13_RUNBOOK

> Merged from `13_RUNBOOK.md` on 2026-09-13. Content unchanged; headings demoted one level. Cross-references to `RUNBOOK.md` → PART `13_RUNBOOK` elsewhere still resolve to this part.

**Date:** 2026-09-13
**Purpose:** the step-by-step for making one video. Every other doc is reference; this is the sequence. An AI agent or you can start here and work through it.

---

### Before any of this

Read `STRATEGY.md` → PART `00_CONTEXT`. If you're scripting, also read `CRAFT.md` → PART `10_MACRO-TO-MICRO` §3 and §5, and `CRAFT.md` → PART `03_CONTENT-AND-VOICE` Part 3.

---

### Step 0 — Pick the tier

| Hours available this fortnight | Tier | Length |
|---|---|---|
| 4–5 | **Floor** — "One Chart" | 6–8 min |
| 10–12 | **Standard** | 14–18 min |
| 15–20 | **Pillar** | 25–30 min |

Pick honestly, based on the fortnight you actually have. **Shipping a Floor video beats skipping a Standard one.**

---

### Step 1 — Title and thumbnail text FIRST (30 min)

Before any research. If you can't write a good title, the idea isn't sharp yet.

- Title: **30–50 characters**, searchable noun front-loaded, question or claim
- Thumbnail text: **2–3 words**, different from the title
- Target search phrase: write it down
- **Validate** in Google Trends and the vidIQ free tier — ten minutes

Reference: `CRAFT.md` → PART `04_TITLES-AND-THUMBNAILS` §5, `CRAFT.md` → PART `12_CRAFT-EVIDENCE` §1.

**Gate:** would you click this in your own feed with no channel name attached? If not, rewrite before continuing.

---

### Step 2 — The chain, before the research (30 min)

Sketch the causal chain from macro event to individual impact. Five links maximum.

```
LINK 1  [macro event]                      DOCUMENTED?  need source
LINK 2  [first-order effect]               DOCUMENTED?  need source
LINK 3  [second-order effect]              LIKELY
LINK 4  [effect on a household]            PLAUSIBLE
LINK 5  [how it feels]                     SPECULATIVE
```

**Gates:**
- Anchored in the financial or career domain? If it only lands on psychology, stop.
- More than five links? The connection is too weak. Drop it.
- Can't name a source for links 1 and 2? Not ready to research — the video may not exist.

Reference: `CRAFT.md` → PART `10_MACRO-TO-MICRO` §5.

---

### Step 3 — Research (Floor 1–2 hrs · Standard 2–3 · Pillar 4–6)

**Research the cluster, not the video.** If this is the first video of a cluster, budget the full session and come out with outlines for 3–4 videos.

1. Gather primary documents — USGS, IMF, World Bank, FRED, UN Comtrade, UNCTAD, EIA, Our World in Data, central banks
2. Feed them to NotebookLM. Use the fact-extraction prompt in `RUNBOOK.md` → PART `05_ASSETS-AND-PROMPTS` §5a

   **NotebookLM discipline — added 2026-09-13.** It is source-grounded and attaches inline citations that jump to the exact passage, which is what makes it compatible with hard rule 1. **But its summary is not "a source you opened" — the cited passage is.** So: use it to *locate*, then **click every citation and read the original sentence** before that fact enters a script. A figure that only ever existed in NotebookLM's prose is an unsourced figure.

   **Two failure modes worth naming:**
   - **Never script from a report.** Its register is uniform and explanatory — script from it and the video sounds exactly like the AI-template content this channel is positioned against. Extract facts; write the prose yourself
   - **Don't paste source text into narration.** Summarise and paraphrase (`§5` of the project rules). The Sources block credits it; the script doesn't quote it at length

   Quotas and feature names change often and the figures circulating are third-party blog claims, not Google documentation — **check in-product rather than trusting any number written down here.**
3. Fill in every source for links 1 and 2. Downgrade any link you can't source
4. Run the historical-parallel prompt. **Note where the analogy breaks** — that goes in the script

**Hard rule:** never accept a figure you haven't seen in a document you opened.

---

### Step 4 — Script (Floor 1 hr · Standard 1.5–2 · Pillar 3)

Boomerang structure (`CRAFT.md` → PART `10_MACRO-TO-MICRO` §3):

| Section | Standard (16 min) |
|---|---|
| Micro hook | 0:00–0:40 |
| **Value claim** | **by 0:15** — what they'll be able to see by the end |
| The gap | 0:40–1:30 |
| Zoom out: macro | 1:30–7:00 |
| The pattern | 7:00–10:30 |
| Zoom in: the chain, labelled | 10:30–14:00 |
| The skill to notice | 14:00–15:00 |
| Close on a better question | last 60s |

**Then:**

1. Run the pre-script fact-check prompt (`RUNBOOK.md` → PART `05_ASSETS-AND-PROMPTS` §5a). Fix every UNSOURCED claim
2. **Vary sentence length deliberately** — long, then short. Variance retains ~1.8× better than uniform short sentences
3. Read aloud. Cut every clause you stumble on
4. Delete "furthermore", "moreover", "it is important to note"
5. Check: does the opening deliver the title's promise within 30 seconds?

---

### Step 5 — Mark asset cues (20 min)

Read the script and mark in the margin. **Target 20–28 unique assets for a 16-minute video, not 150.**

Then **group by type** — all charts together, all archive together. Batching by type rather than script order halves the sourcing time.

Reference: `RUNBOOK.md` → PART `05_ASSETS-AND-PROMPTS` §1 and §6.

---

### Step 6 — Build assets (Floor 1 hr · Standard 2–2.5 · Pillar 3–4)

In this order:

1. **Charts** — from verified data only. Source line baked in
2. **Maps** — Datawrapper or MapChart
3. **Archival images** — Wikimedia, Library of Congress, National Archives, NYPL, Europeana. **Check the rights statement on each individual item**
4. **Document excerpts** — crop tight, attribute on screen
5. **Template frames** — title, chapter, quote, kicker, timeline, table. Text swaps only

**Surface alternation** (`CRAFT.md` → PART `06_MOTION-AND-SURFACE`): paper for title / quotes / archive / timeline · ink for charts / data / kickers.

---

### Step 7 — Record (30–60 min)

- Soft-furnished room, duvet or curtain behind you, never bare walls or glass
- Fifine ~15 cm, slightly off-axis
- Record in sections, not one take
- **Batch two or three videos' audio in one sitting** when you can

---

### Step 8 — Edit (Floor 1–1.5 hrs · Standard 2–3 · Pillar 3–4)

1. Voice track first, then assemble visuals to it
2. **Three-layer composition** — background texture/archive dimmed 60–75%, content, then text
3. Slow push or pan on every archival still, 1–3% scale
4. Animated charts draw over 4–6s, then **hold 30–60s**
5. Fairlight → Voice Isolation on the voice track
6. Film grain as one adjustment layer over the whole timeline
7. **No intro animation for the first 10 videos**
8. End card with both YouTube end-screen zones reserved

---

### Step 9 — Package and publish (1 hr)

- Thumbnail: 1280×720, under 2 MB, 2–3 words, **high contrast mandatory**, one amber element
- **Feed test:** place it beside three competitors at feed size. Does yours read fastest?
- **TV test:** view at ten feet
- Description: summary with the search phrase, chapters, **Sources block**, newsletter link, socials
- Subtitles: accurate, corrected. Never ship auto-generated
- Add to the relevant playlist
- Tags: two minutes, then move on — they barely matter
- Set the next video's end-screen link

---

### Step 10 — After publishing

**Don't open Analytics for 48 hours.** Early numbers are noise.

At 7 days, record four numbers only:

| Metric | Target |
|---|---|
| 30-second retention | >70% |
| Average view duration | >40% (Standard tier) |
| Impressions CTR | >4% |
| Newsletter signups per 100 views | >2 |

**Diagnosis:**

- 40%+ drop in the first 30s → weak hook, or the opening didn't deliver the title
- Low AVD but good 30s → the middle sags; tighten pacing or cut length
- Low CTR, good retention → thumbnail contrast or title
- Everything fine, low views → nothing is wrong. Publish the next one

**One process improvement per video. Never a redesign.**

**Which improvement is already decided** — don't pick it while demoralised. `STRATEGY.md` → PART `09_COUNTER-STRATEGY` §12 names one for every video from 1 to 30, sequenced hook → retention → packaging → cost, with motion deliberately late. Do the named item **even if the last video got zero views**; the ladder is independent of performance, which is the point.

---

### Step 11 — Log it

Append to `LOG.md`:

```
### Video NN — [title]
Published:      YYYY-MM-DD
Tier:           Floor / Standard / Pillar
Hours:          [actual, by step]
Cluster:        [name]
Chain anchor:   financial / career
Weakest link:   [which, and why]
7-day:          views / AVD% / 30s% / CTR% / newsletter
Lesson:         [one line]
Next change:    [one thing]
```

**Log the hours honestly.** The cost ratchet in `STRATEGY.md` → PART `09_COUNTER-STRATEGY` §7 only works if you can see whether cost is actually falling. If video 7 costs the same as video 3, fix the pipeline before making another video.

---

### Total time budget

| Step | Floor | Standard | Pillar |
|---|---|---|---|
| 1–2 Title + chain | 0.5 | 1 | 1 |
| 3 Research | 1–2 | 2–3 | 4–6 |
| 4 Script | 1 | 1.5–2 | 3 |
| 5 Asset cues | 0.2 | 0.3 | 0.5 |
| 6 Assets | 1 | 2–2.5 | 3–4 |
| 7 Record | 0.5 | 0.75 | 1 |
| 8 Edit | 1–1.5 | 2–3 | 3–4 |
| 9 Package | 0.5 | 1 | 1 |
| **Total** | **~5–6** | **~11–13** | **~17–21** |

Expect video 1 to take 1.5× these numbers. By video 6 you should be at or under them.

---

### Stop-and-check gates

Any of these means stop and fix before continuing:

- Can't write a title you'd click → the idea isn't ready
- Chain needs more than five links → connection too weak
- A figure you can't source → cut it or downgrade its label
- A psychological claim doing load-bearing work → re-anchor in financial or career
- The script tells the viewer what to *do* → that's advice; cut it
- Title contains a product name or version number → you're making an instance, not an invariant
- Over 30 unique assets → the script is over-illustrated


---

# PART — 15_SCRIPT-FORMAT

> Merged from `15_SCRIPT-FORMAT.md` on 2026-09-13. Content unchanged; headings demoted one level. Cross-references to `RUNBOOK.md` → PART `15_SCRIPT-FORMAT` elsewhere still resolve to this part.

**Date:** 2026-09-13
**Gap this closes:** the other docs specify voice and structure but not the *formatting* a script needs to be read aloud cleanly in one pass. You're reading verbatim, so the script is a performance document, not prose.

**Where it sits:** output of Step 4 in `RUNBOOK.md` → PART `13_RUNBOOK`, input to Step 7 (record).

---

### 1. Why a special format

A script written to be *read* fails when *spoken*. Four specific failures:

1. **Numerals stall you.** "$1.2bn" makes you compute mid-sentence. Written as "one point two billion dollars," you just read it.
2. **No breath marks means you run out of air** mid-clause and re-take.
3. **Unfamiliar names cause stumbles** you only discover on the recording.
4. **No take boundaries means one flub costs you the whole section.**

All four are avoidable with notation. The format below adds maybe 10 minutes to scripting and removes most re-takes.

---

### 2. Notation

| Mark | Meaning |
|---|---|
`//` | Short pause. Half a beat. Where a comma would be if you were breathing
`///` | Full stop beat. Let it land. Use after a number or a punchline
`////` | Section break. Two seconds. Usually where the visual changes
**`bold`** | Stress this word
`[TAKE 4]` | Recording chunk boundary. Stop, breathe, restart here if you flub
`(pron: soo-EZ)` | Pronunciation guide, inline, first occurrence only
`{S12}` | Scene number from the scene sheet — tells you the visual is changing
`⟨note⟩` | Direction to yourself. Never read aloud

`⟨src: R3⟩` | **Citation tag.** Points at an entry in that video's `sources.md`. Never read aloud

**Numbers are always written as spoken.** Never `69%`, always `sixty-nine percent`. Never `$1.2bn`, always `one point two billion dollars`. Never `1845`, always `eighteen forty-five`.

---

### 2b. Citations inside the script — added 2026-09-13

**The gap this closes:** `RUNBOOK.md` → PART `14_SCENE-SHEET` has a `SOURCE` column and every video needs a Sources block in its description, but nothing tied a *spoken claim* to a *source*. So a claim could drift between draft and publish with nobody able to check it. This is that link.

#### How it works — three files, one ID

1. **`sources.md`** in the video folder. Every source gets a permanent ID: `R1`, `R2`, `R3`…
2. **The script** tags each factual claim inline with `⟨src: R1⟩`. It is a `⟨note⟩`, so it is **never spoken**
3. **The scene sheet's `SOURCE` column** carries the same ID, so the on-screen citation and the spoken claim cannot disagree

#### `sources.md` format

```
### R1
Author / publisher:  Andrew Odlyzko, University of Minnesota
Title:               Collective Hallucinations and Inefficient Markets
Date:                15 January 2010
URL:                 https://ssrn.com/abstract=1537338
Opened:              2026-09-13   ← the date I actually read it
Read:                abstract only / full text / pp. 12–19
Claims it supports:  "greatest technology mania in history"
                     "trustworthy quantitative measures" existed
On-screen credit:    Odlyzko, 2010
```

**`Opened` and `Read` are the point.** Hard rule 1 says no figure that isn't in a source you actually opened — this is where that becomes auditable instead of a promise. **"Read: abstract only" is an honest and common answer.** A claim resting on an abstract is weaker than one resting on page 14, and the file should say which.

#### The three gates

- **Every number in the script carries a `⟨src:⟩` tag, or it is cut.** No exceptions, no "obviously true"
- **A claim whose only support is an AI summary is unsourced.** NotebookLM locates the passage; the passage is the source (`RUNBOOK.md` → PART `13_RUNBOOK` step 3)
- **Before publishing:** every ID used in the script appears in `sources.md`, and every entry in `sources.md` appears in the description's Sources block. Mismatch either way is a bug

#### Example

```
Britain ke do railway manias mein // capital investment tha //
**pandrah se bees percent** // GDP ka. ⟨src: R2⟩ ///
```

Worked example: `videos/01_is-ai-a-bubble-ask-the-railways/sources.md`.

---

### 3. Worked example

Video 1 opening. **Draft. Figures marked `[VERIFY]` need a checked primary source.**

```
[TAKE 1]  {S1}

Somebody is building a data centre near you right now. //
It will use more electricity than the town it sits next to // and more
water than the farms around it. ///
Nobody asked you. ////


[TAKE 2]  {S2}

In the next fifteen minutes you'll be able to see the shape of what's
happening // and spot the next one of these before it arrives. ///

Because this has happened before. // Twice. ///
And both times // the thing being built was **real**. ////


[TAKE 3]  {S3}   ⟨counter animates up — leave 3s of air after the number⟩

Here's the number that starts the argument. //

Roughly [VERIFY] billion dollars is going into AI infrastructure this
year. ///
Not into AI. // Into the **buildings** // the **chips** // and the
**power**. ////


[TAKE 4]  {S4}   ⟨chart draws on over 5s — read slower here⟩

That spending is now big enough that it's holding up growth figures for
entire economies // which means the interesting question isn't whether
AI is useful. ///

It's what happens to **everything else** // if the spending slows. ////


[TAKE 5]  {S5}

So. ///
Railways. ////
```

**Note the sentence-length variance** — long, then "Twice." then long, then "So. Railways." That's the 1.8× retention finding from `CRAFT.md` → PART `12_CRAFT-EVIDENCE` applied, and it's also where the deadpan lives.

---

### 4. Structural requirements

Every script must have:

- **A value claim by `[TAKE 2]`** — what the viewer will be able to see or do by the end. Not just an intriguing observation
- **Take boundaries every 30–60 seconds.** Shorter near the opening where precision matters most
- **`{S}` markers** matching the scene sheet, so you know when the visual shifts and can pace to it
- **One idea per line, lines short enough to say in one breath.** If you can't, break it
- **Chain labels spoken, not just shown.** When you reach an inferred link, say so: *"and here I'm inferring // this next part isn't documented"*
- **No numeral anywhere.** Search the script for digits before recording. Any hit is a bug

---

### 5. Pre-record checklist

- [ ] Read the whole thing aloud once, timed. Long-form reads at roughly 140–155 words/minute
- [ ] Every clause you stumbled on: rewritten, not re-attempted
- [ ] Zero digits in the script
- [ ] Every proper noun you're unsure of has a `(pron:)` guide
- [ ] Take boundaries every 30–60 seconds
- [ ] No line longer than one comfortable breath
- [ ] Value claim lands inside the first 15 seconds
- [ ] "furthermore", "moreover", "it is important to note" — all deleted
- [ ] Every `[VERIFY]` replaced with a sourced figure
- [ ] Sentence lengths visibly vary — no run of four similar-length lines

---

### 6. Paste-ready prompt — produce a script in this format

```
Write a verbatim-read script for a faceless long-form YouTube explainer.

CHANNEL: ThinkLate — hindsight analysis of economics, geopolitics and
technology, landing on individual impact.

VOICE: friendly, direct, dry, occasionally sarcastic, hard facts.
Sarcasm aimed at decisions and systems, NEVER at people. Understatement
over emphasis. The facts carry the joke.

STRUCTURE (boomerang):
  1. Micro hook — something the viewer has personally noticed (0:00-0:40)
  2. Value claim by second 15 — what they'll be able to SEE by the end
  3. The gap — "you've felt this, nobody told you why"
  4. Zoom out — the documented history and mechanism
  5. The pattern — what repeats and why
  6. Zoom back in — the causal chain, link by link, labelled
  7. The skill — what to watch for next time. A pattern, NEVER an action
  8. Close — reframe the opening as a better question. NEVER a prediction

FORMATTING FOR VERBATIM READING — mandatory:
  //     short pause        ///  full beat        ////  section break
  **word**  stress
  [TAKE n]  recording chunk boundary, every 30-60 seconds
  (pron: xxx)  pronunciation guide on first use of any hard name
  {Sn}   scene number where the visual changes
  ⟨note⟩ direction to the reader, not spoken

  - NO NUMERALS ANYWHERE. Write every number as spoken words:
    "sixty-nine percent", "one point two billion dollars",
    "eighteen forty-five"
  - One idea per line. Every line sayable in one breath
  - VARY SENTENCE LENGTH DELIBERATELY. Long, then very short. Uniform
    short sentences read as staccato and flatten retention
  - Target 140-155 words per minute of runtime

HARD RULES:
  - Mark any figure I have not given you a source for as [VERIFY].
    Do not invent figures, dates, quotations or statistics
  - Label causal-chain links in the narration itself where they are
    inferred: "and here I'm inferring", "this part isn't documented"
  - No advice. Explain why something is happening; never say what to do
  - No predictions stated as certainty
  - No "they don't want you to know" framing
  - No mockery of named individuals

TARGET LENGTH: [6-8 / 14-18 / 25-30] minutes

TOPIC: [title]
CHAIN: [paste the five-link chain from Step 2]
SOURCED FACTS: [paste your verified research — this is the only factual
                material you may use]
```

---

### 7. Recording from this format

- Record **take by take**, not in one pass. A flub costs you 40 seconds, not 16 minutes
- Say the `[TAKE n]` number aloud before each chunk — it makes the editor's job trivial
- Leave 2 seconds of silence at the start and end of every take
- `////` breaks are where you stop, drink water, and reset
- Where a `⟨note⟩` says the chart animates, **read slower**. Your instinct will be to rush; the visual needs the air
- Record room tone for 30 seconds at the end — Fairlight uses it for noise reduction

---

### 8. Filing

```
videos/v01_ai-bubble-railways/
  script.md          ← this format
  scene-sheet.md
  sources.md
  audio/
    take_01.wav ... take_28.wav
    room_tone.wav
  assets/
```

Keep the script and scene sheet open side by side while recording. The `{S}` markers are the join between them.


---

# PART — 14_SCENE-SHEET

> Merged from `14_SCENE-SHEET.md` on 2026-09-13. Content unchanged; headings demoted one level. Cross-references to `RUNBOOK.md` → PART `14_SCENE-SHEET` elsewhere still resolve to this part.

**Date:** 2026-09-13
**Gap this closes:** the other docs specify *what frame types exist* and *how many assets a video needs*, but never how to go from a finished script to a per-scene visual spec. This is that bridge — and it's the artifact you paste into an AI tool.

**Where it sits:** between Step 4 (script) and Step 6 (build assets) in `RUNBOOK.md` → PART `13_RUNBOOK`.

---

### 1. The format

One row per scene. A scene is a **visual state**, not a sentence — it holds 20–90 seconds while narration runs over it.

| Col | Meaning |
|---|---|
| `#` | Scene number |
| `TIME` | Start timecode |
| `HOLD` | Seconds this visual stays up |
| `NARRATION` | The actual words. Verbatim from the script |
| `SURFACE` | `ink` or `paper` |
| `FRAME` | Frame type from `BRAND.md` → PART `08_DESIGN-SPEC-FOR-GENAI` §2 |
| `VISUAL` | Exactly what's on screen |
| `SOURCE` | Citation to display, or `—` |
| `LABEL` | Chain confidence, where the scene carries a link |
| `ASSET` | Where it comes from: `template` / `chart` / `archive` / `document` / `map` |
| `MOTION` | What moves |

**Target: 18–26 scenes for a 16-minute Standard video.** More than 30 means the script is over-illustrated and the asset budget will blow out.

---

### 2. Worked example — Video 1, first 3 minutes

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

Note the rhythm: 14s → 20s → 30s → 45s → **8s** → 40s → 35s → 55s. **The 8-second chapter card is doing work** — it breaks a run of long holds. Uniform pacing flattens attention, which is the same finding as sentence-length variance in `CRAFT.md` → PART `12_CRAFT-EVIDENCE`.

Note also the surface alternation: paper, paper, **ink**, ink, paper, paper, paper, **ink**.

---

### 3. Paste-ready prompt — script to scene sheet

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

### 4. Paste-ready prompt — scene to visual

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

### 5. Paste-ready prompt — archive sourcing

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

### 6. Filing

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

### 7. Gates

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


---

# PART — 05_ASSETS-AND-PROMPTS

> Merged from `05_ASSETS-AND-PROMPTS.md` on 2026-09-13. Content unchanged; headings demoted one level. Cross-references to `RUNBOOK.md` → PART `05_ASSETS-AND-PROMPTS` elsewhere still resolve to this part.

**Date:** 2026-09-13
**Problem this solves:** asset gathering is the stated reason previous attempts died. Hunting a unique visual per line of dialogue is unsustainable at 10–15 hrs/week.

---

### 1. The actual fix — reframe the problem

You are trying to source a unique asset per scene. **That is the wrong goal.** It is also why you burned out.

The fix is not better stock hunting. It is **reducing the number of unique assets a video needs.**

> **A 20-minute video needs about 12–18 distinct visual states, not 200.** Each one holds for 45–90 seconds while the narration does the work.

Long-form explainer viewers tolerate — and actually prefer — a chart they can read for 60 seconds over a cut every 3 seconds. Rapid cutting is a short-form grammar. Applying it to long-form costs you enormous production time and *reduces* comprehension.

#### The frame-type library

Build a template for each of these **once**. Then every video is filling templates, not sourcing.

| # | Frame type | Holds for | Source |
|---|---|---|---|
| 1 | Title / chapter card | 2–4s | Your template |
| 2 | Animated line or bar chart | 30–90s | Your data pipeline |
| 3 | Static chart with callout | 20–45s | Your data pipeline |
| 4 | Map with highlight or flow arrows | 30–60s | Datawrapper / MapChart / Natural Earth |
| 5 | Timeline | 30–60s | Your template |
| 6 | Quote card (attributed, dated) | 10–20s | Your template |
| 7 | Document excerpt — filing, report, newspaper | 10–25s | Primary source, cropped |
| 8 | Archival photograph | 15–40s | Public-domain archives |
| 9 | Archival newsreel / film clip | 10–30s | Public domain or licensed |
| 10 | Comparison table | 20–40s | Your template |
| 11 | Simple diagram / schematic | 30–60s | Figma, built once per concept |
| 12 | Kicker card — the one number, full screen | 3–6s | Your template |
| 13 | Textured / abstract background under narration | 20–60s | Reusable loop, made once |
| 14 | Source citation strip | overlay | Your template |

**Reuse rule:** frames 1, 5, 6, 10, 12, 13, 14 are **pure template** — zero sourcing, forever. That's half your runtime covered with no asset hunting at all.

---

### 2. Your unfair advantage — script the charts

You are a Node/JS engineer. Most creators in this niche are not. **This is the single highest-leverage thing in this document.**

Build a small chart-generation pipeline once:

- Input: a CSV or JSON
- Output: a PNG or SVG in ThinkLate's palette (`#1B2A4A` / `#F4F1EA` / `#D99A2B`), correct fonts, source line baked into the corner
  *(hex updated 2026-09-13 — the palette unified on `#1B2A4A`; `#111827` is retired, see `BRAND.md` → PART `02_BRAND` PALETTE ARCHITECTURE)*
- Stack: Python + matplotlib, or Node + D3 / Chart.js / Observable Plot. Either is fine — use what you're faster in

**What this buys you:** chart production drops from ~20 minutes of manual formatting to seconds, every chart is automatically on-brand, and adding an animated reveal is a render setting rather than a design task. This converts your biggest bottleneck into your biggest speed advantage.

Build it in week 2, before video 1. It pays back by video 3.

---

### 3. Sources

**Licensing warning:** "public domain archive" does not mean every item in it is public domain. **Check the rights statement on each individual item.** Assume nothing from the platform's name.

#### Data — for charts (this is most of your visual load)

| Source | What | Note |
|---|---|---|
| **Our World in Data** | Charts and datasets on trade, energy, economics, development | **Most content CC BY** — you can use their charts directly with attribution. Biggest single time-saver available to you |
| **FRED** (St. Louis Fed) | US and international macro series | Downloadable, embeddable, extremely reliable |
| **World Bank Open Data** | Global development and economic indicators | Free API |
| **IMF Data** | Macro, trade, reserves, currency | Authoritative for reserve-currency material |
| **UN Comtrade** | Bilateral trade flows | Essential for chokepoint and trade videos |
| **USGS Mineral Commodity Summaries** | Rare earths, tungsten, graphite production by country | **Primary source for your Cluster A rare-earth video** |
| **OEC** (Observatory of Economic Complexity) | Trade visualisations | Good for quick sanity checks |
| **EIA / IEA** | Energy production, prices, flows | Oil shock and energy material |
| **OECD.Stat** | Developed-economy indicators | |
| **UNCTAD** | Shipping, maritime trade, review of maritime transport | **Directly relevant to chokepoints** |
| **CSIS, Brookings, Peterson Institute** | Analysis with sourced figures | Cite the underlying data, not the think tank |

#### Chart and map tools

| Tool | Use |
|---|---|
| **Flourish** | Animated charts, free tier. Best-looking output for video with least effort |
| **Datawrapper** | Publication-quality static charts and choropleth maps, free tier |
| **MapChart.net** | Fast custom country-highlight maps |
| **Natural Earth** | Public-domain vector map data — build your own base maps |
| **Your own pipeline** | See §2. Long-term answer |

#### Archival images and film

| Source | Note |
|---|---|
| **Wikimedia Commons** | Vast. Licence varies per file — check each |
| **Library of Congress** (loc.gov) | Enormous historical photo collection, much of it PD. Check rights statement |
| **US National Archives** (archives.gov) | US government works, generally PD |
| **Internet Archive** (archive.org) | Film, newsreel, books, documents. Licence varies |
| **NYPL Digital Collections** | Strong PD selection, clearly marked |
| **Getty Open Content** | Explicitly free-use subset |
| **Europeana** | European archives, rights clearly labelled |
| **David Rumsey Map Collection** | Historical maps, much CC-licensed |
| **NASA Image Library** | Public domain. Earth, infrastructure from orbit |
| **Flickr Commons** | Institutional PD collections |

#### Stock footage — use sparingly

| Source | Cost |
|---|---|
| Pexels, Pixabay, Coverr, Mixkit, Videvo | Free. Generic — use for texture only, never as the subject |
| Storyblocks, Artgrid, Pond5 | Paid. Only if a specific shot is genuinely required |
| AP Archive, British Pathé | Licensed newsreel. Real cost; watermarked previews free for planning |

**Rule: stock footage is texture, never evidence.** If a shot is carrying an argument, it needs to be a real document, a real chart, or a real archival image.

---

### 4. AI — where it helps and where it will damage you

| Use | Verdict |
|---|---|
| Research synthesis over **your own** documents (NotebookLM) | **Yes.** Core workflow |
| Chart generation from verified data | **Yes** |
| Upscaling / denoising / restoring archival images | **Yes** |
| Abstract, non-representational backgrounds and textures | **Yes** — low risk, reusable |
| Script structuring and tightening | **Yes** — but the pattern and argument must be yours |
| Subtitle drafting, then human correction | **Yes** |
| **AI-generated illustrative images** | **No.** Slop signal under YouTube's July 2026 inauthentic-content policy |
| **AI video recreations of historical events** | **No.** Looks wrong, and fabricating imagery of real events destroys a credibility channel. This is the single worst thing you could do here |
| **AI-generated "archival" photos** | **No.** Actively dishonest |
| AI voiceover | **No** — use your own voice (strategy doc §7) |
| AI supplying facts or figures | **Never** |

#### Why this line matters more for you than for others

Your entire product is trustworthiness. A channel that shows real filings, real charts and real archive photos, and says where each came from, is doing the exact thing AI content farms cannot. **Fabricated visuals would throw away your only moat** — and under the July 2026 policy, they also threaten monetisation.

---

### 5. Prompt library

#### 5a. Research prompts — the ones that actually matter

**Fact extraction with citation discipline**
```
You have access only to the documents I have provided. Extract every
quantitative claim relevant to [TOPIC].

For each, output:
- The figure, exactly as stated
- The unit and the time period
- The document name and page/section
- Whether the document is the original source or is citing someone else

If a figure appears in more than one document with different values, flag
the discrepancy. Do not supply any figure that is not in these documents.
Do not estimate. If something is missing, say "not in provided sources."
```

**Building the historical parallel (the core of your format)**
```
I am building an explainer on [CURRENT SITUATION].

From the documents provided, identify historical episodes with a similar
structure. For each:
- What happened, with dates
- The mechanism that drove it
- How it resolved
- Where the analogy to today BREAKS DOWN

Be harder on the disanalogies than the analogies. I need to know where
the comparison fails, because that's where I'd mislead people.
```

**Pre-script fact-check (run this every time)**
```
Here is my script. For every factual claim, classify:
- SOURCED — I can point to a document
- UNSOURCED — asserted without a source
- INFERRED — my reasoning, not a fact

List every UNSOURCED claim. For each, tell me exactly what document
would settle it. Do not attempt to verify anything yourself.
```

**Chart specification**
```
From this dataset, propose 4 charts for a long-form video.

For each: chart type, exact series, the single point the viewer should take
away, and the one element to highlight in accent colour.

Constraints: readable on a TV at 10 feet; max 5 data series; no dual axes;
no pie charts.
```

**Script tightening for spoken delivery**
```
Rewrite this passage for spoken delivery in this register: friendly, direct,
dry, occasionally sarcastic — with the sarcasm aimed at decisions and
systems, never at people.

Rules: contractions; sentences under 20 words; fragments allowed; one idea
per sentence; no "furthermore", "moreover", "it is important to note".
Keep every number and every attribution exactly as written.
```

#### 5b. Image prompts — only for abstract, non-representational assets

These are safe because they depict nothing real.

**Background texture loop**
```
Abstract dark background texture, deep ink navy (#1B2A4A), subtle aged paper
grain, faint horizontal scanlines, very low contrast, no objects, no text,
no recognisable imagery, seamless, cinematic, understated. 16:9.
```

**Chapter-card backdrop**
```
Minimal abstract composition, ink navy field, thin ochre (#D99A2B) geometric
lines suggesting a grid or graph paper, heavy negative space in the lower
third for text, archival print feel, no objects, no people, no text. 16:9.
```

**Transition texture**
```
Slow-moving abstract ink-in-water motion, monochrome navy, soft edges,
no discernible objects, loopable, subtle, 6 seconds.
```

**Never prompt for:** historical scenes, real people, real places presented as documentary, anything that could be mistaken for archive footage, or fake newspaper front pages.

---

### 6. Per-video asset budget

Plan every video against this. It's the discipline that keeps production at ~3 hours instead of 12.

| Frame type | Count per 20-min video | Sourcing time |
|---|---|---|
| Charts (animated + static) | 6–8 | 30–45 min *with the pipeline built* |
| Maps | 1–2 | 20 min |
| Archival photos | 4–6 | 30 min |
| Document excerpts | 2–4 | 20 min |
| Quote cards | 2–3 | 0 — template |
| Timeline | 1 | 10 min |
| Title / chapter cards | 5–7 | 0 — template |
| Kicker number cards | 2–3 | 0 — template |
| Background loops | 2–3 reused | 0 after first build |
| Archival film clip | 0–2 | 20 min, optional |
| **Total unique assets** | **~20–28** | **~2–2.5 hrs** |

A unique asset per line of dialogue is 150+ items and unbounded hours. That is the difference.

#### Working order

1. **Script locked first.** Never source assets before the script is final
2. Read the script and mark asset cues in the margin
3. Group cues by frame type — all charts together, all archive together
4. Source in batches by type, not in script order
5. Assemble

Batching by type rather than timeline position is what halves the time.

---

### 7. Completed topic backlog — 34 titles

#### Published slate (see content-slate doc for detail)
1. Every Bubble Looks the Same: Railways, Telecom, Dot-Com, AI
2. The World Runs on Seven Chokepoints. Here's What Happens When One Closes.
3. Why Ships Are Going Around Africa Again
4. China Doesn't Need Tariffs. It Has Rare Earths.
5. Taiwan Makes Over 90% of the World's Advanced Chips. Nobody Planned That.
6. Railway Mania Built Real Railways. That's What Makes It Scary.
7. What Actually Happens to an Economy When the Capex Stops
8. How the Dollar Became a Weapon
9. People Have Predicted the Dollar's Death for 50 Years. Here's Why They Keep Being Wrong.
10. Why Tariffs Always Come Back — And Always Disappoint
11. Why Recessions Are Announced After They've Already Ended
12. Why Every Country Wants Its Own Chip Industry — And Most Will Fail

#### Backlog
13. The Box That Beat the Internet: How Shipping Containers Rewired the World
14. Hormuz and the Forty-Year Bluff
15. Why Sanctions Rarely Work — And Never Stop
16. Panama Is Running Out of Water. The Canal Needs Rain.
17. Who Owns the Cables the Internet Runs On
18. Why a Chip Fab Costs More Than an Aircraft Carrier
19. The 1973 Oil Shock Is Still Running Your Economy
20. The Green Revolution Saved India and Broke Its Water
21. Why the Netherlands Is a Logistics Superpower
22. Why Germany's Industrial Model Stopped Working
23. How Export Controls Actually Get Enforced — And Evaded
24. Nobody Can Rebuild a Supply Chain in Five Years. Everyone Promises To.
25. Why Big Projects Always Run Late and Over Budget
26. Why Some Countries Stay Poor Next Door to Rich Ones
27. Who Actually Owns the Sea
28. Why Cities Flood Now When They Didn't Before
29. The Cartel That Sets the Price of Almost Everything
30. Why Every Empire Goes Broke the Same Way
31. How Bretton Woods Was Designed to Fail
32. Why Currency Pegs Always Break, Eventually
33. The Suez Crisis Ended the British Empire in Nine Days
34. Why Industrial Policy Keeps Coming Back After Failing

**Selection rules:** each must pass the two-year test; each must be chart-and-document-sourceable; no video requiring primary research you can't complete in 3 hours.

---

### 8. Week 2 build list

Before video 1, build these once. They are the entire difference between a sustainable channel and another abandoned one.

- [ ] Chart generation pipeline (§2) — **highest priority**
- [ ] Figma/Canva file: title card, chapter card, quote card, kicker number card, comparison table, timeline, source strip, lower third
- [ ] 3 abstract background loops (§5b prompts)
- [ ] Colour and type styles saved as reusable styles
- [ ] Bookmark folder for every source in §3
- [ ] A blank asset-cue sheet to fill per script

Total: one weekend. Then never do it again.


---

# PART — 16_FREE-TOOL-STACK

> Merged from `16_FREE-TOOL-STACK.md` on 2026-09-13. Content unchanged; headings demoted one level. Cross-references to `RUNBOOK.md` → PART `16_FREE-TOOL-STACK` elsewhere still resolve to this part.

**Date:** 2026-09-13
**Researched:** free-tier limits verified against vendor and aggregator sources on this date.

**Warning on every number here:** free-tier limits change constantly and most of these figures come from comparison blogs and vendor pages, not from the products' own docs. **Check the actual signup page before relying on a limit.** Treat everything below as a starting point, not a contract.

---

### 1. The finding that matters most

**Only 2 of your 11 asset types should use generative AI at all.**

Everything else is layout, data visualisation, or real archival material. That isn't a limitation — it's the whole point. Your credibility moat is that a viewer can check your sources, and YouTube's July 2026 inauthentic-content policy penalises exactly the generated-imagery workflow that most "faceless channel" tooling is built around.

So most of the tools you named — Veo, Google Flow, Higgsfield, Grok Imagine — are **the wrong tools for this channel**, not tools you can't afford. Good to know before spending time on them.

| Asset | Generative AI? |
|---|---|
| Logo / avatar concept | ✅ Yes |
| Abstract background textures | ✅ Yes |
| Banner | ❌ Layout job |
| Thumbnails | ❌ Layout job |
| Charts | ❌ Data viz |
| Maps | ❌ Data viz |
| Archival images | ❌ **Real archive only** |
| Document excerpts | ❌ Real documents |
| Title/chapter/quote frames | ❌ Template |
| Subtitles | ❌ Transcription |
| Voice cleanup | ❌ Audio processing |

---

### 2. Logo and avatar

The one place you genuinely want generative AI.

| Tool | Free tier | Verdict |
|---|---|---|
| **Ideogram** | **Commercial use allowed, no watermark.** ~95% accuracy rendering specific words vs 30–50% for competitors | **Superseded.** The text-rendering advantage no longer matters — the mark contains no text and the wordmark is set in vector. See `08` §6.5 for the current verdict: **Bing Image Creator first, Leonardo for volume, never Recraft or OpenArt (watermark / no commercial licence)** |
| **Recraft** | 30 credits/day. **The only mainstream model producing true editable SVG paths** — real curves and nodes, not a traced raster | **Explore only. Free tier watermarks output and prohibits commercial use.** Excellent for testing whether a concept vectorises; you cannot ship from it |
| Gemini / Nano Banana | ~20 images/day free; Nano Banana Pro capped at ~2/day | Fine for concept sketches. Weaker on text |
| Canva free | Not generative for logos, but a solid editor with vector shapes and free fonts | **Where you assemble the final lockup** |

**Recommended path, all free:**

1. **Ideogram** → generate 20–30 owl-mark concepts using the prompt in `BRAND.md` → PART `08_DESIGN-SPEC-FOR-GENAI` §6a. Commercial-cleared, no watermark
2. Pick one direction
3. **Vectorise it** — free options: **Inkscape** (Path → Trace Bitmap), or **SVGcode** (svgco.de, browser-based). Both free, no signup
4. **Clean up and build the lockup in Canva or Affinity** — you already have Affinity
5. Derive the avatar (owl head only) and the 150×150 watermark from the same file

**The honest caveat:** traced vectors are messier than drawn ones — extra nodes, slightly wrong curves. Good enough for YouTube at 98×98. If you later want it clean for merch or a sponsor deck, ₹1,500–3,000 to a designer to redraw it properly.

---

### 3. Banner, thumbnails, frames

**Not a generation problem. A layout problem.** Free tools do this fully.

| Tool | Free tier | Use |
|---|---|---|
| **Canva free** | Unlimited designs, custom dimensions, free fonts incl. Playfair Display and IBM Plex | **Banner (2560×1440), thumbnail template, all frame types.** Set up as reusable templates with locked layers |
| **Figma free** | 3 files, unlimited personal drafts | Better if you want proper component systems and auto-layout. Steeper learning curve |
| **Affinity** | You already have it | Best precision. No template/cloud convenience |

**Recommendation: Canva for the banner and thumbnail template.** Custom dimensions work on free, the fonts you need are there, and the template-duplicate workflow suits 20+ videos. Affinity for anything needing precision.

Do **not** use Canva's AI image generation for thumbnail subjects. Use a real chart, map, or archival image.

---

### 4. Charts and maps — free, and better than AI

| Tool | Free tier | Use |
|---|---|---|
| **Flourish** | Free tier, public projects | **Animated charts.** Best-looking output for least effort |
| **Datawrapper** | Free tier | Publication-quality static charts and choropleth maps |
| **MapChart.net** | Free | Fast country-highlight maps |
| **Natural Earth** | Public domain data | Custom base maps |
| `templates/charts.py` + `templates/animate.py` | Free, already built | On-brand, scriptable, MP4 output |

No generative AI here at all. Real data in, real chart out.

---

### 5. Archival images and documents — never generated

Full list in `RUNBOOK.md` → PART `05_ASSETS-AND-PROMPTS` §3. All free: **Wikimedia Commons · Library of Congress · US National Archives · NYPL Digital Collections · Europeana · Internet Archive · Getty Open Content · David Rumsey Maps · NASA**.

**Check the rights statement on each individual item.** "Public domain archive" doesn't mean every item in it is public domain.

**Free upscaling/restoration for low-res archive scans:** Upscayl (open source, runs locally, no limits) or Real-ESRGAN. This is a legitimate AI use — you're improving a real image, not inventing one.

---

### 6. The one legitimate generative-video use

Abstract, non-representational background textures and transitions. Nothing depicting anything real.

| Tool | Free tier | Notes |
|---|---|---|
| **Google Flow** | ~50 daily credits on Veo 3.1 and Nano Banana Pro. A "Fast" video ≈20 credits, "Quality" ≈100 | Roughly 2 fast generations/day. Enough for abstract loops |
| **Higgsfield** | ~10 credits/day, **watermarked**, flagship models locked | Watermark rules it out for anything on screen |
| **Grok Imagine** | Credit system, ~5 credits/day, refilling at midnight UTC | Thin |
| Banana Flow | ~20 credits/month | Very thin |

**Honest assessment: you need about three abstract background loops, total, reused across every video.** That's one afternoon on Google Flow's free tier and then you never touch it again. Don't build a workflow around AI video — you need almost none of it.

Free generation typically caps at 5–8 seconds at 720p/1080p, which is fine for a loop.

---

### 7. Audio and subtitles — all free

| Need | Tool | Notes |
|---|---|---|
| Record | Audacity, or Resolve Fairlight | Both free, both owned |
| Noise removal | **Resolve Fairlight → Voice Isolation** | First choice |
| Heavier cleanup | Adobe Podcast Enhance free tier | Genuinely good |
| Transcription / subtitles | **Whisper**, run locally | Free, unlimited, no upload. You're a dev — run it yourself |
| Music / SFX | YouTube Audio Library | Free, monetisation-cleared |

**No AI voice.** Use your own — `STRATEGY.md` → PART `00_CONTEXT`.

---

### 8. The complete free stack

| # | Asset | Tool | Cost |
|---|---|---|---|
| 1 | Logo concepts | Ideogram | Free, commercial-cleared |
| 2 | Vectorise | Inkscape or SVGcode | Free |
| 3 | Logo lockup, avatar, watermark | Canva or Affinity | Free / owned |
| 4 | Banner 2560×1440 | Canva | Free |
| 5 | Thumbnail template | Canva or Affinity | Free |
| 6 | Frame templates | Canva, or `templates/` | Free |
| 7 | Static charts, maps | Datawrapper, MapChart | Free |
| 8 | Animated charts | Flourish, or `templates/animate.py` | Free |
| 9 | Archival images | The nine archives | Free |
| 10 | Upscale old scans | Upscayl | Free, local |
| 11 | Abstract loops (×3, once) | Google Flow | Free tier |
| 12 | Record + edit + colour | DaVinci Resolve | Owned |
| 13 | Audio cleanup | Fairlight, Adobe Podcast | Free |
| 14 | Subtitles | Whisper, local | Free |
| 15 | Music | YouTube Audio Library | Free |
| 16 | Keyword research | vidIQ free, Google Trends | Free |
| 17 | Research synthesis | NotebookLM | Free |

**Total: ₹0.** The only spends remain thinklate.com (~₹1,500/yr) and optionally a designer for clean logo vectors.

---

### 9. Traps

- **Recraft free tier prohibits commercial use and watermarks output.** It's the best SVG generator and you still can't ship from its free tier. Explore only
- **Higgsfield free tier watermarks everything.** Unusable for on-screen assets
- **Canva's AI image generation** — don't use it for thumbnail subjects. Real chart or real archive
- **Nano Banana Pro at ~2 images/day free** will feel unusable fast. Use Ideogram instead
- **Free video tiers cap at 5–8 seconds.** Fine for loops, useless for anything else — which is fine, because you need almost no generated video
- **Don't chase free-tier credits.** If a workflow needs daily credit farming across three tools, it's the wrong workflow. Your bottleneck is hours, not rupees

---

### Sources

[rangy.ai — Ideogram vs Recraft for logos](https://rangy.ai/blog/ideogram-vs-recraft-for-logos/) · [rangy.ai — best AI logo generators 2026](https://rangy.ai/blog/best-ai-logo-generator-2026/) · [Recraft AI vector generator](https://www.recraft.ai/ai-vector-generator) · [vectosolve — AI SVG generators tested](https://vectosolve.com/blog/best-ai-svg-generators-text-to-vector-2026) · [costgoat — Google Flow pricing](https://costgoat.com/pricing/google-flow) · [whiskailabs — Google Flow pricing](https://whiskailabs.net/google-flow-ai-pricing/) · [creetr — Higgsfield free tier](https://creetr.com/blog/is-higgsfield-ai-free) · [costbench — Higgsfield free plan](https://costbench.com/software/ai-video-generators/higgsfield/free-plan/) · [ximagineai — Grok Imagine limits](https://ximagineai.com/grok-imagine-limit-faq) · [datastudios — Gemini free tier 2026](https://www.datastudios.org/post/google-gemini-free-in-march-2026-plans-complete-feature-set-limits-workflows-availability-and) · [evolink — free AI video generators, verified plans](https://evolink.ai/blog/free-ai-video-generator-2026-what-is-actually-free) · [nanobanana pricing](https://nanobanana.im/pricing)
