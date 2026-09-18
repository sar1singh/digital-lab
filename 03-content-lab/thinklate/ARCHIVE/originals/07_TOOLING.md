# ThinkLate — Tooling Stack & Budget

**Date:** 2026-09-13
**Constraint:** under ₹5L for 12 months, solo, ~10–15 hrs/week

---

## Headline finding

**You already own the expensive parts.** DaVinci Resolve, Affinity and Audacity cover editing, graphics and audio — that's the bulk of what a channel like this needs, and Resolve free is genuinely professional-grade.

**Your realistic year-1 spend is ₹15,000–50,000, not ₹5L.** Budget is not your constraint. Time is. So the right question isn't "what should I buy" — it's "what buys back hours."

---

## 1. TubeBuddy vs vidIQ — direct answer

**Use vidIQ's free tier. Buy neither, yet.**

Reasoning specific to your situation, which is 0 published videos and no traffic:

| | TubeBuddy strengths | Useful to you now? |
|---|---|---|
| A/B thumbnail testing | Its best feature | **No** — A/B testing needs meaningful traffic to produce a signal. With 40 views a test tells you nothing |
| Bulk tag/description edits across a library | Genuinely good | **No** — you have no library |
| Lower paid entry price | Real | Irrelevant until you're paying |

| | vidIQ strengths | Useful to you now? |
|---|---|---|
| Keyword research and scores | Core | **Yes** — this is exactly the gap flagged in the titles doc |
| Competitor and outlier research | Core | **Yes** — find which of your 34 topics are actually working for others |
| Trend discovery, idea generation | Good | Yes, moderately |
| Real-time analytics | Good | Not yet |

**So:** vidIQ free tier does the one job you need right now — validating topics and titles before you commit 12 hours to a video. Pair it with **Google Trends** (free, and better for long-run interest curves).

**Revisit at video 12:** if thumbnails are your bottleneck and you have real traffic, TubeBuddy's A/B testing becomes the better buy. Not before.

