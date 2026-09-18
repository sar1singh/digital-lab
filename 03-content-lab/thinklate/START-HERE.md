# START HERE — how to use this folder with any AI

**Created 2026-09-13.** For working outside Cowork: ChatGPT, Gemini, Claude web, NotebookLM, a local CLI agent — anything.

**Two ways in.** The `thinklate` skill if you're in Claude (it loads automatically). Otherwise paste the prompt in §3.

---

## 0. Starting a new session — paste one of these

### In Claude, where the `thinklate` skill loads automatically

```
ThinkLate work. My operating folder is attached.

Read CLAUDE.md, then START-HERE.md §0b and §0c. That's ~20k tokens and
enough to start almost anything. Then pull RUNBOOK.md / CRAFT.md /
BRAND.md / STRATEGY.md as the task needs.

§0c lists what is still stale even after the merge — trust it over any
section you read. Never read ARCHIVE/.

Today: [make video 1 / script video N / build the template set /
        review what I'm getting wrong]

Before you do anything, tell me in under 150 words:
  1. What in my folder is stale or self-contradictory
  2. What I'm about to get wrong, and which rule or evidence says so
Then stop and wait.
```

### In any other AI — ChatGPT, Gemini, a local agent

Attach `CONTEXT-PACK.md`, `CLAUDE.md`, `START-HERE.md`, plus the task's files. Then paste the same block above, and for scripting use the full prompt in §3.

### ⚠️ Order of work — settled 2026-09-13

**Video before templates.** Not the other way round.

- `RUNBOOK.md` → PART `05_ASSETS-AND-PROMPTS` §8 says build the template set in "week 2", before video 1. **That is superseded.** Craft ladder #1 (`09` §12) is "ship it, nothing else"
- **Templates built before a video are built against guesses.** Video 1 revealed the real ratio — five quote cards and one kicker, which nobody would have predicted
- **The template system already exists**: `templates/frames.py` renders 10 frame types from `brand.py` tokens. It does not need to be created, and it does not need AI. Video 1's twelve frames came out of it in one command:

```
cd templates
python3 -c "
import sys; sys.path.insert(0,'.')
from frames import title_card, kicker, quote_card, lower_third, end_card
title_card('Is AI a Bubble?','Ask the Railways', out='../videos/01_x/assets/S04_title.svg')
"
```

**So: make the video, then build the template set from what the video actually used.** Deferred branding items 6 and 8 (three expressions, thumbnail template) belong to that same later pass.

---

## 0b. The folder, after consolidation — 2026-09-13

**35 root docs became 8.** Nothing was deleted: every original sits in `ARCHIVE/originals/`, and each merged file records which file each PART came from.

| Live file | What it holds | Read it when |
|---|---|---|
| **`CLAUDE.md`** | The 13 hard rules, exclusions, fixed decisions, closed topics | **Every session. Binding** |
| **`CONTEXT-PACK.md`** | One screen. Paste into any AI to ground it | Cold start anywhere |
| **`START-HERE.md`** | This file — how to use the folder, **the 30 titles and roadmap**, the channel spec | **Second, every session** |
| **`RUNBOOK.md`** | Making one video: step 0→11, script format and citations, scene sheet, assets, tools | **Every video** |
| **`CRAFT.md`** | Positioning, researched retention/title/thumbnail evidence, the voice guide, motion | **Before scripting or designing** |
| **`BRAND.md`** | Palette, type, channel setup, frame specs, design prompts | Channel or asset work |
| **`STRATEGY.md`** | Locked context, the flat period, the craft ladder, niche and language decisions | Planning, or when views stay flat |
| **`BUSINESS.md`** | Vision, the venture, entity and tax path, portfolio gates, AI stack rules | Quarterly, or before spending money |
| `LOG.md` · `discovery.md` | Working logs — one entry per published video, and frictions as they happen | After publishing |
| `ARCHIVE/` | Every original file, plus superseded material | Only to check history |

**Canonical outside root:** `brand/ART-DIRECTION.md` (character prompts) · `brand/QC.md` (asset rubric) · `brand/EXPORT/` (the only folder you upload from) · `templates/` (working renderers) · `videos/`.

**Reading budget:** `CLAUDE.md` + `CONTEXT-PACK.md` + `START-HERE.md` is roughly 20k tokens and enough to start almost anything. Add `RUNBOOK.md` and `CRAFT.md` for a video. **Never read `ARCHIVE/`** unless checking why a decision was made.

**Cross-references** inside merged files read like `` `CRAFT.md` → PART `12_CRAFT-EVIDENCE` §2 `` — the file, then the part, then the section.

---

## 0c. What is still stale, even after the merge

Merging moved the files; it did not resolve every contradiction. **Trust these warnings over any section you read:**

| Live location | Stale content inside it |
|---|---|
| `START-HERE.md` → PART `THE 30 TITLES` | ✅ **This is the single title list.** Any other list you find is history |
| `CRAFT.md` → PART `04_TITLES-AND-THUMBNAILS` | §2's 12-title slate is **dead**. §5 rules and §5b search data are live. **§1's search-led strategy is contradicted by §5b's own measurements** |
| `RUNBOOK.md` → PART `05_ASSETS-AND-PROMPTS` | §7's 34-title backlog is **dead as titles**, valid as topics. §8's "build templates in week 2" is **superseded** — video first |
| `BRAND.md` → PART `02_BRAND` | §5's channel description is **superseded** by `brand/EXPORT/CHANNEL-SETUP-PASTESHEET.md` §A3 |
| `CRAFT.md` → PART `03_CONTENT-AND-VOICE` | Its slate and script structure are **superseded**. **Part 3's voice guide is live and matters** |
| `BRAND.md` → PART `08_DESIGN-SPEC-FOR-GENAI` | **§6 superseded** by `brand/ART-DIRECTION.md` |
| `STRATEGY.md` → PARTS `19`, `22`, `23` | Carry the audience thesis that is **PARKED** — see §5 below |
| `ARCHIVE/originals/99_RESEARCH_niche-screen.md` | **Superseded on conclusions.** Policy and regulatory evidence still holds |
| `brand/PROMPTS.md` · `brand/BRIEF.md` | **Do not use.** The record of eight rejected rounds |

**If two sections disagree, the more recently dated one wins — and say so rather than picking silently.**

---

## 1. Directories

