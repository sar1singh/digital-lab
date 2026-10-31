# ThinkLate Visual Storytelling & Production Architecture (Post-Video 5 Revamp)

> **Core Mandate:** Permanently retire all Python PIL-generated static cards, boxes, and "company PPT" graphics.  
> **Target Aesthetic:** High-octane investigative infotainment (MagnatesMedia $\times$ Vox $\times$ Johnny Harris) backed by Google Platform (Veo, Imagen, Flourish) and Frontier Global/Chinese Generative Video (Kling AI, MiniMax Hailuo).  
> **Production Sequence:** Strict 5-Phase Linear Waterfall (Scripting $\rightarrow$ Voiceover $\rightarrow$ Visual Assets $\rightarrow$ VFX/Motion Graphics $\rightarrow$ Sound Design/SFX).

---

## ⛔ 1. Permanent Bans & Architectural Sunsets

1. **BANNED: Python PIL / Pillow Media Creation:**
   - No more drawing 2D rounded rectangles, drop-shadow boxes, or colored accent bars via Python scripts. These inherently look like school projects or corporate presentation slides.
   - Python is strictly restricted to metadata parsing, Whisper timecode alignment, and headless FFmpeg concatenation—**never visual asset drawing**.
2. **BANNED: Mechanical SFX Drops:**
   - No more placing generic `whoosh.wav` or `data_blip.wav` 100ms before cards. SFX is permanently relocated to Phase 5 (Sound Design) and must be diegetically motivated by real physical on-screen motion.
3. **BANNED: Static Image Wallpaper Slideshows:**
   - Any static asset (document, archival photo, news clipping) must either have 2.5D camera parallax depth-of-field or be converted into a cinematic moving video via image-to-video AI.

---

## 🎬 2. The Frontier Visual Asset Engine

Instead of drawing flat boxes, visual assets must follow a dual-engine architecture:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   THINKLATE VISUAL ASSET ENGINE                        │
├──────────────────────────────────┬─────────────────────────────────────┤
│      GOOGLE PLATFORM ECOSYSTEM   │   FRONTIER GENERATIVE VIDEO (ASIA)  │
├──────────────────────────────────┼─────────────────────────────────────┤
│ • Google Veo (Gemini API/Vertex) │ • Kling AI (v2.5 Turbo / v3.0)      │
│   - Cinematic photorealism       │   - Extreme physics & motion brush  │
│   - 1080p text-to-video / I2V    │   - ~$0.042 / sec ($0.21 / 5s clip) │
│ • Google Flow / Flourish.studio  │ • MiniMax / Hailuo AI (H3-Lite/High)│
│   - Broadcast animated charts    │   - Dynamic camera glide & staging  │
│   - Dynamic counter multipliers  │   - ~$0.025 – $0.06 / sec           │
│ • Google Imagen 3 (Via API)      │ • Vidu (Shengshu Tech)              │
│   - Primary archival scene plates│   - Rapid 1080p anime / stylized    │
└──────────────────────────────────┴─────────────────────────────────────┘
```

### A. Google Platform Ecosystem
1. **Google Veo (via `google-genai` SDK & Google AI Studio):**
   - High-fidelity cinematic B-roll (e.g., 2007 San Francisco apartment exterior at dusk, Wall Street trading floor commotion, empty luxury hotel lobbies).
   - Image-to-Video: Animate primary archival photos (Brian Chesky in 2007) with natural facial movement and subtle breathing.
2. **Google Flow / Flourish.studio / Google Charts:**
   - Programmatic, broadcast-grade animated charts (valuation multipliers, revenue collapses, hockey-stick curves).
   - Generates interactive MP4 screen recordings or HTML5 animations that look institutional, not amateur.

### B. Frontier Asian & Global Video AI (High Volume, Low Cost)
1. **MiniMax / Hailuo AI (H3-Lite & Highspeed):**
   - Cost: **$0.025 to $0.06 per second** (~$0.15 to $0.30 per 5-second scene).
   - Best for: Fluid cinematic camera tracking shots, atmospheric crowds, and solo-founder grit scenes.
2. **Kling AI (v2.5 Turbo / v3.0):**
   - Cost: **$0.042 per second** (~$0.21 per 5-second scene).
   - Best for: Complex physical interactions, hand movements, and tactile object manipulation (e.g., counting cash, inflating airbed, packing cereal box).
3. **Web Interface / API Bridge:**
   - Can be triggered via official APIs or rapid batch generation via web UI during pre-production.

---

## 🔒 3. The Strict 5-Phase Production Sequence Law

To eliminate bottlenecks and prevent audio/visual thrashing, every video must strictly proceed in this exact sequence:

```
[ Phase 1: Scripting ]
        │
        ▼
