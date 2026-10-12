# Scuff Sensei — YouTube Channel Setup & Brand Kit

**Live Channel URL:** [youtube.com/channel/UCjjaciOfUho7gs30GgZBZEA](https://www.youtube.com/channel/UCjjaciOfUho7gs30GgZBZEA)  
**Studio Customization Direct Link:** [studio.youtube.com/channel/UCjjaciOfUho7gs30GgZBZEA/editing](https://studio.youtube.com/channel/UCjjaciOfUho7gs30GgZBZEA/editing)  
**Handle:** `@ScuffSensei`  
**Niche:** Unscripted gaming walkthroughs, backlog journeys, 4K PC gameplay, conversational commentary  

---

## 1. Generated Brand Assets (Ready to Upload)

All assets have been generated in exact YouTube specs inside [`brand/`](file:///c:/Users/sar1s/Documents/MyWork/Git/digital-lab/03-content-lab/scuff-sensei/brand/):

1. **Profile Picture (800x800):** [`brand/avatar.png`](file:///c:/Users/sar1s/Documents/MyWork/Git/digital-lab/03-content-lab/scuff-sensei/brand/avatar.png)
2. **Channel Banner (2560x1440):** [`brand/banner.png`](file:///c:/Users/sar1s/Documents/MyWork/Git/digital-lab/03-content-lab/scuff-sensei/brand/banner.png) *(Safe zone centered for mobile & desktop)*
3. **Video Watermark (150x150):** [`brand/watermark.png`](file:///c:/Users/sar1s/Documents/MyWork/Git/digital-lab/03-content-lab/scuff-sensei/brand/watermark.png) *(Transparent cybernetic SS badge)*

---

## 2. Copy-Paste Channel Metadata

### Channel Description (About Section)
```text
The unpolished path to gaming enlightenment.

No esports reflexes. No 10-hour overedited fluff. Just master-grade PC gameplay, unscripted walkthroughs, and experiencing the greatest backlogged masterpieces one mistake at a time.

Current Journey:
• The Last of Us Part 1
• Red Dead Redemption 2
• God of War

Hit subscribe and join the scuffed journey.
```

### Channel Keywords / Tags (YouTube Studio → Settings → Channel → Basic Info)
```text
Scuff Sensei, ScuffSensei, The Last of Us Part 1 PC, The Last of Us PC Walkthrough, Red Dead Redemption 2 PC, RDR2 4K, Unscripted Gameplay, PC Gaming Backlog, Story Walkthrough, Casual Gaming Commentary
```

---

## 3. Video Upload Template (Default for Every Video)

### Title Format
`The Last of Us Part 1 - [Chapter Name] | Ep. [Number]`

*Examples:*
* `The Last of Us Part 1 - Hometown & 20 Years Later | Ep. 1`
* `The Last of Us Part 1 - Beyond the Wall & The Slums | Ep. 2`
* `The Last of Us Part 1 - The Cargo & The Outskirts | Ep. 3`

### Video Description Template
```text
Exploring [Game Title] from the beginning. Clean, unscripted playthrough on PC.

TIMESTAMPS:
00:00 - Introduction & Starting Chapter
[Paste 2-3 mission checkpoint timestamps here]

Settings: Native Ultra / High Settings (PC)
Gamer Tag: ScuffSensei

#TheLastOfUs #Gaming #Walkthrough #ScuffSensei
```

---

## 4. OBS Recording Checklist Before Playing

* **Encoder:** NVIDIA NVENC (H.264 or AV1)
* **Rate Control:** CQP (Level 14 to 18)
* **Output Resolution:** 1440p or 4K (Forces YouTube's VP09 high-quality codec)
* **Microphone Filter:** In OBS Audio Mixer → Mic Settings → Filters → Add **Noise Suppression (RNNoise)**
* **Hotkeys:**
  * `F9` (or preferred key) → **Pause Recording / Unpause Recording**
  * Use `F9` when in menus, loading screens, or stepping away to ensure zero editing is needed.