- **`brand/`** — art direction, QC rubric, the Gemini originals in `source-renders/`, and **`EXPORT/`, the only folder you upload from**
- **`templates/`** — working Python. `frames.py` renders 10 frame types, `charts.py` 4 chart types, `animate.py` animated charts. All colour and type come from `brand.py`
- **`videos/`** — one folder per video

---

## 2. The four rules that matter most

Break these and the channel's one advantage — being checkable — is gone.

1. **Never state a figure that isn't in a source you actually opened.** A search-result summary isn't an opened source. A NotebookLM summary isn't either — the cited passage is
2. **Label every causal link** DOCUMENTED / LIKELY / PLAUSIBLE / SPECULATIVE. The label is the product
3. **A pattern to notice, never an action to take.** Advice is out of scope
4. **Never end on a prediction.** End on a better question

---

## 3. Paste-ready prompt — start scripting

Attach or paste `CONTEXT-PACK.md`, `CLAUDE.md`, `RUNBOOK.md` → PART `15_SCRIPT-FORMAT`, and the video's `CHAIN.md` + `RESEARCH.md` if they exist. Then:

```
You are my collaborator and critic on ThinkLate, my YouTube channel. Not a
cheerleader — if something is wrong, say so and name which rule it breaks.

FIRST, before writing anything, read the attached files and tell me in under
150 words:
  1. Which of my hard rules this video is most likely to break
  2. Which claim in my chain is load-bearing and least supported
  3. Anything already stale or self-contradictory in what I gave you

Then STOP and wait for me to respond. Do not write the script yet.

HOUSE STYLE FOR ALL YOUR REPLIES
- Bulleted key highlights only. Short. I don't read long explanations
- No preamble, no recap. Give me the next action or the artefact
- Flag uncertainty explicitly. Say what you did not verify
- Push back. Don't validate everything. I get stuck in planning loops, so
  bias every answer toward the next concrete action

THE VIDEO
Title:        [paste]
Tier:         [Floor 6-8 min / Standard 14-18 / Pillar 25-30]
Micro anchor: [what in the viewer's working life this lands on]
Chain:        [paste the 5 labelled links]
Sourced facts: [paste ONLY verified material — this is the only factual
               content you may use. Invent nothing]

HARD RULES — these are gates, not preferences
- Never state a figure not present in the sourced facts above. No estimates
  as facts. If something is needed but missing, write [VERIFY] or cut it
- Label every chain link DOCUMENTED / LIKELY / PLAUSIBLE / SPECULATIVE, and
  say the label out loud in the narration where a link is inferred:
  "yahan main infer kar raha hoon, yeh documented nahi hai"
- Anchor the chain in the financial or career domain. Psychological effects
  may sit on top, marked as inference, never load-bearing
- Cover the invariant, not the instance. No product names or version numbers
- A pattern to notice, never an action to take. No advice
- Never end on a prediction. End on a better question
- On-screen text complements narration, never duplicates it
- Start directly. No intro, no "before we begin", no fluff
- Never write a spoken like/subscribe call-out. If a prompt is wanted it's a
  visual pop-up over continuing narration

LANGUAGE
Hinglish narration in Roman script — I read it aloud. Technical and economic
terms stay English, because that's how my audience actually speaks. Packaging
(title, thumbnail, on-screen text) is English.

VOICE
Friendly, direct, dry, sarcastic, deadpan, with hard facts underneath.
Sarcasm aimed at decisions and systems, NEVER at people. Understatement over
emphasis — the facts carry the joke. Never corporate, never a hype reel,
never "they don't want you to know".

STRUCTURE — boomerang
  1. Micro hook, something I've personally noticed (0:00-0:40)
  2. Value claim by second 15 — what I'll be able to SEE by the end
  3. The gap — you've felt this, nobody told you why
  4. Zoom out — the documented history and mechanism
  5. The pattern — what repeats, and why
  6. Zoom back in — the chain, link by link, labelled
  7. The skill — what to watch for next time. A pattern, never an action
  8. Close — reframe the opening as a better question

FORMAT — mandatory, this is a performance document
  //  short pause     ///  full beat     ////  section break
  **word** stress     [TAKE n] every 30-60s     (pron: xxx) first use
  {Sn} scene marker   ⟨note⟩ never read aloud   ⟨src: R1⟩ citation

  - NO NUMERALS ANYWHERE. "pandrah se bees percent", never "15-20%".
    Any digit in a spoken line is a bug
  - One idea per line, each sayable in one breath
  - VARY SENTENCE LENGTH DELIBERATELY. Long, then three words. Uniform short
    sentences flatten retention
  - Every number carries a ⟨src:⟩ tag or gets cut
  - Target 140-155 words per minute of runtime

WHEN YOU'RE DONE, tell me honestly:
  - Measured word count and therefore real runtime
  - Which line is weakest and why
  - Which claim you were least comfortable with
  - Anything you had to invent (there should be nothing)
```

**The `FIRST … then STOP` block is the important part.** Any AI will happily write a confident script on unverified facts. Forcing it to criticise the brief first is what catches the problem while it's still cheap.

---

## 4. After the script

1. **Scene sheet** — paste the script plus the prompt in `RUNBOOK.md` → PART `14_SCENE-SHEET` §3
2. **Per-scene visuals** — §4. **Not AI-generated.** Four sources only: your own `templates/frames.py`, charts from verified data, real archive with per-item rights checked, and abstract non-representational loops
3. **Sources file** — `sources.md` per `RUNBOOK.md` → PART `15_SCRIPT-FORMAT` §2b. Record `Opened:` and `Read:` for each. *"Read: abstract only"* is honest and belongs in there
4. **Record** — take by take, say the take number aloud, room tone at the end
5. **Edit** — voice track first, always
6. **Log** — `LOG.md`, and **log the hours honestly** or the cost ratchet is invisible

---

## 5. What's deliberately NOT settled

Raise these; don't let an AI paper over them.

- **AUDIENCE, parked.** Three docs aim the channel at independent knowledge workers because an eventual product would serve them. The venture moved to product-first then an ad agency / digital company, which sells to businesses. **Settle before finalising video 2's title.** README open question 0
- **Search demand is weak** for Phases 2, 3 and 5 — measured, in `04` §5b. Those are browse plays, not search plays
- **Deferred:** watermark, three expressions, thumbnail template, business email, newsletter. Not cancelled
- **Only video 1's topic is search-validated.** Don't treat the other 29 as proven

---

## 6. Closed topics — an AI proposing these is wrong, not creative

The art style · the owl · the mark type · Hinglish narration with English packaging · the palette, unified on `#1B2A4A` · the faceless format until video 24.

