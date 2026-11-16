#!/usr/bin/env python3
"""
ThinkLate Master Shared Asset Vault Indexer
============================================
Scans `digital-lab/03-content-lab/shared/assets/` across all categories:
  1. Documentary B-Roll Videos (`broll/`)
  2. Verified Historical & Science Images (`images/historical_science/`)
  3. Cinema Vault Foley & SFX (`sfx/cinema_vault/`)
  4. Pop-Culture Reaction Clips (`pop_culture/`)
  5. Viral Meme Clips & Templates (`memes/`)
  6. Character Cutout Sprites (`../motion_engine/public/characters/`)

Generates `digital-lab/03-content-lab/shared/assets/SHARED_ASSET_INDEX.md` and
mirrors key memes to `motion_engine/public/memes/` for Remotion rendering.
"""

import os
import sys
import shutil
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(".")
SHARED_ASSETS = os.path.join(PROJECT_ROOT, "digital-lab", "03-content-lab", "shared", "assets")
PUBLIC_DIR = os.path.join(PROJECT_ROOT, "digital-lab", "03-content-lab", "shared", "motion_engine", "public")
PUBLIC_MEMES = os.path.join(PUBLIC_DIR, "memes")
os.makedirs(PUBLIC_MEMES, exist_ok=True)

# Mirror selected memes/pop-culture to public/memes for Remotion access
MIRROR_LIST = [
    (os.path.join(SHARED_ASSETS, "memes", "images", "usa_global", "charlie_conspiracy_(always_sunny_in_philidelphia).jpg"), "charlie_conspiracy.jpg"),
    (os.path.join(SHARED_ASSETS, "memes", "images", "usa_global", "always_has_been.png"), "always_has_been.png"),
    (os.path.join(SHARED_ASSETS, "memes", "images", "usa_global", "clown_applying_makeup.jpg"), "clown_makeup.jpg"),
    (os.path.join(SHARED_ASSETS, "memes", "images", "usa_global", "bell_curve.png"), "bell_curve.png"),
    (os.path.join(SHARED_ASSETS, "memes", "usa_global", "kurt_angle_thousand_yard_stare.mp4"), "kurt_angle_stare.mp4"),
    (os.path.join(SHARED_ASSETS, "pop_culture", "the_big_short_bragging.mp4"), "big_short_bragging.mp4"),
    (os.path.join(SHARED_ASSETS, "memes", "leonardo_pointing.mp4"), "leonardo_pointing.mp4"),
]

for src, dst_name in MIRROR_LIST:
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(PUBLIC_MEMES, dst_name))

def get_video_duration(path):
    try:
        cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", path]
        return float(subprocess.check_output(cmd, creationflags=0x08000000).decode().strip())
    except Exception:
        return 0.0

lines = [
    "# THINKLATE CENTRAL SHARED ASSET VAULT — MASTER INDEX",
    "> **Location:** `digital-lab/03-content-lab/shared/assets/`  ",
    "> **Mirrored Render Engine:** `digital-lab/03-content-lab/shared/motion_engine/public/`  ",
    "> **Shared Across:** ThinkLate (@wethinklate), Off Script (@OffScriptEddy), Sarwanology (@sarwanology)  ",
    "> **Last Indexed:** November 7, 2026",
    "",
    "---",
    "",
    "## 1. Curated Documentary Stock B-Roll (`broll/`)",
    "| File Name | Size (KB) | Duration | Visual Context & Scene Application |",
    "|:---|:---:|:---:|:---|"
]

BROLL_DESCRIPTIONS = {
    "broll_city_grid.mp4": "Nighttime metropolitan power grid & glowing city skyline",
    "broll_cooling_towers.mp4": "Industrial thermal power plant cooling towers & steam",
    "broll_power_lines.mp4": "High-voltage electrical transmission towers at dusk",
    "broll_servers.mp4": "Hyperscale data center server racks with blinking LEDs",
    "courtroom.mp4": "Moody mahogany courtroom interior, witness stand & judge bench",
    "prison_bars.mp4": "Cold steel prison cell bars sliding shut with deep shadows",
    "dna_lab.mp4": "Forensic molecular biology lab with micropipettes & blue lighting",
    "archive_files.mp4": "Investigative case folders & legal dockets sorted on desk",
    "brain_synapse.mp4": "3D neurobiology synaptic axons firing electrical impulses",
    "broll_smartphone_scrolling.mp4": "Close-up hands scrolling smartphone camera roll / gallery",
    "broll_birthday_candles.mp4": "Slow-motion birthday cake candles glowing in dark room",
    "broll_lightbulb_filament.mp4": "Dim 20-Watt tungsten lightbulb filament glowing in darkness",
    "broll_laser_optics.mp4": "Coherent optical laser beam splitting across physics laboratory prism",
    "broll_shattered_glass.mp4": "High-speed slow motion glass plate shattering into shards",
    "broll_neurosurgery_mri.mp4": "Clinical MRI brain slices & neurosurgical cortical diagnostics",
    "broll_shopping_mall.mp4": "Crowded multi-level shopping mall escalators & pedestrian flow",
    "broll_vintage_camcorder.mp4": "Retro 1990s VHS camcorder & nostalgic analog tape playback",
    "broll_psych_notebook.mp4": "Psychologist taking clinical interview notes by hand",
    "broll_protein_molecules.mp4": "Cellular molecular protein synthesis & synaptic receptor bonding",
    "broll_photocopier_scan.mp4": "Office xerox photocopier light bar scanning document",
    "broll_soccer_sunset.mp4": "Golden-hour soccer stadium pitch & nostalgic sports memory",
    "broll_savanna_lion.mp4": "African savanna predator stalking through tall grass at dusk",
    "broll_couple_argument.mp4": "Late-night silhouette of two people in tense disagreement",
    "broll_eye_macro.mp4": "Extreme macro close-up of human iris dilating and blinking",
    "mixkit_money_18296-1080.mp4": "High-speed currency counting & financial liquidity flow",
    "pexels_san_francisco_street_1.mp4": "San Francisco urban street & Victorian residential architecture",
}

