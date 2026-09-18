# ThinkLate — Brand Identity & Channel Setup Spec

**Date:** 2026-09-13
**Companion to:** `01_STRATEGY.md`
**Purpose:** everything needed to make the channel look like an established operation before video 1 exists

---

## 1. Niche classification

| Field | Value |
|---|---|
| Niche | **How work, money and power actually function — and how that reaches your working life.** Economics, geopolitics and technology through hindsight. Narrowed per `22_NICHE-BUSINESS-ALIGNMENT.md` |
| YouTube category | **Education** |
| Why not News & Politics | News & Politics suppresses evergreen recommendation, attracts volatile audiences, and is a weaker sponsor category. Education is the right shelf for content designed to earn for years |
| Sub-shelf | Business & economics explainer / infotainment |
| Audience | **Indian knowledge workers, 22–40** — those considering independence and those already independent serving global clients. Urban/Tier-1+2, English-literate, Hinglish-speaking |
| Language | **Hinglish narration, English packaging** — titles, thumbnails, metadata, subtitles in English (`24_LANGUAGE-REVERSAL.md`) |
| Sponsor-facing line | *Long-form hindsight analysis of work, money and power — and how they reach individual lives — for Indian knowledge workers going independent* |

---

## 2. Design direction

The visual identity has one job: **signal "researched" before a single word is read.** Everything below serves that.

**Concept:** dusk, archive, owl. Hegel's owl of Minerva takes flight at dusk — understanding arrives only after events have played out. That is literally the channel thesis, and it gives you a coherent visual world for free.

**Reject:** neon/tech gradients (reads AI-slop), red news-alert palettes (reads commentary), bright saturated colour (reads entertainment), 3D glossy logos (reads 2015).

### Colour palette

| Role | Colour | Hex | Use |
|---|---|---|---|
| Base | Ink navy | `#111827` | Backgrounds, dark frames |
| Paper | Warm off-white | `#F4F1EA` | Chart backgrounds, text on dark |
| Accent | Amber / ochre | `#D99A2B` | Owl eyes, highlights, the one number that matters in a chart |
| Support | Slate grey | `#6B7280` | Secondary chart lines, captions, sources |
| Alert (sparingly) | Muted brick | `#9B3A2F` | Negative values only. Never for emphasis |

Rule: **one accent per frame.** If everything is highlighted, nothing is.

### Typography

| Role | Typeface | Notes |
|---|---|---|
| Headlines, thumbnails | A high-contrast serif — *Instrument Serif*, *Playfair Display*, or *Libre Baskerville* | Serif = authority and archive. Free on Google Fonts |
| Data, chart labels, UI | *IBM Plex Sans* or *Inter* | Built for data legibility. Free |
| Numbers in charts | *IBM Plex Mono* | Monospace aligns columns |

Two families maximum. Three is amateur.

---

## 3. Logo and avatar

**Concept: the owl of Minerva — the owl head alone.** The "hindsight" signboard was specified here earlier and has been **removed** (see `08_DESIGN-SPEC-FOR-GENAI.md` §6). Text inside a mark is illegible at avatar size, duplicates what "ThinkLate" already means, and reads amateur. "Hindsight" lives in the tagline instead.

| Version | Use | Spec |
|---|---|---|
| **Full logo (lockup)** | Banner, website, end card, sponsor decks | Owl head + wordmark "ThinkLate" set beside it. **No signboard** |
| **Avatar mark** | Profile picture, watermark | **Owl head only.** No text of any kind |

**Why no text in the mark:** the profile picture renders at roughly 98×98 px on desktop and 32–48 px in comment threads and search. Any word inside the artwork becomes a smudge at that size. An owl head with amber eyes on ink navy reads instantly at any size — verified at 32 px in `brand/_assets_sheet.png`.

**Specs**

- Upload profile picture at **800×800 px**, PNG. It renders as a circle — keep content inside a centre-safe circle
- Test it at 32 px. If you can't tell what it is, simplify further
- One-colour version needed for light backgrounds and merch later

**Honest note on AI for the logo:** image generators are weak at clean vector logos, and worse at logos containing text — you'll get warped letters and inconsistent line weight. Use AI to explore *concepts*, then either build the final in Figma yourself or pay a designer ₹1,500–3,000 on Fiverr/Upwork for a proper vector set. This is the one place where ₹2,000 beats free.

---

## 4. Banner

| Spec | Value |
|---|---|
| Upload size | **2560 × 1440 px** recommended (min 2048 × 1152), 16:9, under 6 MB. See §12 |
| Safe area (visible on all devices, incl. mobile) | **1235 × 338 px**, centred |
| Rule | Every critical element — logo, wordmark, tagline, cadence — inside the safe area. Everything outside is decoration that most viewers never see |