Eight rounds of branding were rejected before the current one was locked. **Point any proposal at `brand/ART-DIRECTION.md` §8 rule 7 and move on.**


---

# PART — THE 30 TITLES & ROADMAP

> Merged from `ROADMAP-AND-TITLES.md` on 2026-09-13. **This is the single title list.**

**The single title list. Created 2026-09-13.**

This is an **index that consolidates existing docs, not a new strategy doc** (`CLAUDE.md`: no new strategy docs until video 3). It exists because there were **four conflicting title lists** in this folder and no way to tell which was live.

**For titles, this file now supersedes:** `CRAFT.md` → PART `04_TITLES-AND-THUMBNAILS` §2 · `RUNBOOK.md` → PART `05_ASSETS-AND-PROMPTS` §7 · `CRAFT.md` → PART `03_CONTENT-AND-VOICE`'s slate. Those keep their *rules* — `04` §5 title-writing rules, `04` §3 thumbnail layout, `04` §5b search validation — but their *lists* are stale and marked as such.

---

### The four lists that conflicted, and what happened to each

| Source | What it was | Status |
|---|---|---|
| README publish order | 10 titles, work/money/jobs framing, revised per `22` | ✅ **This is the live order.** Reproduced below |
| `04` §2 | 12 titles with char counts, thumbnail text and search phrases — but the **old geopolitics slate** | ❌ Stale for videos 1–10. Four rows survive; the rest move to 15+ |
| `05` §7 | 34-title backlog, written **before the 60-char rule** and heavily geopolitics | ⚠️ Titles stale, **topics still valid.** Kept below as topics, not as titles |
| `03` | Original slate | ❌ Already marked superseded |

---

### ⚠️ Two open items that gate this list

1. **AUDIENCE — parked** (README open question 0). The venture moved to product-first then an ad agency / digital company, which sells to businesses. Three docs still aim the channel at independent knowledge workers. **Videos 2+ should not be finalised until this is settled.** Video 1 is unaffected.
2. **SEARCH DEMAND — measured, and weak** (`04` §5b). On Google Trends India / YouTube Search, "ai job loss" and "tech layoffs" are below reporting threshold; "future of work" ≈ 11 against "ai bubble" = 100. **Most of videos 2–5 and 10 target phrases nobody searches on YouTube in India.** Either the topics change or the distribution assumption does.

**Do not read the order below as validated.** Only video 1 is.

---

### ✅ THE 30 — six phases, rebuilt 2026-09-13

**Replaces the 10-video order and the 34-title backlog below.** Every title measured: **all 30 fall inside 30–50 chars.** Every title is an **invariant** — no product name, no version number, no figure that needs re-checking next year.

#### Why phases, not a weekly schedule

**A phase is a research cluster, not a calendar block.** Runbook step 3 says research the cluster, not the video — so five videos sharing one evidence base cost far less than five unrelated ones. That is the whole mechanism behind "quick succession":

1. **Research the phase once** — one deep session, 5 outlines out
2. **Script all five** back to back, same sources open
3. **Record all five** in one or two sittings (runbook step 7 already says batch)
4. **Edit and publish** in sequence, as fast as editing allows

Per-video cost should fall inside a phase and fall again across phases. **That is the cost ratchet in `STRATEGY.md` → PART `09_COUNTER-STRATEGY` §7, and it is the number to watch — not views.** Log hours honestly per `LOG.md` or the ratchet is invisible.

**No cadence promise.** Publish when ready. The fortnightly target stays internal.

#### The staleness test every title had to pass

Your own rule (`STRATEGY.md` → PART `11_TECH-AS-SUBSTRATE`): **cover the invariant, use the current technology as the example, never the subject.**

| Invariant — survives years | Instance — dead in months |
|---|---|
| Why infrastructure booms always overbuild | This quarter's data-centre numbers |
| Why compute concentrates in a few hands | The latest chip |
| Why a system rejects you with no reason | One company's new algorithm |

