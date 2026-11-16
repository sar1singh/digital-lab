# ThinkLate Video 04 — DaVinci Resolve Import & Automation Architecture

> **Episode:** *"Why You Will Never Own Anything Again"* (`04_the-subscription-trap`)  
> **Master FCPXML:** [`ThinkLate_Video04_DaVinci.fcpxml`](ThinkLate_Video04_DaVinci.fcpxml)  
> **Master EDL:** [`ThinkLate_Video04.edl`](ThinkLate_Video04.edl)  
> **Rendered Master MP4:** [`ThinkLate_Video04_The_Subscription_Trap.mp4`](ThinkLate_Video04_The_Subscription_Trap.mp4)  

---

## ⚡ 1-Click DaVinci Resolve Import Guide

If you want to open and inspect or polish the project in **DaVinci Resolve**, follow these simple steps:

1. **Launch DaVinci Resolve** and open a new or existing Project (`1080p` or `1440p` at `30 fps` or `60 fps`).
2. Go to the top menu:  
   **`File` ➔ `Import` ➔ `Timeline...`** (or press `Ctrl + Shift + I`).
3. Select the file:  
   `c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\04_the-subscription-trap\ThinkLate_Video04_DaVinci.fcpxml`
4. In the Import Dialog:
   - Check **"Link to source media files"**.
   - DaVinci will automatically populate:
     - **Track V1:** Continuous 1080p60 gameplay B-roll canvas (zoomed 1.15x).
     - **Track V2:** Scoped Blur markers positioned under all active text events.
     - **Track V3:** Full-screen graphic anchor plates (`anchor_01` to `anchor_07`), historical photos, quote cards, and animated SaaS multiplier charts.
     - **Track V4:** Kinetic typography slams (`card_cue01` to `card_cue39`) with transparent PNG overlays.
     - **Track A1:** Master Spoken Voiceover (`assets/audio/voiceover_mastered.mp3`) at `-5.0 dB`.
     - **Track A2:** Ambient Drone Bed (`assets/audio/ambient_music_dark_fog.mp3`) at `-23.0 dB`.
     - **Track A3:** Sub-Bass impact booms (`sfx_sub_boom.wav`) at `-12.0 dB`.
     - **Track A4:** Diegetic Foley whooshes and data blips at `-16.0 dB`.

---

## 🤖 The 100% Autonomous Video Assembly Engine

If you do NOT want to use DaVinci Resolve manually, the ThinkLate automated pipeline renders the full video headlessly:

```bash
# Run end-to-end automated video compilation via GPU NVENC
python digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/render_video_assembly.py
```

### What this autonomous pipeline does:
1. **Audio Mixing:** Automatically mixes dialogue, ducked ambient music, and SFX cues with **leading J-cut offsets (-120ms)** and **trailing L-cut offsets (+200ms)** to ensure audio momentum pulls the viewer into each scene.
2. **GPU NVENC Scene Compositing:** Uses hardware-accelerated NVENC to render all 39 scenes with:
   - Dynamic 3% Ken Burns slow pushes on all static plates.
   - Gaussian Scoped Blur + 35% dark tint on gameplay during text moments.
   - Smooth alpha fades on kinetic typography.
   - Programmatic MP4 chart integration.
3. **Stream Concatenation & Multiplexing:** Stitches all 39 scenes and multiplexes the 4-track master audio into the final broadcast MP4.
4. **Quality Control Audit:** Automatically runs `qc_video.py` to audit loudness compliance (`-16.0` to `-18.5 LUFS`) and verify zero stream sync drift.

