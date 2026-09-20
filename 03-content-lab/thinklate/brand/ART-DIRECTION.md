# ThinkLate — Art Direction & Prompt Library

**CANONICAL. Created 2026-09-13.** Single source of truth for art style and every branding prompt.

**Supersedes:** `PROMPTS.md`, `BRIEF.md`, and §6 of `../08_DESIGN-SPEC-FOR-GENAI.md`. Those remain on disk as a record of what was tried and rejected — **do not use them.**

---

## 1. ART STYLE — LOCKED

| | |
|---|---|
| **Style** | **Modern high-quality Japanese anime.** Clean confident linework, smooth cel shading with soft gradient blending, crisp highlights |
| **Subject** | An anthropomorphic **owl** — a dry-witted office worker |
| **Defining features** | **Thick round charcoal glasses** · two clean pointed ear tufts · white shirt, deep red tie, dark brown blazer |
| **The expression is the brand** | **Half-lowered lids, flat brow, unimpressed.** Someone who predicted this and is waiting for you to catch up |
| **Palette** | Warm tans and creams · deep navy `#1B2A4A` field · charcoal frames · **deep red tie as the only accent** |
| **Never** | Flat vector clipart · enamel or metal emblem · abstract geometric mark · perfect mirror symmetry · sober institutional editorial · cute, moe, fierce, or mascot-cartoon |

### Why, briefly

- **Anime is Sarwan's own taste**, and taste is the deciding factor — `CRAFT.md` → PART `12_CRAFT-EVIDENCE` §8c found **no evidence** on art style for avatars
- **Evidence does support a character over an abstract mark** (§8a) — faces are tracked preattentively
- **The glasses solve the silhouette problem.** Round head + two tufts + two bold circles is identifiable in solid black, which is what makes an avatar function as a logo
- **Eight earlier rounds of flat/geometric/emblem work were rejected.** That ground is closed

### Two registers, one brand

| Surface | Register |
|---|---|
| Avatar, banner, end card, in-video character | **Anime character.** Warm, expressive, personality-forward |
| Thumbnails | **High saturation, bold caps, energetic** |
| Charts, tables, data frames | **Clean and sober.** Deliberate contrast — the host has personality, the evidence does not |

Bridged by the deep navy and by a single accent in both.

---

## 2. THE BASE BLOCK

Every character prompt = **this block, unchanged** + one variable section. Never edit it. **Always attach `00_MASTER_avatar.png` as an image reference** — a reference holds the character far better than words.

```
Anime-style character illustration, front-facing bust portrait, modern
high-quality Japanese anime style — clean confident linework, smooth cel
shading with soft gradient blending, crisp highlights.

THE CHARACTER — must match the reference image exactly
An anthropomorphic character: a stylized Japanese anime owl head set upon an adult human body. Warm tan and cream feathers with subtle brown markings on the head, two clearly separated pointed ear tufts angled outward, smooth unbroken edges, no serrations or wisps. Thick round circular lenses in a bold dark charcoal frame with a bridge across the small beak. Fully human neck, shoulders, torso, and realistic human hands with fingers for natural gestures. White collared dress shirt, deep red silk tie, tailored dark brown wool blazer. Small tan beak.

Same face shape, same proportions, same colours, same glasses, same outfit
as the reference. Only the expression changes.

COLOUR
Flat deep navy blue #1B2A4A background, completely plain and empty. Warm
tans and creams, dark charcoal frames, deep red tie as the only accent.

FRAMING
Head and upper chest. Nothing touches any edge — generous clear margin on
all four sides. Head and glasses occupy the upper two thirds. Square format,
centred.

The background must be completely empty. No sparkles, no stars, no glints,
no four-pointed shapes, no decorative marks, no watermarks, no text, no
letters, no numbers, no signboards, no held objects.

EXPRESSION:
```

---

## 3. PROMPT 1 — Avatar master *(the canonical asset)*

BASE BLOCK + this expression:

