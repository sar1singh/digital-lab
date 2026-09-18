# Branding Session — Scope and Close-Out

**Created 2026-09-13.** One-time work. **When the checklist below is done, branding is closed and every session after this is content only.**

---

## Decisions locked 2026-09-13

| | |
|---|---|
| **Art style** | Modern anime. Owl in thick round charcoal glasses, white shirt, deep red tie, brown blazer, half-lidded deadpan. `ART-DIRECTION.md` §1 |
| **Mark type** | Character with a face. Not abstract, not wordmark-only |
| **Palette** | Warm tans/creams · navy `#1B2A4A` field · charcoal frames · **red tie as sole accent** |
| **Published video 1** | *"How NOT To Start a YouTube Channel"* — **kept public as video zero.** An origin/intro piece. The spec is not widened; meta content is not a pillar |
| **Channel description** | **Rewrite to the locked positioning.** Clear and searchable, in the dry register. The joke voice is retired from the description |
| **Banner** | **Character right, text left.** Wordmark, tagline and cadence in the empty left two-thirds of the safe area |

---

## The close-out checklist — 8 assets, then stop

| # | Asset | Spec | Source |
|---|---|---|---|
| 1 | ✅ `00_MASTER_avatar.png` | 800×800, deadpan, forward gaze, clean margin | `ART-DIRECTION.md` §3 |
| 2 | ✅ `01_DP_avatar_800.png` | Head-tight, circle-safe, verified at 98 px and 32 px | Crop of #1 |
| 3 | `stamp.png` | One-colour, lenses knocked out, 32 px legible | §4 |
| 4 | Watermark | 150×150, from the stamp, rim so it survives light footage | From #3 |
| 5 | Banner | 2560×1440, character right, all text inside 1235×338 | §6 |
| 6 | Three expressions | E1 neutral · E2 deadpan · E4 talking | `EXPRESSIONS.md` |
| 7 | Channel description | Rewrite, plain first line, dry second, searchable | Below |
| 8 | Thumbnail template | Character cut-in on green, text added in Affinity | §7 |

**Nothing else.** No end card, no merch, no expressions 5–10, no rigging until the character has survived five videos unchanged.

### ⚠️ SCOPE CUT — 2026-09-13. The 8-item checklist is reduced to 4.

Sarwan's call, and the right one: branding was consuming time that belongs to content. **Bare minimum only — profile picture, banner, description, keywords/upload defaults.** Everything else is deferred, not cancelled.

| Old # | Item | Now |
|---|---|---|
| 1 | Master avatar | ✅ done |
| 2 | DP crop | ✅ done |
| 3 | Stamp | ⏸ deferred |
| 4 | Watermark | ⏸ deferred — worth ~nothing at zero subscribers, revisit ~video 5 |
| 5 | Banner | ⏳ one Gemini render away |
| 6 | Three expressions | ⏸ deferred to the template phase — in-video asset, not channel setup |
| 7 | Channel description | ✅ done — `EXPORT/CHANNEL-SETUP-PASTESHEET.md` §A3 |
| 8 | Thumbnail template | ⏸ deferred to the template phase — needed before video 1 publishes, not before the channel looks presentable |

**Also cut:** business email, newsletter and social links — all left blank. Nothing to link to yet, and a link to a dead landing page is worse than none.

**No public cadence.** The "New video every two weeks" line is removed from the description and the banner. Fortnightly stays an internal commitment; publishing it only creates a public miss.

**Operative file is now `EXPORT/CHANNEL-SETUP-PASTESHEET.md`.** This file is the decision record.

### Progress — 2026-09-13

- **#1 DONE.** Gemini render accepted. QC verdict FIX FIRST; three defects repaired mechanically (forbidden four-pointed sparkle on right shoulder removed · stray red dot on right lens rim removed, restoring the one-accent rule · background flattened to exact `#1B2A4A`, re-centred and padded to 800×800 so tuft tips clear the inscribed circle). **Do not regenerate.**
- **#2 DONE.** `01_DP_avatar_800.png` — head-tight crop of #1, 9% navy breathing room, tufts clear the circle, glasses read as two distinct circles at 32 px. This is the file that gets uploaded as the profile picture; `00_MASTER_avatar.png` is the reference image attached to every later prompt.
- **YouTube spec verified against the Help Centre, not from memory:** profile picture needs only PNG ≤15 MB rendering at 98×98 — 800×800 is comfortably above requirement. Banner minimum 2048×1152, recommended 2560×1440, file ≤6 MB, no shadows/borders/frames. Watermark minimum 150×150, square, <1 MB.
- **Banner safe-area correction:** YouTube states 1235×338 as the safe area *at the 2048×1152 minimum*. On a 2560×1440 canvas it scales to roughly 1544×423. This folder's "text inside 1235×338 on a 2560×1440 canvas" rule is therefore over-conservative rather than wrong — safe to keep, but there is more usable room than assumed.

---

## Channel description — draft to refine in the next session

Structure: one plain searchable line · one dry line · what to expect · cadence.

```
How work, money and power actually function — and how that reaches your
working life.

Twenty years too late, but at least it's sourced.

Long-form explainers on economics, geopolitics and technology, traced from
the decision that caused it down to the bill you pay. Every claim sourced.
Every guess labelled as a guess.

New video every two weeks.
```

**Open:** Hinglish or English description text. Narration is Hinglish, packaging is English (`STRATEGY.md` → PART `24_LANGUAGE-REVERSAL`) — so the description should be English, but test it.

---

## Definition of done

- All 8 rows above complete and uploaded to YouTube
- `QC.md` run and passed on items 1–5
- Old cyan banner and signboard avatar replaced
- This file updated with "CLOSED" and the date

**After that: branding is a closed topic.** Any future session that proposes new marks, palettes or styles should be stopped and pointed at `ART-DIRECTION.md` §8 rule 7.

### Progress — 2026-09-13, second pass

- **Stamp generated and QC'd (old item 3).** Reads as an owl in glasses at 32 px — the test that matters. The generator interpreted the glasses as navy *rings* with cream lens interiors rather than punched-through holes; **accepted, because it reads better at small size than the spec would have.** Minor flaw: the shoulder wedge sits slightly detached from the head. Invisible at watermark size. Banked at `brand/stamp.png` and `EXPORT/stamp_800.png`. Still deferred — nothing depends on it yet.
- **Banner composited.** `EXPORT/banner_2560x1440.png`, text-free, ready for Affinity. Two defects repaired: the recurring four-pointed sparkle (right lapel this time) and a rectangular seam at the character patch edge.
- **Lesson for every future character prompt:** the generator ignores "no sparkles" reliably — it has now added one in both renders, in the same place. **Expect it and check the shoulders every time.**
- **Remaining to close branding:** set two lines of type on the banner in Affinity, upload avatar + banner, paste sections A/C/D/E/F. Nothing else.
