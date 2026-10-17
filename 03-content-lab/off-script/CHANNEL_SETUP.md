# Off Script — YouTube Channel Setup & Brand Kit

**Channel Name:** `Off Script`  
**Live Channel URL:** [youtube.com/channel/UCjjaciOfUho7gs30GgZBZEA](https://www.youtube.com/channel/UCjjaciOfUho7gs30GgZBZEA)  
**Studio Customization Direct Link:** [studio.youtube.com/channel/UCjjaciOfUho7gs30GgZBZEA/editing](https://studio.youtube.com/channel/UCjjaciOfUho7gs30GgZBZEA/editing)  
**Handle:** `@OffScriptEddy` *(Temporary: `@sarwansenpai` during YouTube's 14-day cooldown)*  
**Host Persona:** Eddy (The Unfiltered Developer / Gamer)  
**Niche:** Unedited 4K PC gameplay archives, politically incorrect reality checks, Anand Ranganathan empirical fact-roasts, Deadpool 4th-wall commentary  

> [!NOTE]
> **Handle Cooldown:** YouTube limits handle changes to twice every 14 days. The channel currently sits on `@sarwansenpai` and will switch to `@OffScriptEddy` as soon as the cooldown lifts. All channel display naming, branding, banners, and video titles operate strictly under **Off Script** immediately.

---

## 1. Brand Assets

All assets are located in [`brand/`](file:///c:/Users/sar1s/Documents/MyWork/Git/digital-lab/03-content-lab/off-script/brand/):

1. **Profile Picture / Logo Mark (Emblem):** [`brand/emblem.jpg`](file:///c:/Users/sar1s/Documents/MyWork/Git/digital-lab/03-content-lab/off-script/brand/emblem.jpg)
   - Dark Noir / Graphic Novel style: Bold black inking, halftone dots, hazard amber banner with electric cyan slash.
   - Zero mascot maintenance, 100% scalable icon.
2. **Channel Banner (2560x1440):** [`brand/banner.png`](file:///c:/Users/sar1s/Documents/MyWork/Git/digital-lab/03-content-lab/off-script/brand/banner.png) *(Centered safe zone for mobile and desktop)*
3. **Video Watermark (150x150):** Transparent emblem badge.

---

## 2. Copy-Paste Channel Metadata

### Channel Name (Display Name)
```text
Off Script
```

### Channel Handle
```text
@OffScriptEddy
```

### Channel Description (About Section)
```text
No PR filters. No corporate scripts. Just raw 4K gameplay, unedited logs, and calling out real-world absurdity with facts and zero apologies.

Hosted by Eddy.

Current Archives:
- The Last of Us Part 1 (PC 4K60)
- Red Dead Redemption 2
- Cyberpunk 2077

Unfiltered rants on geopolitics, cinema, anime, and modern society.

Hit subscribe, or don't. Going Off Script.
```

### Channel Keywords / Tags (YouTube Studio -> Settings -> Channel -> Basic Info)
```text
Off Script, OffScriptEddy, Eddy, Unscripted Gameplay, 4K PC Walkthrough, The Last of Us Part 1 4K, Cyberpunk 2077 4K, Geopolitics Commentary, Unfiltered Rants, Hinglish Commentary, No Commentary Walkthrough, Gaming Archive
```

---

## 3. Video Upload Template (Default for Every Video)

### Title Format (Phase 1: Silent Gameplay Archive)
`Off Script | [Game Title] — [Chapter / Mission Name] | 4K60 [Ep. XX]`

*Examples:*
* `Off Script | The Last of Us Part 1 — Hometown & 20 Years Later | 4K60 [Ep. 01]`
* `Off Script | The Last of Us Part 1 — Beyond the Wall & The Slums | 4K60 [Ep. 02]`
* `Off Script | The Last of Us Part 1 — The Cargo & The Outskirts | 4K60 [Ep. 03]`

### Video Description Template
```text
Unedited 4K 60FPS gameplay capture on PC. No script, no fluff.
Played and captured by Eddy.

TIMESTAMPS:
00:00 - Introduction & Starting Chapter
[Paste 2-3 mission checkpoint timestamps here]

Settings: Native Ultra / High Settings (PC)
Gamer Tag: OffScriptEddy

#Gaming #Walkthrough #4K #OffScript #TheLastOfUs
```

---

## 4. OBS Recording Checklist Before Playing

* **Encoder:** NVIDIA NVENC (H.264 or AV1)
* **Rate Control:** CQP (Level 14 to 18)
* **Output Resolution:** 1440p or 4K (Forces YouTube VP09 / AV01 high-quality codec)
* **Microphone Filter:** In OBS Audio Mixer -> Mic Settings -> Filters -> Add **Noise Suppression (RNNoise)**
* **Hotkeys:**
  * `F9` (or preferred key) -> **Pause Recording / Unpause Recording**
  * Use `F9` when in menus, loading screens, or stepping away to guarantee zero editing is needed.
