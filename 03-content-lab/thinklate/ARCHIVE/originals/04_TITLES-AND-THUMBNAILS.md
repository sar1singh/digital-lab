# ThinkLate — Titles, Thumbnails & Searchability

**Date:** 2026-09-13
**Replaces:** the long working titles in `03_CONTENT-AND-VOICE.md`

---

## 1. Two problems with my earlier titles

### Too long

YouTube truncates titles at roughly **60 characters** on most surfaces — search results, suggested, mobile home. Titles like *"People Have Predicted the Dollar's Death for 50 Years. Here's Why They Keep Being Wrong."* (88 chars) get cut mid-sentence. The punchline never renders.

**Rule: 30–50 characters. Hard ceiling 60.**

### Wrong title *type* for a new channel

This is the bigger error. There are two kinds of title and they do different jobs:

| Type | Wins in | Needs |
|---|---|---|
| **Search title** | Search results | Matches what people actually type |
| **Curiosity title** | Browse, Suggested, Home | An existing audience and watch history for the algorithm to work with |

My earlier titles were curiosity titles. **A channel with 21 subscribers gets almost no browse distribution** — the algorithm has nothing to work with. So early videos live or die on search, and the titles have to match search phrasing.

**Strategy: videos 1–10 use search-led titles. From ~video 15, once there's an audience, shift toward curiosity titles.** That's the opposite order from what I first gave you.

### What I could not verify

**I have not measured search volume for any of these.** That needs keyword tooling — vidIQ, TubeBuddy, Ahrefs, or Google Trends. Everything below is reasoned from search *intent phrasing*, not from volume data.

**Do this before scripting video 1:** check your top 3 candidate phrases in Google Trends (free) and vidIQ's free tier. Ten minutes, and it replaces my guess with evidence.

---

## 2. Revised slate — title, thumbnail text, search target

Thumbnail text: **2–3 words, 4 is the ceiling** (revised down per `12_CRAFT-EVIDENCE.md` — under 4 words shows ~30% higher CTR). Legible at 10% scale. It must not repeat the title — title and thumbnail should say two different things that combine into one idea.

| # | Title | Chars | Thumbnail text | Search phrase targeted |
|---|---|---|---|---|
| 1 | **Is AI a Bubble? Ask the Railways** | 33 | `IS AI NEXT?` | ai bubble explained |
| 2 | **The 7 Chokepoints That Run the World** | 37 | `7 CHOKEPOINTS` | global trade chokepoints |
| 3 | **Why Ships Now Avoid the Suez Canal** | 35 | `+10 DAYS` | why are ships avoiding suez |
| 4 | **China's Real Weapon Isn't Tariffs** | 34 | `90% OF REFINING` | china rare earth export controls |
| 5 | **How Taiwan Got 90% of the World's Chips** | 41 | `ONE ISLAND` | why does taiwan make all the chips |
| 6 | **The Bubble That Built Real Railways** | 36 | `REAL — AND A BUBBLE` | railway mania 1840s |
| 7 | **What Happens When the AI Money Stops** | 37 | `WHEN CAPEX STOPS` | ai capex spending economy |
| 8 | **How the Dollar Became a Weapon** | 30 | `THE DOLLAR WEAPON` | dollar weaponization sanctions |
| 9 | **The Dollar Has Been Dying for 50 Years** | 39 | `STILL NOT DEAD` | de-dollarization explained |
| 10 | **Why Tariffs Never Work** | 22 | `BUT THEY ALWAYS RETURN` | do tariffs actually work |
| 11 | **Recessions Are Declared Too Late** | 33 | `YOU FIND OUT LAST` | how is a recession declared |
| 12 | **Why Chip Factories Keep Failing** | 32 | `$20B. STILL FAILS.` | semiconductor industrial policy |

Every title now fits in the visible field. Every thumbnail adds information rather than repeating.

### How title and thumbnail combine

- Title: *Is AI a Bubble? Ask the Railways* → Thumbnail: `IS AI NEXT?` over an 1840s railway share certificate beside an AI capex chart
- Title: *China's Real Weapon Isn't Tariffs* → Thumbnail: `90% OF REFINING` over a rare-earth production-share chart
- Title: *Why Ships Now Avoid the Suez Canal* → Thumbnail: `+10 DAYS` over a map with the Cape of Good Hope route in amber

