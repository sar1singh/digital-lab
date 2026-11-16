# @wethinklate: Solo Creator Strategy & Pipeline Blueprint
**Grounded:** 2026-11-06 (live runtime clock). 5–8 h/week · AI voice only · zero code.

> [!IMPORTANT]
> **Evidence labels.** I ran live searches, but the results were secondary blogs and tool-vendor pages. They returned no publication timestamps, so I can't confirm they fall inside your 72-hour freshness window.
> - **[SRC]** = repeated across the live searches. Treat it as a working heuristic, not an official YouTube number.
> - **[JUDGMENT]** = my own call from the data. Pricing and free-tier credits are **UNVERIFIED**. Check each tool's pricing page before paying anything.
> - I can't see your YouTube Studio data. Section 1 gives you a 10-minute diagnostic to run, and the verdict depends on it.

---

## 1. Forensic autopsy

### The honest verdict
You have **5 uploads total**. That is not a failing channel, it is an untested one. Most channels need roughly 30–50 uploads before the data means anything [JUDGMENT]. Your 103 views are almost certainly a **cold-start distribution result**, not a verdict on quality. But there are real, fixable design flaws:

| # | Flaw | Why it kills a 0-sub channel |
|---|---|---|
| 1 | **Topic with no demand signal.** "Financial paradoxes / corporate exposés" are not things people type or click on. | A new channel has no audience graph. YouTube needs a topic that already has viewers. [SRC] |
| 2 | **Wrong format for the test.** Long, heavily produced videos give the algorithm very few clean data points per hour of your effort. | One long video = one weak test. Four Shorts = four tests. |
| 3 | **Mixed topic signal.** Four videos on four different subjects. | The system can't tell who your seed audience should be. [SRC] |
| 4 | **Production over distribution.** Your repo has a motion engine, 24 workspace rules, a Remotion library and avatar rigs, against 5 videos. | You have optimised the part viewers can't see. |
| 5 | **Packaging probably unvalidated.** | If the first pool of dozens to hundreds of impressions ignores the thumbnail, impressions stop. [SRC] |

### "Bad content" vs "cold-start filter": diagnose in 10 minutes
Open Studio → each video → **Analytics → Reach**. Read **Impressions**, **CTR**, **Avg view duration**.

| What you see | Diagnosis | Fix |
|---|---|---|
| Impressions < ~300, CTR undefined or noisy | **Cold-start / zero distribution.** Not enough data to judge. | Make more, shorter tests (Section 6). |
| Impressions 300+, CTR < 2% | **Packaging problem** (title/thumbnail, topic has no pull). | Different topic and a new thumbnail concept. |
| CTR ≥ 3–4% but average view duration < 30% | **Content/hook problem.** | Rewrite the first 30 seconds. |
| Most views come from "Direct / external" or your own device | **No distribution at all.** The views are you and friends. | You have zero algorithmic data. Start from scratch. |

### How the recommender tests a 0-sub account [SRC]
1. **Micro-batch.** A few dozen to a few hundred impressions, picked from people with matching watch history.
2. **Feedback.** CTR and retention for long-form. Viewed-vs-swiped and completion for Shorts.
3. **Expand or flatline.** Good response means the next, larger tier. A weak response means impressions stop and the graph goes flat.
4. **Small-sample trap.** At 100–200 impressions, CTR is noise. Don't redesign off it.

### Why Short 01 shows 0
Check these in order:
1. **Age.** Published today. Zero in the first hours is not abnormal. Judge at 24–48 h.
2. **Studio → Content → the Short → Visibility/Checks.** Look for processing stuck, a copyright claim (music or clips), or "Restricted".
3. **Format.** It must be vertical, 9:16, ≤ 3 min. Confirm it is classified as a Short and not a normal video.
4. **Reused or template content.** The originality filter throttles recycled clips, template edits and watermarked footage. [SRC]
5. **Screenshot test.** Does it have a text and visual hook in the first 1.5 s? If frame 1 is a logo or black, viewers swipe and distribution dies.

---

## 2. The 2026–2027 meta for faceless channels

**What works [SRC]:** high-editorial-value formats with a distinct point of view. That means case studies built on real data, animated explainers with strong visual sync, and documentary-style essays with research. A synthetic voice is acceptable. A flat, low-effort one is not.

**What gets throttled or demonetised [SRC]:**
- Template-swap channels where only the subject name changes.
- Slideshow plus robotic TTS.
- Random shocking AI clips.
- **AI personas or "experts" delivering financial, medical or legal advice.** This applies to you. Your cartoon owl is fine as a commentator. Never have it tell people what to do with their money. Frame everything as "here is what happened and why".

