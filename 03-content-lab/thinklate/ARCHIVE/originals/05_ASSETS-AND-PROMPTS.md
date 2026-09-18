# ThinkLate — Asset Pipeline, Sources & Prompt Library

**Date:** 2026-09-13
**Problem this solves:** asset gathering is the stated reason previous attempts died. Hunting a unique visual per line of dialogue is unsustainable at 10–15 hrs/week.

---

## 1. The actual fix — reframe the problem

You are trying to source a unique asset per scene. **That is the wrong goal.** It is also why you burned out.

The fix is not better stock hunting. It is **reducing the number of unique assets a video needs.**

> **A 20-minute video needs about 12–18 distinct visual states, not 200.** Each one holds for 45–90 seconds while the narration does the work.

Long-form explainer viewers tolerate — and actually prefer — a chart they can read for 60 seconds over a cut every 3 seconds. Rapid cutting is a short-form grammar. Applying it to long-form costs you enormous production time and *reduces* comprehension.

### The frame-type library

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

## 2. Your unfair advantage — script the charts

You are a Node/JS engineer. Most creators in this niche are not. **This is the single highest-leverage thing in this document.**

Build a small chart-generation pipeline once:

- Input: a CSV or JSON
- Output: a PNG or SVG in ThinkLate's palette (`#1B2A4A` / `#F4F1EA` / `#D99A2B`), correct fonts, source line baked into the corner
  *(hex updated 2026-09-13 — the palette unified on `#1B2A4A`; `#111827` is retired, see `02_BRAND.md` PALETTE ARCHITECTURE)*
- Stack: Python + matplotlib, or Node + D3 / Chart.js / Observable Plot. Either is fine — use what you're faster in

**What this buys you:** chart production drops from ~20 minutes of manual formatting to seconds, every chart is automatically on-brand, and adding an animated reveal is a render setting rather than a design task. This converts your biggest bottleneck into your biggest speed advantage.

Build it in week 2, before video 1. It pays back by video 3.

---

## 3. Sources

**Licensing warning:** "public domain archive" does not mean every item in it is public domain. **Check the rights statement on each individual item.** Assume nothing from the platform's name.

### Data — for charts (this is most of your visual load)

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

### Chart and map tools

| Tool | Use |
|---|---|
| **Flourish** | Animated charts, free tier. Best-looking output for video with least effort |
| **Datawrapper** | Publication-quality static charts and choropleth maps, free tier |
| **MapChart.net** | Fast custom country-highlight maps |
| **Natural Earth** | Public-domain vector map data — build your own base maps |
| **Your own pipeline** | See §2. Long-term answer |

### Archival images and film

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

### Stock footage — use sparingly

| Source | Cost |
|---|---|
| Pexels, Pixabay, Coverr, Mixkit, Videvo | Free. Generic — use for texture only, never as the subject |
| Storyblocks, Artgrid, Pond5 | Paid. Only if a specific shot is genuinely required |
| AP Archive, British Pathé | Licensed newsreel. Real cost; watermarked previews free for planning |

**Rule: stock footage is texture, never evidence.** If a shot is carrying an argument, it needs to be a real document, a real chart, or a real archival image.

---

## 4. AI — where it helps and where it will damage you

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

### Why this line matters more for you than for others

Your entire product is trustworthiness. A channel that shows real filings, real charts and real archive photos, and says where each came from, is doing the exact thing AI content farms cannot. **Fabricated visuals would throw away your only moat** — and under the July 2026 policy, they also threaten monetisation.

---

## 5. Prompt library

### 5a. Research prompts — the ones that actually matter

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

### 5b. Image prompts — only for abstract, non-representational assets

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

## 6. Per-video asset budget

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

### Working order

1. **Script locked first.** Never source assets before the script is final
2. Read the script and mark asset cues in the margin
3. Group cues by frame type — all charts together, all archive together
4. Source in batches by type, not in script order
5. Assemble

Batching by type rather than timeline position is what halves the time.

---

## 7. Completed topic backlog — 34 titles

### Published slate (see content-slate doc for detail)
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

### Backlog
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

## 8. Week 2 build list

Before video 1, build these once. They are the entire difference between a sustainable channel and another abandoned one.

- [ ] Chart generation pipeline (§2) — **highest priority**
- [ ] Figma/Canva file: title card, chapter card, quote card, kicker number card, comparison table, timeline, source strip, lower third
- [ ] 3 abstract background loops (§5b prompts)
- [ ] Colour and type styles saved as reusable styles
- [ ] Bookmark folder for every source in §3
- [ ] A blank asset-cue sheet to fill per script

Total: one weekend. Then never do it again.