**AI appears in exactly one title, and only as the example** (#1). If AI stops being the live buildout, #1 dates and the other 29 don't.

---

#### Phase 1 — Bubbles & capital cycles

*Pillar 1. Shared evidence: railway mania, telecom fibre, dot-com, capex series. Video 1 is already specced in `videos/01_.../CHAIN.md`.*

| # | Title | Chars | Lands on |
|---|---|---|---|
| 1 | Is AI a Bubble? Ask the Railways | 32 | your job security |
| 2 | The Bubble That Built Real Railways | 35 | real assets, wiped-out investors |
| 3 | What Happens When the Capex Stops | 33 | who gets cut first |
| 4 | Why Infrastructure Booms Always Overbuild | 41 | the pattern itself |
| 5 | Who Actually Pays for an Investment Boom | 40 | who carries the bill |

#### Phase 2 — The invention of the job

*Pillar 1. Shared evidence: labour history, wage and productivity series, the history of employment statistics.*

| # | Title | Chars | Lands on |
|---|---|---|---|
| 6 | Why the Job Was Invented at All | 31 | the default path isn't permanent |
| 7 | Who Decided the Length of Your Week | 35 | your hours were set by someone |
| 8 | Why Your Pay Stopped Tracking Output | 36 | wage vs productivity |
| 9 | Who Captures the Value You Create | 33 | where the surplus goes |
| 10 | How the Salary Replaced the Trade | 33 | what was traded away |

#### Phase 3 — Decided by machines

*Pillar 4. Shared evidence: credit scoring history, algorithmic decision systems, pricing. **Pure education, zero recommendation** — the line your own hard rule 5 draws.*

| # | Title | Chars | Lands on |
|---|---|---|---|
| 11 | Who Actually Decides Your Credit Score | 38 | systems deciding your options |
| 12 | Why a System Rejects You With No Reason | 39 | opacity as a design choice |
| 13 | How Prices Learned to Watch You | 31 | what you pay vs what others pay |
| 14 | Why Nobody Can Explain the Decision | 35 | accountability gap |
| 15 | Who Answers When Software Decides | 33 | who you appeal to |

#### Phase 4 — Independent work

*Pillar 1. **The one phase with measured search demand** — "freelancing" ≈ 725 against "ai bubble" = 100 (`04` §5b). Mechanism and history only; "how to freelance" is advice and stays out of scope.*

| # | Title | Chars | Lands on |
|---|---|---|---|
| 16 | How the Freelance Economy Got Built | 35 | who designed the arrangement |
| 17 | Why Independent Work Pays Unevenly | 34 | the rate you can charge |
| 18 | Who Sets the Rate for Global Work | 33 | arbitrage, and its ceiling |
| 19 | Why the Middleman Never Disappears | 34 | platforms take a cut, always |
| 20 | What Changes When Clients Are Abroad | 36 | currency, payment, leverage |

#### Phase 5 — How downturns reach you

*Pillar 1. Shared evidence: recession dating methodology, hiring and layoff sequencing.*

| # | Title | Chars | Lands on |
|---|---|---|---|
| 21 | Recessions Are Declared Too Late | 32 | you find out last |
| 22 | Why the Worker Always Finds Out Last | 36 | the information order |
| 23 | Who Gets Cut First, and Why It Repeats | 38 | the sequence is predictable |
| 24 | Why Hiring Freezes Before Firing | 32 | the first signal to watch |
| 25 | How a Slowdown Reaches Your Team | 32 | the transmission path |

#### Phase 6 — Power & chokepoints

*Pillars 2 and 3. **Deliberately last.** These attract geopolitics viewers rather than the people the channel serves — fine once an audience exists, wrong as a first impression. Mostly specced already in `04` §2.*

| # | Title | Chars | Note |
|---|---|---|---|
| 26 | Why Trade Runs Through a Few Straits | 36 | **retitled** — was "The 7 Chokepoints That Run the World". A number in the title reads as a listicle, and listicles are out of scope |
| 27 | How One Island Got Most of the World's Chips | 44 | **retitled** — was "How Taiwan Got 90% of the World's Chips". **A title asserting 90% needs a source opened** (hard rule 1), and the share moves. "Most" is durable and needs no footnote |
| 28 | China's Real Weapon Isn't Tariffs | 33 | |
| 29 | How the Dollar Became a Weapon | 30 | |
| 30 | Why Chip Factories Keep Failing | 31 | |

---

#### What each phase teaches you — the skill ratchet

**Per-video detail: `STRATEGY.md` → PART `09_COUNTER-STRATEGY` §12** — the craft ladder names one concrete improvement for each of the 30, plus the diagnosis table for the zero-views case. The table below is the phase-level summary of it.

The channel is also the apprenticeship. One operational skill per phase, and it compounds:

| Phase | The skill you're actually buying |
|---|---|
| 1 | **The whole pipeline once.** Research → script → record → edit → publish. Everything after this is repetition with less friction |
| 2 | **Batching.** First phase where you research a cluster once and get five scripts out. This is where cost per video should visibly drop |
| 3 | **Retention editing.** Abstract, systems-heavy material that lives or dies on pacing. Hardest to hold an audience through — which is why it's worth learning on |
| 4 | **Demand meeting supply.** The only phase with measured search demand, so the first honest read on whether titles and thumbnails work when the audience actually exists |
| 5 | **Speed.** Five short structural videos. Target: under the Floor budget each |
| 6 | **Scale economics.** By here you either have a repeatable unit cost or you have a hobby. `09` §7 decides which |

**Decision point at video 12** (`STRATEGY.md` → PART `09_COUNTER-STRATEGY`) — roughly end of Phase 3. Don't reassess before it.

---

#### Honest read on this list

- **Only video 1 is search-validated.** Phases 2, 3 and 5 target phrases with little measured YouTube demand in India. They are **browse and suggested plays**, which means curiosity titles and thumbnails carry them, not search. That contradicts `04` §1's search-led strategy — the contradiction is real and documented in `04` §5b
- **Phase 4 is the commercial pocket.** If you want revenue sooner rather than later, Phase 4 moves up. It is the only place measured demand, allowed scope and the business thesis overlap
- **Thumbnail text exists for 4 of 30.** The rest need it before scripting — 2–3 words, never repeating the title
- **The parked audience question** (README open question 0) mainly affects Phase 4's framing. Phases 1, 2, 3 and 5 land on working life either way

---

### Videos 1–10 — SUPERSEDED by The 30 above

> Kept as the record of the order that came out of `22`. **The 30 replaces it.** Four of these titles broke the char rule; all are fixed above.

Char rule: **30–50, hard ceiling 60** (`04` §1). Thumbnail text: **2–3 words, 4 is the ceiling.**

| # | Title | Chars | Thumbnail text | Search target | Validated? |
|---|---|---|---|---|---|
| 1 | **Is AI a Bubble? Ask the Railways** | 32 ✅ | `IS AI NEXT?` | ai bubble explained | ✅ **Yes** — real demand, live competition, global-English not Indian |
| 2 | **What Happens When the AI Money Stops** | 36 ✅ | `WHEN CAPEX STOPS` | ai capex spending economy | ❌ Below threshold |
| 3 | Why the Job Was Invented | 24 ⚠️ short | *needs one* | *none defined* | ❌ Unmeasured |
| 4 | Who Actually Captures the Value You Create | 42 ✅ | *needs one* | *none defined* | ❌ Unmeasured |
| 5 | Why Your Pay Stopped Tracking Your Productivity | 47 ✅ | *needs one* | wages vs productivity | ❌ Unmeasured |
| 6 | **The Bubble That Built Real Railways** | 35 ✅ | `REAL — AND A BUBBLE` | railway mania 1840s | ❌ Unmeasured |
| 7 | How the Freelance Economy Got Built — And What's Missing | **56 ⚠️ over** | *needs one* | freelance economy | ⚠️ "freelancing" ≈ 725 vs ai bubble 100 — **the one big serveable pocket** |
| 8 | **Recessions Are Declared Too Late** | 32 ✅ | `YOU FIND OUT LAST` | how is a recession declared | ⚠️ "recession" ≈ 83 |
| 9 | Who Decides Your Credit Score | 29 ⚠️ short | *needs one* | credit score | ⚠️ ≈870, but **transactional intent** — that search wants the score fixed, not explained |
| 10 | Why Every Government Is Suddenly Worried About Workers | **54 ⚠️ over** | *needs one* | *none defined* | ❌ Unmeasured |

#### Titles that break the char rule — fix before scripting

| # | Problem | Candidates, measured |
|---|---|---|
| 3 | 24, under the 30 floor — too thin to carry search terms | *Why the Job Was Invented at All* (31) · *Someone Invented the Job. Recently.* (35) |
| 7 | 56, over 50 | *How the Freelance Economy Got Built* (35) · *Who Built the Freelance Economy* (31) |
| 9 | 29, marginal | acceptable as-is; the noun is the search term |
| 10 | 54, over 50 | *Why Governments Are Watching Workers* (36) · *Why Every Government Now Tracks Workers* (39) |

**Six of ten have no thumbnail text and four have no search phrase.** That's the real gap in the slate, not the titles themselves.

---

### Videos 15+ — deferred, was the old first slate

Good videos, wrong first impression: they attract geopolitics viewers rather than the people the business serves. All have char counts and search phrases already done in `04` §2.

| Title | Chars | Search target |
|---|---|---|
| The 7 Chokepoints That Run the World | 37 | global trade chokepoints |
| Why Ships Now Avoid the Suez Canal | 35 | why are ships avoiding suez |
| China's Real Weapon Isn't Tariffs | 34 | china rare earth export controls |
| How Taiwan Got 90% of the World's Chips | 41 | why does taiwan make all the chips |
| How the Dollar Became a Weapon | 30 | dollar weaponization sanctions |
| The Dollar Has Been Dying for 50 Years | 39 | de-dollarization explained |
| Why Tariffs Never Work | 22 | do tariffs actually work |
| Why Chip Factories Keep Failing | 32 | semiconductor industrial policy |

---

### Topic backlog — 22 topics, not titles

From `05` §7. **The original wording predates the 60-char rule — treat these as topics to be retitled, never as titles to use.** Selection rules still apply: must pass the two-year test, must be chart-and-document-sourceable, no video needing primary research you can't finish in 3 hours.

**Infrastructure & trade** — shipping containers · Hormuz · Panama Canal water · undersea cables · the cost of a chip fab · Netherlands logistics · rebuilding supply chains · why big projects run late

**Money & power** — how sanctions actually work · the 1973 oil shock · Bretton Woods · currency pegs breaking · why empires go broke · the cartel behind most prices · who owns the sea

**States & industry** — Germany's industrial model · export-control enforcement and evasion · industrial policy's return · why neighbours stay poor · India's Green Revolution and its water · cities flooding · Suez 1956

**Gap worth noting:** this backlog is almost entirely geopolitics and infrastructure. **It contains nothing for the work/money/jobs niche the channel actually committed to** — so after video 10 there is no runway in the current niche. That needs filling, and it's a better use of a planning session than re-deciding branding.

---

### Roadmap — the sequence, not dates

| Stage | What | Gate to leave it |
|---|---|---|
| **Now** | Branding minimum: avatar ✅ · banner ⚠️ needs type · description ✅ · keywords ✅ | All uploaded, `BRANDING-SESSION.md` marked CLOSED |
| **Next** | Video 1 end to end. `RUNBOOK.md` → PART `13_RUNBOOK` step 0 → 11 | Published, `LOG.md` entry written |
| **Then** | Template set: video layout, thumbnail template, 3 expressions (deferred branding items 6 and 8) | One set, reused not redesigned |
| Videos 2–3 | One at a time. **Do not bulk-record before video 1 publishes** — the runbook rule stands even in phase mode | — |
| Phase 1 rest | Batch research → batch script → batch record | Cost per video below video 1's |
| Phase 2 on | Full batching. Keep one video in reserve from video 5 | Cost still falling |
| Video 12 | **First decision point** (`STRATEGY.md` → PART `09_COUNTER-STRATEGY`). End of Phase 3. Don't reassess earlier | — |
| Video 20+ | Property 2 unlocks only at ≥20 videos **and** per-unit cost down ≥40% | — |
| Video 30 | The 30 complete. Re-plan from real data, not guesses | — |
| Month 12 | Minimum success test: **₹10,000/month recurring, 3 consecutive months** | — |

**Three tiers per video:** Floor 6–8 min (~5–6 hrs) · Standard 14–18 min (~11–13 hrs) · Pillar 25–30 min (~17–21 hrs). Expect video 1 at 1.5× those.

---

### Scripting elsewhere — what to take with you

This folder is self-contained. For scripting on another platform, the four files that matter:

1. **`CONTEXT-PACK.md`** — paste first, always. Grounds any AI in one screen
2. **`RUNBOOK.md` → PART `15_SCRIPT-FORMAT`** — the verbatim-read format and the prompt that produces it
3. **`CRAFT.md` → PART `10_MACRO-TO-MICRO`** §3 and §5 — boomerang structure and the labelled-chain rigour rule
4. **`videos/01_.../CHAIN.md`** — video 1's chain, gates and source list

Plus `CLAUDE.md` for the hard rules. **Rule 1 travels with you: no figure that isn't in a source you actually opened.**


---

# PART — CHANNEL SPEC & FILE HISTORY

> Merged from `README.md` on 2026-09-13. The one-screen spec, plus the known-gaps audit.

Self-contained. Copy this whole folder to any machine and everything needed to run the channel is here.

**Holding brand:** ThinkLate Media · **Property 1:** ThinkLate (@wethinklate) · **Status:** live, 1 video published ("How NOT To Start a YouTube Channel")

> **Property 1 of an intended portfolio.** Holding-level thesis, decomposition and launch gates: `BUSINESS.md` → PART `20_PORTFOLIO-ARCHITECTURE`. Property 2 is earned by a falling cost curve on Property 1, not by wanting it.
**Last updated:** 2026-09-13

---

### THE SPEC — one screen, canonical

**Niche:** How work, money and power actually function — and how that reaches your working life. Economics, geopolitics and technology, through hindsight.

**YouTube category:** Education. **Sub-shelf:** business & economics explainer / infotainment.

**Language:** **Hinglish narration. English packaging** — titles, thumbnails, on-screen text, charts, description, subtitles all English.

**Audience:** Indian knowledge workers 22–40. Those considering independence (the mission audience) and those already independent serving global clients (the paying audience).

**Lens:** Who decided this, what were they optimising for, why is it still shaped that way — and how does it reach your life.

**Method:** documented history → the pattern → something happening now → the chain down to the individual, **every link labelled** DOCUMENTED / LIKELY / PLAUSIBLE / SPECULATIVE.

**Topics — in scope**

| Pillar | Covers | When |
|---|---|---|
| 1. Mechanism & precedent | Bubbles, capex cycles, wages vs productivity, tariffs, recessions, the history of the job itself | Videos 1–30 |
| 2. Built, and who paid | Megaprojects and infrastructure — who paid, who benefited, who carried the bill | 30+ |
| 3. How power accumulated | Currencies, companies, nations — and the technological chokepoint under each | 30+ |
| 4. Decided by machines | Credit scoring, algorithmic hiring, pricing, attention, allocation | 20+ |
| 5. How ideas spread | Intellectual history only, never hot-take | 50+, if ever |

**Substrate:** technology under everything — *because of it · with it · for it · by it*.

**Topics — out of scope:** finance/investing/trading advice (SEBI + YouTube AI-narration ban) · automotive and dealership (employer) · medical, legal, health advice · top-10s, listicles, compilations · news coverage and commentary · true crime · history narration · self-help and "how to succeed" · anything requiring AI-generated imagery.

**Format:** faceless · own voice · Floor 6–8 min / Standard 14–18 / Pillar 25–30 · **fortnightly** · document-and-data visuals, ink + paper surfaces alternating.

**Minimum success:** ₹10,000/month recurring, 3 consecutive months, by month 12.

---

### Working outside Cowork

- **`START-HERE.md`** — **read this first if you're working in any other AI.** Which file to open for which task, the four rules that matter most, and a paste-ready scripting prompt that makes the AI criticise the brief before it writes anything

- **`CONTEXT-PACK.md`** — one screen. Paste into any AI chat to ground it. Start every cold session with this
- **`HANDOFF.md`** — per-task file bundles, free local CLI agent options, and why the VPS/agent stack is still premature

### Start here

**Read `BUSINESS.md` → PART `21_VISION` for why, then `STRATEGY.md` → PART `00_CONTEXT` for what.** It carries the locked decisions, hard exclusions, editorial rules and the evidence base. Everything else is detail you open only when the task needs it.

#### Starting a new AI session

> Read `STRATEGY.md` → PART `00_CONTEXT` for full context on my ThinkLate YouTube channel. To make a video, follow `RUNBOOK.md` → PART `13_RUNBOOK` step by step. Open other docs only as the runbook points to them. Today I want to [make video 1 / build the templates / set up the channel].

---

### Files

| File | What's in it | Open when |
|---|---|---|
| **`START-HERE.md`** | **How to use this folder with any AI.** File-per-task index · the four rules that matter most · paste-ready scripting prompt · what is deliberately unsettled · closed topics | **Working outside Cowork** |
| **`START-HERE.md` → PART `ROADMAP-AND-TITLES`** | **The single title list and the phase roadmap.** Videos 1–10 with char counts / thumbnail text / search targets / validation · the deferred 15+ slate · 22 backlog topics · scripting-elsewhere file list. **Supersedes the title lists in `04`, `05` and `03`** | **Any title, or planning what's next** |
| **`BUSINESS.md` → PART `21_VISION`** | **Why any of this exists.** The vision structured into diagnosis / end state / mechanism / role / horizon · "modern dharma" made specific (viveka, sreyas-preyas, svadharma, artha, rina) · the decade-version goal · the builder→leader trigger · 4 questions still open | **Sits above everything. Read when direction feels unclear** |
| **`STRATEGY.md` → PART `00_CONTEXT`** | **Master context.** Locks, lens, exclusions, editorial rules, evidence base, reversed decisions | **Always first** |
| `STRATEGY.md` → PART `01_STRATEGY` | Positioning, content pillars, monetisation ladder, metrics and kill criteria, 16-week plan, risks | Planning, reviews |
| `BRAND.md` → PART `02_BRAND` | Niche classification, palette, type, logo/avatar/banner specs with dimensions, channel description, layout, SEO metadata, pre-launch checklist | Channel setup |
| `CRAFT.md` → PART `03_CONTENT-AND-VOICE` | Current-affairs grounding with sources, 12-video slate in 4 clusters, **full voice and scripting guide** — script structure, signature devices, before/after rewrites, robotic-delivery checklist | **Scripting** |
| `CRAFT.md` → PART `04_TITLES-AND-THUMBNAILS` | Short titles with char counts, thumbnail text, target search phrases, thumbnail layout, searchability triage, title-writing rules. **Supersedes the titles in 03** | Any title or thumbnail |
| `RUNBOOK.md` → PART `05_ASSETS-AND-PROMPTS` | Frame-type library, source list (data/archival/stock), AI do-and-don't, research prompt library, per-video asset budget, **34-title backlog** | Production, sourcing |
| `CRAFT.md` → PART `06_MOTION-AND-SURFACE` | Why static cards fail, motion specs and timing, three-layer composition, the two-surface system, surface sequencing | Editing, design |
| `BRAND.md` → PART `07_TOOLING` | vidIQ vs TubeBuddy verdict, Resolve/Affinity usage, tool gaps, budget, what to skip | Tool decisions |
| **`BRAND.md` → PART `08_DESIGN-SPEC-FOR-GENAI`** | **Paste-ready prompts** — design tokens, the 10 in-video frame types, animated charts, and **channel branding: logo, avatar, banner, watermark** (§6). `02` has the specs; this has the prompts | **Building templates or channel art** |
| **`STRATEGY.md` → PART `09_COUNTER-STRATEGY`** | **Surviving the flat period.** Three-format system (Floor/Standard/Pillar), cluster research economics, what to measure instead of views, the cost ratchet, guilt-spiral safeguards, decision points at video 12 and 24 | **When motivation dips, or before committing** |
| **`CRAFT.md` → PART `10_MACRO-TO-MICRO`** | **Core positioning.** The macro-to-micro thesis, the boomerang script structure, the four micro domains, **the causal-chain rigour rule**, psychological-claims guardrail, micro-led titles | **Before scripting anything** |
| **`STRATEGY.md` → PART `11_TECH-AS-SUBSTRATE`** | Tech as the substrate under every topic. The because-of/with/for/by taxonomy as a topic generator, the invariant-vs-instance decay rule, **revised pillars incl. new "Decided by machines"** | Topic generation, planning |
| **`CRAFT.md` → PART `12_CRAFT-EVIDENCE`** | **Researched benchmarks** for retention, hooks, titles and thumbnails — plus two corrections to earlier docs and the honest faceless-CTR headwind | **Before scripting or designing thumbnails** |
| **`RUNBOOK.md` → PART `13_RUNBOOK`** | **The per-video sequence, step 0 to 11.** Tier choice, title first, the chain, research, script, assets, record, edit, package, measure, log. Time budgets and stop-gates | **Every video. Start here to make one** |
| **`RUNBOOK.md` → PART `14_SCENE-SHEET`** | **Script → per-scene visual spec.** The scene-sheet format, a worked 3-minute example, and three paste-ready AI prompts: script→sheet, scene→visual, archive sourcing | **Between script and asset building** |
| **`RUNBOOK.md` → PART `15_SCRIPT-FORMAT`** | **Verbatim-read script format.** Pause/stress/take notation, numbers-as-spoken rule, worked example, pre-record checklist, and the paste-ready prompt that produces a script in this format | **Before recording** |
| **`RUNBOOK.md` → PART `16_FREE-TOOL-STACK`** | **Free-tier tool per asset**, researched. Ideogram vs Recraft for the logo, Canva for layout, the Recraft commercial-use trap, and why most AI video tools are the wrong tool here | **Before making any asset** |
| **`BUSINESS.md` → PART `17_BUSINESS-AND-SCALE`** | **Channel → business.** Entity path (individual → LLP/Pvt Ltd), GST thresholds and the AdSense zero-rating/LUT rule, trademark Class 41 and the file-as-individual saving, FEMA/FIRC, the five scaling phases, and what makes it a sellable asset vs a job | **At first sponsor, and before incorporating anything** |
| **`BUSINESS.md` → PART `18_INVERSION-BUSINESS-FIRST`** | **The counter-strategy.** Why content-as-marketing beats content-as-product, the defensible core of the mission vs the part the evidence doesn't support, six candidate ventures scored, and the three sequencing models | **Strategic review** |
| **`STRATEGY.md` → PART `19_PROBLEM-THESIS`** | **What the venture is committed to.** The Indian→global segment, the problem statement, review gates at months 6/12/18/24, how discovery fits inside the channel work, and what not to build | **Quarterly, and before building anything** |
| **`BUSINESS.md` → PART `20_PORTFOLIO-ARCHITECTURE`** | **Holding-level view.** The unifying thesis and 3-question portfolio test, the vision decomposed into demographic × problem × property, the 10 shared assets that make a portfolio beat one business, gates for launching Property N+1, and the 5-phase sequence | **Before considering any second property** |
| **`STRATEGY.md` → PART `22_NICHE-BUSINESS-ALIGNMENT`** | **Resolves YouTube↔business.** The niche was pointed at the wrong audience; keeps the lens, narrows the subject to work/money/economic life. **Revised publish order.** Honest money model per revenue line — and why the channel is a good second income, not freedom | **Read with `19` and `21`** |
| **`STRATEGY.md` → PART `23_REVENUE-ROADMAP`** | **Net position after all revisions** (12 changed / 9 unchanged) and the **revenue roadmap** — first rupee month 4, real revenue month 6-9 via a paid reference product built from your own compliance research, recurring month 9-12 via newsletter sponsorship sold on precision not size | **Read after `22`. The practical answer** |
| **`STRATEGY.md` → PART `24_LANGUAGE-REVERSAL`** | **Language reversed to Hinglish narration + English packaging** — because the buyer is 100% Indian and AdSense was deprioritised. What it costs (the audience graph becomes permanently Indian). **Defines minimum success: ₹10k/month recurring, 3 months, by month 12** | **Before scripting video 1** |
| **`BUSINESS.md` → PART `25_AI-ARCHITECTURE`** | **AI stack review.** Layer discipline (substrate/retrieval/runtime/orchestration), verified verdicts on OpenClaw, Paperclip, Obsidian, OpenRouter, Letta, Mem0, Zep — why markdown+git beats all of them here, why you retrieve rather than train, and **the automate-assembly-never-judgement rule** | **Before adopting any AI tool** |
| `CLAUDE.md` | Standing rules any AI runtime reads first — hard rules, exclusions, fixed decisions | Auto-loaded by agents |
| `discovery.md` | Discovery log — own frictions, newsletter replies, conversations, complaints, pain tally | Ongoing |
| `LOG.md` | Production log — one entry per published video | After publishing |
| `ARCHIVE/originals/99_RESEARCH_niche-screen.md` | 20 sub-niches scored, ~180 sources. **Superseded on conclusions** (weighted toward a technical niche) but the policy, regulatory and economic evidence holds | Background only |
| `videos/` | One folder per video: script, scene sheet, assets, sources | Production |
| `templates/` | Working Python reference implementation + rendered previews. Optional if using GenAI tools | Reference |

---

### `templates/` — what it is

A tested reference implementation. `templates/brand.py` holds the tokens; `templates/frames.py` renders 10 SVG frame types; `templates/charts.py` renders 4 static chart types; `templates/animate.py` renders animated charts to MP4; `templates/surface_demo.py` renders the ink-vs-paper comparison.

**If you're building templates with GenAI tools instead, you don't need this.** Use `BRAND.md` → PART `08_DESIGN-SPEC-FOR-GENAI` and keep this folder as proof the spec renders correctly.

Previews worth looking at:

- `templates/preview/_sheet_frames.png` — all 8 main frames
- `templates/preview/_sheet_charts.png` — the 4 chart types
- `templates/preview/_sheet_surfaces.png` — ink vs paper, same content
- `templates/preview/anim_*.mp4` — working motion samples

Preview PNGs were rendered without the brand fonts installed, so serif shows as sans. Charts used an installed serif and look correct.

---

### The channel at a glance

- **Lens:** who decided this, what were they optimising for, why is it still shaped that way — **and how does it reach your life**
- **Move:** documented history → the pattern → something happening now → **the chain down to the individual**, with every link labelled by confidence
- **Meta-thesis:** in an AI-saturated world the scarce skill is observation and pattern recognition. Every video leaves the viewer with a sharper eye, not just a fact
- **Substrate:** technology, running under everything — *because of it, with it, for it, by it*
- **Pillar 1:** economics, geopolitics and business. Mechanism and precedent, never news coverage
- **Format:** faceless, **Hinglish narration / English packaging**, own voice, document-and-data visuals. **Three tiers — Floor 6–8 min, Standard 14–18 min, Pillar 25–30 min. Every two weeks.**
- **Stance:** information-first, not advice-first. No track record yet, so investigate and explain
- **First video:** *Is AI a Bubble? Ask the Railways*
- **What the channel is FOR:** the trust-and-research layer for an eventual software product serving **Indian knowledge workers who go independent and serve global clients.** Problem committed, product deferred to month 12+ (`STRATEGY.md` → PART `19_PROBLEM-THESIS`)

---

### Immediate next actions

1. Display name → "ThinkLate" (capitalised); handle @wethinklate
2. Claim @wethinklate on X and Instagram
3. Unlist the old single video
4. New channel description, category → Education, channel keywords
5. Logo: lockup + avatar mark — **owl head only, no text inside the mark**. Built in SVG, not generated: `brand/build_assets.py`
6. Banner **2560×1440**, critical content inside 1235×338, no borders or shadows
6b. **Video watermark** — owl mark 150×150, square, <1MB, set to "entire video"
6c. **Contact info** — business email for sponsor enquiries
6d. Links — newsletter first; it gets the prominent slot beside Subscribe
7. Build the template set — prompts in `BRAND.md` → PART `08_DESIGN-SPEC-FOR-GENAI`, tools in `RUNBOOK.md` → PART `16_FREE-TOOL-STACK`
8. Install fonts: Instrument Serif, IBM Plex Sans, IBM Plex Mono
9. Validate top 3 search phrases in Google Trends + vidIQ free tier
10. Newsletter live from video 1
11. **Cut one 60-second segment end to end before scripting video 1**

#### Publish order — first 10

> **Consolidated 2026-09-13 into `START-HERE.md` → PART `ROADMAP-AND-TITLES`** — the single title list, with char counts, thumbnail text, search targets and validation status. Four conflicting lists existed; that file resolves them. The order below is still correct.

**Revised per `STRATEGY.md` → PART `22_NICHE-BUSINESS-ALIGNMENT` §3** — every video now lands on the viewer's working life, which is both the mission audience and the paying audience.

1. Is AI a Bubble? Ask the Railways — *your job security*
2. What Happens When the AI Money Stops — *who gets cut first*
3. Why the Job Was Invented — *the default path isn't permanent*
4. Who Actually Captures the Value You Create — *wage vs output*
5. Why Your Pay Stopped Tracking Your Productivity
6. The Bubble That Built Real Railways — *real assets, wiped-out investors*
7. How the Freelance Economy Got Built — And What's Missing
8. Recessions Are Declared Too Late — *you find out last*
9. Who Decides Your Credit Score — *systems deciding your options*
10. Why Every Government Is Suddenly Worried About Workers

**Chokepoints, Suez, rare earths, Taiwan → backlog for videos 15+.** Good videos, wrong first impression — they attract geopolitics viewers rather than the people the business serves.

**Do not bulk-record before video 1 is published.** Videos 1–3 one at a time; batch voice from video 4; keep one in reserve from video 5.

---

### Open questions

0. **⚠️ AUDIENCE — PARKED 2026-09-13, decide before video 2.** `STRATEGY.md` → PART `19_PROBLEM-THESIS`, `STRATEGY.md` → PART `22_NICHE-BUSINESS-ALIGNMENT` and `CONTEXT-PACK.md` all point the channel at *Indian knowledge workers who go independent and serve global clients*, because the eventual product was meant to serve them. **The venture direction has since changed** — product first, then an ad agency / digital company building and running digital platforms for others. That sells to businesses: founders, SME owners, marketing and digital leads. **Different buyer, so the funnel claim in those three docs may no longer hold.** Three options were on the table: follow the business to operators · keep independent knowledge workers and treat the agency as separate · decouple and decide at month 12. **Deliberately not settled.** Video 1 is unaffected either way, so it proceeds. Nothing was rewritten. Settle this before titling video 2 — it changes every title decision from there on.
1. Newsletter platform — beehiiv or Substack
3. **Cox employment agreement review** — IP assignment, moonlighting, non-compete, conflict-of-interest, work-product definition. **Blocks incorporation, not publishing.** *Needs an employment lawyer; nothing here is legal advice*
4. Buy thinklate.com
5. ~~Hindi MLA track~~ — **closed.** Hinglish is now primary (`STRATEGY.md` → PART `24_LANGUAGE-REVERSAL`)

---

### Consistency check — 2026-09-13

Audited for contradictions and fixed: cadence is **every two weeks** everywhere (was three different answers) · length is the **three-tier system** everywhere (was "18–30 min" in two docs) · banner is **2560×1440** everywhere (was 2048×1152 in three places) · thumbnail text is **2–3 words** everywhere (was 3–5) · stale filename cross-references repointed to the numbered files · `03`'s script structure marked superseded by the boomerang in `10`.

**Known intentional overlap:** pillars appear in both `01` and `11` (`11` is authoritative) · titles appear in `03`, `04` and `10` (`04` is authoritative for videos 1–10, `10` for video 15+).

---

### Note on duplication

These files were copied from the wider workspace (`00_Context/projects/`, `03_Strategy/`, `01_Research/`, `05_Build-Prompts/`). The originals still exist there. **This folder is now the canonical copy** — edit here, and treat the originals as stale.

---

### ⚠️ KNOWN GAPS — verified 2026-09-13

**A fresh session should read this first.** These are real and named rather than hidden.

#### Blocking

| Gap | Effect |
|---|---|
| **`brand/00_MASTER_avatar.png` does not exist** | All five prompts in `brand/ART-DIRECTION.md` reference it as the consistency anchor. **Save the approved avatar there before any branding work.** Derived files `brand/stamp.png` and the expression PNGs also do not exist yet |
| ~~Palette dark tone undecided~~ | ✅ **CLOSED 2026-09-13 — unified on `#1B2A4A`.** `templates/brand.py` updated, all 13 preview SVGs re-rendered, `SLATE` lightened to `#98A2B3` to pass WCAG AA. `BRAND.md` → PART `02_BRAND` PALETTE ARCHITECTURE |

#### Non-blocking, worth knowing

| Gap | Note |
|---|---|
| **Branding not applied to the live channel** | The channel still shows the old cyan banner and the signboard avatar. Old description still live |
| **Video 1 not started** | `RUNBOOK.md` → PART `13_RUNBOOK` step 0. Published video is off-niche "video zero", deliberately kept |
| **Duplicate copies of some docs exist** outside this folder | In the wider workspace (`00_Context/projects/`, `03_Strategy/`, `01_Research/`, `05_Build-Prompts/`). **This folder is canonical.** Removal not yet authorised |
| **`brand/PROMPTS.md` and `brand/BRIEF.md` are SUPERSEDED** | Marked at the top of each. Kept as a record of eight rejected rounds. Do not use |
| **`brand/` contains many test renders** | `C1*.png`, `p1*.png`, `owl_*`, `row*` — experiment output, not assets. Safe to ignore |
| **Cox employment agreement unreviewed** | Moonlighting and IP clauses. **The only existential risk on the list.** Do before spending money |
| **Unset:** thinklate.com · GST LUT · trademark Class 41 · newsletter platform · weekly time budget · dated kill criteria | Not urgent until revenue, except the LUT annual deadline |
