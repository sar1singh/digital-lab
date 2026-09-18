# ThinkLate Master Video Audit & Quality Control Framework
> **Production Standard for ThinkLate Explainer Documentaries** (`@wethinklate`)  
> *Target: High-prestige, intellectually honest visual essays for mature knowledge workers (Ages 22–40).*

---

## 🧭 Production Pipeline Overview

Every ThinkLate video must systematically pass through **8 Specialized Audits** across 4 production phases:

```
┌────────────────────────────────────────────────────────────────────────┐
│ PHASE 1: PRE-PRODUCTION                                                │
│  [1. Script Auditor]        ───▶ [2. Research Auditor]                 │
└────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ PHASE 2: PACKAGING & VISUAL SYSTEM                                    │
│  [3. Thumbnail Design Auditor]  ───▶ [4. UI/UX Design Expert Audit]    │
└────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ PHASE 3: PRODUCTION & ASSET ASSEMBLY                                  │
│  [5. Visual Elements QC]     ───▶ [6. Audio-Video Auditor]             │
└────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ PHASE 4: POST-PRODUCTION & DISTRIBUTION                               │
│  [7. Content & Retention Audit] ───▶ [8. Overall Video Audit (Gate)]   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 1. 📝 Script Auditor
* **Owner:** Lead Writer / Editorial Director
* **Tool:** `python audit_script.py script.md`
* **Objective:** Ensure natural, conversational human spoken flow, authentic Indian-Global English register, and zero broadcast friction.

### Mandatory Criteria & Checkpoints:
1. **Zero Numeral Rule:** Spoken dialogue must contain **0 raw digits** (`\b\d+\b`). All numbers must be spelled out phonetically (*"fifteen to twenty percent"*, *"three hundred to four hundred billion"*).
2. **The 15-Second Hook Rule:** The cold open must land within **35–38 words** (~16 seconds at 135 WPM). It must immediately connect to the viewer's everyday reality (salary, workplace, tech boom) before introducing history.
3. **Conversational Pause Notation:** Spoken text must be marked with rhythm cues:
   - `//` = Brief conversational pause (0.3s–0.5s)
   - `///` = Full clause pause (0.8s–1.0s)
   - `////` = Section breath / idea transition (1.5s–2.0s)
4. **Tone Directives per Take:** 100% of scenes must specify an explicit emotional register `⟨TONE: ...⟩` (e.g., *low conspiratorial*, *confident thesis*, *stunned gravity*, *humble inference*).
5. **Zero Algorithmic Begging:** Spoken lines are strictly forbidden from saying *"like, share, subscribe"*, *"smash that like button"*, or *"hit the bell icon"*. Subscriptions are earned through viewer respect.
6. **Word Count Sanity:** Total script must land between 650–850 spoken words (5.5 to 6.5 minutes at 135 WPM), staying strictly inside the 6–8 minute floor tier.

---

## 2. 🔬 Research Auditor
* **Owner:** Lead Researcher / Fact Checker
* **Reference Docs:** `sources.md` & `NOTEBOOKLM-SOURCES.md`
* **Objective:** Ensure 100% intellectual honesty, verifiable primary sources, and zero ungrounded hype.

### Mandatory Criteria & Checkpoints:
1. **1:1 Primary Source Traceability:** Every factual claim, statistic, or historical date must map directly to a verified Source ID (`<src: ID>`) in `sources.md`.
2. **Verbatim Quote Verification:** Direct quotes attributed to scholars or institutions (e.g. Prof. Andrew Odlyzko, Goldman Sachs, Sequoia Capital) must be verified word-for-word against opened PDF copies:
   - *Odlyzko (2010):* *"greatest technology mania in history"*.
   - *Goldman Sachs (2024):* *"Gen AI: Too Much Spend, Too Little Benefit?"*.
   - *Sequoia (2024):* *"AI's $600B Question"*.
3. **Framing & Magnitude Accuracy:** Figures must preserve the author's exact framing.
   - *Example:* "15 to 20% of GDP" must be explicitly framed as *actual capital provided by investors*, NOT stock market capitalization.
4. **Inference vs Fact Transparency:** Any modern extrapolation or unfiling estimate must be explicitly labeled in dialogue and on screen as an **"inference / hypothesis"** (Take 11). Never present speculation as settled fact.
5. **NotebookLM Ingestion:** All primary PDFs must be downloaded and ingested into a dedicated NotebookLM notebook for real-time claim cross-examination.

---

## 3. 🖼️ Thumbnail Design Auditor
* **Owner:** Art Director / Creative Lead
* **Reference Artifact:** `thumbnail_v1_cinematic.jpg`
* **Objective:** Maximize high-intent Click-Through Rate (CTR) among mature professionals while maintaining prestige documentary credibility.