```
EXPRESSION:
Heavy half-lowered eyelids behind the lenses, flat level brow, looking
straight forward at the viewer, completely unimpressed. The look of someone
who predicted this outcome and is waiting for you to catch up. Beak closed.
Dry, deadpan, quietly amused. Not angry, not sleepy, not cute, not moe.

SILHOUETTE
The outline must be identifiable as solid black. Bold simple contour,
distinct separated tufts with clear negative space between them and the
head, simple clean wedge shoulders. Every edge a decisive line.
```

**Output:** `00_MASTER_avatar.png`. Everything else derives from it. **Do not regenerate once locked.**

---

## 4. PROMPT 2 — One-colour stamp

For the video watermark, merch, favicon, and any single-colour print.

```
A single-colour silhouette logo of an owl wearing round glasses, in solid
warm cream #F4F1EA on a flat deep navy #1B2A4A square. One colour only —
no shading, no gradients, no tones, no outlines, no linework.

The owl's head and shoulders as one solid filled shape: rounded head, two
smooth pointed ear tufts with clean unbroken edges, simple wedge shoulders.

THE GLASSES ARE CUT OUT AS HOLES — two perfect circles of the navy
background punched through the cream shape, joined by a thin cut-out bridge.
The background shows through the lenses. The frames are negative space, not
drawn lines.

Two small solid shapes inside each lens hole suggest half-lowered lids.
A small notch cut out for the beak.

Bold, graphic, stencil-like. Absolutely flat. Identifiable at 32 pixels.
Centred with clear margin on all sides. No text, no sparkles, nothing else
in the frame. Square format.
```

---

## 5. PROMPT 3 — Expressions

**See `EXPRESSIONS.md`.** Ten expression lines, each appended to the same BASE BLOCK. Includes the green-screen variant for corner cut-ins and the 5-point consistency check.

**Video 1 needs three only:** E1 neutral, E2 deadpan, E4 talking.

---

## 6. PROMPT 4 — Channel banner

Character sits inside the 1235×338 safe area; everything else is atmosphere.

```
Anime-style wide landscape illustration for a YouTube channel banner.

The same owl character as the reference image — warm tan feathers, thick
round charcoal glasses, white shirt, deep red tie, dark brown blazer,
half-lowered unimpressed eyelids. Positioned on the RIGHT side of the
frame, head and shoulders, looking toward the viewer.

The LEFT two thirds is empty deep navy #1B2A4A space for text to be added
later — completely plain, nothing in it.

Behind the character, very faint low-contrast atmosphere: barely visible
darker navy shapes suggesting a night sky or a faint grid. Nothing readable,
nothing that competes, no focal point.

Wide 16:9 landscape. Clean cel shading, crisp linework.
No text, no letters, no numbers, no sparkles, no logos, no borders,
no frames, no shadows.
```

---

## 7. PROMPT 5 — Thumbnail character cut-in

The energetic register. Character reacts; the data stays sober.

```
Anime-style character illustration of the same owl as the reference image
— warm tan feathers, thick round charcoal glasses, white shirt, deep red
tie, dark brown blazer.

EXPRESSION: [pick one — wide-eyed surprise / flat deadpan stare / one brow
raised in scepticism], turned slightly toward the viewer, upper body, one
wing raised into frame.

Flat solid bright green #00B140 background, completely plain, for keying out.

Bold saturated colour, strong rim light on the character, high contrast,
punchy. Clean linework.
No text, no letters, no numbers, no sparkles, nothing else in frame.
```

**Then in Resolve or Affinity:** key out the green, composite over the thumbnail, add English text separately. **Never let the generator set type.**

---

## 8. Standing rules

1. **Never re-invent the mark.** Every asset describes *this* owl, from the reference image
2. **Always attach `00_MASTER_avatar.png`.** Words alone will drift the character
3. **Edit only the EXPRESSION section.** The BASE BLOCK is identity
4. **Generators never set type.** All text is added in Affinity, Resolve or Canva
5. **Run the consistency check** in `EXPRESSIONS.md` before any frame enters a video
6. **`QC.md` before anything is published**
7. **The art-style question is closed.** Do not reopen without a reason stronger than taste
