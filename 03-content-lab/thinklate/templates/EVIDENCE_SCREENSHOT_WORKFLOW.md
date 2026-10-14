# ThinkLate Standard: Evidence Screenshot & Multi-Crop Workflow
> **Master Guide for Affinity Photo / Designer & DaVinci Resolve**  
> *Saved for Video 03 and all future ThinkLate video productions.*

---

## 1. Resolution & Canvas Standard (The "4K to 1080p" Law)

### Why 4K Canvas in Affinity is Perfect for a 1080p Timeline:
* **The Principle:** Both 4K (`3840×2160`) and 1080p (`1920×1080`) are **16:9 widescreen**. They share the exact same aspect ratio.
* **The Advantage:**
  * When you create a card or composite graphic in Affinity at 4K, you can drop it onto a 1080p DaVinci timeline and zoom in by **1.5x or 2.0x** without losing a single pixel of sharpness.
  * When DaVinci places a 4K image on a 1080p timeline, it automatically scales it down with high-quality bicubic/lanczos filtering. Zero black bars, zero letterboxing.
* **The Free AI & Gameplay Reality:**
  * Free AI platforms (Gemini Nano, Kling, Luma) generate at **1080p 16:9**.
  * OBS game captures (RDR2, Black Flag) record at **1080p 60fps**.
* **The Master Timeline Rule:**
  * **Keep your DaVinci Resolve Timeline at 1080p (1920×1080).**
  * It renders 4x faster, uses less VRAM, handles free AI clips natively, and your 4K Affinity graphics will look ultra-crisp.
  * *(Optional: On final YouTube export, set Deliver Resolution to 3840×2160 to unlock YouTube's premium 4K VP9/AV01 streaming bitrate).*

---

## 2. In DaVinci Resolve: How to Show 2–3 Screenshots in One Frame

### Option A: The "Vertical Stack" (Header on Top, Quote Below)
*Place two screenshot crops directly one above the other:*

```
[VIDEO TRACK 3] -> Screenshot 2 (The specific sentence / quote crop)
                    Inspector: Position Y = -160 | Zoom = 0.90 | OpenFX: Drop Shadow

[VIDEO TRACK 2] -> Screenshot 1 (Website header / Logo / Article Title)
                    Inspector: Position Y = +240 | Zoom = 0.75 | OpenFX: Drop Shadow

[VIDEO TRACK 1] -> Background (Cinematic gameplay B-roll / dark studio video)
```

**Steps in DaVinci:**
1. Put the **Website Header crop** on Track 2. In Inspector $\rightarrow$ Transform: set `Position Y: 240` and `Zoom: 0.75`.
2. Put the **Zoomed Quote crop** on Track 3. In Inspector $\rightarrow$ Transform: set `Position Y: -160` and `Zoom: 0.90` (larger so viewers on phones can read easily).
3. In Effects $\rightarrow$ OpenFX: Drag **Drop Shadow** onto both clips.
4. *Result:* Two distinct, floating document cards stacked vertically with depth over your background video!

---

### Option B: The "Side-by-Side Context Split"
*Left side shows the full article for proof; Right side zooms into the key takeaway:*
* **Track 2 (Left):** Full page screenshot $\rightarrow$ `Position X: -380` | `Zoom: 0.70`
* **Track 3 (Right):** Cropped highlight card $\rightarrow$ `Position X: +380` | `Zoom: 1.05`

---

## 3. Your Installed DaVinci Template: "Paper Animator"

You already have the **`MrJustinEdits - Paper Animator.drfx`** template pack installed in:  
`C:\Users\sar1s\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Templates\`

### How to use it for evidence screenshots:
1. In DaVinci Resolve, go to the **Edit Page**.
2. Open the **Effects** panel (top-left).
3. Under **Templates / Fusion Titles / Effects**, look for **Paper Animator**.
4. Drag the Paper Animator effect directly onto your screenshot clip or an **Adjustment Clip** above your screenshots.
5. In the Inspector, you can customize:
   * **Paper Texture & Edges:** Adds authentic torn-paper or newspaper borders.
   * **Drop Animation:** Slides or floats the paper into the frame with natural physics.
   * **Shadows:** Automatic realistic ambient occlusion underneath the document.

---

## 4. The 30-Second "Vox / Johnny Harris" Highlighter Trick (Zero Plugins)

To make a yellow highlighter sweep across your text in DaVinci:
1. Place your article screenshot on **Track 2**.
2. Go to Effects $\rightarrow$ Generators $\rightarrow$ Drag **Solid Color** onto **Track 3** directly above the text.
3. Change the Solid Color to **Warm Amber / Yellow (`#F59E0B` or `#FACC15`)**.
4. In Inspector $\rightarrow$ **Cropping**: Crop the top and bottom so the yellow bar sits over the exact sentence.
5. Under Video $\rightarrow$ **Composite Mode**: Change from *Normal* to **`Multiply`**.  
   *(The text instantly shines through the yellow color like authentic marker ink!)*
6. Keyframe `Crop Right` from 1000 down to 0 over 15 frames (0.5 seconds).
