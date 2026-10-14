# ThinkLate Reusable Asset Vault
> **Permanent Shared Asset & Template Archive**  
> *Assets in this directory are shared across all videos and are NEVER purged during post-publishing cleanups.*

---

## 📂 Vault Structure

* `davinci_macros/` — Exported `.setting` Fusion macros, Power Bin reference clips, and timeline templates.
* `affinity_templates/` — 4K layered templates (`.aftemplate`, `.afphoto`) for Evidence Cards, split layouts, and charts.
* `motion_overlays/` — High-bitrate alpha MP4s/MOVs (film grain, light leaks, dust particles, paper wipes).
* `sfx/` — Universal SFX pack (sub-braams, paper shuffles, whooshes, cash registers, UI clicks).

---

## 🔒 Preservation Guarantee
The post-publishing cleanup script (`tools/cleanup_published_video.py`) strictly targets `videos/<slug>/` and is explicitly forbidden from deleting files inside `reusable_vault/` or `templates/`.