The pattern: **title asks or claims, thumbnail delivers the number.** Consistent, fast to produce, and instantly recognisable in a feed.

---

## 3. Thumbnail layout spec

One template. Build it once in Figma.

```
┌──────────────────────────────────────────────┐
│                              │               │
│                              │  THUMBNAIL    │
│      VISUAL ZONE             │  TEXT         │
│      (chart / map /          │  2–3 words    │
│       archival image)        │  serif, large │
│      ~60% width              │  ~40% width   │
│                              │               │
│  [one amber accent element]  │               │
└──────────────────────────────────────────────┘
1280 × 720 px · under 2 MB
```

| Element | Spec |
|---|---|
| Text | Serif (Instrument Serif / Playfair). Paper `#F4F1EA` on ink navy `#1B2A4A`, or reverse |
| Text size | Large enough to read at 128×72 px. Test by zooming out, not by squinting |
| Accent | Exactly **one** amber `#D99A2B` element — the thing the eye lands on |
| Visual zone | A real chart, real map, or real archival image. Never AI-generated, never a stock businessman |
| Never | Red arrows, circles, shocked expressions, more than 4 words, two accent colours |

**Two checks before upload:**

1. **Feed test** — place it beside three competitor thumbnails at feed size. Does yours read fastest?
2. **TV test** — view at ten feet. YouTube reports over a billion hours of daily TV watch time, and long-form explainer is exactly what that surface serves.

---

## 4. Which backlog topics are actually searchable

Honest triage of the 34-title backlog. This matters for sequencing.

| Searchability | Topics | When to publish |
|---|---|---|
| **High search intent** — people type these | AI bubble · rare earths China · Taiwan chips · Suez shipping · do tariffs work · de-dollarization · how recessions are declared · shipping containers · 1973 oil shock · Hormuz · do sanctions work | **Videos 1–15** |
| **Medium** — searched, but less | Bretton Woods · currency pegs · why big projects run late · chip fab costs · undersea cables · Panama Canal water | Videos 15–25 |
| **Low search, browse-dependent** | Netherlands logistics · Germany's industrial model · why poor countries stay poor next to rich ones · who owns the sea · why cities flood · the cartel that sets prices · why empires go broke | **Videos 25+, after an audience exists** |

**The mistake to avoid:** publishing a low-search browse-dependent video early. It will get 40 views, and you'll conclude the topic was wrong when the real problem was that nobody was searching and the algorithm had no audience to suggest it to.

---

## 5. Title-writing rules

For every future video.

**Do**

- 30–50 characters
- Front-load the searchable noun — *"Suez"*, *"rare earths"*, *"AI bubble"*
- Question or claim, never a topic label. *"Why Tariffs Never Work"* beats *"Tariffs Explained"*
- Include the number when the number *is* the story — *"90% of the World's Chips"*
- Write the title **before** the script. If you can't write a good title, the video idea isn't sharp yet

**Don't**

- No colons stacking two ideas — *"Tariffs: A History of Failure and What It Means Now"*
- No "…and here's why" tails. They eat 15 characters and add nothing
- No ALL CAPS words
- No clickbait you don't deliver on. One broken promise costs more than ten weak titles
- Don't repeat the thumbnail text in the title — wasted surface

**Test:** would you click it if it appeared in your own feed with no channel name attached? If not, rewrite.

---

## 5b. ⚠️ SEARCH VALIDATION — measured 2026-09-13. Read this before anything else in this file.

**§2's table above is stale.** It is the pre-`22` geopolitics slate — Suez, Taiwan, chokepoints, dollar, tariffs. The revised publish order (`22_NICHE-BUSINESS-ALIGNMENT.md` §3, mirrored in README) moved all of those to video 15+. **Only 4 of the 12 rows survive into the actual first ten**, and six of the real first ten have no search phrase defined anywhere.

### Method, and its limits

Google Trends, **region India, property YouTube Search, past 12 months.** Two comparison batches, each anchored on "ai bubble" so the batches can be rescaled against each other. vidIQ was not used — it needs an account.

**What this does not tell us:** absolute volume. Trends is a relative index, values are rounded integers, and a reported `0` means *below the reporting threshold*, not zero. Rescaling across batches via the anchor is approximate. Treat everything below as order-of-magnitude, not measurement.

