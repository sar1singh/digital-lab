# Standing instructions — ThinkLate

**Folder consolidated 2026-09-13: 35 root docs → 8.** Read `CLAUDE.md` (this file), then `START-HERE.md` §0b and §0c. That is ~20k tokens and enough to start almost anything. Pull `RUNBOOK.md` / `CRAFT.md` / `BRAND.md` / `STRATEGY.md` / `BUSINESS.md` as the task needs. Originals are in `ARCHIVE/originals/` — **do not read ARCHIVE unless checking history.**

To make a video: `RUNBOOK.md`, step 0 → 11.

## Hard rules — never break these

1. **Never state a figure not present in a source actually opened.** No estimates presented as facts. Mark anything unsourced `[VERIFY]`
2. **Label every causal-chain link:** DOCUMENTED / LIKELY / PLAUSIBLE / SPECULATIVE. Never present an inferred link at a documented link's confidence
3. **Anchor every chain in the financial or career domain.** Social/psychological effects may sit on top, marked as inference — never load-bearing
4. **Cover the invariant, not the instance.** If a title contains a product name or version number, rewrite it
5. **Offer a pattern to notice, never an action to take.** Explaining why is analysis; telling someone what to do is advice, and advice is out of scope
6. **No AI-generated illustrative imagery, no fake archival material, no AI voice.** Real charts, real documents, real archive only
7. **Never end on a prediction.** End on a better question
8. **On-screen text must complement the narration, never duplicate it** — redundancy principle, `CRAFT.md` → PART `12_CRAFT-EVIDENCE` §7d. Say the number, show the subject; or show the number, say the meaning
9. **Automate assembly, never judgement** (`BUSINESS.md` → PART `25_AI-ARCHITECTURE` §5)
10. **No text inside the logo mark.** No wordmark, tagline, signboard, or held prop. The mark is an owl head and nothing else — it must read at 32 px. The "hindsight" signboard was specified and removed on 2026-09-13; do not reintroduce it (`BRAND.md` → PART `08_DESIGN-SPEC-FOR-GENAI` §6)
11. ~~**Branding assets are drawn in SVG, not generated.** `brand/build_assets.py` is the source of truth. AI image tools are for shape exploration only — **nothing generated is ever uploaded to YouTube.**~~ **SUPERSEDED 2026-09-13.** This rule predates the art-style lock and directly contradicts it: the locked anime character cannot be drawn in SVG by hand, and `ART-DIRECTION.md` exists to generate it. Replaced by:

    **11a. Branding character assets are generated from `brand/ART-DIRECTION.md` prompts, then QC'd and repaired before upload.** `brand/build_assets.py` and the `owl_*` / `C*` / `p*` SVG renders are the record of the rejected geometric route — reference only, not the source of truth. **`brand/00_MASTER_avatar.png` is the identity anchor.**

    **11b. The ban on AI imagery still holds absolutely for EDITORIAL content** — no AI-generated illustration, no fake archival material, no AI voice inside any video. Charts, documents and archive are real. The exception is the brand character and nothing else.

    **11c. Never use Recraft or OpenArt free tiers** (watermark and/or no commercial licence). Check the commercial-use terms of whatever generator produced a published asset — `RUNBOOK.md` → PART `16_FREE-TOOL-STACK`

12. **Start directly. No fluff, no warm-up, no "before we begin".** The first line is the hook. No channel intro, no "in today's video", no asking for anything before the viewer has been given anything.

