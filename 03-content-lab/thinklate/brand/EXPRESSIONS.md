# ThinkLate — Character Expression Library

**Created 2026-09-13.** Production asset file, not strategy.
**Character:** the ThinkLate owl — anime-style, glasses, shirt/tie/blazer, deadpan.

---

## How to use this — the anti-drift method

**The problem:** GenAI cannot hold a character consistent across separate generations. Ask for "the same owl, surprised" and you get a different owl.

**The method:** three things every time, in this order.

1. **Attach the locked master image** as a reference (`00_MASTER_avatar.png`). Every tool that accepts image input will hold the character far better from a reference than from words
2. **Paste the BASE BLOCK below, unchanged.** Never edit it. It is the character's identity
3. **Append exactly ONE expression line.** Change nothing else

If the character still drifts, the fix is a better reference image, never more adjectives.

---

## THE BASE BLOCK — paste unchanged, every time

```
Anime-style character illustration, front-facing bust portrait, modern
high-quality Japanese anime style — clean confident linework, smooth cel
shading with soft gradient blending, crisp highlights.

THE CHARACTER — must match the reference image exactly
An anthropomorphic owl. Warm tan and cream feathers with subtle brown
markings. Soft rounded head with two clearly separated pointed ear tufts
angled outward, smooth unbroken edges, no serrations or wisps. Thick round
circular lenses in a bold dark charcoal frame with a bridge across the beak
and visible arms. White collared shirt, deep red tie, dark brown blazer.
Small tan beak.

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

## THE EXPRESSION LINES — append one

### Core six — build these first

| # | Name | Append this line | Use in script |
|---|---|---|---|
| **E1** | **Neutral** | `Eyes open and level behind the lenses, looking straight forward, calm and attentive. Beak closed. Relaxed, composed, no strong emotion.` | Default narration, the base pose for rigging |
| **E2** | **Deadpan** | `Heavy half-lowered eyelids, flat level brow, looking straight forward, completely unimpressed. The look of someone who predicted this and is waiting for you to catch up. Beak closed. Dry and quietly amused, not angry, not sleepy.` | **The signature.** Absurd facts, "this was the good option" |
| **E3** | **Sceptical** | `One eyebrow raised high, the other level, eyes slightly narrowed, looking straight forward with mild doubt. Beak closed, slightly tilted head. Unconvinced but polite about it.` | Questioning a claim, a suspicious number |
| **E4** | **Talking** | `Beak open mid-speech, eyes open and engaged, brow relaxed, looking straight forward. Mid-sentence, animated but controlled.` | Lip-sync frames, any speaking cut |
| **E5** | **Surprised** | `Eyes wide open behind the lenses, brow raised, beak slightly open, pupils large. Genuinely caught off guard for once. Startled, not comic.` | The reveal, a figure landing, the turn |
| **E6** | **Explaining** | `Eyes open and focused, brow slightly lowered in concentration, beak slightly open mid-explanation, one wing raised into frame with the tip pointing upward as if making a point.` | Walking through the causal chain |

### Optional four — add when a script needs them

| # | Name | Append this line | Use in script |
|---|---|---|---|
| **E7** | **Side-eye** | `Eyes cut sharply to the side away from the viewer, eyelids half lowered, brow flat, beak closed. A knowing sideways glance. Sardonic.` | The sarcastic aside |
| **E8** | **Exasperated** | `Eyes closed, brow furrowed, one wing raised to the forehead in a weary facepalm, beak set in a flat line. Patient despair.` | Genuine absurdity |
| **E9** | **Thinking** | `Eyes looking upward and slightly to the side, eyelids relaxed, brow softly raised, beak closed. Considering something unresolved.` | The open question that ends the video |
| **E10** | **Approving** | `Eyes gently narrowed into a warm satisfied look behind the lenses, brow relaxed, beak closed in a subtle upward set. Quietly pleased. Understated, not a grin.` | A rare moment where something worked |

---

## Production notes

### Background and keying

Generators do not produce true transparency. Two options:

| Approach | How | When |
|---|---|---|
| **Navy native** | Generate on `#1B2A4A` as above, use as-is | Full-frame cuts, avatar, end card |
| **Key it out** | Replace the background line with `flat solid bright green #00B140 background, completely plain` then key in Resolve | Corner cut-ins over footage or charts |

### Consistency check before you use a frame

1. Are the glasses the same shape and thickness?
2. Same tuft angle and length?
3. Same tie colour and collar shape?
4. Same feather tone — not lighter or darker?
5. Same head-to-shoulder proportion?

**Any no → regenerate. Do not mix inconsistent frames in one video; viewers notice character drift even when they can't name it.**

### Naming convention

`E2_deadpan_v1.png` · `E4_talking_v2.png` — expression number, name, version. Store in `brand/expressions/`.

### Build order

- **Video 1 needs three:** E1 neutral, E2 deadpan, E4 talking. Nothing else
- **Add E3 and E5** once you hit a script that needs them
- **E6–E10 only on demand.** Do not batch-generate ten expressions before you know which you actually use

### Later: rigging

If you move to Live2D or Inochi2D, the artwork must be redrawn in separated layers — eyes, lids, brow, beak, head, body. **Do not start that until the character has survived 5+ videos unchanged.** Static expression swaps are enough until then.