**Why academic long-form fails for a new channel [JUDGMENT]:**
- Zero trust means zero patience. The first 30 seconds must be a conflict, not a thesis.
- Long form tests slowly (days to weeks) and forgives nothing.
- Viewers can't tell if you are worth 8 minutes yet.
- Replacement format: a **short, story-first explainer** (30–45 s Short, or 4–6 min long-form) with one character, one conflict, one surprising number, and a payoff.

**Shorts benchmarks [SRC, heuristic only]:**

| Metric | Stall | Healthy | Breakout |
|---|---|---|---|
| Viewed vs swiped away ("chose to view") | < 60% | ~70% | 75%+ |
| Average % viewed (finance explainer) | < 45% | 55–65% | 65–70%+ with rewatches |
| Length sweet spot | – | 30–45 s | – |
| Hook | – | decided in ≤ 1.5–3 s | – |

---

## 3. Non-speaker AI audio stack

**Pick: ElevenLabs v3 (audio tags).** Use it because you write scripts ahead of time and need performance control. Cartesia Sonic is built for real-time voice agents and has no script-level direction. It is the wrong tool for narration. [SRC]

### Workflow
1. Pick **one** narrator voice and use it on every video. Consistency is brand, and it avoids the "template channel" look. Browse the Voice Library or use Voice Design.
2. Generate **per paragraph** (3–5 sentences), not the whole script. Delivery drifts over long text.
3. Generate **3 takes per paragraph**, keep the best. This takes about 10 minutes per Short.
4. Settings to start from (confirm against the current UI) [JUDGMENT]: Stability low-to-mid for expressive delivery, Similarity high, Style moderate.

### Directing without speaking
| Intent | How to write it |
|---|---|
| Deadpan sarcasm | `[deadpan]` before the line, then a short sentence. |
| Beat before a reveal | New paragraph + `...` or `[pause]`. Silence is mostly cut-timing in the editor. |
| Emphasis | One word in CAPS. Don't overuse it. |
| Shock or whisper | `[whispers]`, `[shocked]`. |
| Pacing | Short sentences are fast. A long one is a slow, thoughtful beat. |

### Post-processing (CapCut or DaVinci, 5 minutes)
- Trim breaths and gaps to roughly 0.1–0.2 s.
- Light compression, then normalise to about -14 LUFS (YouTube target) for Shorts.
- Music at about -22 to -24 dB, with a speech-band dip around 1.5 kHz so the voice stays clear.

---

## 4. Zero-code visual stack

**Honest default for a 6-hour week:** stills + real evidence + a few video-generated hero shots. Don't generate every shot as AI video. It is slow, expensive, and makes everything look like AI slop.

| Layer | Pick | Why |
|---|---|---|
| **Cinematic scene plates** | **Midjourney v7** | Strongest look. Weak on long text (~70–80% text accuracy). [SRC] |
| **Text-heavy cards / posters / thumbnails** | **Ideogram 3** | Best typography (~95%). [SRC] |
| **Infographic / document layouts** | **Nano Banana Pro** (Gemini) | Reasons about structure. [SRC] |
| **Flux 1.1 Pro** | Skip | Photoreal but you don't need it. |
| **Image → video** | **Kling** for human motion; **Veo 3.1** for photoreal cinematic; **Runway** for camera control; **Hailuo** for expressive faces; **Luma** for push-ins. [SRC] Use **one**. Start with Kling. | 3–5 hero clips per video, ≤ 5 s each. |
| **Editor** | **CapCut Desktop** for Shorts now. **DaVinci Resolve** only for long-form later. | Auto-captions, templates, speed. |

### Sourcing real evidence in under 15 minutes
| Need | Source |
|---|---|
| Company filings | SEC EDGAR (10-K, 8-K), screenshot the real page. |
| Court records | CourtListener / PACER dockets. |
| Charts and data | FRED, company investor pages. |
| Archival photos and clips | Wikimedia Commons, Internet Archive, Library of Congress, Chronicling America. |
| Stock B-roll | Pexels, Pixabay. |

> [!WARNING]
> **Never AI-generate fake "evidence"** (a fake newspaper clipping or fake filing). It breaches your own fact-check rule, risks policy action, and destroys trust. AI images are for atmosphere only. Evidence is always a real screenshot.

---

