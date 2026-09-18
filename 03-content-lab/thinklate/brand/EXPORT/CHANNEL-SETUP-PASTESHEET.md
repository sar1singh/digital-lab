# ThinkLate — Channel Setup Paste-Sheet

**One sitting, top to bottom. Every value is decided — copy the blocks, don't rewrite them.**
Created 2026-09-13. Assets live beside this file in `brand/EXPORT/`.

## SCOPE — bare minimum, decided 2026-09-13

Sarwan's call: **ship the minimum that makes the channel not look abandoned, then stop.** Branding was eating time that belongs to content.

**In scope — four things:**

| # | Item | Status |
|---|---|---|
| 1 | Profile picture | ✅ done |
| 2 | Banner | ⏳ needs one Gemini render |
| 3 | Channel description | ✅ done, §A3 |
| 4 | Channel keywords + upload defaults | ✅ done, §D2 / §E |

**Deferred — not blocking anything, do not reopen until asked:**

- **Stamp and video watermark** (items 3–4 of the old checklist). The watermark is a passive subscribe nudge worth roughly nothing at zero subscribers. Revisit around video 5
- **Three expressions** (item 6) — needed for in-video cut-ins, so it belongs to the template phase, not channel setup
- **Thumbnail template** (item 8) — a production asset, not channel branding. Needed before video 1 publishes, not before the channel looks presentable
- **Business email / Contact info** — left blank. Matters at the first sponsor conversation, not now
- **Newsletter and social links** — left blank. Nothing to link to yet; beehiiv vs Substack stays open (README question 1)

**No cadence promise anywhere.** Removed from the description and the banner. The fortnightly target stays an internal commitment (`CLAUDE.md`) — publishing it just creates a public miss. Add it once the rhythm is real.

Every spec below was checked against YouTube's Help Centre on 2026-09-13, not from memory. Sources at the bottom.

---

## Section A — Studio → Customisation → Profile

### A1. Name

```
ThinkLate
```

**Capitalised, one word, no space.** You get **2 changes per 14 days** — don't burn one experimenting. Changing the name removes the verification badge (irrelevant now, matters later).

### A2. Handle

```
@wethinklate
```

Also **2 changes per 14 days.**

### A3. Description

**English, not Hinglish — decided.** Narration is Hinglish; packaging is English (`STRATEGY.md` → PART `24_LANGUAGE-REVERSAL`). This field is packaging, and it is also the field sponsors read.

The first two lines are all that shows above "…more" — they carry the search weight.

```
How work, money and power actually function — and how that reaches your working life.

Twenty years too late, but at least it's sourced.

Long-form explainers on economics, geopolitics and technology, traced from the decision that caused it down to the bill you pay. Every claim sourced. Every guess labelled as a guess.

Hinglish narration. English charts, sources and subtitles.
```

**Cadence line removed 2026-09-13.** No public schedule until the schedule is real.

**Chosen over the `BRAND.md` → PART `02_BRAND` §5 draft**, which opened on a question nobody types into search and ended on two competing taglines. That version is marked superseded in place.

**Do not reintroduce** from the old live description: *"pseudo intellectual"* — the product is credibility, and sponsors read this field. *"Universe's beta tester / crashing since spawn"* — signals nothing about the content and costs you discovery.

### A4. Links — SKIP for now

**Leave empty.** Nothing to link to yet. An empty links row is invisible; a link to a dead newsletter landing page is worse than no link.

**When you do come back:** the first link is displayed prominently beside the Subscribe button and the rest hide behind "see more" — so the newsletter takes slot 1 when it exists, then X, then Instagram. Cap is 14. Claim both handles before you need them (README action 2), because the names go regardless of whether you post.

### A5. Contact info — SKIP for now

**Leave empty.** This is how sponsors reach you, so it becomes a direct cost later — but there is nothing to sponsor at zero subscribers. Fill it at the first inbound conversation, with a dedicated address rather than your personal one, since the field is semi-public.

---

## Section B — Studio → Customisation → Branding