13. **Never voice a like/subscribe call-out.** Let viewers decide. If a prompt is wanted, it is a **visual pop-up over continuing narration** — never a spoken break, never a pause in the argument. **A spoken CTA breaks momentum, which costs more than the conversion is worth.** Same logic as rule 8: the screen and the voice do different jobs. *(Added 2026-09-13, Sarwan's call.)*

## Out of scope — do not propose

Finance/investing/trading advice (SEBI + YouTube AI-narration ban) · automotive and dealership (employer conflict) · any Cox Automotive specifics · medical, legal, health advice · top-10s, listicles, compilations · news coverage and commentary · true crime · history narration · self-help or "how to succeed".

## Fixed decisions — do not re-litigate

- Brand ThinkLate · handle @wethinklate · faceless
- **Hinglish narration, English packaging** (titles, thumbnails, on-screen text, subtitles)
- Niche: how work, money and power function — and how that reaches your working life
- **CADENCE REVISED 2026-09-13: 2–3 videos per fortnight, not one.** Sarwan's call — push hard through videos 1–12 to build a base, then reassess. Three tiers unchanged: Floor 6–8 min / Standard 14–18 / Pillar 25–30. **Expect Floor tier to carry almost all of the first twelve** — that is what makes the rate arithmetically possible
  - **The honest constraint:** AI compresses research and scripting, not recording and editing. At Floor, that irreducible human time is roughly 2–3 hrs per video (record ~0.5, edit ~1–1.5, package ~1). **Three videos a fortnight is therefore ~7–9 hrs of work AI cannot do for you**, on top of a full-time job. Feasible; not comfortable
  - **What makes it work is batching, not speed.** A phase is a research cluster (`START-HERE.md` → PART `THE 30 TITLES`): research once, script five, record in one or two sittings. Sequential one-at-a-time production will not hit this rate
  - **Still applies:** do not bulk-record before video 1 is published
- Publish order: `STRATEGY.md` → PART `22_NICHE-BUSINESS-ALIGNMENT` §3 (not the slate in `03`)
- Minimum success: ₹10,000/month recurring, 3 consecutive months, by month 12
- Property 2 unlocks only at ≥20 videos with per-unit cost down ≥40%

**Mark type — LOCKED 2026-09-13: a character with a face.** Not abstract geometry, not wordmark-only. Reason: the avatar renders as a 32–48 px circle and the channel is faceless, so the mark is the only face-like signal available (`CRAFT.md` → PART `12_CRAFT-EVIDENCE` §2 — 69% of breakout videos use a face). **ART STYLE — LOCKED 2026-09-13: expressive warm character illustration, matching the published avatar** (`BRAND.md` → PART `02_BRAND` → ART STYLE). **Modern Japanese anime style** — owl in **thick round charcoal glasses**, shirt, red tie and blazer, warm tans, clean linework and cel shading, **half-lidded deadpan expression — that look is the brand voice.** **Not flat vector, not an enamel emblem, not a geometric mark, not symmetrical, not sober-institutional** — eight rounds of those were rejected. Any new asset describes THIS owl; never re-invent the mark. **Canonical prompts: `brand/ART-DIRECTION.md`. `brand/PROMPTS.md` and `brand/BRIEF.md` are SUPERSEDED — do not use.**

**The creature is an OWL — LOCKED 2026-09-13.** Sarwan's reason, and it is the correct one: in fiction and idiom the owl already means wisdom, libraries, knowledge, the know-it-all. **That semantic shortcut is worth more than novelty** — it reads instantly, to a stranger, at 32 px, with no explanation. A nightjar, moth or mantis needs a paragraph. **Distinctiveness must therefore come from how the owl is DRAWN, not from changing the species.** Do not propose non-owl creatures again. Abstract concepts (the redaction bars, the concentric wake) are retained as **in-video graphic devices and candidates for the ThinkLate Media holding mark**, never as the channel mark. Do not reopen without a reason stronger than taste.

**Branding is a ONE-TIME, CLOSING topic.** Scope and the 8-item close-out checklist: `brand/BRANDING-SESSION.md`. Once that checklist is done, **every session is content only.** Any proposal for a new mark, palette or art style should be refused and pointed at `brand/ART-DIRECTION.md` §8 rule 7. **Video 1 ("How NOT To Start a YouTube Channel") stays public as video zero** — the niche spec is NOT widened to include meta content.

## Keeping these docs current

The markdown files in this folder are the memory. Keep them accurate; nothing else is tracked.

- **Update the relevant existing doc** when a decision changes. Do not create a new doc for a revision
- After each session: `git add -A && git commit` with a one-line message
- `LOG.md` after every published video · `discovery.md` whenever a friction, reply or conversation happens
- Mark superseded sections in place rather than deleting them — the history is the value
- **No new strategy docs. Ever, without asking first.** The folder hit 35 root docs and ~116k tokens before a single on-niche video existed. Consolidated to 8 on 2026-09-13. **Add sections to an existing file; do not add files.** The only new files that are automatically fine are per-video working files under `videos/`

## House style

**Bulleted key highlights only. Short.** Sarwan does not read long responses — if it's long, it doesn't get read. Detail goes in the md files, not the chat reply. No preamble. Flag uncertainty explicitly. Correct me when the evidence disagrees with me — including when it disagrees with something in these docs.
