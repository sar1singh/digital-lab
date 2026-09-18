# ThinkLate — Per-Video Runbook

**Date:** 2026-09-13
**Purpose:** the step-by-step for making one video. Every other doc is reference; this is the sequence. An AI agent or you can start here and work through it.

---

## Before any of this

Read `00_CONTEXT.md`. If you're scripting, also read `10_MACRO-TO-MICRO.md` §3 and §5, and `03_CONTENT-AND-VOICE.md` Part 3.

---

## Step 0 — Pick the tier

| Hours available this fortnight | Tier | Length |
|---|---|---|
| 4–5 | **Floor** — "One Chart" | 6–8 min |
| 10–12 | **Standard** | 14–18 min |
| 15–20 | **Pillar** | 25–30 min |

Pick honestly, based on the fortnight you actually have. **Shipping a Floor video beats skipping a Standard one.**

---

## Step 1 — Title and thumbnail text FIRST (30 min)

Before any research. If you can't write a good title, the idea isn't sharp yet.

- Title: **30–50 characters**, searchable noun front-loaded, question or claim
- Thumbnail text: **2–3 words**, different from the title
- Target search phrase: write it down
- **Validate** in Google Trends and the vidIQ free tier — ten minutes

Reference: `04_TITLES-AND-THUMBNAILS.md` §5, `12_CRAFT-EVIDENCE.md` §1.

**Gate:** would you click this in your own feed with no channel name attached? If not, rewrite before continuing.

---

## Step 2 — The chain, before the research (30 min)

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

Reference: `10_MACRO-TO-MICRO.md` §5.

---

## Step 3 — Research (Floor 1–2 hrs · Standard 2–3 · Pillar 4–6)

**Research the cluster, not the video.** If this is the first video of a cluster, budget the full session and come out with outlines for 3–4 videos.

1. Gather primary documents — USGS, IMF, World Bank, FRED, UN Comtrade, UNCTAD, EIA, Our World in Data, central banks
2. Feed them to NotebookLM. Use the fact-extraction prompt in `05_ASSETS-AND-PROMPTS.md` §5a

   **NotebookLM discipline — added 2026-09-13.** It is source-grounded and attaches inline citations that jump to the exact passage, which is what makes it compatible with hard rule 1. **But its summary is not "a source you opened" — the cited passage is.** So: use it to *locate*, then **click every citation and read the original sentence** before that fact enters a script. A figure that only ever existed in NotebookLM's prose is an unsourced figure.

   **Two failure modes worth naming:**
   - **Never script from a report.** Its register is uniform and explanatory — script from it and the video sounds exactly like the AI-template content this channel is positioned against. Extract facts; write the prose yourself
   - **Don't paste source text into narration.** Summarise and paraphrase (`§5` of the project rules). The Sources block credits it; the script doesn't quote it at length

   Quotas and feature names change often and the figures circulating are third-party blog claims, not Google documentation — **check in-product rather than trusting any number written down here.**
3. Fill in every source for links 1 and 2. Downgrade any link you can't source
4. Run the historical-parallel prompt. **Note where the analogy breaks** — that goes in the script

**Hard rule:** never accept a figure you haven't seen in a document you opened.

---

## Step 4 — Script (Floor 1 hr · Standard 1.5–2 · Pillar 3)

Boomerang structure (`10_MACRO-TO-MICRO.md` §3):

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

1. Run the pre-script fact-check prompt (`05_ASSETS-AND-PROMPTS.md` §5a). Fix every UNSOURCED claim
2. **Vary sentence length deliberately** — long, then short. Variance retains ~1.8× better than uniform short sentences
3. Read aloud. Cut every clause you stumble on
4. Delete "furthermore", "moreover", "it is important to note"
5. Check: does the opening deliver the title's promise within 30 seconds?

---

## Step 5 — Mark asset cues (20 min)

Read the script and mark in the margin. **Target 20–28 unique assets for a 16-minute video, not 150.**

Then **group by type** — all charts together, all archive together. Batching by type rather than script order halves the sourcing time.

Reference: `05_ASSETS-AND-PROMPTS.md` §1 and §6.

---

## Step 6 — Build assets (Floor 1 hr · Standard 2–2.5 · Pillar 3–4)

In this order:

1. **Charts** — from verified data only. Source line baked in
2. **Maps** — Datawrapper or MapChart
3. **Archival images** — Wikimedia, Library of Congress, National Archives, NYPL, Europeana. **Check the rights statement on each individual item**
4. **Document excerpts** — crop tight, attribute on screen
5. **Template frames** — title, chapter, quote, kicker, timeline, table. Text swaps only

**Surface alternation** (`06_MOTION-AND-SURFACE.md`): paper for title / quotes / archive / timeline · ink for charts / data / kickers.

---

## Step 7 — Record (30–60 min)

- Soft-furnished room, duvet or curtain behind you, never bare walls or glass
- Fifine ~15 cm, slightly off-axis
- Record in sections, not one take
- **Batch two or three videos' audio in one sitting** when you can

---

## Step 8 — Edit (Floor 1–1.5 hrs · Standard 2–3 · Pillar 3–4)

1. Voice track first, then assemble visuals to it
2. **Three-layer composition** — background texture/archive dimmed 60–75%, content, then text
3. Slow push or pan on every archival still, 1–3% scale
4. Animated charts draw over 4–6s, then **hold 30–60s**
5. Fairlight → Voice Isolation on the voice track
6. Film grain as one adjustment layer over the whole timeline
7. **No intro animation for the first 10 videos**
8. End card with both YouTube end-screen zones reserved

---

## Step 9 — Package and publish (1 hr)

- Thumbnail: 1280×720, under 2 MB, 2–3 words, **high contrast mandatory**, one amber element
- **Feed test:** place it beside three competitors at feed size. Does yours read fastest?
- **TV test:** view at ten feet
- Description: summary with the search phrase, chapters, **Sources block**, newsletter link, socials
- Subtitles: accurate, corrected. Never ship auto-generated
- Add to the relevant playlist
- Tags: two minutes, then move on — they barely matter
- Set the next video's end-screen link

---

## Step 10 — After publishing

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

**Which improvement is already decided** — don't pick it while demoralised. `09_COUNTER-STRATEGY.md` §12 names one for every video from 1 to 30, sequenced hook → retention → packaging → cost, with motion deliberately late. Do the named item **even if the last video got zero views**; the ladder is independent of performance, which is the point.

---

## Step 11 — Log it

Append to `LOG.md`:

```
## Video NN — [title]
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

**Log the hours honestly.** The cost ratchet in `09_COUNTER-STRATEGY.md` §7 only works if you can see whether cost is actually falling. If video 7 costs the same as video 3, fix the pipeline before making another video.

---

## Total time budget

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

## Stop-and-check gates

Any of these means stop and fix before continuing:

- Can't write a title you'd click → the idea isn't ready
- Chain needs more than five links → connection too weak
- A figure you can't source → cut it or downgrade its label
- A psychological claim doing load-bearing work → re-anchor in financial or career
- The script tells the viewer what to *do* → that's advice; cut it
- Title contains a product name or version number → you're making an instance, not an invariant
- Over 30 unique assets → the script is over-illustrated