### Mandatory Criteria & Checkpoints:
1. **The 3-Second Glance Rule:** A viewer scrolling on mobile must grasp the emotional tension within 3 seconds.
2. **The 120px Mobile Simulation Test:** When scaled down to 120px height in YouTube mobile feed:
   - Can you read the overlay text without squinting?
   - Is the visual subject immediately identifiable?
3. **Curiosity Gap Over Title Restatement:** Never repeat the video title on the thumbnail. Text overlay must be 2 to 4 punchy words that create tension:
   - Approved: `REAL, BUT RUINED` / `IS AI NEXT?`
   - Forbidden: `Is AI a Bubble? Ask the Railways (Full Video)`.
4. **High-Contrast Cinematic Photorealism:** Zero cartoonish AI illustrations, zero exaggerated YouTube shock faces. Must feel like a high-budget BBC/Bloomberg Originals documentary.
5. **Safe Margin Compliance:** Keep critical visual elements and text away from the bottom-right corner (where the YouTube timestamp badge overlays).

---

## 4. 🎨 UI/UX Design Expert Audit
* **Owner:** Motion Designer / Design System Lead
* **Reference File:** `preview_deck.html`
* **Objective:** Enforce broadcast-grade typography, color harmony, and visual accessibility.

### Mandatory Criteria & Checkpoints:
1. **Brand Palette Lock:**
   - **Background Canvas:** Deep Slate Navy (`#1B2A4A` / `#0D1524`) — zero harsh pure black.
   - **Accent / Focus:** Warm Amber Gold (`#D99A2B`) — highlights, progress indicators, key quote bars.
   - **Body Text:** Warm Off-White / Paper (`#F4F1EA`) — maximum readability without eye strain.
   - **Muted Metadata:** Slate Gray (`#98A2B3`) — timestamps, secondary attributions.
2. **The 10-Foot Living Room TV Legibility Test:** All text must remain comfortable to read on a 55-inch television screen from 10 feet away:
   - Primary Headlines: Minimum 48px equivalent.
   - Document Titles: Minimum 32px equivalent.
   - Citation Lower-Thirds: Minimum 22px equivalent.
3. **Title-Safe Margins (EBU R95):** No critical UI card, text, or data chart placed within 120px of the 1920x1080 canvas borders.
4. **Information Architecture Hierarchy:** Every citation card must follow the standard visual stack:
   `[CATEGORY PILL]` ➔ `[PRIMARY DOCUMENT TITLE]` ➔ `[AUTHOR & INSTITUTION]` ➔ `[EXACT VERIFIED CLAIM]`.

---

## 5. 🎥 Visual Elements & B-Roll QC
* **Owner:** Video Editor / Compositor
* **Tools:** `render_draft_video_v2.py`, FFmpeg / DaVinci Resolve
* **Objective:** Eradicate the static "slideshow / PowerPoint" feel and deliver continuous cinematic documentary momentum.

### Mandatory Criteria & Checkpoints:
1. **The 3-Second Stagnation Rule:** No image, document screenshot, or title card may remain static for more than 3 seconds without dynamic motion:
   - Slow continuous 2% push-in (Ken Burns effect).
   - Slow subtle pan across document highlights.
2. **Authentic Primary Evidence over Vector Graphics:** Viewers trust real artifacts. Feature:
   - High-resolution scans of the 1845 railway share certificates.
   - Real screenshots of the opened Goldman Sachs and Sequoia PDFs with highlighted text.
   - Historical portraits of Charles Darwin and John Stuart Mill.
3. **Lower-Third Choreography:**
   - Enters at **1.0s after the scene cut** via a smooth slide-in or 0.4s crossfade.
   - Holds for **4.0 to 6.0 seconds** while the narrator cites the source.
   - Smoothly exits before the next thought transition.
4. **Scene Cutting Rhythm:** Long scenes (>25s) must utilize multi-shot sub-cuts (switching between wide atmospheric establishing shots and punchy document zoom-ins).
5. **Frame Rate & Resolution:** Strict 1080p (1920x1080) at 25fps (PAL broadcast standard), progressive scan, H.264 / ProRes 422.

---

## 6. 🎧 Audio-Video Auditor
* **Owner:** Sound Designer / Audio Engineer
* **Tool:** `python audit_audio.py <audio_file> <take_num>`
* **Objective:** Ensure pristine vocal clarity, natural Indian-Global English pronunciation, and immersive atmospheric sound design.

