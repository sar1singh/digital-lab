---
name: thinklate-visual-qc
description: Visual elements, cinematic B-roll, and animation quality control skill for ThinkLate documentaries. Eliminates static slideshow feel via the 3-second stagnation rule, generates Google Vids cinematic AI prompts, orchestrates real document overlays, and choreographs ThinkLate Owl Avatar host appearances.
---

# ThinkLate Visual Elements & Cinematic QC Skill

## Purpose
Eradicates the static "PowerPoint presentation" feel, orchestrates cinematic motion via Ken Burns effects, generates dynamic Google Vids scene prompts, and integrates the ThinkLate Anime Owl mascot host.

## Mandatory Quality Standards
1. **The 3-Second Stagnation Rule:**
   - No still image, document screenshot, or chart may sit frozen for more than 3 seconds without dynamic motion.
   - Every background shot must feature continuous slow 2% push-in (`zoompan` / Ken Burns effect) or camera tracking.
2. **Authentic Primary Evidence over Vector Placeholders:**
   - Prefer real high-resolution scans of opened academic papers, share certificates, and institutional charts with authentic highlighting.
3. **Lower-Third Choreography:**
   - Enters at **1.0s** after scene transition via a smooth slide-in or 0.4s crossfade.
   - Holds for **4.0 to 6.0 seconds** during the citation spoken dialogue.
   - Exits smoothly before the next thought break.

## Google Vids & AI Video Prompt Generation Workflow
For creating dynamic, living background video footage without visual drift:
- **Mandatory Deliverable:** Generate `AI-VIDEO-GENERATION-BIBLE.md` matching **every scene and dialogue line** to an explicit AI video generation prompt.
- **Master Consistency Anchor (Style Lock Suffix):**
  Append to every prompt:
  ```text
  cinematic documentary photography, BBC historical documentary aesthetic, 35mm film grain, anamorphic lens, natural filmic lighting, deep slate navy #1B2A4A and warm amber #D99A2B color grading, realistic atmospheric haze, 8k resolution, photorealistic, 16:9 widescreen, no CGI look, no cartoon, no oversaturation, no artificial 3D render.
  ```
- **Negative Prompt:**
  ```text
  cartoon, anime, 3d render, blender, cgi, bright plastic colors, stock footage watermark, text, typography, low quality, blur, deformed, oversaturated, amateur video, slideshow, powerpoint.
  ```
- **3 Broadcast Compositing Layouts:**
  1. **Layout 1:** Full-Frame Living AI Video (100% canvas with continuous 2% camera push).
  2. **Layout 2:** Split-Screen Evidence Card (Left 55% AI B-roll, Right 45% floating PDF screenshot with drop shadow and yellow highlight).
  3. **Layout 3:** Animated Number / Chart Graphic (Left 50% amber counter/chart, Right 50% ambient B-roll or host).
- **Manual Evidence Sourcing:** Every scene featuring evidence must provide exact web links, direct PDF links, offline PDF paths, and page numbers for manual high-DPI capture.

## ThinkLate Owl Avatar Choreography
The ThinkLate mascot (`brand/00_MASTER_avatar.png`, `expressions/E1_neutral.png`, `expressions/E4_talking.png`) acts as the intelligent documentary host:
- **Rule of Economy:** Do NOT keep the avatar on screen 100% of the time (avoid looking like a low-effort streamer cam).
- **The 4 Anchor Host Moments:**
  1. **Scene 1–2 (Cold Open / Thesis Promise):** Host appears in lower corner card with `E1_neutral` / `E4_talking` introducing the inquiry.
  2. **Scene 4 (Historical Pivot):** Host appears for the deadpan transition: *"So... let's look at the railways."*
  3. **Scene 8–9 (The Invariant Payoff):** Host delivers the channel thesis: *"The tracks survived. The shareholders didn't."*
  4. **Scene 13 (Lingering Close):** Host looking directly at viewer with the concluding philosophical question.
- **Visual Styling:** Contained inside an amber-bordered circular or pill card on deep slate navy `#1B2A4A` with subtle talking pulse animation.