broll_dir = os.path.join(SHARED_ASSETS, "broll")
for fname in sorted(os.listdir(broll_dir)):
    fpath = os.path.join(broll_dir, fname)
    if os.path.isfile(fpath) and fname.endswith(".mp4"):
        sz = os.path.getsize(fpath) // 1024
        dur = get_video_duration(fpath)
        desc = BROLL_DESCRIPTIONS.get(fname, "Curated documentary B-roll footage")
        lines.append(f"| <a href=\"broll/{fname}\" target=\"_blank\">{fname} ↗</a> | {sz:,} KB | {dur:.1f}s | {desc} |")

lines.extend([
    "",
    "---",
    "",
    "## 2. Verified Archival Portraits & Scientific Diagrams (`images/historical_science/`)",
    "| File Name | Size (KB) | Attribution / Source | Documentary Application |",
    "|:---|:---:|:---|:---|"
])

IMG_DESCRIPTIONS = {
    "Jennifer_Thompson_Cannino_and_Ronald_Cot.jpg": ("Wikimedia Commons (PopTech 2010)", "Jennifer Thompson & Ronald Cotton together post-exoneration"),
    "GelDoc_DNA_gel_electrophoresis_photograp.jpg": ("Wikimedia Commons (Ethidium Bromide Gel)", "Forensic DNA gel electrophoresis banding proof"),
    "dennis_gabor_portrait.jpg": ("Wikimedia Commons (1971 Nobel Archive)", "Dennis Gabor, Father of Optical Holography (1948/1971)"),
    "elizabeth_loftus_portrait.jpg": ("Wikimedia Commons (TAM 2011)", "Psychologist Elizabeth Loftus, pioneer of False Memory / Lost in the Mall study"),
    "holography_diagram.jpg": ("Wikimedia Commons (Optical Hologram)", "3D laser interference reconstruction of holographic plate"),
    "hippocampus_brain.jpg": ("Gray's Anatomy Fig. 739 (Public Domain)", "Anatomical diagram highlighting the human hippocampus & temporal lobe"),
    "dna_profiling.jpg": ("Wikimedia Commons", "Molecular double-helix DNA structure diagram"),
}

img_dir = os.path.join(SHARED_ASSETS, "images", "historical_science")
if os.path.exists(img_dir):
    for fname in sorted(os.listdir(img_dir)):
        fpath = os.path.join(img_dir, fname)
        if os.path.isfile(fpath) and fname.lower().endswith((".jpg", ".png", ".jpeg")):
            sz = os.path.getsize(fpath) // 1024
            src_attr, desc = IMG_DESCRIPTIONS.get(fname, ("Wikimedia Commons", "Verified archival reference image"))
            lines.append(f"| <a href=\"images/historical_science/{fname}\" target=\"_blank\">{fname} ↗</a> | {sz:,} KB | {src_attr} | {desc} |")

lines.extend([
    "",
    "---",
    "",
    "## 3. Warm Cinema Vault Foley & SFX (`sfx/cinema_vault/`)",
    "| File Name | Size (KB) | Acoustic Profile |",
    "|:---|:---:|:---|"
])

sfx_dir = os.path.join(SHARED_ASSETS, "sfx", "cinema_vault")
if os.path.exists(sfx_dir):
    for fname in sorted(os.listdir(sfx_dir)):
        fpath = os.path.join(sfx_dir, fname)
        if os.path.isfile(fpath) and fname.endswith(".mp3"):
            sz = os.path.getsize(fpath) // 1024
            lines.append(f"| <a href=\"sfx/cinema_vault/{fname}\" target=\"_blank\">{fname} ↗</a> | {sz:,} KB | Warm low-passed (<8kHz) broadcast Foley |")

lines.extend([
    "",
    "---",
    "",
    "## 4. Sub-Catalogs & Specialized Vaults",
    "- **Pop-Culture & Cinema Clips:** <a href=\"pop_culture/CLIP_INDEX.md\" target=\"_blank\">pop_culture/CLIP_INDEX.md ↗</a>",
    "- **Global & India Viral Memes (150+ Clips & Templates):** <a href=\"memes/MEME_CATALOG.md\" target=\"_blank\">memes/MEME_CATALOG.md ↗</a>",
    "- **Competitor Packaging Benchmarks:** <a href=\"competitor_thumbnails/PACKAGING_DOSSIER.md\" target=\"_blank\">competitor_thumbnails/PACKAGING_DOSSIER.md ↗</a>",
    ""
])

index_path = os.path.join(SHARED_ASSETS, "SHARED_ASSET_INDEX.md")
with open(index_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"[+] Updated Master Shared Asset Index: {index_path}")