### Measured, rescaled to `ai bubble = 100`

| Term | Index | Read |
|---|---|---|
| credit score | **~870** | Dominant — and unusable, see below |
| freelancing | **~725** | Large and serveable |
| recession | ~83 | Comparable to ai bubble |
| gig economy | ~25 | Thin |
| future of work | ~11 | Effectively nothing |
| ai job loss | **~0** | Below threshold |
| tech layoffs | **~0** | Below threshold |
| economic bubble | ~0 | Below threshold |

Raw batch figures, for the record — batch 1: credit score 78 · ai bubble 9 · future of work 1 · ai job loss 0 · tech layoffs 0. Batch 2: freelancing 87 · ai bubble 12 · recession 10 · gig economy 3 · economic bubble 0.

### Three findings

**1. The highest-volume term has an intent mismatch — not a compliance problem.**

> **Correction, same day.** This finding originally claimed credit-score content was out of scope on compliance grounds. **That was wrong, and it misread `CLAUDE.md`.** The exclusion is on finance *advice and recommendation*, not finance *education*. "Who decides your credit score and how the scoring system came to work this way" is education and mechanism — squarely in scope, and it is exactly what hard rule 5 describes: offer a pattern to notice, never an action to take. Financial education is not the restricted activity; personalised recommendation is.

What survives is a **distribution** argument. YouTube search in India for credit score is owned by *"How to Increase CIBIL Score Fast"* — people with transactional intent who want their score fixed. An explainer on who designed the system is a different product and will not win that query, however large it is. **High volume, wrong intent.** Video 9 is publishable; it just cannot expect to capture that search demand.

**2. The AI-jobs framing has no YouTube search demand in India.** "ai job loss" and "tech layoffs" both sit below the reporting threshold; "future of work" is ~11. Videos **2, 3, 4, 5 and 10 of the revised order** — the ones carrying the new niche — are aimed at phrases essentially nobody types into YouTube in India.

**3. Video 1 is the best-validated pick in the slate, by luck.** "ai bubble" has modest but genuine demand, and — checked directly on YouTube — real recent performance: *The AI Bubble Explained Like You're 5* at 438k views (9 months), *Why Everyone Wants You To Believe AI is a Bubble* at 51k views (8 days). Competitive, alive, and currently served by **global English channels, not Indian ones.** Keep it at video 1.

### The strategy contradiction this exposes

§1 above argues: a 21-subscriber channel gets no browse distribution, therefore videos 1–10 live or die on search, therefore use search-led titles. **The premise now fails.** If the topics themselves have near-zero search demand, search-led titles cannot rescue them — you would be optimising phrasing for queries that don't exist.

Only two honest ways out, and they are a real choice:

- **Change the topics** to where measured demand overlaps what ThinkLate covers. On this data the largest serveable pocket is **independent/freelance work** (~725 index) — served as mechanism and history, not as "how to freelance" advice. **Caveat added after review:** this is an *audience* argument only. Sarwan is not building a freelancing career — the venture is product-first, then an ad agency / digital company. Whether the channel should still serve independent knowledge workers is now an open question, not a settled one (see below)
- **Change the distribution assumption** — accept that the work/pay topics reach people through browse and suggested rather than search, which means curiosity titles from video 2, not from video 15

**Unresolved. Do not script videos 2+ until this is decided.** Video 1 is unaffected either way.

### Still unmeasured

- Third batch (railway mania, salary, layoffs, productivity) — **Trends rate-limited before it returned.** Re-run it
- Nothing checked against vidIQ or absolute volume
- No Hinglish-phrase testing. Narration is Hinglish but packaging is English, so English phrasing is the right thing to validate — but Indian viewers searching Hinglish topics in Hindi transliteration is untested, and the CIBIL result above ("credit score kaise badhaye") suggests that pattern is real and large

---

## 6. Before video 1

- [x] ~~Check the top 3 search phrases in Google Trends~~ — **done 2026-09-13, see §5b.** Result: the slate is worse-validated than assumed. vidIQ still unchecked (needs an account)
- [ ] Build the single thumbnail template in Figma
- [ ] Write titles and thumbnail text for videos 1–3 **before** scripting any of them
- [ ] Run the feed test against three real competitors
