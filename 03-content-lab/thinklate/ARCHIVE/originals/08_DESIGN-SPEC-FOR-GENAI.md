# ThinkLate — Design Spec for GenAI Tools

**Purpose:** paste-ready specifications and prompts for building the template set in a GenAI tool (Figma AI, v0, Canva Magic, Claude, Gemini, Lovable, Cursor) instead of the Python code in `templates/`.

The Python in `templates/` stays as a working reference implementation — it proves the spec renders correctly and it's there if you ever want deterministic batch output. **You don't need it if you go the GenAI route.** The spec below is the contract; the tool is interchangeable.

---

## 1. Design tokens — paste this block into any tool

```
BRAND: ThinkLate
POSITIONING: how work, money and power actually function - and how that reaches your working life.
             Economics, geopolitics and technology through hindsight.
LANGUAGE:    Hinglish narration. ALL on-screen text, titles and thumbnails in ENGLISH.
VOICE: friendly, direct, dry, occasionally sarcastic, hard facts
TAGLINE: Master of none, expert of after
HANDLE: @wethinklate

TWO SURFACES (alternate across the video — never one surface throughout):

  SURFACE "ink"  — use for charts, data, kickers, counters
    background  #1B2A4A
    text        #F4F1EA
    dim text    #A8A29A
    rules/grid  #2A3341
    panel       #1C2433
    accent      #D99A2B

  SURFACE "paper" — use for quotes, documents, archival, timelines, title cards
    background  #F4F1EA
    text        #1A1A17
    dim text    #6E6A61
    rules       #D6D0C4
    panel       #EAE5DA
    accent      #A8741A     <- darker ochre; #D99A2B fails contrast on paper

NEGATIVE (use only for negative values, never for emphasis)  #9B3A2F

TYPE
  Headlines     Instrument Serif  (fallback Playfair Display, Libre Baskerville)
  Body/labels   IBM Plex Sans     (fallback Inter)
  Numbers/source IBM Plex Mono
  Two families maximum. Three is amateur.

CANVAS
  Video frame   1920 x 1080
  Thumbnail     1280 x 720
  Safe margin   120 px all sides

TYPE SCALE (sized for a TV at 10 feet — do not shrink)
  hero      136    video title card
  h1         92    chapter card
  h2         64    chart title
  kicker    240    the one big number
  quote      58
  body       40
  label      32    axis labels
  caption    28    sources, attribution

HARD RULES
  - Exactly ONE accent element per frame. If everything is highlighted, nothing is.
  - Max 5 data series per chart. Above that, split into two charts.
  - No dual axes. No pie charts. No 3D. No gradients on data.
  - Every frame carrying a figure MUST show a source: name + date, bottom-left, mono, dim.
  - Wordmark "ThinkLate" bottom-right, caption size, dim, letter-spacing 1.5.
  - No AI-generated illustrative imagery, no fake archival photos.
```

---

## 2. Frame types to build

Ten types. Build each once; every video is text and data swaps.

| # | Frame | Surface | Holds | Contents |
|---|---|---|---|---|
| 1 | Title card | paper | 2–4s | Amber rule, title line 1 (text colour), line 2 (accent), tagline, wordmark |
| 2 | Chapter card | paper | 2–4s | Two-digit number in mono accent, thin rule, chapter title in serif |
| 3 | Kicker / counter | ink | 3–6s | One huge number centred in accent serif, label beneath in caps, optional subline |
| 4 | Quote card | paper | 10–20s | Oversized opening quote mark at 35% opacity, quote in serif, amber rule, speaker, date in mono, source |
| 5 | Timeline | paper | 30–60s | Horizontal rule, 3–6 accent dots, year above each in mono accent, label below |
| 6 | Comparison table | ink | 20–40s | Header row in dim caps, alternating panel row stripes, one highlighted column in accent, mono for numbers |
| 7 | Lower third | transparent | overlay | Left-aligned panel at 92% opacity, 10px accent bar on the left edge, primary + secondary line |
| 8 | Source strip | transparent | overlay | Full-width bar at 78% opacity along the bottom, mono text |
| 9 | End card | paper | 15s | Wordmark, tagline, amber rule, "NEXT" in mono accent, next video title, newsletter line, handle. **Reserve two empty zones for YouTube end-screen elements: 560×315 and 270×270 on the right side** |
| 10 | Thumbnail | paper (default) | — | Left 60% visual zone, right 40% text zone. **2–3 words** (4 ceiling), serif, first line accent. One amber rule above the text. High contrast mandatory |

---

## 3. Paste-ready prompts

### 3a. Full template set, one prompt