## 5. Weekly operating system (≈ 6 h/week, 3 Shorts per cycle)

| Day | Block | Output |
|---|---|---|
| **1** | 60 min: Demand check | 3 validated topics |
| **2** | 75 min: Scripts | 3 scripts, ~105 words each |
| **3** | 90 min: Audio and assets | 3 voiceovers and ~12 images, 3–5 video clips |
| **4** | 90 min: Assembly | 3 captioned Shorts |
| **5** | 45 min: Packaging and scheduling | Titles, metadata, 3 scheduled uploads |

### Day 1: demand check (60 min)
There is no way to *guarantee* demand. Cut the risk with the **outlier test**:
1. Search the topic on YouTube, filter by this year, sort by popular.
2. Look for **≥ 3 videos from channels under ~10K subs with 10× their usual views** [JUDGMENT].
3. Check YouTube autocomplete and Google Trends for the keywords.
4. Check Reddit top posts for the story.
5. Write the **one-sentence conflict**. If you can't, the topic is dead.

### Day 2: Short script (30–45 s, ~105 words)
| Time | Beat |
|---|---|
| 0–2 s | **Hook:** one concrete number or conflict, spoken and in on-screen text. |
| 2–10 s | **Stakes:** who is hurt, who profits. |
| 10–30 s | **Three beats** joined by "but" and "therefore". |
| 30–38 s | **Reveal.** |
| 38–42 s | **Loop line** that echoes the opening so the Short replays. |

Long-form (4–6 min, ~650–850 words): cold-open conflict in the first 15 s, then a promise, 4 beats each ending on an open loop, a payoff, and a one-line close. No "Act 1" announcements.

### Day 3: audio and assets
Voice first (Section 3), then images, then 3–5 hero clips. Use one style prompt on every image so visuals stay consistent.

### Day 4: assembly
- CapCut: vertical 9:16, auto-captions (large, 2–3 words per line), a zoom or cut at least every ~2–3 s.
- 3–5 sound hits maximum, kept warm and low.
- Export 1080×1920.

### Day 5: packaging
- **Short title:** ≤ 5 words, a curiosity gap, no clickbait lies.
- **Long-form title:** ≤ 50 characters.
- **Thumbnail:** one physical prop, one emotion, ≤ 3 words in the top banner.
- Description: one sentence plus sources. Add chapters for long-form.
- Schedule uploads for later in the week.

---

## 6. 30-day cold-start playbook

**Recommendation: Shorts-first, about 80/20.**
- **Weeks 1–3:** 3 Shorts per week, with one topic family. Consistent topic signal tells the system who your audience is.
- **Week 4:** 1 long-form (4–6 min) made from the best-performing Short topic.
- Reason: Shorts give you roughly 10 tests for the effort of one long video. Shorts subscribers convert poorly to long-form viewers, so the goal is **data and hook learning**, not subscribers.

### The next 10 videos
Pick **one topic family**: *"How companies quietly take money from you."* It is consumer-pain, concrete, and falls inside your existing niche.

Hook patterns (examples are angles only and **UNVERIFIED**; fact-check before scripting):
1. Hidden-fee stories (resort fees, ticket fees, subscription traps).
2. "The company that [obvious thing] and nobody noticed."
3. One shocking number, then the explanation.
4. A product that costs less than its packaging promises.
5. "Why [familiar brand] keeps doing [irritating thing]."

Mix 7 Shorts, 2 hook-variant repeats of a winner, and 1 long-form.

### What to check at 48 hours (Shorts) [heuristics]
| Signal | Dead | Working |
|---|---|---|
| Viewed vs swiped away | < 60% | ≥ 70% |
| Average % viewed | < 45% | ≥ 60% |
| Views 24 h → 48 h | flat | growing |
| Retention curve | cliff at 0–3 s | smooth with rewatch bumps |

Long-form: **CTR 2–5% in Browse** is normal [SRC]. Judge it only after 300+ impressions. Check that **30-second retention ≥ 70%** [JUDGMENT].

**Rules:**
- Don't change titles or thumbnails in the first 48 h. [SRC]
- If one Short beats the rest by 3× or more, make 3 more variants on the same hook within a week.

---

## Open decisions for you
1. **Budget.** Your global rule is free-tier compute only. A free tier might cover Shorts-first volume (unverified). Long-form with premium voice will probably cost money. Which do you want?
2. **Workspace rules.** Your `AGENTS.md` mandates Remotion, dual voices, 6–8 min videos and a heavy QC process. That conflicts with zero-code and 5–8 hours. I have not changed it. Do you want me to add a "30-Day Sprint Mode" override?
3. **Facts.** I won't fabricate current examples. Tell me which channel metrics you're seeing, or paste your Studio reach numbers, and I'll adjust the diagnosis.

