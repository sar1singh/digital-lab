# ThinkLate Gameplay B-Roll Archive & Trimming Guide
> **Permanent Shared Gameplay Archive**  
> *Record 1 game per video session. Trim into modular loops. Store here permanently.*

---

## 🎮 The "Single-Game Session" Law
* To save GPU/RAM overhead and prevent workflow exhaustion, **record only ONE game per video**:
  * **Video 03 (Current):** ***Assassin's Creed IV: Black Flag*** (Theme: High-seas piracy, naval combat, Gabe Newell's "Piracy is a service problem").
  * **Video 04 (Next):** ***Red Dead Redemption 2*** (Theme: The frontier, corporate trusts, trains, outlaws).
  * **Video 05:** Alternate back or choose the next thematic title.

---

## ⚡ How to Trim 15-to-30s Clips from a 2-Hour Raw Recording in 1 Second (Zero RAM)

Never drag a massive 2-hour 50GB file into an editor just to cut small clips. Use FFmpeg stream copying (instant, 0% CPU/RAM re-encoding):

### 1-Line FFmpeg Command (Lossless Slice):
```bash
ffmpeg -ss 00:14:20 -to 00:14:50 -i "raw_session.mp4" -c copy "reusable_vault/gameplay_broll/ac_black_flag/clip_01_open_sea_sunset.mp4"
```
* `-ss 00:14:20` = Start time (14 mins 20 secs)
* `-to 00:14:50` = End time (30-second duration)
* `-c copy` = **Instant stream copy** (takes ~0.5 seconds, zero quality loss, zero RAM strain)

---

## 📦 Master Clip Schedule for Video 03 (Assassin's Creed Black Flag)

Save your trimmed clips directly into `reusable_vault/gameplay_broll/ac_black_flag/`:
1. `clip_01_jackdaw_sailing_open_water.mp4` (~30s, sailing under clear/golden skies)
2. `clip_02_naval_cannon_combat.mp4` (~25s, broadside cannons firing at sea)
3. `clip_03_caribbean_docks_nassau.mp4` (~20s, Edward Kenway walking past wooden docks/taverns)
4. `clip_04_stormy_seas_waves.mp4` (~30s, Jackdaw navigating high ocean storm swells)

Once trimmed, copy them to `videos/03_death_of_ownership/assets/` or link directly from this vault!