```
Build a reusable template set for a YouTube explainer channel called ThinkLate.
It covers how work, money and power function - economics, geopolitics and
technology through historical hindsight, landing on the viewer's working life.
Serious, archival, data-led. Think Patrick Boyle or Wendover, not a startup deck.
Narration is Hinglish; all on-screen text is English.

Use these design tokens exactly:
[PASTE THE TOKEN BLOCK FROM SECTION 1]

Produce these frames at 1920x1080 (thumbnail at 1280x720), each on the surface
specified, with all text as editable layers:
[PASTE THE TABLE FROM SECTION 2]

Constraints:
- Exactly one accent element per frame
- Every frame with a figure shows a source line: bottom-left, mono, dim colour
- Wordmark bottom-right on every frame except the transparent overlays
- Generous negative space; these are read on a TV, not a phone
- No gradients, no glows, no drop shadows, no 3D, no stock-photo people
- No AI-generated illustrative imagery of any kind

Deliver each frame as a separate editable artboard or component.
```

### 3b. Single frame, when iterating

```
Design one [FRAME TYPE] for ThinkLate at 1920x1080 on the [ink|paper] surface.

Tokens: [PASTE TOKEN BLOCK]

Content:
  [exact text that goes on this frame]

Requirements:
- One accent element only
- Source line bottom-left in mono, dim
- Wordmark "ThinkLate" bottom-right, caption size, dim
- 120px safe margin
- Legible on a TV at 10 feet
```

### 3c. Animated chart

```
Build an animated [bar|line|stacked-area] chart for a long-form YouTube video.

Surface: ink. Tokens: [PASTE TOKEN BLOCK]

Data: [paste your verified data]
Title: [chart title]
Source: [source name and date — required]
Highlight: [the single series that gets the amber accent]

Motion:
- [Bars grow in sequence, staggered 0.12s, values counting up]
  or [line draws left to right; series labels appear only in the final 20%]
  or [stacked area fills in over time]
- Ease-out cubic. Linear motion reads mechanical.
- 4-6 seconds to draw on, then HOLD. Do not loop.

Output: 1920x1080, 30fps, MP4 (H.264, yuv420p) for editing in DaVinci Resolve.
```

### 3d. Abstract background layer — the only safe image-generation use

```
Abstract dark background texture, deep ink navy #1B2A4A, subtle aged paper grain,
faint horizontal scanlines, very low contrast, no objects, no people, no text,
no recognisable imagery, seamless, understated. 16:9.
```

**Never prompt an image generator for:** historical scenes, real people, real places presented as documentary, anything resembling archive footage, or fake newspaper front pages. Fabricated visuals destroy the credibility this channel runs on and risk monetisation under YouTube's July 2026 inauthentic-content policy.

---

## 4. Motion and layering — what the tool must not flatten

A GenAI tool will happily hand back beautiful static cards. That's the mistake the first version of this template set made.

**The three-layer composition:**

```
Layer 3   text / callout / source strip
Layer 2   chart, diagram or document excerpt
Layer 1   archival image or texture, dimmed 60-75%, slow drift
```

A chart floating over a dimmed 1840s railway photograph is video. The same chart full-screen on flat navy is a slide. Build the composition as a layered template, not as flat frames.

**Also required, and usually done in Resolve rather than the GenAI tool:**

- Slow push or pan on every archival still — 1–3% scale over the shot. Never fully static
- Text builds that reveal as the narration reaches them
- Animated arrows along routes on maps
- A highlight box drawn on a document excerpt as it's cited
- Film grain as **one** adjustment layer over the whole timeline

**Surface sequencing across a video:**

```
paper   title
ink     kicker
paper   archival + document
ink     chart 1
paper   quote
ink     charts 2-3
paper   timeline
ink     final chart
paper   end card
```

Alternation is the point. Each switch re-engages attention at no production cost.

---

## 5. Acceptance checklist

Before you commit a template set to 20+ videos:

- [ ] Every frame legible on a TV at ten feet
- [ ] Thumbnail legible at 128×72 px (10% scale)
- [ ] Exactly one accent element per frame
- [ ] Source line present on every frame carrying a figure
- [ ] Paper accent is `#A8741A`, not `#D99A2B` — check contrast
- [ ] Both surfaces exist and alternate
- [ ] Charts animate; nothing is a static full-screen card for 45 seconds
- [ ] End card reserves both YouTube end-screen zones
- [ ] Text is editable, not baked into an image
- [ ] One 60-second segment cut end to end before scripting video 1

---

## 6. Channel branding assets — MOVED

> **⛔ This section is superseded, 2026-09-13.**
>
> All channel-branding art direction and prompts now live in **`brand/ART-DIRECTION.md`** — the single canonical source.
>
> The removed content specified flat vector, SVG geometry, and enamel-emblem directions. **All were tried and rejected across eight rounds.** The locked style is **modern anime character illustration** — an owl in thick round glasses, shirt and tie, with a half-lidded deadpan expression.
>
> Sections 1–5 above still apply: they cover **in-video frame types, charts and motion**, which remain in the clean, sober register. Only the *character and branding* art direction moved.