[ Phase 2: Voiceover & Alignment ]
        │
        ▼
[ Phase 3: Visual Assets & Storytelling ]
        │
        ▼
[ Phase 4: Transitions, VFX & Motion Graphics ]
        │
        ▼
[ Phase 5: Sound Design & Diegetic Foley ]
```

### Phase 1: Scripting (100% Locked)
- Character-driven narrative, Dan Harmon Story Circle, Sumeet Jain satirical roast wit.
- Zero syllabus clichés ("Act 1", "Chapter 1", "Let's examine").
- Mandatory automated fact-check pass (`fact_check_qc.py`).

### Phase 2: Voiceover & Whisper Ground Truth (100% Locked)
- Synthesize master voiceover (`en-US-AndrewMultilingualNeural` @ +4% rate).
- Golden audio balance: Voice 90% (`volume=0.90`) + Ambient BGM 30% (`volume=0.30,normalize=0`).
- Transcribe with Whisper to generate millisecond-accurate timecodes (`transcription_timestamps.json`).

### Phase 3: Visual Assets & Visual Storytelling (Sourcing & Generation)
- Sourcing authentic primary evidence (SEC filings, court dockets, original photos, vintage ads).
- Generating cinematic AI video plates via **Google Veo**, **Kling**, or **MiniMax Hailuo**.
- Curating living gameplay/documentary B-roll spine on Track 1.
- Zero static cards or PPT slides.

### Phase 4: Transitions, VFX & Motion Graphics (Assembly & Animation)
- **Kinetic Typography:** Word-by-word active text delivery via DaVinci Resolve Text+ (Track 4) or vector motion graphics.
- **Forensic Tactile Collages:** Ripped kraft paper edges, yellow highlighter strokes, red grease-pencil circles drawn over real documents.
- **2.5D Parallax:** Primary sources floating in 3D space with subtle camera push and depth-of-field.
- **Animated Data:** Flourish / Google Charts video renders for financial multipliers.

### Phase 5: Sound Design & Diegetic Foley (The Final Polish)
- **Kept for the very end:** Sound design is applied *only after* visual cuts and transitions are 100% locked.
- **Tactile Foley Vault:** Paper slides, page turns, rubber stamps, pen scribbles, metallic thuds, typewriter clicks, and 40Hz sub-bass drops.
- **Motivated Placement:** Every sound effect must correspond directly to a physical action on screen.

---

## 🛠️ 4. Immediate Implementation Plan (For Video 06 & Beyond)

1. **Set Up Google GenAI & Veo Pipeline:**
   - Configure Vertex AI / Gemini API access for `veo-3.1-generate-preview`.
   - Create automated generation helper script `tools/generate_veo_scene.py`.
2. **Establish MiniMax / Kling Developer Accounts:**
   - Connect API keys or set up batch web workflow for high-volume scene generation ($0.025–$0.04/s).
3. **Build the ThinkLate Forensic Motion Kit:**
   - Download transparent 4K PNG assets: torn paper borders, Scotch tape, paperclips, highlighter overlays, and ink stamp alpha masks.
   - Curate the 50-sample ThinkLate Tactile Foley sound library.

