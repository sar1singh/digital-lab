# The Commercial Production-Grade Video Architecture & Quality Standards
> **The North Star:** Every video, Short, and visual asset produced by our autonomous pipeline must meet commercial broadcast quality—so high that a luxury brand, media company, or tech enterprise would pay top-dollar for it.

---

## 🏛️ The 6 Pillars of Commercial-Grade AI Video

### Pillar 1: The "Paid Commercial" Test
Every 10–15 second visual sequence across our productions must satisfy one question:
> *"Would a company or client willingly pay $2,500+ for this 15-second sequence as a polished commercial?"*

If a shot looks like low-effort AI slop (floating logos in space, generic matrix code, distorted AI hands, unreadable tiny text, blurry stock clips), it is **rejected at the QC gate**.

---

### Pillar 2: The Two-Track Rule (Paivio's Law & Bomx Benchmark)
*Extracted from `Bomx/super-video-maker-skill` (`VIDEO_COPY_PLAYBOOK.md`):*

1. **Audio Track (The Argument):** Voiceover carries the narrative tension, wit, logic, and emotional punch.
2. **Visual Track (The Concrete Evidence):** The screen carries the physical proof, receipts, court dockets, product mechanics, or dynamic data spikes.
3. **Zero Redundancy:** Voice and screen must NEVER speak/display the exact same sentence. 
   - *Mute the video:* The visual story must still track seamlessly.
   - *Blank the screen:* The spoken argument must still land powerfully.
4. **The Pointing Test:** If the viewer cannot point their finger at the specific physical noun or interface change currently being discussed, the shot fails.

---

### Pillar 3: Anti-AI Slop Aesthetic Directives
Commercial-grade AI content never looks synthetic. All visual assets must strictly ban:
- ❌ **Floating Objects:** No laptops, icons, or phones floating in a dark cosmic void. All subjects must be physically grounded in an environment with shadows, table surfaces, or hands.
- ❌ **Generic Sci-Fi / Cyber Cliches:** No glowing neon blue grids, neural network nodes, cyber particles, or "hacker green" code rain.
- ❌ **Volumetric AI Hazes:** Banned: "ethereal volumetric light rays", surreal fantasy glows, and muddy black shadows.
- ✅ **Required Grounding:** Real physical materials (brushed metal, polished glass, textured wood, newsprint ink, 8% analog film grain, and diegetic mechanical Foley sounds).

---

### Pillar 4: The 5-Level Production Capability Roadmap

To systematically build our commercial portfolio, our agents follow a 5-tier production progression:

```
LEVEL 1: The 6-Second Product / Artifact Hero
│   (Cinematic macro shot, slow camera push-in, controlled moving studio lighting)
▼
LEVEL 2: The 15-Second 3-Shot Narrative Sequence
│   (Cause → Action → Consequence; character / prop continuity across cuts)
▼
LEVEL 3: The 15–30s Broadcast Commercial Spec Ad
│   (Beat-locked VO, Swiss Brutalist typography, dynamic Remotion cards, sound bus)
▼
LEVEL 4: The High-Retention Vertical Short (30–60s)
│   (Audience pull engine for YouTube Shorts / Reels / LinkedIn case study)
▼
LEVEL 5: The Master Documentary Deep Dive (8–10 Mins)
    (ThinkLate flagship: 15–20 Level 1–3 building blocks chained seamlessly)
```

---

### Pillar 5: Staged Production & Approval Pipeline
*Extracted from `sb-dev/video-production-skills`:*

Never jump from an unvetted prompt directly to final master rendering:
1. **Intake & Four-Line Spine:** One viewer, one promise, one mechanism, one action step.
2. **Shot Development & Reference Frame:** Create a static reference frame first to lock composition, lighting, and color.
3. **Candidate Generation (2 Candidates):** For any generative video shot, generate at least 2 candidates. Compare camera stability and motion before selecting the winner.
4. **Assembly (The 4-Track Living Canvas):**
   - Track 1: Moving Gameplay Spine or 4K Stock
   - Track 2: Dynamic Gaussian Focus Blur (sigma 14 during card windows)
   - Track 3: Apple ProRes 4444 Transparent Remotion Card (from our 39-template catalog)
   - Track 4: Concurrent kinetic typography slam, pill badge, or rubber stamp
5. **Master Audio Finishing:** Voiceover at -1.0 dB true peak, BGM at -24 dB with 1.5 kHz parametric EQ dip, pre-emptive J-cut SFX 3 frames before visual cuts.
6. **Automated QC Gate:** Zero static frames, zero 404s, mobile contrast score $\ge 65$.

---

### Pillar 6: Packaging & The 150ms Mobile Screen Test

Commercial quality extends to packaging:
- **110px–130px Architectural Two-Tone Typography:** Legible on a 1.2-inch mobile phone.
- **Electric Rim Lighting:** Cyan/Lime glow on character cutouts to separate from backdrops.
- **Dark Mode Immunity:** High-saturation radial backgrounds (Hot Magenta, Radiant Crimson, Deep Cobalt) with contrast glow borders to prevent blending into YouTube's pure `#0F0F0F` mobile feed.
- Rendered headlessly via [`ThumbnailStudio.tsx`](motion_engine/src/components/packaging/ThumbnailStudio.tsx).
