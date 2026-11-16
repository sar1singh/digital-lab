# Off Script — 3D AI Anime Avatar Setup Guide ($0 Cost)

> **Channel:** Off Script (`@OffScriptEddy`)  
> **Host Persona:** Eddy (The Unfiltered Developer / Gamer)  
> **Aesthetic:** Dark Noir / Graphic Novel / Cyberpunk Hoodie Gamer  
> **Method:** Real-Time AI Computer Vision Tracking (Webcam $\rightarrow$ Warudo $\rightarrow$ OBS Studio)  
> **Total Software Cost:** **$0.00** (100% Free, Zero Cloud GPU Bills)

---

## 1. System Architecture Overview

```
[Standard USB Webcam / Smartphone]
              │
              ▼ (Real-time Video Feed)
[Warudo Engine (Steam App 2074980)]
   ├── AI Face & Eye Tracking (MediaPipe / Google CV)
   ├── Hand & Gesture Tracking (MediaPipe)
   ├── Audio Lip-Sync (Microphone Frequency Analysis)
   └── 3D Avatar Physics (.vrm model with cloth & hair dynamics)
              │
              ▼ (Direct Memory / Spout2 / Window Capture with Alpha)
[OBS Studio (Track 3: Over Gameplay Canvas)]
   ├── Video Track 1: 4K PC Gameplay (AC Black Flag / TLoU / RDR2)
   ├── Video Track 2: Optional Subtle Focus Blur Under Avatar
   ├── Video Track 3: 3D Animated Eddy Avatar (Bottom-Right / Bottom-Left)
   └── Audio Track 1: Master Voiceover with Dynamic Game Audio Ducking (-24 dB)
```

---

## 2. Phase 1: Install the Free Software Stack

Both tools are official, trusted, and available directly through Steam:

1. **Warudo (The Tracking & Physics Engine):**
   * Steam Store Link: [Warudo on Steam](https://store.steampowered.com/app/2074980/Warudo/)
   * 1-Click Steam URI: `steam://install/2074980`
   * *What it does:* Loads your 3D `.vrm` character, runs AI webcam tracking (using Google MediaPipe), calculates realistic hair/clothing physics, and sends the video feed to OBS with transparent background.

2. **VRoid Studio (The 3D Character Creator):**
   * Steam Store Link: [VRoid Studio on Steam](https://store.steampowered.com/app/1486350/VRoid_Studio_v1260/)
   * 1-Click Steam URI: `steam://install/1486350`
   * *What it does:* Free 3D modeling tool designed specifically for anime characters. Let you customize face shape, hair strands, eyes, hoodies, jackets, and accessories, and exports standard `.vrm` files with complete bone rigs and blendshapes.

---

## 3. Phase 2: Sourcing Eddy's 3D Model (`.vrm`)

You have two paths to get Eddy's avatar file:

### Option A: Build Eddy in VRoid Studio (Recommended — 20 Minutes)
* Open VRoid Studio $\rightarrow$ Click **New Model (Male)**.
* Match Eddy's signature brand persona:
  * **Hair:** Dark messy anime hair with slight stylized fringe.
  * **Face:** Sharp, confident eyes (matching the dark noir comic aesthetic).
  * **Outfit:** Dark oversized hoodie (black/charcoal `#1A1A1A`) with electric cyan or hazard amber accent stripes.
  * **Accessories:** Over-ear gaming headphones.
* Click **Export as VRM** $\rightarrow$ Choose **VRM 0.0 or 1.0** $\rightarrow$ Save as `Eddy_OffScript_v1.vrm` in `digital-lab/03-content-lab/off-script/avatar/`.

### Option B: Download a Free Pre-Made Community Model
* If you want to test in 60 seconds without creating a model:
  * Browse [VRoid Hub](https://hub.vroid.com/) or [Booth.pm](https://booth.pm/en/items?tags%5B%5D=VRM).
  * Filter by **Free** and **Commercial Use: OK**.
  * Download any `.vrm` file into this directory.

---

## 4. Phase 3: Calibrating AI Tracking in Warudo

1. **Launch Warudo from Steam.**
2. **Load Character:**
   * In the main menu, click **Character** $\rightarrow$ **Load Custom Character** $\rightarrow$ Select your `.vrm` file.
3. **Setup Camera & AI Tracking:**
   * Go to **Onboarding / Tracking Setup** or the **Trackers** panel.
   * Select **Tracker Type:** `MediaPipe Tracker` (built-in AI vision).
   * **Camera:** Select your webcam from the dropdown list.
   * **Tracking Scope:**
     * Enable **Face Tracking** (Tracks head rotations, eye gaze, blinks, eyebrow raises).
     * Enable **Hand Tracking** (Optional: allows you to gesture with your hands while speaking).
   * **Lip-Sync Method:**
     * Select **Audio Lip-Sync (Recommended)**: Set audio input to your primary recording microphone. This guarantees 100% accurate mouth opening and syllable sync even when your face is partially shadowed.
4. **Calibrate:**
   * Sit comfortably in your normal gaming chair, look straight at your monitor, and click **Calibrate**.

---

## 5. Phase 4: Routing into OBS Studio (Zero Green-Screen Keying)

Never use a green screen. Warudo outputs native alpha transparency directly to OBS:

### Method A: Spout2 (Best Quality & Lowest Latency)
1. In Warudo: Go to **Settings** $\rightarrow$ **Output** $\rightarrow$ Enable **Spout2 Output**. Set background to **Transparent**.
2. In OBS Studio:
   * Click `+` under **Sources** $\rightarrow$ Add **Spout2 Capture**.
   * Select **Warudo** from the dropdown.
   * Check **Composite mode: Default (Premultiplied alpha)**.
   * *Result:* Crisp 3D anime Eddy floating with perfect transparent edges and zero green spill.

### Method B: Game Capture (Standard Fallback)
1. In Warudo: Set window background color to **Transparent**.
2. In OBS Studio:
   * Click `+` under **Sources** $\rightarrow$ Add **Game Capture**.
   * Mode: **Capture specific window** $\rightarrow$ Select `[Warudo.exe]`.
   * Check **Allow Transparency**.

---

## 6. Phase 5: Placement & Audio Dynamics on the Gameplay Spine

1. **Positioning in OBS:**
   * Scale the avatar to occupy roughly **15% to 20% of screen height** in the **bottom-right** or **bottom-left** corner.
   * Ensure it does not cover critical game HUD elements (minimap or weapon inventory).
2. **Audio Ducking Automation:**
   * When Eddy speaks, gameplay audio automatically ducks down to `-24 dB`.
   * During the scheduled **[GAME AUDIO TAKEOVER]** pauses (every 8–10 minutes), stop speaking, let the avatar idle naturally with breathing physics, and let the Caribbean sea audio surge back up to `-10 dB`.

---

## 7. Lighting & Hardware Optimization Tips
* **Webcam Lighting:** Frontal soft light is ideal. A standard desk lamp or monitor light bar reflecting off a wall prevents tracking jitter.
* **Frame Rate Cap:** In Warudo settings, cap target FPS to **60 FPS** to minimize GPU load so your PC dedicates 95% of graphics resources to Assassin's Creed Black Flag.
