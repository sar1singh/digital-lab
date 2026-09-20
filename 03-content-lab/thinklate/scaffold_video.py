#!/usr/bin/env python3
"""
ThinkLate Video Scaffolding Engine (Video 2+ Fast-Track Setup)
=============================================================
Instantly generates a complete, turnkey production workspace for any future video.
Eliminates 100% of repetitive setup friction for Video 2 onwards.

Usage:
    python scaffold_video.py <video_number> <slug> "<video_title>"

Example:
    python scaffold_video.py 2 copper-chokehold "The World Runs on One Copper Wire"
"""

import sys
import os
import shutil
import re

def main():
    if len(sys.argv) < 4:
        print("Usage: python scaffold_video.py <video_number> <slug> \"<video_title>\"")
        print("Example: python scaffold_video.py 2 copper-chokehold \"The World Runs on One Copper Wire\"")
        sys.exit(1)

    video_num = int(sys.argv[1])
    slug = sys.argv[2].strip().lower().replace(" ", "-")
    title = sys.argv[3].strip()

    dir_name = f"{video_num:02d}_{slug}"
    base_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = os.path.join(base_dir, "videos", dir_name)

    print(f"🎬 Initializing ThinkLate Workspace for Video {video_num}: '{title}'...")
    print(f"📁 Target Directory: {target_dir}")

    # Create directory tree
    assets_dir = os.path.join(target_dir, "assets")
    audio_dir = os.path.join(target_dir, "audio_takes")
    brand_dir = os.path.join(target_dir, "brand_assets")
    os.makedirs(assets_dir, exist_ok=True)
    os.makedirs(audio_dir, exist_ok=True)
    os.makedirs(brand_dir, exist_ok=True)

    # 1. Copy audit_audio.py and master_take.py if exist in video 01 or root
    v1_audit = os.path.join(base_dir, "videos", "01_is-ai-a-bubble-ask-the-railways", "audit_audio.py")
    target_audit = os.path.join(target_dir, "audit_audio.py")
    if os.path.exists(v1_audit):
        shutil.copyfile(v1_audit, target_audit)
        print("  ✓ Copied audio auditor (audit_audio.py)")

    v1_master = os.path.join(base_dir, "videos", "01_is-ai-a-bubble-ask-the-railways", "master_take.py")
    target_master = os.path.join(target_dir, "master_take.py")
    if os.path.exists(v1_master):
        shutil.copyfile(v1_master, target_master)
        print("  ✓ Copied podcast audio master (master_take.py)")

    # 2. Copy brand assets (avatar master and expressions)
    v1_brand = os.path.join(base_dir, "videos", "01_is-ai-a-bubble-ask-the-railways", "brand_assets")
    if os.path.exists(v1_brand):
        for item in os.listdir(v1_brand):
            src_f = os.path.join(v1_brand, item)
            dst_f = os.path.join(brand_dir, item)
            if os.path.isfile(src_f):
                shutil.copyfile(src_f, dst_f)
        print("  ✓ Copied ThinkLate Owl Avatar master & expression assets")

    # 3. Generate AI-VIDEO-GENERATION-BIBLE.md
    bible_path = os.path.join(target_dir, "AI-VIDEO-GENERATION-BIBLE.md")
    bible_content = f"""# ThinkLate Video {video_num} — Master AI Video Generation & Compositing Bible
> **Video {video_num}: {title}**  
> **Channel:** ThinkLate (`@wethinklate`) | **Target Runtime:** ~6 minutes (10–13 Scenes)  
> **Aesthetic Standard:** BBC Storyville / Bloomberg Originals / Vox Borders. Zero PPT slides. 100% dynamic cinematic AI video, animated charts, and authentic primary evidence compositing.

---

## 🔒 Part 1: The Master Consistency Anchor (Style Lock)

Append our **Locked Consistency Suffix** to the end of **every single prompt** in Google Vids / Google Flow / Veo / Runway Gen-3 / Midjourney:

### 📋 The Style Lock Suffix (Append to every prompt):
```text
cinematic documentary photography, BBC historical documentary aesthetic, 35mm film grain, anamorphic lens, natural filmic lighting, deep slate navy #1B2A4A and warm amber #D99A2B color grading, realistic atmospheric haze, 8k resolution, photorealistic, 16:9 widescreen, no CGI look, no cartoon, no oversaturation, no artificial 3D render.
```

### 🚫 Negative Prompt (Paste in Negative Prompt box):
```text
cartoon, anime, 3d render, blender, cgi, bright plastic colors, stock footage watermark, text, typography, low quality, blur, deformed, oversaturated, amateur video, slideshow, powerpoint.
```

---

## 📐 Part 2: Screen Compositing Layouts (Where Everything Goes)

Never place raw flat screenshots over the whole screen. Instead, use these **3 Broadcast Compositing Layouts**:

### Layout 1: Full-Frame Cinematic AI Video (A-Roll or B-Roll)
* **Canvas:** 100% full-screen living 1080p AI video (slow 2% continuous camera tracking/push).
* **Used for:** Atmospheric world-building, macro operations, full-screen talking host.

### Layout 2: Split-Screen Evidence Card (Right 45% Overlay)
* **Left 55%:** Cinematic living AI video continuing in background.
* **Right 45%:** Dark slate navy `#1B2A4A` floating card with subtle 24px drop shadow containing the **authentic primary PDF screenshot**, with yellow animated highlighter sweep over the operative quote.

### Layout 3: Animated Number & Chart Callout (Left 50% Graphic)
* **Left 50%:** Dynamic graphic element (e.g. animated amber counter or diverging financial line chart).
* **Right 50%:** Ambient atmospheric video or host presenter.

---

## 🎬 Part 3: Scene-by-Scene Visual Generation & Compositing Blueprint

*(Fill in per scene as script is finalized)*

### SCENE 1: The Hook / Cold Open
* **Spoken Dialogue:**  
  *"(First 15 seconds opening hook // direct, personal dilemma ////)"*
* **Visual Breakdown & Timing:**
  * `00:00 – 00:06`: **A-Roll (Full-Body Host Presenter)** standing centered in dark navy studio.
  * `00:06 – 00:18`: **B-Roll (Cinematic AI Video)** — Slow camera push into macro subject.
* **AI Video Generation Prompt (B-Roll):**
  > `Cinematic wide tracking shot of [SUBJECT]. Moody atmospheric lighting, deep slate navy #1B2A4A and warm amber #D99A2B color grading, 35mm documentary film grain, anamorphic lens, 8k resolution, photorealistic, 16:9 widescreen.`
* **📸 Manual Screenshot Source & Capture Guide:**
  * **Source URL:** [URL to Primary Document]
  * **Direct PDF:** [Direct PDF Link] (or local `assets/[filename].pdf`)
  * **Where to screenshot:** Page X, Paragraph Y.
  * **Verbatim Text to Highlight:** *"..."*
  * **Lower-Third Banner:** `assets/LT_S01.png`

---

## 🛠️ Step-by-Step Compositing in Google Vids / Editor

1. **Track 1 (Bottom): AI Video B-Roll** (1080p clips generated using prompts above).
2. **Track 2: A-Roll Host Clips** (Animated ThinkLate Owl clips at anchor moments).
3. **Track 3: Evidence Overlay Cards (Right 45%)** (High-DPI primary screenshots with 0.3s slide-in).
4. **Track 4: Lower-Third Citations** (Transparent PNG banners, fade in at +1.0s, hold 5s).
5. **Track 5: Audio Narration & Ambient Music** (Recorded takes + ambient drone at -22 dB).
"""
    with open(bible_path, "w", encoding="utf-8") as f:
        f.write(bible_content)
    print("  ✓ Created AI-VIDEO-GENERATION-BIBLE.md")

    # 4. Generate SCREENSHOT-GUIDE.md
    guide_path = os.path.join(target_dir, "SCREENSHOT-GUIDE.md")
    guide_content = f"""# Video {video_num} — Manual Evidence Screenshot & Primary Source Guide
> **Channel:** ThinkLate (`@wethinklate`) | **Episode {video_num}:** *{title}*  
> **Purpose:** Direct web URLs, local PDF file links, exact page/paragraph coordinates, and browser capture instructions for manually capturing crisp, high-DPI screenshots.

---

## 💡 Quick Tips for Clean, High-DPI Screenshots

1. **Browser Zoom:** Zoom your browser to **125% or 150%** before taking the screenshot so text is crisp and vector-sharp in 1080p/4K video.
2. **Authentic Styling:** Keep authentic white paper or publication styling; avoid dark-mode plugins that invert PDF colors unnaturally.
3. **Margins:** Capture at least 30–50px of breathing room around paragraphs or charts.
4. **Compositing:** Save your manual crops into `assets/` to link directly into your video timeline.

---

## 📑 Primary Source Evidence Catalog

*(Add 3–5 verified primary sources below)*

### Screenshot 1: [Primary Source Title] (`Scene X` — Take X)
* **Topic:** [Topic / Claim]
* **Web URL:** [Web URL]
* **Direct Web PDF:** [PDF URL]
* **Local Offline PDF:** [Local PDF Path]
* **Exact Location:** Page X, Paragraph Y.
* **Verbatim Text to Highlight:**
  > *"..."*
* **Video Layout:** Right 45% floating card over living AI B-roll.
* **Citation Lower-Third Overlay:** `assets/LT_S0X.png`

---

## 📂 Quick Links Directory

| Scene | Target Document | Web Link | Offline PDF Link | Exact Page & Crop |
| :--- | :--- | :--- | :--- | :--- |
| **Scene 1** | Primary Source 1 | [URL]() | [Local File]() | Page 1 Header |
"""
    with open(guide_path, "w", encoding="utf-8") as f:
        f.write(guide_content)
    print("  ✓ Created SCREENSHOT-GUIDE.md")

    # 5. Generate script.md template
    script_path = os.path.join(target_dir, "script.md")
    script_content = f"""# Script — Video {video_num}: {title}
> **Target Runtime:** ~6 minutes | **Pacing:** 130–150 WPM (Indian-Global English)  
> **Hard Rule:** Zero digits in spoken text (spell out all numbers: fifteen, three hundred).  
> **Pause Notation:** `//` = micro-breath (0.3s), `///` = 1-second beat, `////` = 2-second dramatic beat.

---

### [TAKE 1] — The Hook (00:00 – 00:15)
* **Visual Cue:** `[A-ROLL: Full-Body Host]` ➔ `[B-ROLL: Cinematic Push]`
* **Tone Directive:** `[Conversational, intimate, grounded]`
* **Spoken Narration:**  
  *"(Spoken text here with explicit pause notations // and spelled-out numerals ////)"*

---

### [TAKE 2] — The Core Thesis Promise (00:15 – 00:40)
* **Visual Cue:** `[A-ROLL: Medium Host]` ➔ `[KINETIC CARDS: Thesis]`
* **Tone Directive:** `[Direct, confident, intellectual authority]`
* **Spoken Narration:**  
  *"(Spoken text here // leading into the core thesis ////)"*
"""
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(script_content)
    print("  ✓ Created script.md")

    # 6. Generate sources.md and NOTEBOOKLM-SOURCES.md
    sources_path = os.path.join(target_dir, "sources.md")
    sources_content = f"""# Sources & Primary Verification — Video {video_num}: {title}

| ID | Author / Entity | Year | Document Title | Primary URL | Verified Claim |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **S1** | Author | 2024 | Title | https://... | Claim verified on page X |
"""
    with open(sources_path, "w", encoding="utf-8") as f:
        f.write(sources_content)

    nlm_path = os.path.join(target_dir, "NOTEBOOKLM-SOURCES.md")
    nlm_content = f"""# Google NotebookLM Source Pack — Video {video_num}: {title}
> Ingest these primary URLs into your NotebookLM project (`ThinkLate Video {video_num}`).

### Source 1: [Document Title]
* **URL:** https://...
* **Direct PDF:** https://...
* **Key Evidence:** Page X quote.
"""
    with open(nlm_path, "w", encoding="utf-8") as f:
        f.write(nlm_content)
    print("  ✓ Created sources.md & NOTEBOOKLM-SOURCES.md")

    # 7. Generate recording_studio.html
    studio_path = os.path.join(target_dir, "recording_studio.html")
    # Read template from video 1 if available
    v1_studio = os.path.join(base_dir, "videos", "01_is-ai-a-bubble-ask-the-railways", "recording_studio.html")
    if os.path.exists(v1_studio):
        with open(v1_studio, "r", encoding="utf-8") as f:
            studio_html = f.read()
        # customize title
        studio_html = re.sub(r"ThinkLate Recording Studio — Video 1.*?</title>", f"ThinkLate Recording Studio — Video {video_num}: {title}</title>", studio_html)
        studio_html = re.sub(r"Video 1: Is AI a Bubble\? Ask the Railways", f"Video {video_num}: {title}", studio_html)
        with open(studio_path, "w", encoding="utf-8") as f:
            f.write(studio_html)
        print("  ✓ Generated pre-wired recording_studio.html teleprompter")

    print("\n🎉 Turnkey Workspace Ready!")
    print(f"👉 Path: {target_dir}")
    print("\nNext Steps:")
    print("1. Add your NotebookLM sources to NOTEBOOKLM-SOURCES.md")
    print("2. Draft script.md & populate AI-VIDEO-GENERATION-BIBLE.md prompts")
    print(f"3. Open http://localhost:8080/videos/{dir_name}/recording_studio.html to record your takes")
    print(f"4. Run: python audit_audio.py audio_takes/take_01.wav 1 to verify acoustics")

if __name__ == "__main__":
    main()
