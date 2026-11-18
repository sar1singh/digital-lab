# Off Script (`@OffScriptEddy`) — Tonight's Organic Session Card
> **Session:** *Assassin's Creed Black Flag* — Spanish Naval Fort Rematch  
> **Thumbnail:** Re-using existing Off Script thumbnail (zero thumbnail work tonight).  
> **Mic Rule:** **Leave your mic live 100% of the time.** Zero muting/unmuting during combat or sailing — noise gating, breathing cleanup, and game-audio un-ducking happen automatically in post-production.

---

## 0. Pre-OBS 10-Second Check
- [ ] **Encoder:** Rate Control **`CQP 20–22`**, Preset **`P5`** (`1080p60` → ~14 GB for 2 hrs instead of 77.5 GB).
- [ ] **Audio Tracks:** Track 1 = Game + Mic | Track 2 = **Isolated Mic Only** (leave mic unmuted start-to-finish).

---

## 1. Where You Left Off Last Session (Nov 15 Recap)
- Upgraded **Jackdaw** Hull & Broadsides (`Grade 12`) after grinding `15,000` reales.
- Unlocked the **4 Templar Armor Keys**.
- Scouted the **Spanish Naval Fort** that forced the retreat in the prior episode — tonight you are ready for the rematch.

---

## 2. Organic Recording Rule (Zero Forced Topics)
- **Zero Outline Topics Required:** Ignore forced news/current-affairs bullet lists. Just play and enjoy the game.
- **Speak Naturally:** Talk whenever a real reaction, game memory, random thought, or tangent hits naturally. Whenever you want to lock into combat, stealth, or sea shanties, just stay quiet — **never touch the mute button**.

---

## 3. What Post-Production Handles Automatically Afterward
1. **Zero-Mute Audio Cleanup:** `-64 dB` noise gate + stereo phase-cancellation removes room hum and auto-ducks game audio strictly when you speak, un-ducking naturally during quiet combat/sailing.
2. **Automatic Breathing & Stall Cuts:** Long dead stalls (`> 20s`) are trimmed automatically via `trim_timeline.py`, keeping 15–20s game-audio breathing windows intact.
3. **Post-Session Title & Chapters:** Whisper transcription pulls whatever natural moments or rants actually happened tonight to build the title, chapters, and any highlight slice.
