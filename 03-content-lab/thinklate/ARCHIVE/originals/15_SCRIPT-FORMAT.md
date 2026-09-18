# ThinkLate — Verbatim-Read Script Format

**Date:** 2026-09-13
**Gap this closes:** the other docs specify voice and structure but not the *formatting* a script needs to be read aloud cleanly in one pass. You're reading verbatim, so the script is a performance document, not prose.

**Where it sits:** output of Step 4 in `13_RUNBOOK.md`, input to Step 7 (record).

---

## 1. Why a special format

A script written to be *read* fails when *spoken*. Four specific failures:

1. **Numerals stall you.** "$1.2bn" makes you compute mid-sentence. Written as "one point two billion dollars," you just read it.
2. **No breath marks means you run out of air** mid-clause and re-take.
3. **Unfamiliar names cause stumbles** you only discover on the recording.
4. **No take boundaries means one flub costs you the whole section.**

All four are avoidable with notation. The format below adds maybe 10 minutes to scripting and removes most re-takes.

---

## 2. Notation

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

## 2b. Citations inside the script — added 2026-09-13

**The gap this closes:** `14_SCENE-SHEET.md` has a `SOURCE` column and every video needs a Sources block in its description, but nothing tied a *spoken claim* to a *source*. So a claim could drift between draft and publish with nobody able to check it. This is that link.

### How it works — three files, one ID

1. **`sources.md`** in the video folder. Every source gets a permanent ID: `R1`, `R2`, `R3`…
2. **The script** tags each factual claim inline with `⟨src: R1⟩`. It is a `⟨note⟩`, so it is **never spoken**
3. **The scene sheet's `SOURCE` column** carries the same ID, so the on-screen citation and the spoken claim cannot disagree

### `sources.md` format

```
## R1
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

### The three gates

- **Every number in the script carries a `⟨src:⟩` tag, or it is cut.** No exceptions, no "obviously true"
- **A claim whose only support is an AI summary is unsourced.** NotebookLM locates the passage; the passage is the source (`13_RUNBOOK.md` step 3)
- **Before publishing:** every ID used in the script appears in `sources.md`, and every entry in `sources.md` appears in the description's Sources block. Mismatch either way is a bug

### Example

```
Britain ke do railway manias mein // capital investment tha //
**pandrah se bees percent** // GDP ka. ⟨src: R2⟩ ///
```

Worked example: `videos/01_is-ai-a-bubble-ask-the-railways/sources.md`.

---

## 3. Worked example

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

**Note the sentence-length variance** — long, then "Twice." then long, then "So. Railways." That's the 1.8× retention finding from `12_CRAFT-EVIDENCE.md` applied, and it's also where the deadpan lives.

---

## 4. Structural requirements

Every script must have:

- **A value claim by `[TAKE 2]`** — what the viewer will be able to see or do by the end. Not just an intriguing observation
- **Take boundaries every 30–60 seconds.** Shorter near the opening where precision matters most
- **`{S}` markers** matching the scene sheet, so you know when the visual shifts and can pace to it
- **One idea per line, lines short enough to say in one breath.** If you can't, break it
- **Chain labels spoken, not just shown.** When you reach an inferred link, say so: *"and here I'm inferring // this next part isn't documented"*
- **No numeral anywhere.** Search the script for digits before recording. Any hit is a bug

---

## 5. Pre-record checklist

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

## 6. Paste-ready prompt — produce a script in this format

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

## 7. Recording from this format

- Record **take by take**, not in one pass. A flub costs you 40 seconds, not 16 minutes
- Say the `[TAKE n]` number aloud before each chunk — it makes the editor's job trivial
- Leave 2 seconds of silence at the start and end of every take
- `////` breaks are where you stop, drink water, and reset
- Where a `⟨note⟩` says the chart animates, **read slower**. Your instinct will be to rush; the visual needs the air
- Record room tone for 30 seconds at the end — Fairlight uses it for noise reduction

---

## 8. Filing

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