---

## Appendix A: Live public audit of @wethinklate (fetched 2026-11-06 22:21 IST)
Source: public YouTube pages via yt-dlp (no login). Impressions, CTR, AVD and subscriber count are NOT public, so the Section 1 decision tree is still unresolved.

| # | Published | Title | Length | Views | Chapters | Manual subs | Tags |
|---|---|---|---|---|---|---|---|
| 1 | 2026-09-19 | Is AI a Bubble? Ask the 1845 Railways. | 4:45 | 37 | 8 | none | 24 incl. competitor names |
| 2 | 2026-10-09 | Why A 500-Year Castle Costs Less Than A City Condo | 10:50 | 10 | 23 | en | none |
| 3 | 2026-10-17 | You Don't Own What You Buy | 10:08 | 23 | 19 | en | 15 |
| 4 | 2026-10-30 | How Companies Turned Ownership Into Rent (metadata still reads "Why You Will Never Own Anything Again") | 6:40 | 33 | 7 | none | 14 |
| S1 | 2026-11-06 | Why Your Power Bill Just Spiked 800% #Shorts #thinklate #economics | 1:00 | 0 | - | en | none |

Findings:
1. Upload cadence is irregular (gaps of 20, 8, 13, 7 days). There are 5 data points in total.
2. The shortest long-form (4:45) and the 6:40 one are the top two. The two ~10-minute videos are lowest. n=4, so treat this as a hint only.
3. Topics scatter across AI bubble, housing, digital ownership and power bills. Videos 3 and 4 share one theme (ownership) and are the most consistent signal.
4. Castle/condo thumbnail is a vertical image pillarboxed with black bars inside a 16:9 frame. It is a packaging defect.
5. Video 1 tags name other channels (Polymatter, ColdFusion, Vox Borders). Remove them. Misleading metadata can breach YouTube spam policy.
6. Short is 60 s (target 30-45 s) and has no tags. Its title claims "800%", but its own thumbnail and description say "+\/month". Verify the 800% figure against a primary source or change the title.
7. Short title carries three hashtags inside the title at 66 characters. Move hashtags to the description.
8. Chapters of ~30 s each (19 to 23 chapters in 10 minutes) are over-granular. 5-7 is enough.

---

## Appendix B: Full content audit (downloaded public files, 2026-11-06)
Method: ffmpeg loudness/silence analysis, caption transcripts, frame contact sheets. I did NOT listen to the voices, so voice naturalness is unjudged. Scene-cut counts undercount dark animated slides (V2, V3); rely on the frame review there.

| Video | Loudness (LUFS) | Visual style seen | Key defects |
|---|---|---|---|
| V1 AI Bubble 4:45 | -15.5 (ok) | Vintage illustrations + charts | Auto-captions only; competitor tags; claims unverified |
| V2 Castle 10:50 | **-24.1 (�10 LU too quiet)**, 80 pauses = 51 s | Dark grid slides, tiny text, "ACT" labels on screen | 8 s static opening, garbled script ("morts", "old Europe lands"), ends with investment advice, pillarboxed thumbnail |
| V3 Own What You Buy 10:08 | -18.3 | **Ubisoft Assassin's Creed gameplay** as background + article cards | Copyright-claim risk, off-topic footage, captions misrecognise speech |
| V4 Rent 6:40 | -16.1 (ok) | Stock B-roll + lower-thirds, cut every ~10 s | Auto-captions only; strongest hook; best execution |
| S1 Power Bill 1:00 | **-91 dB: AUDIO TRACK IS SILENT** | Text cards on black, top half empty | Silent render; video says "+\/mo" but title/thumb say "\"; "800%" and "voters snapped today" unverified; 60 s |

Cross-cutting: four long videos use four different visual identities; audio levels range from -24 to -15.5 LUFS.
Fixes in priority order:
1. Delete the silent Short, re-render with audio, upload a 30-45 s version.
2. Pick one visual identity and one thumbnail template for all uploads.
3. Normalise every export to about -14 LUFS.
4. Unlist V2 and V3 until recut (remove game footage, fix script and thumbnail).
5. Remove advice-style endings. Frame as "what happened and why".
6. Fact-check ledger before every publish.
