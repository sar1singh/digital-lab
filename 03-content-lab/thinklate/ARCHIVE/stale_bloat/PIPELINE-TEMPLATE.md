# ThinkLate — Video 2+ Fast-Track Production Pipeline
> **The Zero-Setup Turnkey Engine for Video 2 Onwards**  
> **Channel:** ThinkLate (`@wethinklate`) | **Target Runtime:** 6–8 minutes (Floor Tier)  
> **Core Objective:** Eliminate 100% of repetitive technical setup so Video 2 onwards moves from idea to finished video in **under 2.5 hours of human time**.

---

## ⚡ The Video 2+ Speed Invariant: What Is Already Done Once & For All

| Setup Layer | Video 1 Status | Video 2+ Status | Time Saved |
| :--- | :--- | :--- | :--- |
| **Acoustic Mastering** | Tested, dialled, filtered | **1-Click Audacity Macro (`ThinkLate Voice Chain`)** | **~45 mins saved** |
| **Teleprompter Studio** | Designed, debugged | **Auto-scaffolded `recording_studio.html`** with live VU meter & pause notation | **~30 mins saved** |
| **AI Video Style Lock** | Prompt tested against drift | **Locked Suffix & Negative Prompt copied automatically** | **~25 mins saved** |
| **Compositing Layouts** | 3 layouts designed | **Pre-formatted Layout 1 (Full), Layout 2 (Split Card), Layout 3 (Graphic)** | **~20 mins saved** |
| **Project Directories** | Created by hand | **1-Command Scaffolding (`python scaffold_video.py`)** | **~15 mins saved** |

---

## 🛠️ The 6-Stage Fast-Track Workflow

```
[1. NotebookLM Research] ➔ [2. Scaffold Project (10s)] ➔ [3. Script & Scene-Wise AI Video Prompts]
                                                                        │
[6. Timeline Assembly] 🠄 [5. Voice Teleprompter & Audit] 🠄 [4. Manual Screenshot Capture]
```

---

### Stage 1: Research Ingest & Authority Anchoring (15–20 mins)
1. **Open Google NotebookLM:** Create a new notebook titled `ThinkLate — Video XX [Topic]`.
2. **Upload 3–4 Authoritative Primary Sources:**
   - Academic papers (SSRN, NBER, university archives).
   - Institutional reports (Goldman Sachs, IMF, World Bank, Sequoia Capital, Central Banks).
   - Historical records (British Library, National Archives, SEC 10-Ks).
3. **Extract 3 Essentials:**
   - The **Core Invariant**: What historical infrastructure boom mirrors this?
   - The **Surprise Data Point**: One jaw-dropping number (e.g., 15–20% of GDP).
   - The **Counter-Intuitive Truth**: What did everyone get wrong?

---

### Stage 2: Instant Project Scaffolding (10 seconds)
Run this single command from `digital-lab/03-content-lab/thinklate/`:
```bash
python scaffold_video.py <video_number> <slug> "<video_title>"
```
*Example for Video 2:*
```bash
python scaffold_video.py 2 copper-chokehold "The World Runs on One Copper Wire"
```
**This automatically initializes:**
- `videos/02_copper-chokehold/`
- Pre-wired `recording_studio.html` teleprompter.
- Turnkey `AI-VIDEO-GENERATION-BIBLE.md` with style lock suffix and layout rules.
- Turnkey `SCREENSHOT-GUIDE.md` with link and page tables.
- Turnkey `script.md` with pause notation (`//`, `///`, `////`) and zero numerals rule.
- Turnkey `sources.md` and `NOTEBOOKLM-SOURCES.md`.
- `audit_audio.py` and ThinkLate Owl Avatar master assets copied to `brand_assets/`.

---

### Stage 3: Script & Scene-Wise AI Video Prompts (30–40 mins)
1. **Draft `script.md`:**
   - Write 10–13 takes (20–35s each).
   - **Hard Rule:** Zero digits in spoken text (spell out all numbers).
   - **Pause Notation:** `//` (micro-breath 0.3s), `///` (1-second beat), `////` (2-second dramatic beat).
   - Include explicit tone directives: `[Conversational, intimate]`, `[Cold, analytical]`, `[Stunned gravity]`.
2. **Populate `AI-VIDEO-GENERATION-BIBLE.md`:**
   - For **every single scene and dialogue line**, write:
     1. Spoken Dialogue & Timing.
     2. Visual Breakdown (A-Roll host vs. B-Roll living video vs. motion graphic).
     3. **AI Video Prompt** with the locked suffix:
        ```text
        cinematic documentary photography, BBC historical documentary aesthetic, 35mm film grain, anamorphic lens, natural filmic lighting, deep slate navy #1B2A4A and warm amber #D99A2B color grading, realistic atmospheric haze, 8k resolution, photorealistic, 16:9 widescreen, no CGI look, no cartoon, no oversaturation, no artificial 3D render.
        ```
     4. **Manual Screenshot Guide** (Exact web link, direct PDF link, local file path, page number, and quote to crop).

---

### Stage 4: High-DPI Screenshot Capture (15 mins)
1. Open the links pre-cataloged in `SCREENSHOT-GUIDE.md`.
2. Set browser zoom to **125% or 150%** for razor-sharp typography at 1080p/4K.
3. Use Windows Snipping Tool (`Win + Shift + S`) to capture clean crops with 30–50px margins.
4. Save directly into `videos/<video_dir>/assets/`.

---

### Stage 5: Voice Recording & 1-Click Mastering (15–20 mins)
1. **Open Teleprompter:**
   Navigate to `http://localhost:8080/videos/<video_dir>/recording_studio.html`.
2. **Record Takes:**
   - Read off the teleprompter in your natural, informal conversational English meeting register.
   - Record take by take into Audacity or the in-browser recorder.
3. **Run 1-Click Audacity Macro:**
   - `Tools` ➔ `Macro Manager` ➔ Select **`ThinkLate Voice Chain`** ➔ Click **`Apply to Project`**.
   - *(Applies: High-Pass Filter 80Hz ➔ Compressor 2.5:1 ➔ Loudness Normalization -16 LUFS ➔ Soft Limiter -2.0 dB).*
4. **Audit Audio:**
   ```bash
   python audit_audio.py audio_takes/take_01.wav 1
   ```
   Must score **≥80/100 [PASS]** on True Peak (< -1.0 dB), WPM (130–150), and pause ratio (15–30%).

---

### Stage 6: Video Assembly & Timeline Polish (20–30 mins)
1. **Generate Video Clips:**
   Copy the scene prompts from `AI-VIDEO-GENERATION-BIBLE.md` into **Google Vids** (`vids.google.com`) or **Google Flow / Veo / Runway Gen-3**.
2. **Assemble Timeline (5 Tracks):**
   * **Track 1 (Bottom):** Living 1080p AI B-roll video.
   * **Track 2:** Full-body or waist-up animated ThinkLate Owl Avatar (Scenes 1, 2, 4, 8, 12, 13).
   * **Track 3:** High-DPI Evidence Cards (Right 45% with 24px drop shadow).
   * **Track 4:** Lower-third citations (fade in at +1.0s, hold for 5s).
   * **Track 5:** Voiceover audio + `ambient_drone.wav` (ducked to -22 dB).
3. **Living Room TV Legibility Check:**
   Ensure text on cards and charts reads effortlessly from 10 feet away.
4. **Export in 1080p!**