### Mandatory Criteria & Checkpoints:
1. **Integrated Broadcast Loudness:** Must measure **-14 LUFS** (±1.0 LUFS) to match YouTube's audio normalization target.
2. **True Peak Headroom:** Peak ceiling must remain between **-3.0 dBFS and -1.0 dBFS**. Zero digital clipping allowed.
3. **Vocal Pacing & Cadence:** Speaking rate must land in the **130–150 WPM** range.
   - Flag if < 115 WPM (dragging/lethargic).
   - Flag if > 165 WPM (rushing/syllable-timed Indian English trap).
4. **Conversational Breathing (Pause Ratio):** 15% to 30% of total scene duration must consist of natural thinking/cadence pauses (`//`).
5. **Vocal Modulation & Monotone Check:** Loudness Range (LRA) must measure between **3.0 and 7.5 LU**. (Below 2.5 LU indicates flat, uninspired monotone).
6. **Pronunciation Verification per Take:**
   - Take 4: *Odlyzko* ➔ `[OD-liz-ko]` (stress first syllable, never "odd-leez-ko").
   - Take 4: *mania* ➔ `[MAY-nee-uh]` (never "maa-ni-yaa").
   - Take 7: *Brontë* ➔ `[BRON-tay]` (never "bron-tee").
   - Take 10: *prematurely* ➔ `[pree-muh-CHUR-lee]`.
   - Take 11/12: *depreciation* ➔ `[dih-pree-shee-AY-shun]` (stress `AY`, never "dee-pre-see-a-shun").
   - Take 11: *inference* ➔ `[IN-fer-ens]` (stress first syllable).
7. **Soundscape & Music Ducking:**
   - Ambient synthesizer drone (`ambient_drone.wav`) ducked to **-22 dBFS** under voiceover.
   - Low-frequency whoosh SFX (`transition_whoosh.wav`) aligned exactly to scene cuts at -18 dBFS.

---

## 7. 📈 Content & Retention Audit
* **Owner:** Executive Producer / Growth Strategist
* **Objective:** Architect narrative momentum so the YouTube audience retention curve stays above 50% through the end.

### Retention Curve Milestones:
```
100% ────┐
         │ (0:00 Hook: Office reality)
 80%     └───┐
             │ (1:30 Scale Peak: 15-20% GDP)
 65%         └───┐
                 │ (2:45 Paradox: Darwin & Mill wiped out)
 55%             └───┐
                     │ (3:45 Invariant: Tracks survived, shareholders didn't)
 50%                 └───────┐ (5:00 Modern Mirror: AI Capex vs Headcount)
                             └─── (6:00 Lingering Close into silence)
```

### Mandatory Checkpoints:
1. **The 30-Second Retention Gate:** Does the opening immediately introduce tension and personal stakes before any historical exposition?
2. **Pacing Peaks:** Is a fresh insight, chart reveal, or paradox introduced every **45 to 60 seconds**?
3. **No Dead Air or Fillers:** Zero rambling, zero repetitive transitional phrases (*"as we all know"*, *"moving forward"*).
4. **The "Coffee Test":** Does the video provide a clear, memorable mental model that the viewer will want to explain to a friend over lunch?
   - *Mental model:* "A technology can be completely real and transformative, while simultaneously destroying the capital that built it."

---

## 8. 🚀 Overall Video Audit (Master Release Gatekeeper)
* **Owner:** Channel Executive (Final Sign-off)
* **Objective:** Comprehensive pre-flight verification before flipping video from Unlisted to Public.

### Master Pre-Flight Checklist:
- [ ] **Voiceover Legitimacy:** 100% real human voice recorded; zero robotic AI TTS.
- [ ] **Acoustic Integrity:** All 13 takes verified through `audit_audio.py` with Score ≥ 85.
- [ ] **Video Master Render:** 1080p 25fps H.264 / AAC 320kbps, audio synced perfectly to visual cuts.
- [ ] **Color & Contrast Check:** Watched on a mobile phone screen and an external monitor.
- [ ] **YouTube Policy Compliance:** "Altered or Synthetic Content" checkbox reviewed in YouTube Studio.
- [ ] **Metadata Package Complete:**
  - [ ] Title: `Is AI a Bubble? Ask the Railways`
  - [ ] Description: Includes full **Sources & Bibliography Block** with academic links.
  - [ ] Chapter Markers: Timestamps formatted for YouTube chapters (00:00, 00:19, 00:46...).
- [ ] **Packaging Verification:** Thumbnail tested via `thumbnail_v1_cinematic.jpg` at 100%, 50%, and 120px mobile size.
- [ ] **Sign-off:** Approved for global release.