**No shadows, borders or frames on the banner file** (YouTube's own guidance).

**Content, in the safe area:**

- Wordmark: **ThinkLate**
- Tagline: *Master of none, expert of after*
- One line of positioning: *Work · Money · Power — explained in hindsight*
- Cadence: *New video every two weeks*

**Outside the safe area:** ink navy field, faint archival texture, or a muted map/chart motif at low opacity. Nothing that needs to be read.

Do not put your face, a collage of thumbnails, or a "subscribe" arrow on it. All three read amateur.

---

## 5. Channel description (paste-ready)

> **SUPERSEDED 2026-09-13.** Sarwan chose the `brand/BRANDING-SESSION.md` draft instead — plainer searchable first line, one dry second line, no competing taglines. **The canonical description lives in the export paste-sheet.** The version below is kept as the record of what was rejected: two taglines is one too many, and "Why did it turn out this way" wastes the highest-value search line on a question nobody types.

First two lines are what shows above "…more". Front-load topic words for search.

```
Why did it turn out this way — and why does it show up in your life?

ThinkLate takes documented history in economics, geopolitics and technology,
traces the pattern, and follows it down to the things you actually notice:
your pay, your job, your choices, the sense that something changed.

Every video shows the chain link by link — and says plainly which links are
documented and which are inference.

Hinglish narration. English charts, sources and subtitles.

Master of none, expert of after.
Thinks late, explains straight.

New video every two weeks.
Newsletter: [link]
```

**Do not include** (from the old description): *"pseudo intellectual"* — your product is credibility, and sponsors read this field. *"Universe's beta tester / crashing since spawn"* — signals nothing about the content and hurts discovery.

---

## 6. Channel layout

Set under Customisation → Layout in YouTube Studio.

| Slot | What to use |
|---|---|
| Channel trailer (non-subscribers) | **Leave empty until video 3.** A trailer promising content that doesn't exist is worse than no trailer. From video 3, use your best-performing video, not a purpose-made trailer |
| Featured video (returning subscribers) | Latest upload |
| Section 1 | **Videos** (most recent) |
| Section 2 | *Start Here* — a playlist of your 3 best, hand-picked |
| Section 3 | The lead pillar playlist, e.g. *Bubbles & Manias* |
| Later sections | One playlist per recurring series, added as the library grows |

**Playlists from day one.** Even with 3 videos. Playlists drive session watch time, which drives everything else — and they make a new channel look intentional rather than empty.

**Links:** newsletter first, then X, then Instagram. Newsletter is the asset you own; put it above the platforms you rent.

---

## 7. Thumbnail system

Build **one template** and reuse it. Consistency is what makes a channel recognisable in a feed.

| Spec | Value |
|---|---|
| Size | 1280 × 720 px, under 2 MB |
| Layout | Left ~60% = subject image or chart. Right ~40% = **2–3 word** text block |
| Text | Serif, ink navy on paper OR paper on ink navy. **2–3 words; 4 is the ceiling** (see `12_CRAFT-EVIDENCE.md`). **Must be legible at 10% scale** |
| Accent | Exactly one amber element per thumbnail. **High contrast is mandatory, not stylistic** — it substitutes for the face you're not using (69% of breakout thumbnails use a face; see `12_CRAFT-EVIDENCE.md` §2) |
| Never | Red arrows, circles, shocked expressions, more than 4 words, two accent colours |

**Design for TV.** YouTube reports over a billion hours of daily watch time on TV screens, and long-form explainer content is what that surface rewards. Check every thumbnail at ten feet.

**Test:** put your thumbnail beside three competitors' at feed size. If yours doesn't read fastest, redo it.

---

## 8. SEO and metadata — what actually matters

Honest framing first, because most "YouTube SEO" advice is theatre:

- **Video tags have close to no ranking effect.** Fill them in, spend two minutes, move on
- **Channel keywords** (Studio → Settings → Channel → Basic info) have minor effect. Fill once
- **What actually drives distribution:** title, thumbnail, first 30 seconds of retention, and average view duration. In that order. Nothing else is close

**Channel keywords (set once):**

**REVISED 2026-09-13.** The previous list — *tariffs explained, supply chains, global trade, geopolitics explained* — was written for the pre-`22` niche and pointed at geopolitics viewers. Per `22_NICHE-BUSINESS-ALIGNMENT.md` the subject narrowed to work, money and economic life, and none of the first ten videos is about trade or tariffs. Keywords now follow what actually gets published. Chokepoints and trade return to this list around video 15 if that backlog ships.

```
economics explained, economic history, why your pay stopped rising,
wages vs productivity, is AI a bubble, AI job losses, future of work,
knowledge work, freelance economy, independent work, tech layoffs explained,
capex cycle, asset bubbles explained, credit scoring, algorithmic decisions,
recession explained, documentary explainer, hindsight analysis
```

**Not yet validated.** These are aligned to the slate, not to measured search volume — that is README step 9, Google Trends plus the vidIQ free tier. Treat the ordering as a guess until then. Channel keywords have minor ranking effect anyway, so do not spend a second weekend on this.

**Video description template:**
```
[2–3 sentence summary containing the main search phrase naturally]

Chapters:
00:00 The question
0X:XX [section]
...

Sources:
- [Name, publication, date] — [URL]
- ...

Newsletter: [link]
X: x.com/wethinklate
Instagram: instagram.com/wethinklate

#economics #geopolitics #economichistory
```

**The Sources block is not optional.** It is your single strongest differentiator against AI-generated competitors, it is what sponsors check, and it is what makes a viewer trust video two.

**Subtitles:** upload accurate English subtitles for every video. Not auto-generated. They help search, accessibility, and non-native viewers — and they materially reduce accent friction.

---

## 9. Intro and outro

- **No intro animation for the first 10 videos.** Half of all viewers leave in the first 90 seconds. Do not spend three of those seconds on a logo sting
- Open with the question. Context comes after the viewer commits
- A 1-second wordmark card is acceptable *after* the hook, around 0:30, once you have one
- **Outro:** 15 seconds max — one line of conclusion, newsletter call to action, two end-screen elements (subscribe + next video). Nothing else

---

## 10. Where AI helps, and where it doesn't

| Task | Verdict |
|---|---|
| Logo concept exploration | Useful |
| Final logo vector | **Weak.** Warped text, inconsistent line weights. Pay a designer ₹1,500–3,000 |
| Banner composition | Workable in Canva/Figma with AI assist |
| Thumbnail generation per video | **Don't.** Build one template, swap the content. Consistency > novelty |
| Palette and font pairing | Useful for exploration; specifications above already decided |
| Research synthesis | Useful — feed it *your* real documents (NotebookLM). Never let it supply a fact you haven't seen in a source you opened |
| Chart generation from verified data | Useful and recommended |
| AI-generated illustrative images | **Avoid.** Slop signal under YouTube's July 2026 inauthentic-content policy |
| Script drafting | Useful for structure. The pattern and the argument must be yours — that's the product |
| Voiceover | **Use your own voice.** See strategy doc §7 |

---

## 11. Pre-launch checklist

Order matters. Everything here is achievable in two weekends.

**Weekend 1 — identity**
- [ ] Display name → **ThinkLate** (capitalised)
- [ ] Handle → @wethinklate; claim on X and Instagram
- [ ] Commission or build logo (full + avatar mark)
- [ ] Upload profile picture (800×800, owl head only)
- [ ] Upload banner (**2560×1440**, content inside 1235×338, no borders/shadows)
- [ ] Paste new channel description
- [ ] Set channel keywords
- [ ] Category → Education
- [ ] Add newsletter + social links
- [ ] Delete or unlist the old @eddythinklate video

**Weekend 2 — production system**
- [ ] Figma/Canva file: thumbnail template, chart template, title card, lower-third, end card
- [ ] Colour and font styles saved as reusable styles
- [ ] Create the 3 empty playlists
- [ ] Newsletter platform live with a landing page
- [ ] Record a 60-second voice test and listen back yourself
- [ ] Build the 30-title backlog

**Then publish. Do not iterate on branding again until video 12.**

---

## 12. Verified against YouTube's official documentation

Checked 2026-09-13 against [Manage your channel branding](https://support.google.com/youtube/answer/10456525) and [Manage your channel's profile](https://support.google.com/youtube/answer/2657964). Everything in this section is from YouTube's own spec, not third-party blogs.

### Corrections to the specs given earlier in this doc

| Item | Official spec | Change |
|---|---|---|
| **Banner** | Minimum upload **2048 × 1152** (16:9). Safe area for text and logos at that size: **1235 × 338**. **Recommended: 2560 × 1440, especially for TV.** Max file 6 MB | **Use 2560 × 1440, not 2048 × 1152.** You're explicitly designing for TV viewing — take the recommended size |
| Banner content | *"Do not include any additional file embellishments (e.g. shadows, borders, and frames)"* | New constraint — no borders or shadows on the banner file |
| **Profile picture** | JPG, GIF, BMP or PNG. **No animated GIFs.** Max 15 MB. Must render at **98 × 98 px** | 800 × 800 upload is still sensible; 98 × 98 is the render size to test against |

### Gaps — things missing from this doc entirely

**1. Video watermark — the significant miss**

A persistent subscribe button overlaid on your videos. Free, passive, and it has its own analytics.

- **Minimum 150 × 150 px, square, under 1 MB**
- Display options: **end of video** (last 15s), **custom start time**, or **entire video**
- Landscape only on computer and mobile; **not clickable on mobile**
- Not available on videos set as made for kids
- Conversions appear in the **Subscription source** report in Analytics
- Set at: Studio → Customisation → Profile → Video watermark

**Recommendation for ThinkLate:** the one-colour owl stamp at 150 × 150, cream on navy, with a rim so it survives light footage. Set to **"entire video"** — long-form viewers decide to subscribe mid-video, not at the end.

**Correction 2026-09-13: not "amber eyes".** Amber belongs to the in-video data palette; the character's only accent is the deep red tie (`ART-DIRECTION.md` §1). A second accent on the watermark also breaks the one-accent rule in `QC.md` 2.1. The watermark derives from `brand/stamp.png`, one colour, no accent at all.

**2. Contact info / business email**

A dedicated field under Studio → Customisation → Profile → Contact info, surfaced for business enquiries. **This is how sponsors reach you.** Given sponsorship is your main projected revenue line, leaving it empty is a direct cost. Use a dedicated address, not your personal one.

**3. Channel links — the cap and the prominence rule**

- Up to **14 links** on the Home tab
- **The first link is displayed prominently next to the subscribe button.** The rest are hidden behind a "see more" click

So the newsletter goes first — confirmed by the mechanism, not just instinct. X and Instagram after it.

**4. Name and handle change limits, and a real risk**

- Channel name: changeable **twice per 14 days**
- Handle: changeable **twice per 14 days**
- **Changing your channel name removes your verification badge**

You've already renamed once. Be deliberate about the "ThinkLate" capitalisation fix — you have limited changes in the window. The badge point is irrelevant now but matters later.

**5. Name and description translations**

Studio → Customisation → Profile → Add language. **Note: the Hindi-MLA-at-video-20–30 plan is dropped** — Hinglish is now the primary narration (`24_LANGUAGE-REVERSAL.md`). Translations only become relevant if a separate English property launches later.

### Not yet verified against official docs

Standard advice that appears in third-party checklists but which I have not confirmed against YouTube's documentation. Treat as unverified:

- Upload defaults — default description, category, visibility, licence, comment settings (Studio → Settings → Upload defaults). Worth setting regardless; it saves time per upload
- Country/region and currency settings
- Phone verification as a gate for custom thumbnails and longer uploads
- End screens and cards configuration

### Revised branding checklist — verified items marked ✓

- [ ] ✓ Display name → **ThinkLate** (capitalised). Note: 2 changes per 14 days
- [ ] ✓ Handle → @wethinklate. Note: 2 changes per 14 days
- [ ] ✓ Profile picture — owl head only, 800 × 800 upload, PNG, test legibility at 98 × 98
- [ ] ✓ Banner — **2560 × 1440**, critical content inside the 1235 × 338 safe area, under 6 MB, **no borders or shadows**
- [ ] ✓ **Video watermark — owl mark, 150 × 150, square, under 1 MB, set to "entire video"**
- [ ] ✓ Channel description with topic keywords in the first two lines
- [ ] ✓ **Contact info — dedicated business email for sponsor enquiries**
- [ ] ✓ Links — **newsletter first** (it gets the prominent slot), then X, then Instagram
- [ ] Category → Education
- [ ] Channel keywords set
- [ ] Upload defaults configured
- [ ] Country/region set
- [ ] Phone verification complete
- [ ] Playlists created (from day one, even with 3 videos)
- [ ] Channel trailer — **leave empty until video 3**
- [ ] End screen template built into the end card (both zones reserved)

---

## ART STYLE — LOCKED 2026-09-13

**Corrects a significant error.** Sections above specify a sober editorial ink/paper system. **Sarwan's actual published channel uses expressive warm character illustration, and it is better.** The existing avatar was never reviewed before those specs were written. This section overrides earlier palette and style guidance wherever they conflict.

### The character — the brand's core asset

| | |
|---|---|
| **Who** | An owl in **thick round charcoal glasses**, white shirt, deep red tie and dark brown blazer — a dry-witted office worker who has seen this all before. **The glasses are a defining feature: they carry the silhouette and make the avatar function as a logo** |
| **The expression IS the brand** | **Half-lidded, unimpressed, deadpan.** "I've seen this before and I'm not impressed." That single look is Sarwan's stated voice — friendly, direct, sarcastic, satirical — rendered in one image |
| **Render style** | **Modern high-quality Japanese anime.** Clean linework, smooth cel shading, crisp highlights, warm tans and creams. **Not flat vector. Not an enamel emblem. Not a geometric mark** |
| **Never** | Perfectly symmetrical, mask-like, flat two-tone, sober, or institutional. Eight rounds of that were rejected |

### Palette

| Role | Colour | Note |
|---|---|---|
| Character | Warm tans and browns | As published |
| Field | **Deep blue** — indigo `#1B2A4A` range | **Change from current:** the bright cyan clashes with a warm brown owl. Deepening it warms the character immediately |
| Accents | Red tie, amber | Already present, keep |
| Data graphics | Deep blue + cream + one amber | The chart system bridges to the character via the shared blue |

### Two registers, one brand

| Surface | Register |
|---|---|
| Avatar, banner, end card, in-video character | **Expressive character illustration.** Warm, personality-forward |
| Thumbnails | **High saturation, bold caps, energetic** — as already published |
| Charts, tables, data frames | **Clean and sober.** The contrast is deliberate: the host has personality, the evidence does not |

**This is not inconsistency.** The character carries voice; the data carries credibility. They are bridged by the deep blue and by using amber as the single accent in both.

### Avatar fix — no redesign needed

1. **Crop to the head.** The HINDSIGHT signboard consumes roughly 40% of the frame and is illegible below ~200 px. Cropping removes the only real defect and enlarges the eyes, which are the strongest element
2. **Deepen the background blue**
3. **Keep everything else.** The character is correct

### Rule for every future asset

**Match the published character.** Any new asset — expression, pose, thumbnail, end card — must be generated by describing *this* owl, not by re-inventing a mark. Consistency of character beats quality of any single image.

> **Prompts:** all branding prompts live in `brand/ART-DIRECTION.md` (canonical) and `brand/EXPRESSIONS.md`. `brand/PROMPTS.md` and `brand/BRIEF.md` are superseded.

---

## PALETTE ARCHITECTURE — read before using any colour

**There are two palettes in this folder, for two different jobs.** This was not stated clearly before and it reads as a contradiction. It is not.

| | Palette | Used for |
|---|---|---|
| **Brand / character** | Navy `#1B2A4A` field · warm tans and creams · charcoal frames · **deep red tie as sole accent** | Avatar, banner, watermark, the character in any form, thumbnail character cut-ins |
| **In-video graphics** | Ink `#111827` · paper `#F4F1EA` · amber `#D99A2B` · slate `#6B7280` · Instrument Serif / IBM Plex | Charts, tables, title cards, chapter cards, lower thirds, quote cards — everything produced by `templates/` |

**Why two:** the character is warm and expressive; the evidence is clean and sober. Deliberate contrast — *the host has personality, the data does not.*

### ✅ DECIDED 2026-09-13 — unified on `#1B2A4A`

**Option 1 taken.** `templates/brand.py` now sets `INK = #1B2A4A`. The brand owns one dark, shared between the character art and the data frames. Derived tokens re-derived: `INK_SOFT #24365C`, `GRID #2E4270`. All 13 preview SVGs re-rendered; no `#111827` remains in `templates/preview/`.

**One consequence, fixed in the same pass.** `SLATE` was `#6B7280` — 3.67:1 on the old dark, **2.94:1 on the new one. Failing WCAG AA (4.5:1) either way**, and it carries the captions and the source lines, which is the one place this channel cannot afford to be unreadable. Lightened to **`#98A2B3`, 5.52:1**. Verified contrast on the new `INK`: PAPER 12.61:1 · AMBER 5.83:1 · SLATE 5.52:1 · PAPER_DIM 5.62:1.

**`BRICK #9B3A2F` is 2.06:1 and still fails** — acceptable only because it is a chart fill for negative values, never text. Do not use it for type.

The tables above this line are retained as the record of the decision.

### ⚠️ Open decision — CLOSED, see above

**The two dark tones differ:** `#111827` (near-black blue-grey) vs `#1B2A4A` (true navy). **That is a real inconsistency, not a design.** Two options:

1. **Unify on `#1B2A4A`** — recommended. `#111827` is functionally greyscale, so the brand currently owns no colour. Requires editing `templates/brand.py` (one constant) and re-rendering the preview sheets
2. **Keep both** — accept that character art and data frames sit on different darks. Viewers are unlikely to notice across separate frames

**Undecided as of 2026-09-13. Pick one before producing video 1's graphics.**
