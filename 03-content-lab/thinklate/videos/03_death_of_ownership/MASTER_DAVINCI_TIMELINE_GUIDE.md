# ThinkLate Video 03 — Master DaVinci Resolve Timeline & SFX Editing Guide
> **Episode:** *"You Don't Own What You Buy."* (`03_death_of_ownership`)  
> **Channel:** ThinkLate (`@wethinklate`) | **Target Runtime:** 10m 07s  
> **Aesthetic Standard:** BBC Storyville / Bloomberg Originals / Vox Borders  
> **Master Audio:** `assets/voiceover_raw_mastered.wav` (10m 07s | 222 Whisper segments)  
> **Master BGM:** `assets/bgm_leberch_loop_master.wav` (10m 50s continuous loop)  

---

## 🛠️ 1. The Step-by-Step DaVinci Resolve Assembly Protocol

Follow these 9 phases sequentially to assemble the video from scratch:

### Phase 1: Project Setup & Media Import
1. Open DaVinci Resolve $\rightarrow$ Create a new project named: `ThinkLate_03_Death_of_Ownership`.
2. Open **Project Settings** (Gear icon bottom right):
   - **Timeline Resolution:** `1920 x 1080 Processing` (or `3840 x 2160` if mastering in 4K).
   - **Timeline Frame Rate:** `60 fps` (matching your gameplay capture) or `30 fps`.