| Slot | File | Spec | Status |
|---|---|---|---|
| **Profile picture** | `01_DP_avatar_800.png` | PNG, ≤15 MB, renders at **98×98**. 800×800 upload is 8× render size — sharp on high-DPI | ✅ **READY** |
| **Banner** | `banner_2560x1440.png` | 2560×1440, 706 KB, no borders or shadows. **Text not set** — add it in Affinity per the spec below, then upload | ⚠️ **needs type set** |
| **Video watermark** | `stamp_800.png` banked | **DEFERRED**, but the stamp now exists — resize to 150×150 when you want it, set to "entire video" | ⏸ |

**Banner QC — 2026-09-13.** Character right, left field plain navy, mobile-safe box clean. Two defects found and repaired: **another four-pointed sparkle on the right lapel** (same failure as the avatar — the generator ignores that instruction consistently), and a **visible rectangular seam** where the character patch met the canvas. The seam is gone because the character was masked out of its background entirely and placed on flat `#1B2A4A` — which also removed the faint "atmosphere", no loss.

### Banner text — set in Affinity, do not let a generator do it

`ART-DIRECTION.md` rule 4: generators never set type. The production file ships text-free.

```
ThinkLate
Work · Money · Power — explained in hindsight
```

| | |
|---|---|
| Font | **Instrument Serif** (install it — the preview uses Lora as a stand-in because Instrument Serif isn't available to me) |
| Title | ~172 px, `#F4F1EA` |
| Tagline | ~38 px, `#98A2B3` |
| Text left edge | **x = 707** — that is 45 px inside the conservative 1235×338 box |
| Do not cross | **x = 1575.** The character begins there |
| Vertical | Title top ~y 591, tagline top ~y 803 |

**Why x=707 and not 563.** The first attempt placed text inside the *scaled* safe area (1544×423) and the "T" of ThinkLate was **clipped in the mobile crop**. The conservative 1235×338 centred box is the real constraint on phones. Use it.

`banner_2560x1440_PREVIEW-type.png` shows the intended composition with the stand-in font. **Do not upload the preview.**

### Banner text — three lines, set inside the safe area

Cut from four to three. `BRAND.md` → PART `02_BRAND` §4 specified wordmark + tagline + positioning + cadence, which with the character is five elements against `QC.md` 4.4's cap of three — and *"Master of none, expert of after"* and *"explained in hindsight"* are the same joke twice.

```
ThinkLate
Work · Money · Power — explained in hindsight
```

**Cadence line dropped** per the scope decision. The *"Master of none"* tagline survives where it already works — the in-video title card (`templates/preview/01_title.svg`).

**Banner safe-area note.** YouTube states the 1235×338 safe area **at the 2048×1152 minimum**. On a 2560×1440 canvas it scales to roughly **1544×423**. The folder's "text inside 1235×338" rule is therefore over-conservative rather than wrong — keep it if you want the margin, but you have more room for the wordmark than assumed.

**Do not upload `00_MASTER_avatar.png`.** That file is the identity anchor you attach to every future prompt. `01_DP_avatar_800.png` is the one that goes live.

---

## Section C — Studio → Customisation → Layout

| Slot | Value | Why |
|---|---|---|
| Channel trailer (non-subscribers) | **Leave empty until video 3** | A trailer promising content that doesn't exist is worse than no trailer. From video 3, use your best performer — don't make a purpose-built one |
| Featured video (returning subscribers) | Latest upload | |
| Section 1 | **Videos** (most recent) | |
| Section 2 | **Start Here** — playlist of your 3 best, hand-picked | |
| Section 3 | Lead pillar playlist | |

**Create the playlists on day one, even with three videos.** Playlists drive session watch time, and they make a new channel look intentional rather than empty.

Playlist names to create now:

```
Start Here
Bubbles & Manias
How Work Got This Way
```

---

## Section D — Studio → Settings → Channel → Basic info

### D1. Country of residence

```
India
```

### D2. Channel keywords

Comma-separated. **Minor ranking effect — fill once, spend two minutes, move on.**

```
economics explained, economic history, why your pay stopped rising, wages vs productivity, is AI a bubble, AI job losses, future of work, knowledge work, freelance economy, independent work, tech layoffs explained, capex cycle, asset bubbles explained, credit scoring, algorithmic decisions, recession explained, documentary explainer, hindsight analysis
```

**Revised 2026-09-13.** The old list pushed *tariffs, supply chains, global trade, geopolitics* — written for the pre-`22` niche, and **not one of your first ten videos is about trade.** Those terms come back around video 15 if the chokepoints backlog ships.

**Not volume-validated.** Aligned to the slate, not to measured search demand — that's README step 9 (Google Trends + vidIQ free tier). Treat the ordering as a guess.

---

## Section E — Studio → Settings → Upload defaults

### ⚠️ Correction to the folder: there is no channel-level category field

`BRAND.md` → PART `02_BRAND` §11 and README step 4 both say "Category → Education" as a channel setting. **It isn't one.** Category is a per-video field. The way to set it once is here, as an upload default — otherwise you'd be picking it manually on every upload. Don't waste time looking for it under Customisation.

**Basic info tab**

| Field | Value |
|---|---|
| Category | **Education** |
| Title | leave blank |
| Description | paste the video description template below |
| Visibility | **Private** — so a misfire can't publish itself |
| Language | English |
| Comments | Hold potentially inappropriate for review |

**Caveat from YouTube's own docs:** upload defaults **only apply to browser uploads** at youtube.com/upload. Mobile and the video editor ignore them. Upload from the browser.

**Also set:** channel-level audience → **not made for kids.** Watermarks don't show on made-for-kids videos, so this setting silently kills the watermark if it's wrong.

### E1. Default video description template

```
[2–3 sentence summary containing the main search phrase naturally]

Chapters:
00:00 The question
0X:XX [section]

Sources:
- [Name, publication, date] — [URL]

#economics #futureofwork #economichistory
```

**Newsletter and social lines removed** while those don't exist. Add them back to this template the day the newsletter goes live — not before.

**The Sources block is not optional.** It is the single strongest differentiator against AI-generated competitors, it is what sponsors check, and it is what makes a viewer trust video two.

### E2. Video tags

**Video tags have close to no ranking effect.** What drives distribution: title, thumbnail, first 30 seconds of retention, average view duration — in that order, and nothing else is close. Fill tags in, two minutes, move on.

---

## Section F — one-time account hygiene

- [ ] **Phone verification** — gates custom thumbnails and longer uploads. Without it the whole thumbnail system is unusable. *(Listed as unverified against official docs in `BRAND.md` → PART `02_BRAND` §12; treat as likely but confirm in Studio.)*
- [ ] **Subtitles:** upload accurate English subtitles per video, **not auto-generated.** Helps search, accessibility, non-native viewers, and materially reduces accent friction.
- [ ] **Unlist the old off-niche video?** — **No. Keep it public as video zero** (`BRANDING-SESSION.md`). README immediate action 3 says unlist; that was reversed. The niche spec is not widened to include meta content.
- [ ] Replace the old cyan banner and signboard avatar — this sheet is what does it.

---

## No intro animation

Not a Studio setting, but it belongs in the one-time decisions: **no intro sting for the first 10 videos.** Half of all viewers leave in the first 90 seconds; do not spend three of those on a logo. A 1-second wordmark card after the hook, around 0:30, is acceptable once you have one.

---

## Definition of done — bare minimum

- [ ] Upload `01_DP_avatar_800.png` as the profile picture
- [ ] Generate the banner background, then upload the composited `banner_2560x1440.png`
- [ ] Paste the description (§A3), keywords (§D2), country (§D1)
- [ ] Set upload defaults (§E) — this is where Education category lives
- [ ] Create the three playlists (§C)
- [ ] Skip links, contact info, watermark, trailer

**Then branding is CLOSED.** Deferred items are listed in the scope section at the top; they are not reopened by asking "what about the watermark" — they are reopened when a video needs them.

---

Sources — YouTube Help Centre, opened 2026-09-13:
[Manage your channel branding](https://support.google.com/youtube/answer/10456525?hl=en&co=GENIE.Platform%3DDesktop) ·
[Manage your channel's profile](https://support.google.com/youtube/answer/2657964?hl=en&co=GENIE.Platform%3DDesktop) ·
[Set default upload settings](https://support.google.com/youtube/answer/2660027?hl=en) ·
[Channel banner & profile picture tips](https://support.google.com/youtube/answer/12950272?hl=en)
