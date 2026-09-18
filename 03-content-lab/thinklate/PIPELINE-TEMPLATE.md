# ThinkLate — Video Production Pipeline Template

> **The Repeatable 7-Stage Engine** for high-RPM, faceless documentary video production. Designed to scale from Video 1 onwards, minimizing turnaround time while maximizing retention and borrowed authority.

---

## 🛠️ Integrated Tool Stack

| Stage | Primary Tool | Purpose / Output |
|---|---|---|
| **1. Research & Synthesis** | **Google NotebookLM** | Ingest source PDFs/URLs; synthesize quotes; generate audio discussion to stress-test conversational flow. |
| **2. Script & Tone Audit** | Local Markdown / AI Pair | Verified claims (`<src: ID>`), Hinglish register, explicit `[TONE]` cues, zero numerals. |
| **3. Visual Proof Sourcing** | Web Browser / Snipping Tool | Capture authentic screenshots of academic papers, financial articles, and historical archives. |
| **4. Generative B-Roll** | **Google AI Studio / ImageFX / Veo** | High-contrast cinematic documentary stills and subtle 2–4s ambient background video. |
| **5. Graphic & Lower-Third Engine** | **Python Script (`generate_evidence_suite.py`)** | Automated generation of 1920×1080 transparent lower-third citation boxes and composite slides. |
| **6. Audio Narration & Isolation** | Microphone + **DaVinci Resolve Fairlight** | High-fidelity voiceover; Resolve Voice Isolation (100% room noise removal). |
| **7. Final Assembly & Timeline** | **DaVinci Resolve / CapCut Pro** | Multi-track timeline assembly with 2% slow zoom, 1-second delayed lower-thirds, and subtle film grain. |

---

## 📋 The 7-Stage Workflow (Repeatable per Video)

```
[1. NotebookLM Research] ➔ [2. Script & Tone Cues] ➔ [3. Source Screenshots & Links]
                                                                │
[7. Final Render (TV Ready)] 🠄 [6. Voice & Fairlight] 🠄 [5. Python Lower-Thirds] 🠄 [4. AI Studio B-Roll]
```

---

### Stage 1: Research & Synthesis (Google NotebookLM)
1. **Source Ingest**: Create a new notebook titled `ThinkLate — Video XX [Topic]`. Upload 2–4 authoritative primary sources (Academic PDFs, 10-Ks, Wall Street consensus reports, official archives).
2. **NotebookLM Prompts to Run**:
   * *"Extract the top 5 surprising or counter-intuitive data points with exact quotes and page numbers."*
   * *"Identify the 'Invariant Pattern' — what happened historically that mirrors what is happening today?"*
   * *"What did the smartest investors or experts get completely wrong at the time?"*
3. **Audio Overview Stress-Test**: Generate the NotebookLM "Deep Dive Audio Overview". Listen to the two AI hosts discuss the topic — note the conversational pivots, analogies, and questions that feel most natural for spoken Hinglish delivery.

---

### Stage 2: Scripting & Tone Mapping
1. **Document Structure**: Write in `script.md` using Roman Hinglish (`RUNBOOK.md` §15).
2. **Mandatory Elements per Take**:
   * `[TAKE X]` (20–45s segments for easy recording).
   * `[TONE]` (Specific delivery cue: e.g. *Cold, analytical*, *Quiet sarcasm*, *Stunned gravity*).
   * `[VISUAL EVIDENCE]` (Explicit screenshot or B-roll trigger).
   * `[LOWER-THIRD]` (Exact citation data).
3. **Audit Rules**:
   * Zero digits in spoken text (spell out: *pandrah*, *bees percent*, *teen sau*).
   * Every factual claim must tie directly to an opened source in `sources.md`.

---

### Stage 3: Visual Proof Sourcing (The Day 1 Trust Engine)
Borrowing authority from recognized institutions (Goldman Sachs, SSRN, Bloomberg, University of Minnesota) gives Day 1 credibility:
1. Open the primary URLs from the video's `SCREENSHOT-GUIDE.md`.
2. Capture full-resolution (1080p+) screenshots of the paper title, key chart, or headline.
3. Apply a semi-transparent amber/yellow highlighter rectangle (`rgba(255, 230, 0, 0.4)`) over the exact quoted sentence.

---

### Stage 4: Generative Visuals (Google AI Studio / ImageFX / Veo)
For documentary texture without talking cartoon avatars:
1. **ImageFX / Imagen 3 Prompts (Photorealistic Documentary Stills)**:
   * *Style Token:* `Cinematic 35mm film documentary photography, shot on Arri Alexa, low key moody lighting, deep slate navy (#1B2A4A) atmosphere, volumetric haze, 16:9, highly detailed, photorealistic.`
   * *Examples:* Modern hyperscale server rooms, 1845 Victorian rail construction, quiet corporate office at twilight.
2. **Veo / VideoFX Prompts (Ambient Motion Snippets)**:
   * *Constraint:* 2–4 second slow push or drift. Zero fast action. Atmospheric background texture.

---

### Stage 5: Automated Lower-Third & Graphic Generation
Run the local python script `generate_evidence_suite.py`:
1. Generates 1920×1080 transparent PNG lower-thirds (`LT_S*.png`).
2. Generates complete 1920×1080 composite slides with cropped paper snippets + highlights + lower-thirds.
3. Automatically adheres to the unified ThinkLate palette: `#1B2A4A` (Navy), `#D99A2B` (Amber), `#F4F1EA` (Paper), `#98A2B3` (Slate).

---

### Stage 6: Voice Narration & Audio Mastering
1. **Recording Setup**: Quiet room, USB/XLR mic 6 inches away at 45° angle.
2. **Read-Aloud Workflow**: Record take by take (`[TAKE 1]`, `[TAKE 2]...`). Leave 2 seconds of room tone at the end.
3. **Fairlight Audio Chain (DaVinci Resolve)**:
   * Equalizer: High-pass filter at 80 Hz (cuts mic rumble).
   * Voice Isolation: Set to **40%–60%** (eliminates background hiss/fan noise).
   * Dynamics (Compressor): 2.5:1 ratio for broadcast-level consistency.

---

### Stage 7: Final Assembly & TV-Optimized Polish
1. **Timeline Layer Order**:
   * **V4**: Film grain adjustment layer (1.5–2% subtle texture)
   * **V3**: Transparent Lower-Third Overlay (`LT_S*.png`) — enters 1.0s after cut, holds for 5s
   * **V2**: Content (Paper screenshot, chart, or graphic card)
   * **V1**: Background Archival Still / AI B-Roll (with continuous 1.5% to 2.5% slow scale push)
   * **A1**: Clean Voice Track (master level centered at −14 LUFS)
   * **A2**: Low ambient documentary drone / drone pad (ducked to −26 dB under speech)
2. **Living Room TV Legibility Check**: Ensure all lower-thirds and highlight text are clearly readable from 10 feet away.