3. In the **Media Pool**, drag the entire [`assets/`](file:///c:/Users/sar1s/Documents/MyWork/Git/digital-lab/03-content-lab/thinklate/videos/03_death_of_ownership/assets/) folder and your gameplay file `ACBF_Full_GamePlay_1.mp4`.

### Phase 2: Laying the Spoken Audio Spine (Audio Track 1)
1. Drag [`voiceover_raw_mastered.wav`](file:///c:/Users/sar1s/Documents/MyWork/Git/digital-lab/03-content-lab/thinklate/videos/03_death_of_ownership/assets/voiceover_raw_mastered.wav) onto **Audio Track 1 (A1)**.
2. Snap the start of the audio file strictly to **`00:00:00:00`**.
3. Right-click track header A1 $\rightarrow$ Click **Lock Track** temporarily so your spoken timing never accidentally shifts while editing video.

### Phase 3: The 7 Chapter Breath Breaks (Blade Cuts)
Listen to the voiceover or use the timeline playhead to find the 7 natural chapter pauses. Add timeline markers (Press `M`) or use the Blade tool (`B`) to slice the track at these exact timestamps:
* **Break 1 (`02:01 – 02:03`):** 2.5s pause after Act 1 Hook.
* **Break 2 (`04:16 – 04:18`):** 2.0s pause after Gabe Newell quote.
* **Break 3 (`04:58 – 05:01`):** 3.0s pause before Act 3 "Follow the Money".
* **Break 4 (`05:28 – 05:30`):** 2.0s dramatic pause before *"Exactly $0"*.
* **Break 5 (`06:25 – 06:27`):** 2.0s transition into the India disc market segment.
* **Break 6 (`07:46 – 07:49`):** 3.0s pause before Act 4 Digital Resistance.
* **Break 7 (`10:03 – 10:04`):** 1.5s pause before the final outro punchline.

### Phase 4: Laying Background Ambience & Music (Audio Track 2)
1. Drag [`bgm_leberch_loop_master.wav`](file:///c:/Users/sar1s/Documents/MyWork/Git/digital-lab/03-content-lab/thinklate/videos/03_death_of_ownership/assets/bgm_leberch_loop_master.wav) onto **Audio Track 2 (A2)**, starting at `00:00:00`.
2. Set the track fader volume to **`-23.0 dB`**.
3. During the 7 breath breaks listed in Phase 3, keyframe the volume to swell up to **`-16.0 dB`**, then dip back down to **`-23.0 dB`** as soon as speech resumes.

### Phase 5: Laying the Gameplay Base Canvas (Video Track 1)
1. Drag `ACBF_Full_GamePlay_1.mp4` onto **Video Track 1 (V1)**.
2. Select the gameplay clip $\rightarrow$ Open **Inspector** $\rightarrow$ Set **Zoom** to **`1.15x`** (this crops out the minimap, health bar, and HUD icons).
3. Cut and curate dynamic moments:
   - High-seas naval combat and sailing during dramatic arguments.
   - City parkour and rooftop sprints during fast-paced commentary.
   - 360° viewpoint synchronization pans during the 7 breath breaks.
   - Delete all idle walking or aimless street running.

### Phase 6: Adding Full-Screen Foreground Media (Video Track 3)
*Whenever the schedule calls for an AI video, hero image, evidence card, or animated chart, place it on **Video Track 3**:*
1. **AI Videos:**
   - Place [`discu_breaking.mp4`](file:///c:/Users/sar1s/Documents/MyWork/Git/digital-lab/03-content-lab/thinklate/videos/03_death_of_ownership/assets/discu_breaking.mp4) at `00:00 – 00:02.7`.
   - Place [`video_game_case_open.mp4`](file:///c:/Users/sar1s/Documents/MyWork/Git/digital-lab/03-content-lab/thinklate/videos/03_death_of_ownership/assets/video_game_case_open.mp4) at `00:02.7 – 00:11.5`.
2. **Hero AI Images:**
   - Apply a **3% Ken Burns Slow Push** on each hero photo (Inspector $\rightarrow$ Keyframe Zoom from `1.000` at start to `1.030` at end).
3. **Evidence Cards & Animated Chart:**
   - Drop the animated chart [`CHART_SALES_COLLAPSE_animated.mp4`](file:///c:/Users/sar1s/Documents/MyWork/Git/digital-lab/03-content-lab/thinklate/videos/03_death_of_ownership/assets/CHART_SALES_COLLAPSE_animated.mp4) at `05:38 – 05:52`.
   - Place evidence cards right after their corresponding hero image (The 1-2 Cut).
4. **Strict Rule:** **LEAVE TRACK 2 EMPTY (NO BLUR)** under all Track 3 media clips.

### Phase 7: Kinetic Typography & Gaussian Blur (Tracks V4 & V2)
*Whenever the schedule calls for a transparent Kinetic Typography slam (`KT_01` to `KT_09`):*
1. Place the transparent PNG on **Video Track 4 (V4)**.
2. In the **Effects Library**, find **Adjustment Clip** and drag it onto **Video Track 2 (V2)** for the *exact duration* of the text slam.
3. On that Adjustment Clip:
   - Add **Gaussian Blur** effect (Blur Strength: `0.18`).
   - In Inspector $\rightarrow$ Set **Composite Opacity** to `85%` (darkens gameplay so text stands out).

### Phase 8: Synchronizing Sound Effects (Audio Tracks A3 & A4)
1. **Track A3 (Heavy Impacts):**
   - Place [`cinematic-impact-boom.mp3`](file:///c:/Users/sar1s/Documents/MyWork/Git/digital-lab/03-content-lab/thinklate/videos/03_death_of_ownership/assets/cinematic-impact-boom.mp3) or [`sfx_sub_boom.wav`](file:///c:/Users/sar1s/Documents/MyWork/Git/digital-lab/03-content-lab/thinklate/videos/03_death_of_ownership/assets/sfx_sub_boom.wav) (Fader: `-12 dB` to `-14 dB`) at frame 0 of every text slam and chapter break.
2. **Track A4 (Movement & UI):**
   - Place [`whoosh-cinematic.mp3`](file:///c:/Users/sar1s/Documents/MyWork/Git/digital-lab/03-content-lab/thinklate/videos/03_death_of_ownership/assets/whoosh-cinematic.mp3) (Fader: `-16 dB` to `-18 dB`) 3 to 4 frames before an evidence card slides onto screen.
   - Place [`swoosh-sound-effect-for-fight-scenes-or-transitions-.mp3`](file:///c:/Users/sar1s/Documents/MyWork/Git/digital-lab/03-content-lab/thinklate/videos/03_death_of_ownership/assets/swoosh-sound-effect-for-fight-scenes-or-transitions-.mp3) (Fader: `-18 dB` to `-20 dB`) for quick cuts.
   - Place [`sfx_data_blip.wav`](file:///c:/Users/sar1s/Documents/MyWork/Git/digital-lab/03-content-lab/thinklate/videos/03_death_of_ownership/assets/sfx_data_blip.wav) on highlighted clauses and price badges.

### Phase 9: Fairlight Audio QC & Export Delivery
1. Switch to the **Fairlight** page:
   - Verify integrated loudness sits at **`-14 LUFS`** ($\pm 1$ LUFS).
   - Ensure True Peak does not exceed **`-1.0 dBFS`**.
2. Switch to the **Deliver** page:
   - Format: `MP4` or `QuickTime`.
   - Video Codec: `H.264` or `H.265 Master`.
   - Resolution: `1920x1080` (or `3840x2160`).
   - Frame rate: `60 fps` (or `30 fps`).
   - Audio: `Linear PCM` or `AAC 320 kbps`, `48 kHz`, Stereo.

---

## 🎚️ 2. The Timeline Track Architecture

```
════════════════════════════════════════════════════════════════════════════════════════════════════════════
VIDEO TRACKS
────────────────────────────────────────────────────────────────────────────────────────────────────────────
Video Track 4 (V4) │ [TRANSPARENT SLAMS] Kinetic Typography Slams (KT_01 to KT_09).
Video Track 3 (V3) │ [FULL-SCREEN MEDIA] Broadcast Evidence Cards, Animated Sales Chart MP4,
                   │                     Full-Screen Hero Photos (Ken Burns), or Video (discu_breaking.mp4).
Video Track 2 (V2) │ [DYNAMIC FOCUS CLIP] Adjustment Clip with Gaussian Blur (0.18) + Dimming (85% Opacity).
                   │  ⚠️ STRICT RULE:
                   │     • V3 Full-Screen Media: TRACK 2 IS EMPTY (NO BLUR).
                   │     • V4 Transparent Text:  TRACK 2 IS ACTIVE (GAUSSIAN BLUR ON).
                   │     • Clean Gameplay:       TRACK 2 IS EMPTY (100% Crisp 60fps Gameplay).
Video Track 1 (V1) │ [SPINE BASE] Assassin's Creed: Black Flag 1080p60 (Zoom: 1.15x to crop HUD/minimap).
────────────────────────────────────────────────────────────────────────────────────────────────────────────
AUDIO TRACKS
────────────────────────────────────────────────────────────────────────────────────────────────────────────
Audio Track 1 (A1) │ [VOICEOVER] voiceover_raw_mastered.wav (Locked at 00:00:00, cut at 7 Breath Breaks).
Audio Track 2 (A2) │ [BGM] bgm_leberch_loop_master.wav (Set to -23 dB; swells to -16 dB during Breath Breaks).
Audio Track 3 (A3) │ [IMPACT SFX] sfx_sub_boom.wav, deep sub-bass braams, heavy chapter hits (-12 dB to -15 dB).
Audio Track 4 (A4) │ [MOVEMENT & UI SFX] sfx_whoosh.wav, sfx_data_blip.wav, foley clicks (-16 dB to -20 dB).
════════════════════════════════════════════════════════════════════════════════════════════════════════════
```

---

## 🔊 3. SFX Toolkit & Sound Architecture

### A. Local Files Ready in `assets/` (WAV & Downloaded MP3)
You now have 6 production-ready sound effects directly in your project [`assets/`](file:///c:/Users/sar1s/Documents/MyWork/Git/digital-lab/03-content-lab/thinklate/videos/03_death_of_ownership/assets/) folder:

1. **Impacts & Booms (Audio Track 3 | Fader: -12 dB to -14 dB):**
   - **`cinematic-impact-boom.mp3` (New Download):** Deep, resonant cinematic impact boom. Perfect for Chapter Breaks 1, 3, 6, 7 and heavy text slams.
   - **`sfx_sub_boom.wav`:** Sub-bass braam / punch. Ideal for fast kinetic typography hits (`KT_02`, `KT_06_ZERO_DOLLARS`).

2. **Whooshes & Swooshes (Audio Track 4 | Fader: -16 dB to -20 dB):**
   - **`whoosh-cinematic.mp3` (New Download):** Wide, sweeping cinematic air whoosh. Place 3–4 frames before large evidence cards (`EVID_01`, `EVID_03`, `CARD_FIRST_SALE_1908_hero.png`) or the animated chart.
   - **`swoosh-sound-effect-for-fight-scenes-or-transitions-.mp3` (New Download):** Snappy, aggressive transition swoosh. Ideal for rapid kinetic typography entries and gameplay action beats (sword parry at 00:54).
   - **`sfx_whoosh.wav`:** Clean broadcast whoosh for quick UI reveals.

3. **UI Data Blips (Audio Track 4 | Fader: -18 dB to -20 dB):**
   - **`sfx_data_blip.wav`:** Subtle electronic tick for statutory highlights (AB 2426), price counters, and Steam cart warnings.

### B. Free DaVinci Resolve Built-in Sound Library
* **How to enable:** Go to the **Fairlight** tab at the bottom $\rightarrow$ Open the **Sound Library** window (top left) $\rightarrow$ Click **"Download Sound Library"** (Blackmagic provides an official 500+ sound effects pack covering whooshes, impacts, clicks, and ambient noise completely free).

### C. Recommended Free Foley (Pixabay Sound Effects / Freesound.org CC0)
If you want extra organic textures for specific real-world metaphors:
* **Plastic Case Click:** Search Pixabay for *"CD jewel case snap"* or *"box latch"* (for `CARD_EMPTY_CASE` at 00:02).
* **Cash Register Bell:** Search Pixabay for *"cash register bell"* (for *"Zero Dollars"* at 05:28).
* **Digital Access Denied Buzz:** Search Pixabay for *"error buzzer"* or *"access denied beep"* (for `CARD_PENTHOUSE_LOCK` at 02:04 and `EVID_06_BMW_HEATED_SEATS` at 07:14).

---

## 🖼️ 4. Revised Static Hero Image Prompts ("All Frames in a Single Image")
*Instead of temporal multi-second Veo video clips, these prompts condense the entire narrative arc into a single broadcast-grade 16:9 hero image. In DaVinci Resolve, apply a **subtle 3% Ken Burns slow push** (Zoom `1.000` $\rightarrow$ `1.030`) over the clip's duration.*

### Master Consistency Suffix (Append to all prompts):
```text
cinematic documentary photography, BBC historical documentary aesthetic, 35mm film grain, anamorphic lens, natural filmic lighting, deep slate navy #1B2A4A and warm amber #D99A2B color grading, realistic atmospheric haze, 8k resolution, photorealistic, 16:9 widescreen, no CGI look, no cartoon, no oversaturation, no artificial 3D render.
```

### Master Negative Prompt:
```text
cartoon, anime, 3d render, blender, cgi, bright plastic colors, stock footage watermark, text, typography, low quality, blur, deformed, oversaturated, amateur video, slideshow, powerpoint, disfigured hands, extra fingers.
```

---

### HERO PROMPT 01: The Empty Collector's Steelbook (All-in-One Frame)
* **Timecode:** 00:02 – 00:11 (8.8s) | **Asset:** `video_game_case_open.mp4` (AI Video 2) or `CARD_EMPTY_CASE.png`
* **Narrative:** Shows both the empty physical tray AND the tiny paper voucher code simultaneously in one macro shot.
```text
Cinematic macro top-angle shot of male hands opening a luxury matte-black embossed collector video game steelbook case on a dark walnut desk. The case is spread open flat, clearly displaying a completely empty circular plastic hub with no disc, and a solitary white paper voucher slip resting in the tray with a printed alphanumeric 16-digit download code. Warm amber tungsten desk lamp rim light, dark slate navy shadows, shallow depth of field, 35mm documentary film grain, BBC investigative aesthetic, 8k resolution, photorealistic, 16:9 widescreen.
```

---

### HERO PROMPT 02: Corporate Hyperscale Server Room Shutdown (Split Active/Dead)
* **Timecode:** 00:57 – 01:14 (17.0s) | **Asset:** `EVID_04_UBISOFT_CREW_LAWSUIT.png`
* **Narrative:** One continuous hallway where the background servers are glowing blue/green, while the foreground blade racks have all turned dark with pulsing crimson indicator lights.
```text
Cinematic eye-level photograph down an endless corridor of high-density server blade racks inside a hyperscale enterprise data center. The foreground server racks are completely powered down, with dark unlit chassis and flashing crimson error LEDs indicating terminated licenses, while the distant background racks still hum with cold blue lighting. Volumetric cold mist, industrial amber accents on the concrete floor, dramatic cinematic lighting, 35mm film grain, BBC Horizons technology documentary style, 8k photorealistic, 16:9 widescreen.
```

---

### HERO PROMPT 03: The $400k Penthouse Digital Lock Revocation
* **Timecode:** 02:04 – 02:24 (20.0s) | **Asset:** `CARD_PENTHOUSE_LOCK_HERO.png` + `CARD_PENTHOUSE_LOCK.png`
* **Narrative:** Macro framing of a luxury bronze door handle with an illuminated digital lock displaying 'ACCESS REVOKED', while rain streaks down floor-to-ceiling glass in the background.
```text
Cinematic close-up of a modern brushed-bronze luxury penthouse entrance door at twilight. An integrated digital smart lock keypad on the heavy door handle is illuminated in a stark crimson warning light displaying the text 'ACCESS REVOKED'. Wet exterior floor-to-ceiling glass windows in the soft-focus background reflect a moody rain-soaked city skyline. Warm amber interior foyer glow contrasting with cold teal exterior dusk, 35mm anamorphic documentary photography, photorealistic, 8k, 16:9 widescreen.
```

---

### HERO PROMPT 04: The 1908 Supreme Court First Sale Legal Tome
* **Timecode:** 02:40 – 03:12 (32.0s) | **Asset:** `CARD_FIRST_SALE_1908_hero.png` + `CARD_FIRST_SALE_1908.png`
* **Narrative:** Open antique leather law book with embossed gold lettering under a classic green banker's lamp.
```text
Cinematic atmospheric still photograph of an authentic 1900s mahogany law library reading room. A large antique leather-bound legal book lies open on the polished dark wood table beneath the warm directional glow of a brass and emerald-green glass banker's desk lamp. Floating dust motes dance in the amber light cone, with tall bookshelves of vintage gilded tomes receding into deep shadows. Rich archival texture, 35mm historical documentary film grain, 8k photorealistic, 16:9 widescreen.
```

---

### HERO PROMPT 05: Emerging Market Physical Disc Bazaar (India)
* **Timecode:** 06:27 – 06:45 (18.0s) | **Asset:** `CARD_INDIA_DISC_MARKET_HERO.png` + `EVID_05_INDIA_DISC_RESALE.png`
* **Narrative:** High-energy electronics arcade in Mumbai/Delhi with counters stacked high with physical PS4/PS5 disc cases and gamers trading discs.
```text
Cinematic documentary photograph inside a bustling electronics market arcade in Mumbai during evening hours. Glass display counters are densely stacked with physical blue PS4 and PS5 game disc cases. Two young South Asian gamers are seen in authentic natural interaction over the counter, inspecting a pre-owned game disc case. Warm tungsten and neon amber shop lights, natural urban atmosphere, deep contrast, 35mm documentary photography, BBC human interest aesthetic, 8k photorealistic, 16:9 widescreen.
```

---

### HERO PROMPT 06: Connected Car Subscription Paywall
* **Timecode:** 07:14 – 07:26 (12.0s) | **Asset:** `EVID_06_BMW_HEATED_SEATS_hero.png` + `EVID_06_BMW_HEATED_SEATS.png`
* **Narrative:** Inside a luxury cockpit at night, finger on the central touchscreen where a seat heater button has an overlaid pop-up modal: 'FEATURE LOCKED - $18/MO'.
```text
Cinematic macro shot inside a luxury modern automobile interior at night. Close-up on the sleek center-console OLED touchscreen showing a climate control menu, where the seat heater function is overlaid with an electric cyan and red subscription prompt reading '$18/MONTH - ACTIVATE SUBSCRIPTION'. Moody ambient cockpit LED lighting in cool teal and warm amber, rain streaking down the windshield in background, 35mm film grain, photorealistic, 8k, 16:9 widescreen.
```

---

### HERO PROMPT 07: 21st Century Freedom — The Offline Solid-State Drive
* **Timecode:** 09:54 – 10:07 (13.0s) | **Asset:** `KT_09_FREEDOM_OFFLINE_Hero.png` + `KT_09_FREEDOM_OFFLINE.png`
* **Narrative:** Heavy brushed-titanium external SSD on a dark slate desk with an amber pulsing activity light and braided USB-C cable.
```text
Cinematic low-angle still photograph of a rugged brushed-titanium external solid-state hard drive resting on a dark slate desk. A discreet warm amber LED activity indicator pulses along the metallic rim of the drive, connected via a heavy-duty braided USB-C cable. Minimalist workspace background, soft low-key architectural lighting, feeling of permanence, privacy, and digital sovereignty, 35mm documentary film grain, 8k resolution, photorealistic, 16:9 widescreen.
```

---

## 🎬 5. Complete Step-by-Step DaVinci Resolve Timeline Schedule (Exact Visuals & Text)

*Follow this table sequentially from 00:00:00 to 10:07:00 as you listen to `voiceover_raw_mastered.wav`.*

### ACT 1: THE $80 HOOK & TANGIBLE ABSURDITY (00:00 – 02:03)

| Timecode | Asset File in `assets/` | Track & Action | Track 2 Blur? | What the Viewer Sees on Screen (Exact Visual & Text) | Audio SFX & Track | Spoken Voiceover Trigger |
| :--- | :--- | :---: | :---: | :--- | :---: | :--- |
| **00:00 – 00:02** (2.7s) | `discu_breaking.mp4` | **Track V3** (Full-Screen Video) | **NO BLUR** | **Visual:** Macro 35mm footage of an iridescent holographic Blu-ray disc cracking across its surface on a dark slate pedestal. | `cinematic-impact-boom.mp3` (-12 dB) on **A3** at frame 0 | *"You paid eighty dollars for a brand new game."* |
| **00:02 – 00:11** (8.8s) | `video_game_case_open.mp4` (or `CARD_EMPTY_CASE.png`) | **Track V3** (Full-Screen Video / Card) | **NO BLUR** | **Visual:** Hands opening a matte-black steelbook case flat on a walnut desk.<br>**On-Screen Elements:** Empty circular disc tray (no disc) + a solitary white voucher paper slip printed with a 16-digit download code. | `whoosh-cinematic.mp3` (-18 dB) on **A4** at 00:02 | *"You walk home, unbox the collector case, and there is no disc. Just an empty plastic circle and a tiny paper slip with a printed code."* |
| **00:11 – 00:16** (5.0s) | *Clean Gameplay* | **Track V1** (1.15x HUD Crop) | **NO BLUR** | **Visual:** The Jackdaw ship cutting across high-seas ocean waves in vibrant 1080p60 color. No overlays. | Gameplay ocean waves / BGM bed (-23 dB) | *"Sony just launched a console for $700. It has no disc drive."* |
| **00:16 – 00:25** (9.2s) | `EVID_03_PS5_PRO_DISC_DRIVE.png` | **Track V3** (Full Card) | **NO BLUR** | **Visual:** Broadcast comparison card:<br>• **Left Box:** PS5 Pro Console: `$699.99 USD` (Disc-less Architecture)<br>• **Right Box:** Disc Drive Accessory: `+$79.99 USD` with red badge `[CURRENTLY OUT OF STOCK]`. | `whoosh-cinematic.mp3` (-18 dB) + `sfx_data_blip.wav` (-18 dB) on **A4** | *"Want to play the physical games you already own? Pay another $80 for the snap-on plastic drive... Assuming scalpers didn't buy them all first."* |
| **00:25 – 00:44** (19.0s) | *Clean Gameplay* | **Track V1** (1.15x HUD Crop) | **NO BLUR** | **Visual:** Edward Kenway walking through Havana colonial docks and harbor (clean 60fps gameplay). | BGM bed at -23 dB on **A2** | *"At the exact same time, retail giants like Best Buy wiped physical games... Over 90% digital... You worked 40 hours, paid $80, hit big green buy button."* |
| **00:44 – 00:54** (10.0s) | `KT_02_OWN_ZERO.png` | **Track V4** (PNG) + **Track V2** (Adjustment Clip) | **BLUR ACTIVE (0.18)** | **Exact On-Screen Typography:**<br>• Top Badge: `ACT 1 BODY • OVERLAY 04`<br>• Giant Bold Crimson Headline: **`YOU PAID $80. YOU OWN 0%.`**<br>• Subtext: `YOU DID NOT BUY A GAME. YOU RENTED A TEMPORARY PASS.`<br>• Dark slate card floating over blurred gameplay. | `cinematic-impact-boom.mp3` (-13 dB) on **A3** at 00:44 | *"Under corporate law, you own 0% of that purchase. You did not buy a game. You rented a temporary pass that can disappear tomorrow."* |
| **00:54 – 00:57** (3.0s) | *Clean Gameplay* | **Track V1** (1.15x HUD Crop) | **NO BLUR** | **Visual:** Quick sword parry and counter-kill in Havana street duel. | Sword clash foley + `swoosh-sound-effect-for-fight-scenes-or-transitions-.mp3` (-18 dB) on **A4** | *"Think that is an exaggeration?"* |
| **00:57 – 01:14** (17.0s) | `EVID_04_UBISOFT_CREW_LAWSUIT.png` | **Track V3** (Full Card) | **NO BLUR** | **Visual:** Legal court docket card:<br>• Header: `CLASS ACTION LAWSUIT: UBISOFT (DOCKET 3:24-CV-07482)`<br>• Highlighted Clause: *"Ubisoft reached into 12 million player libraries, revoked the digital licenses, and deleted the game files... every single copy vanished."* | `whoosh-cinematic.mp3` (-18 dB) + `sfx_data_blip.wav` (-18 dB) on **A4** | *"In 2024 Ubisoft shut down servers for The Crew... reached into 12 million player libraries and deleted the game files... Every single copy vanished."* |
| **01:14 – 01:21** (7.0s) | *Clean Gameplay* | **Track V1** (1.15x HUD Crop) | **NO BLUR** | **Visual:** The Jackdaw cutting through sea spray under bright tropical sunlight. | Ocean waves / wind audio | *"Sony did the exact same thing."* |
| **01:21 – 01:36** (15.0s) | `CARD_SONY_DISCOVERY.png` | **Track V3** (Full Card) | **NO BLUR** | **Visual:** PlayStation Store notification card:<br>• Red Warning Badge: `[ACCESS TERMINATED]`<br>• Text: *"Sony PlayStation revoking 1,312 Discovery TV episodes from player accounts due to licensing expiration."*<br>• Quotes user outrage forcing Sony back-pedal. | `whoosh-cinematic.mp3` (-18 dB) on **A4** at 01:21 | *"With 1,300 digital TV episodes... people bought entire seasons... Sony erasing them because contracts expired. Public rage forced Sony to back down..."* |
| **01:36 – 01:46** (10.0s) | `KT_03_SERVERS_DIE.png` | **Track V4** (PNG) + **Track V2** (Adjustment Clip) | **BLUR ACTIVE (0.18)** | **Exact On-Screen Typography:**<br>• Top Badge: `ACT 1 ENDING • OVERLAY 07`<br>• Giant Bold Headline: **`WHEN SERVERS DIE, YOUR PURCHASES DIE TOO.`**<br>• Subtext: `THE COMPANY HOLDS THE REMOTE KILL SWITCH.` | `cinematic-impact-boom.mp3` (-13 dB) on **A3** at 01:36 | *"When you buy digital goods, you are standing on quicksand. The company holds the remote switch and can pull the plug whenever they want."* |
| **01:46 – 01:55** (9.0s) | `CARD_GTA6_BOX.png` | **Track V3** (Full Card) | **NO BLUR** | **Visual:** Neon Vice City magenta/cyan card:<br>• GTA 6 physical retail box art with `$79.99` price tag.<br>• Giant yellow diagonal hazard banner across box: **`EMPTY BOX • DOWNLOAD CODE ONLY`**. | `whoosh-cinematic.mp3` (-18 dB) on **A4** at 01:46 | *"The biggest game in history, Grand Theft Auto 6, is landing at $80. Physical retail copies are shipping as download codes in empty plastic boxes."* |
| **01:55 – 02:01** (6.0s) | *Clean Gameplay* | **Track V1** (1.15x HUD Crop) | **NO BLUR** | **Visual:** Kenway standing on ship bow looking out across the golden horizon. | Warm BGM swell | *"We traded physical boxes for modern convenience. And in that trade, we accidentally gave up property rights that took centuries to build."* |
| **02:01 – 02:03** (2.5s) | **BREATH BREAK 1** | **Track V1** (Gameplay) | **NO BLUR** | **Visual:** Full 360° viewpoint synchronization camera sweep over coastal cliffs (Zero HUD). Chapter pause. | `cinematic-impact-boom.mp3` (-10 dB) on **A3** + BGM swell (-16 dB) on **A2** | *[Vocal Silence]* |

---

### ACT 2: THE LEGAL TRAP, CALIFORNIA AB 2426 & STEAM (02:04 – 05:01)

| Timecode | Asset File in `assets/` | Track & Action | Track 2 Blur? | What the Viewer Sees on Screen (Exact Visual & Text) | Audio SFX & Track | Spoken Voiceover Trigger |
| :--- | :--- | :---: | :---: | :--- | :---: | :--- |
| **02:04 – 02:14** (10.0s) | `CARD_PENTHOUSE_LOCK_HERO.png` | **Track V3** (Hero Photo • 3% Ken Burns) | **NO BLUR** | **Visual:** Atmospheric photo of a brushed bronze luxury penthouse front door at dusk. Rain streaks down exterior glass. Integrated smart lock keypad glows stark crimson reading: **`ACCESS REVOKED`**. | `whoosh-cinematic.mp3` (-16 dB) on **A4** at 02:04 | *"Imagine buying a house for $400,000. You pay the mortgage in full, move your family in, and unpack your kitchen."* |
| **02:14 – 02:24** (10.0s) | `CARD_PENTHOUSE_LOCK.png` | **Track V3** (Full Card) | **NO BLUR** | **Visual:** Real Estate Contract card:<br>• Left: Luxury Penthouse Title Deed ($400,000 Ownership)<br>• Right: Highlighted fine print excerpt: **`"Page 47: You bought a temporary room pass. Builder changes lock after 3 years."`** | `sfx_data_blip.wav` (-18 dB) on **A4** at 02:14 | *"3 years later, the builder walks up to your front door and changes the digital lock... page 47: you bought a temporary room pass."* |
| **02:24 – 02:40** (16.0s) | *Clean Gameplay* | **Track V1** (1.15x HUD Crop) | **NO BLUR** | **Visual:** Kenway walking past cobblestones and colonial buildings in Havana. | BGM bed at -23 dB on **A2** | *"In real estate, that would be illegal fraud. In tech, we call it the End User License Agreement. Every time you click I AGREE, you sign away true ownership."* |
| **02:40 – 02:54** (14.0s) | `CARD_FIRST_SALE_1908_hero.png` | **Track V3** (Hero Photo • 3% Ken Burns) | **NO BLUR** | **Visual:** 1900s mahogany law library reading room photo. Antique leather law tome open on dark wood under the glowing emerald banker's lamp. Dust motes dancing in amber light. | `whoosh-cinematic.mp3` (-16 dB) on **A4** at 02:40 | *"Over one hundred years ago, the Supreme Court heard a landmark case that established one of the greatest consumer protections in modern history."* |
| **02:54 – 03:12** (18.0s) | `CARD_FIRST_SALE_1908.png` | **Track V3** (Full Card) | **NO BLUR** | **Visual:** Gold parchment Supreme Court card:<br>• Header: `THE FIRST SALE DOCTRINE (1908)`<br>• Ruling text: *"Once you purchase a physical copy of a copyrighted work, publisher control terminates. You own the object: resell, lend, or burn it."* | `sfx_whoosh.wav` (-18 dB) on **A4** at 02:54 | *"The First Sale Doctrine. Once you buy a physical book, record, or painting, it belongs to you. You can resell it, lend it to a friend, or burn it in your backyard. Publishers could never touch it."* |
| **03:12 – 03:24** (12.0s) | *Clean Gameplay* | **Track V1** (1.15x HUD Crop) | **NO BLUR** | **Visual:** Kenway climbing cathedral wall and sprinting across clay tile roofs in Havana. | Parkour footstep foley | *"In 1998, digital copyright laws changed everything... digital encryption locks... companies claimed you never bought property. You were merely granted a license."* |
| **03:24 – 03:46** (22.0s) | `EVID_01_CA_AB2426_composite_card.png` | **Track V3** (Full Card) | **NO BLUR** | **Visual:** California Legislature official document card:<br>• Header: California Capitol Dome seal + `CALIFORNIA AB 2426`<br>• Yellow Highlight: *"Prohibits digital storefronts from using 'BUY' or 'PURCHASE' without explicit warning that consumer is merely receiving a revocable license."* | `whoosh-cinematic.mp3` (-16 dB) + `sfx_data_blip.wav` (-18 dB) on **A4** | *"This scam became so blatant that California just stepped in. They passed AB 2426... illegal to use BUY or PURCHASE without license warning... Politicians finally admitted the truth."* |
| **03:47 – 04:00** (13.0s) | `EVID_02_STEAM_CART_composite_card.png` | **Track V3** (Full Card) | **NO BLUR** | **Visual:** Steam shopping cart checkout capture:<br>• Game total: `₹3,599 ($70 USD)`<br>• Cyan Highlight Box: **`"A purchase of a digital product grants a license on Steam, not ownership. Just a license."`** | `sfx_data_blip.wav` (-18 dB) on **A4** at warning box | *"And the response was immediate. Look at Steam. Open your checkout cart right now... says clearly: A purchase of a digital product grants a license on Steam, not ownership. Just a license."* |
| **04:00 – 04:08** (8.0s) | *Clean Gameplay* | **Track V1** (1.15x HUD Crop) | **NO BLUR** | **Visual:** Jackdaw cruising on open clear Caribbean waters with sails billowing. | Gentle ocean lap / BGM bed (-23 dB) | *"Now gamers actually love Steam and for good reason. Valve built deep customer trust over 20 long years."* |
| **04:08 – 04:16** (8.0s) | `CARD_GABE_QUOTE.png` | **Track V3** (Full Card) | **NO BLUR** | **Visual:** Gabe Newell workshop quote card:<br>• Large Gold Typography: **`"Piracy is almost always a service problem, not a pricing problem."`**<br>• Attribution: *Gabe Newell, Co-founder & President, Valve Corporation*. | `whoosh-cinematic.mp3` (-18 dB) on **A4** at 04:08 | *"Valve founder Gabe Newell famously gave us the golden rule: Piracy is almost always a service problem, not a pricing problem."* |
| **04:16 – 04:18** (2.0s) | **BREATH BREAK 2** | **Track V3** (Quote Card Lingers) | **NO BLUR** | **Visual:** Gabe Newell quote card stays steady on screen as music pad swells. | Warm acoustic BGM swell to -18 dB on **A2** | *[Vocal Silence]* |
| **04:18 – 04:40** (22.0s) | *Clean Gameplay* | **Track V1** (1.15x HUD Crop) | **NO BLUR** | **Visual:** Night naval battle: Jackdaw firing heavy cannons, mortar explosions lighting up waves in bright orange fire. | Cannon fire & explosions audio | *"Valve gave players instant downloads, automated cloud saves, family sharing, 2-hour refunds. With Steam Deck, open handheld computer... treats gamers like intelligent adults."* |
| **04:40 – 04:58** (18.0s) | `KT_04_DEAD_SERVER.png` | **Track V4** (PNG) + **Track V2** (Adjustment Clip) | **BLUR ACTIVE (0.18)** | **Exact On-Screen Typography:**<br>• Top Badge: `ACT 2 ENDING • OVERLAY 14`<br>• Giant Crimson Headline: **`EVEN GABE CANNOT SAVE A DEAD SERVER.`**<br>• Subtext: `THE ENTIRE DIGITAL GAMING WORLD IS BUILT ON RENTED GROUND.` | `cinematic-impact-boom.mp3` (-13 dB) on **A3** at 04:40 | *"Even Valve cannot change the law... publishers like EA or Ubisoft retain control. If publisher deletes a game, even Steam cannot save it. The entire digital gaming world is built on rented ground."* |
| **04:58 – 05:01** (3.0s) | **BREATH BREAK 3** | **Track V1** (Gameplay) | **NO BLUR** | **Visual:** Viewpoint 360° pan over dark stormy ocean and lightning. | `cinematic-impact-boom.mp3` (-10 dB) on **A3** + BGM swell (-16 dB) on **A2** | *[Vocal Silence]* |

---

### ACT 3: USED GAMES, RESALE MURDER & THE INDIA LIFELINE (05:01 – 07:49)

| Timecode | Asset File in `assets/` | Track & Action | Track 2 Blur? | What the Viewer Sees on Screen (Exact Visual & Text) | Audio SFX & Track | Spoken Voiceover Trigger |
| :--- | :--- | :---: | :---: | :--- | :---: | :--- |
| **05:01 – 05:10** (9.0s) | `KT_05_FOLLOW_MONEY.png` | **Track V4** (PNG) + **Track V2** (Adjustment Clip) | **BLUR ACTIVE (0.18)** | **Exact On-Screen Typography:**<br>• Top Badge: `ACT 3 HOOK • OVERLAY 15`<br>• Bold Gold/Red Headline: **`FOLLOW THE MONEY: KILLING THE USED GAME MARKET.`**<br>• Subtext: `IT HAS NOTHING TO DO WITH CONVENIENCE OR SAVING TREES.` | `swoosh-sound-effect-for-fight-scenes-or-transitions-.mp3` + boom on **A4 / A3** | *"Why are Sony and Microsoft pushing so hard to kill the disc? Nothing to do with saving trees... It is about killing the used game market forever."* |
| **05:10 – 05:28** (18.0s) | *Clean Gameplay* | **Track V1** (1.15x HUD Crop) | **NO BLUR** | **Visual:** Naval broadside combat: heavy cannon volleys tearing into enemy galleon with splintering wood. | Cannon wood splinters / explosions | *"Think back 20 years ago. Halo 2 / GTA San Andreas on disc... sold to friend for $30... cash in pocket. How much money did Sony make on that second transaction?"* |
| **05:28 – 05:30** (2.0s) | `KT_06_ZERO_DOLLARS.png` | **Track V4** (PNG) + **Track V2** (Adjustment Clip) | **BLUR ACTIVE (0.18)** | **Exact On-Screen Typography:**<br>• Top Badge: `ACT 3 HOOK • OVERLAY 16`<br>• Massive Crimson Headline (Takes up center screen): **`ZERO DOLLARS.`**<br>• Subtext: `HOW MUCH SONY MAKES WHEN YOU RESELL A PHYSICAL DISC.` | `cinematic-impact-boom.mp3` (-11 dB) on **A3** at 05:28 | *"Exactly $0."* |
| **05:30 – 05:38** (8.0s) | *Clean Gameplay* | **Track V1** (1.15x HUD Crop) | **NO BLUR** | **Visual:** Kenway walking past Caribbean dock taverns in golden sunlight. | BGM bed at -23 dB on **A2** | *"Publishers hated the second-hand market with an absolute burning passion. For decades, physical discs gave power to consumers."* |
| **05:38 – 05:52** (14.0s) | `CHART_SALES_COLLAPSE_animated.mp4` | **Track V3** (Full MP4 Video) | **NO BLUR** | **Visual:** Broadcast animated area chart:<br>• Title: `THE 20-YEAR SALES COLLAPSE (2004 vs 2024)`<br>• Cyan Physical Sales line collapsing from `90% ➔ 8%`<br>• Red Digital Storefront line rising from `10% ➔ 92%`<br>• Animated dynamic line draw with glow. | `whoosh-cinematic.mp3` (-16 dB) + `sfx_data_blip.wav` (-18 dB) on **A4** | *"Look at this chart. In 20 years the entire industry flipped. Physical sales collapsed from 90% down to less than 8%."* |
| **05:52 – 06:08** (16.0s) | *Clean Gameplay* | **Track V1** (1.15x HUD Crop) | **NO BLUR** | **Visual:** Havana harbor and ship rigging in bright tropical sunlight. | Harbor waves & sea breeze | *"Once disc drive is removed, competition completely disappears. Cannot buy cheap copy on eBay. Cannot borrow from your cousin."* |
| **06:08 – 06:18** (10.0s) | `CARD_PS_STORE_PRICES.png` | **Track V3** (Full Card) | **NO BLUR** | **Visual:** Digital Console Storefront Monopoly card:<br>• PlayStation Store interface crop showing 5-year-old title sitting at full `$59.99` USD.<br>• Contrasted with physical used disc selling for `$14.99` on eBay. | `whoosh-cinematic.mp3` (-18 dB) on **A4** at 06:08 | *"Trapped inside one single digital store. Sony and Microsoft set price. 5-year-old digital game sits at full price, you have zero alternatives."* |
| **06:18 – 06:25** (7.0s) | *Clean Gameplay* | **Track V1** (1.15x HUD Crop) | **NO BLUR** | **Visual:** High-speed rooftop sprint and chimney leap across Havana. | Dynamic parkour footsteps | *"Pay $80 for game, pay $80/yr for multiplayer... not just an American problem. Look at emerging markets. Let's talk about India."* |
| **06:25 – 06:27** (2.0s) | **BREATH BREAK 5** | **Track V1** (Gameplay) | **NO BLUR** | **Visual:** Parkour landing on town square. Beat drop. | BGM percussion swell (-18 dB) on **A2** | *[Vocal Silence]* |
| **06:27 – 06:45** (18.0s) | `CARD_INDIA_DISC_MARKET_HERO.png` | **Track V3** (Hero Photo • 3% Ken Burns) | **NO BLUR** | **Visual:** Vibrant photograph inside a crowded electronics arcade in Mumbai (Nehru Place / Lamington Road style) at dusk. Display glass packed with physical PS4/PS5 disc cases, gamers trading discs. | `whoosh-cinematic.mp3` (-18 dB) on **A4** at 06:27 | *"In India, console gaming never grew on expensive digital pre-orders. It grew on the second-hand disc lifeline. Gamers in Mumbai, Delhi, and Bangalore swapped discs with friends."* |
| **06:45 – 07:00** (15.0s) | `EVID_05_INDIA_DISC_RESALE.png` | **Track V3** (Full Card) | **NO BLUR** | **Visual:** Economic Proof Card:<br>• Pre-Owned Buy Price: `₹2,499`<br>• Resale Trade-in Value: `₹1,900`<br>• Highlighted Green Badge: **`NET COST TO PLAY = ₹599 ($7 USD)`**<br>• Contrasted with Digital ₹5,999 launch price ($72 USD, 100% sunk cost). | `sfx_data_blip.wav` (-18 dB) on **A4** on ₹599 highlight | *"Bought pre-owned copies on trade sites, played them, sold them back. That secondary market was the only way middle-class kids could afford this hobby."* |
| **07:00 – 07:13** (13.0s) | *Clean Gameplay* | **Track V1** (1.15x HUD Crop) | **NO BLUR** | **Visual:** Kenway walking Caribbean pirate docks in Nassau. | BGM bed at -23 dB on **A2** | *"GTA 6 at 6,000 rupees... locked in vault forever... cannot sell back... killed economic engine that kept gaming alive in developing countries."* |
| **07:14 – 07:20** (6.0s) | `EVID_06_BMW_HEATED_SEATS_hero.png` | **Track V3** (Hero Photo • 3% Ken Burns) | **NO BLUR** | **Visual:** In-cockpit luxury vehicle photo at night. Driver finger touching the touchscreen where seat heater is blocked by an electronic paywall window. | `whoosh-cinematic.mp3` (-18 dB) on **A4** at 07:14 | *"BMW tried putting heated seats behind an $18 monthly subscription."* |
| **07:20 – 07:26** (6.0s) | `EVID_06_BMW_HEATED_SEATS.png` | **Track V3** (Full Card) | **NO BLUR** | **Visual:** Official BMW ConnectedDrive screenshot card:<br>• Title: `BMW CONNECTEDDRIVE: HEATED FRONT SEATS`<br>• Red Box: **`$18 / Month Subscription`**<br>• Proof: The heating coils and wires were already physically installed in the seat. | Digital error click on **A4** at 07:20 | *"The physical heaters were already built inside the car... The motors exist, the battery exists. The code demands a credit card."* |
| **07:27 – 07:38** (11.0s) | `CARD_EV_SCOOTER_OTA.png` | **Track V3** (Full Card) | **NO BLUR** | **Visual:** Indian EV Scooter Software Paywall card:<br>• Feature checklist showing Hill-Hold, Cruise Control, and Hyper-Charging locked behind ₹1,200/yr software subscription packs. | `sfx_data_blip.wav` (-18 dB) on **A4** at 07:27 | *"Electric scooters in India paywalling hill-hold and cruise control behind software packs. Motors exist, battery exists. Code demands credit card."* |
| **07:39 – 07:46** (7.0s) | `KT_07_HARDWARE_PERMISSION.png` | **Track V4** (PNG) + **Track V2** (Adjustment Clip) | **BLUR ACTIVE (0.18)** | **Exact On-Screen Typography:**<br>• Top Badge: `ACT 3 ENDING • OVERLAY 23`<br>• Giant Crimson Headline: **`YOU OWN THE HARDWARE. THEY OWN THE PERMISSION.`**<br>• Subtext: `SELL YOU THE SHELL. CHARGE YOU RENT FOREVER TO TURN IT ON.` | `cinematic-impact-boom.mp3` (-13 dB) on **A3** at 07:39 | *"This is modern corporate playbook: Sell you physical shell, then charge you rent forever for permission to turn it on."* |
| **07:46 – 07:49** (3.0s) | **BREATH BREAK 6** | **Track V1** (Gameplay) | **NO BLUR** | **Visual:** Ship wheel spinning in rolling morning fog. Chapter transition. | `cinematic-impact-boom.mp3` (-10 dB) on **A3** + BGM swell (-16 dB) on **A2** | *[Vocal Silence]* |

---

### ACT 4: THE DIGITAL RESISTANCE & TRUE OWNERSHIP (07:49 – 10:07)

| Timecode | Asset File in `assets/` | Track & Action | Track 2 Blur? | What the Viewer Sees on Screen (Exact Visual & Text) | Audio SFX & Track | Spoken Voiceover Trigger |
| :--- | :--- | :---: | :---: | :--- | :---: | :--- |
| **07:49 – 08:14** (25.0s) | `CARD_STOP_KILLING_GAMES.png` | **Track V3** (Full Card) | **NO BLUR** | **Visual:** European Citizens' Initiative official campaign portal card:<br>• Header: `STOP KILLING GAMES`<br>• Official Counter: **`1,250,000+ VERIFIED SIGNATURES`**<br>• Legal demand: Mandate publishers release an offline patch when shutting down servers. | `whoosh-cinematic.mp3` (-18 dB) on **A4** at 07:49 | *"Where does this end? Accept digital feudalism? Pushback started. Stop Killing Games movement in Europe... 1M signatures... Mandate clean offline patch when servers die."* |
| **08:14 – 08:35** (21.0s) | *Clean Gameplay* | **Track V1** (1.15x HUD Crop) | **NO BLUR** | **Visual:** The Jackdaw fighting in heavy stormy seas, waves crashing across the deck, lightning flashing across the sky. | Thunder crash & storm waves audio | *"Consumers find their own way... retro game emulation... ripped offline backups... build your own safety net. Here are three rules of digital survival."* |
| **08:38 – 08:56** (18.0s) | `CARD_RULE1_GOG.png` | **Track V3** (Full Card) | **NO BLUR** | **Visual:** GOG.com digital freedom card:<br>• Header: `RULE 1: SUPPORT TRUE DRM-FREE PLATFORMS`<br>• GOG store crop showing green `DRM-FREE` badge.<br>• Highlighted button: **`DOWNLOAD OFFLINE BACKUP INSTALLER (.EXE)`**.<br>• Explanation: Independent file launches forever with zero server checks. | `whoosh-cinematic.mp3` + `sfx_data_blip.wav` on **A4** | *"Rule 1: Support DRM-free... GOG download standalone offline installer file... yours forever. GOG bankrupt tomorrow, file launches 50 years from now."* |
| **08:56 – 09:03** (7.0s) | *Clean Gameplay* | **Track V1** (1.15x HUD Crop) | **NO BLUR** | **Visual:** Kenway standing at the ship wheel under a clearing dusk sky. | BGM bed at -23 dB on **A2** | *"Rule number two."* |
| **09:03 – 09:19** (16.0s) | `CARD_RULE2_OPEN_HARDWARE.png` | **Track V3** (Full Card) | **NO BLUR** | **Visual:** Open Hardware vs Locked Consoles card:<br>• Left Column (Red): Closed Ecosystems (Locked to 1 store, paid multiplayer, remote kill switch)<br>• Right Column (Cyan): Open Hardware Freedom (PC / Steam Deck Linux, root OS control, emulator backups, zero multiplayer fees). | `whoosh-cinematic.mp3` (-18 dB) on **A4** at 09:03 | *"Choose open hardware... PC or Steam Deck lets you control operating system. Not locked into one single corporate store."* |
| **09:19 – 09:23** (4.0s) | *Clean Gameplay* | **Track V1** (1.15x HUD Crop) | **NO BLUR** | **Visual:** Viewpoint climb on Havana cathedral peak, reaching the top spire cross. | Clean gameplay motion | *"And rule number three for creators and entrepreneurs."* |
| **09:23 – 09:43** (20.0s) | `KT_08_OWN_AUDIENCE.png` | **Track V4** (PNG) + **Track V2** (Adjustment Clip) | **BLUR ACTIVE (0.18)** | **Exact On-Screen Typography:**<br>• Top Badge: `ACT 4 BODY • OVERLAY 27`<br>• Giant Bold Amber Gold Headline: **`OWN YOUR AUDIENCE. OWN YOUR DISTRIBUTION.`**<br>• Subtext: `LOCAL SOURCE CODE • OFFLINE BACKUPS • DIRECT EMAIL LIST`<br>• Principle: Never build on rented digital land where terms can change overnight. | `cinematic-impact-boom.mp3` (-13 dB) on **A3** at 09:23 | *"Never build life on rented digital land... digital tenant. Build email list, local backups of source code, offline copies of creative work... terms change overnight."* |
| **09:43 – 09:54** (11.0s) | *Clean Gameplay* | **Track V1** (1.15x HUD Crop) | **NO BLUR** | **Visual:** The Jackdaw sailing smoothly towards the golden hour horizon. | Warm orchestral BGM swell on **A2** | *"Think back to that empty plastic game case... 20th century freedom meant having physical property in your hands."* |
| **09:54 – 10:00** (6.0s) | `KT_09_FREEDOM_OFFLINE_Hero.png` (V3) **+** `KT_09_FREEDOM_OFFLINE.png` (V4) | **V3 (Hero Photo)** **+** **V4 (Text Slam Overlaid)** | **NO BLUR (Photo covers canvas)** | **Simultaneous Layered Composition:**<br>• **Background (V3):** Rugged brushed-titanium external SSD resting on dark slate with pulsing amber LED activity light.<br>• **Foreground Text (V4):** High-Voltage Gold Bebas Headline:<br>**`IN THE 21ST CENTURY, FREEDOM IS AN OFFLINE FILE.`**<br>• Subtext: `IF YOU NEED PERMISSION TO OPEN IT, YOU NEVER BOUGHT IT.` | `cinematic-impact-boom.mp3` (-11 dB) on **A3** at 09:54 | *"In the 21st century, freedom is having the offline files on your hard drive."* |
| **10:00 – 10:03** (3.0s) | *Clean Gameplay* | **Track V1** (1.15x HUD Crop) | **NO BLUR** | **Visual:** Ship cutting across calm waters under a starry night sky with gentle moonlit wake. | Sea breeze / gentle water lap | *"If you need an active internet connection just to ask for permission to open it, you never bought it."* |
| **10:03 – 10:04** (1.5s) | **BREATH BREAK 7** | **Track V1** (Gameplay) | **NO BLUR** | **Visual:** Gentle camera drift behind the ship stern lantern. Final silence. | Subtle low-end drone fade | *[Vocal Silence]* |
| **10:04 – 10:07** (3.0s) | *Cinematic Fade to Black* | **Track V1** | **NO BLUR** | **Visual:** Jackdaw sails into dark distance as the screen smoothly fades to black. End of video. | BGM built-in 10-second outro fade to silence | *"You are just paying rent. See you next time."* |

---

## 🎛️ 6. Fairlight Audio Mixer Quick Settings

| Track | Type | Volume Fader | EQ / Dynamics |
| :--- | :--- | :---: | :--- |
| **A1: Voiceover** | Spoken Dialogue | **0.0 dB** (Mastered) | High-pass filter at 80 Hz, slight presence boost at 3.5 kHz. Integrated loudness: -14 LUFS. |
| **A2: BGM** | Ambient Bed Loop | **-23.0 dB** | Notch filter: -2.5 dB cut at 2.5 kHz (leaves clear frequency corridor for voiceover). |
| **A3: Impacts** | Sub-Bass Booms | **-12.0 dB to -15.0 dB** | Low-end punch (40 Hz – 120 Hz). Let it rumble underneath without clipping. |
| **A4: Movement/UI**| Whooshes & Blips | **-16.0 dB to -20.0 dB** | High-end sparkle (4 kHz – 10 kHz). Keep clean and tight. |