**Pricing caution:** figures circulating in 2026 put TubeBuddy Pro around $3.60/mo and Legend around $23–27/mo (annual), and vidIQ Boost around $17/mo (annual). **These come mostly from vendor and affiliate pages — verify on the actual sites before paying.** Sources: [vidIQ comparison](https://vidiq.com/compare/vidiq-vs-tubebuddy/) · [TubeBuddy comparison](https://www.tubebuddy.com/blog/tubebuddy-vs-vidiq/) · [OutlierKit](https://outlierkit.com/resources/vidiq-vs-tubebuddy/) · [LinoDash](https://linodash.com/vidiq-vs-tubebuddy/)

---

## 2. What you already have, and how to use it properly

| Tool | Use it for | Note |
|---|---|---|
| **DaVinci Resolve (free)** | Edit, motion graphics (Fusion), colour, **and audio (Fairlight)** | Also has built-in subtitle generation and Voice Isolation. Most people don't realise the free version includes all of this |
| **Affinity (free)** | Thumbnails, title cards, chapter cards, all templates | Affinity Designer for vector, Photo for raster. Build your template file here or in Figma |
| **Audacity** | Quick audio cleanup | Honestly — **use Resolve's Fairlight instead** for anything synced to video. Keep Audacity for standalone recording only |

**Resolve features worth learning specifically (in this order):**

1. **Fusion titles** — build your title/chapter/quote/kicker cards as reusable Fusion templates. Then it's text swaps forever
2. **Voice Isolation** (Fairlight) — removes room noise. Reduces the need for acoustic treatment
3. **Subtitle generation** — then correct manually. Never ship auto-subs uncorrected
4. **Render presets** — save one YouTube preset, never think about export settings again

---

## 3. The genuine gaps

### Charts — your biggest visual load

| Tool | Cost | Use |
|---|---|---|
| **Flourish** | Free tier | **Animated** charts. Best-looking output for least effort. Start here |
| **Datawrapper** | Free tier | Publication-quality static charts and choropleth maps |
| **Your own code pipeline** | Free | **The real answer.** See asset doc §2 — CSV in, branded SVG/PNG out. This is your unfair advantage |
| Google Sheets / Excel | Free | Fine for quick exploration, not for on-screen output |

### Maps

| Tool | Cost |
|---|---|
| **MapChart.net** | Free — fast country-highlight maps |
| **Datawrapper** | Free tier — choropleths and symbol maps |
| **Natural Earth** | Free, public-domain vector map data. Use with your own pipeline for full brand control |

### Research and notes

| Tool | Cost | Use |
|---|---|---|
| **NotebookLM** | Free | Synthesis over documents **you** supply, with citations back to them. Not a fact source |
| **Obsidian** or **Notion** | Free tiers | Topic backlog, per-video research notes, source library. Pick one and stop evaluating |
| **Zotero** | Free | If you want proper source management. Optional |
| **Google Trends** | Free | Long-run interest curves. Better than any paid tool for "is this durable" |

### Recording and audio

| Tool | Cost |
|---|---|
| **OBS Studio** | Free — screen recording for document scroll-throughs. Essential for your visual style |
| **Adobe Podcast Enhance** | Free tier — one-click voice cleanup. Genuinely good; use if Resolve's Voice Isolation isn't enough |
| **Whisper** (local) | Free — you're a dev, run it locally for accurate transcripts and subtitles |
| **YouTube Audio Library** | Free — music and SFX, cleared for monetisation |
| **Epidemic Sound / Artlist** | ~₹800–1,200/mo — only if free library music becomes limiting. Not year 1 |

### Newsletter

| Tool | Cost |
|---|---|
| **beehiiv** or **Substack** | Free tiers | Start free from video 1. Don't over-research this — pick one in week 1 and move |

---

## 4. Hardware

**Covered — Fifine USB mic already owned. No hardware spend required.**

Audio matters more than visuals for retention: viewers forgive mediocre visuals and leave on bad audio. Since the mic is fixed, the remaining gains are free and come from technique and room.

| Action | Cost |
|---|---|
| Record in a soft-furnished room. Duvet or heavy curtain behind you. Never bare walls, never near glass | ₹0 |
| Mic ~15 cm from mouth, speaking slightly off-axis to reduce plosives | ₹0 |
| Resolve **Fairlight → Voice Isolation** on every track | ₹0 |
| Adobe Podcast Enhance free tier if Voice Isolation isn't enough | ₹0 |
| Keep the mic off the desk surface, or on a folded towel, to stop vibration transfer | ₹0 |

Most Fifine USB models are condensers, which pick up more room reflection than a dynamic mic — so room choice does more work for you than it would otherwise. Test one 60-second read in two different rooms and keep the better one.

**Skip entirely:** camera, lighting, green screen, capture card, audio interface, second microphone.

---

## 5. Year-1 budget

| Item | Cost |
|---|---|
| All software above (free tiers) | **₹0** |
| Hardware | **₹0** — mic already owned |
| thinklate.com | ~₹0 year 1, ~₹1,500/yr after |
| Logo (designer, vector set) | ₹1,500–3,000 one-time |
| Newsletter | ₹0 (free tier until ~1,000 subscribers) |
| **Year-1 core total** | **₹1,500–4,500** |
| *Optional, only if justified by data* | |
| vidIQ or TubeBuddy paid | ~₹18,000/yr |
| Music library | ~₹12,000/yr |
| **Realistic ceiling** | **~₹35,000** |

Under 1% of budget at the core level, under 10% at the ceiling.

> **Money is not the constraint. Hours are.** Judge every tool on hours saved, not rupees spent. The chart pipeline (§3) is the highest-value item available and costs one weekend.

---

## 6. Decide these in week 1

- [ ] vidIQ free tier — install the browser extension
- [ ] Flourish + Datawrapper accounts
- [ ] Obsidian **or** Notion — pick one, don't compare
- [ ] beehiiv **or** Substack — pick one, don't compare
- [ ] NotebookLM
- [ ] OBS Studio
- [ ] Test the Fifine in two rooms, 60-second read each, keep the better room
- [ ] Watch two Resolve tutorials: Fusion titles, and Fairlight Voice Isolation

No new tool gets added until a specific video is blocked without it.

---

## 7. Not worth it for you

| Tool | Why not |
|---|---|
| Premiere Pro / Final Cut | Resolve free is sufficient and you already have it |
| Canva Pro | Affinity covers it |
| AI video generators (Runway, Kling, Veo) | Fabricated visuals destroy a credibility channel and risk monetisation under YouTube's July 2026 policy |
| AI voice (ElevenLabs etc.) | Use your own voice — see strategy doc §7 |
| Faceless-channel automation suites | Built to mass-produce exactly the content YouTube is now demonetising |
| Thumbnail A/B tools | No traffic to test against yet. Revisit at video 12 |
| Stock footage subscriptions | Your style is charts and documents. Free libraries cover the texture you need |
| Paid analytics beyond vidIQ | YouTube Studio's own analytics are better than people assume, and free |
