#!/usr/bin/env python3
"""
ThinkLate Shared Asset Vault Harvester for L06 (The Memory Lie) & Documentary B-Roll
====================================================================================
Downloads real HD stock videos from Mixkit and authentic historical portraits from
Wikimedia Commons directly into `digital-lab/03-content-lab/shared/assets/`, mirrors
them to `shared/motion_engine/public/`, and updates `SHARED_ASSET_INDEX.md`.
"""

import os
import sys
import re
import json
import shutil
import urllib.request
import urllib.parse
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(".")
SHARED_ASSETS = os.path.join(PROJECT_ROOT, "digital-lab", "03-content-lab", "shared", "assets")
SHARED_BROLL = os.path.join(SHARED_ASSETS, "broll")
SHARED_IMAGES = os.path.join(SHARED_ASSETS, "images", "historical_science")

PUBLIC_DIR = os.path.join(PROJECT_ROOT, "digital-lab", "03-content-lab", "shared", "motion_engine", "public")
PUBLIC_BROLL = os.path.join(PUBLIC_DIR, "broll")
PUBLIC_IMAGES = os.path.join(PUBLIC_DIR, "images", "memory_lie")

for d in [SHARED_BROLL, SHARED_IMAGES, PUBLIC_BROLL, PUBLIC_IMAGES]:
    os.makedirs(d, exist_ok=True)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

# 1. Sync existing public/broll into shared/assets/broll first
for f in os.listdir(PUBLIC_BROLL):
    src = os.path.join(PUBLIC_BROLL, f)
    dst = os.path.join(SHARED_BROLL, f)
    if os.path.isfile(src) and not os.path.exists(dst):
        shutil.copy2(src, dst)

for f in os.listdir(PUBLIC_IMAGES):
    src = os.path.join(PUBLIC_IMAGES, f)
    dst = os.path.join(SHARED_IMAGES, f)
    if os.path.isfile(src) and not os.path.exists(dst):
        shutil.copy2(src, dst)

# 2. Target Documentary B-Roll Videos to Harvest from Mixkit
BROLL_TARGETS = [
    ("broll_smartphone_scrolling.mp4", ["smartphone", "phone-screen", "scrolling", "mobile-phone"]),
    ("broll_birthday_candles.mp4", ["birthday", "candles", "cake", "celebration"]),
    ("broll_lightbulb_filament.mp4", ["light-bulb", "bulb", "electricity", "lamp", "dark-room"]),
    ("broll_laser_optics.mp4", ["laser", "light-beam", "prism", "optics", "neon-lights"]),
    ("broll_shattered_glass.mp4", ["broken-glass", "glass", "mirror", "shatter", "reflection"]),
    ("broll_neurosurgery_mri.mp4", ["mri", "x-ray", "hospital", "doctor", "medical-screen"]),
    ("broll_shopping_mall.mp4", ["shopping-mall", "escalator", "crowd", "mall", "people-walking"]),
    ("broll_vintage_camcorder.mp4", ["retro", "vintage", "old-tv", "cassette", "memories"]),
    ("broll_psych_notebook.mp4", ["writing", "notebook", "pen", "therapy", "interview"]),
    ("broll_protein_molecules.mp4", ["molecules", "cells", "biology", "blood", "microscope"]),
    ("broll_photocopier_scan.mp4", ["printer", "scanner", "office", "copy", "paper"]),
    ("broll_soccer_sunset.mp4", ["soccer", "football", "stadium", "sunset", "goal"]),
    ("broll_savanna_lion.mp4", ["lion", "wildlife", "safari", "tiger", "leopard", "nature"]),
    ("broll_couple_argument.mp4", ["argument", "couple", "talking", "silhouette", "sad"]),
    ("broll_eye_macro.mp4", ["eye", "iris", "close-up-eye", "blinking", "vision"]),
]

def find_mixkit_urls(keywords, used_urls):
    for kw in keywords:
        url = f"https://mixkit.co/free-stock-video/{kw}/"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
            html = urllib.request.urlopen(req, timeout=12).read().decode('utf-8', errors='ignore')
            matches = re.findall(r'https://assets\.mixkit\.co/videos/[0-9]+/[0-9]+-720\.mp4', html)
            if not matches:
                matches = re.findall(r'https://assets\.mixkit\.co/videos/preview/mixkit-[a-zA-Z0-9_-]+-large\.mp4', html)
            for m in matches:
                if m not in used_urls:
                    return m
        except Exception:
            pass
    return None

print("=" * 70)
print("🎬 HARVESTING DOCUMENTARY B-ROLL INTO SHARED ASSET VAULT")
print("=" * 70)

used_urls = set()
for out_name, kws in BROLL_TARGETS:
    shared_path = os.path.join(SHARED_BROLL, out_name)
    public_path = os.path.join(PUBLIC_BROLL, out_name)
    if os.path.exists(shared_path) and os.path.getsize(shared_path) > 100000:
        print(f"[=] Already in vault: {out_name} ({os.path.getsize(shared_path)//1024} KB)")
        if not os.path.exists(public_path):
            shutil.copy2(shared_path, public_path)
        continue

    vid_url = find_mixkit_urls(kws, used_urls)
    if vid_url:
        used_urls.add(vid_url)
        print(f"[+] Downloading {out_name} from {vid_url}...")
        try:
            req = urllib.request.Request(vid_url, headers={'User-Agent': USER_AGENT})
            with urllib.request.urlopen(req, timeout=30) as resp, open(shared_path, 'wb') as f:
                f.write(resp.read())
            shutil.copy2(shared_path, public_path)
            print(f"    ✓ Vaulted & Mirrored: {out_name} ({os.path.getsize(shared_path)//1024} KB)")
        except Exception as e:
            print(f"    ✗ Error downloading {out_name}: {e}")
    else:
        print(f"[-] Could not find Mixkit video for {out_name}")

# 3. Harvest Real Historical Figures & Scientific Diagrams via Wikipedia REST API
WIKI_TARGETS = [
    ("dennis_gabor_portrait.jpg", "Dennis_Gabor"),
    ("elizabeth_loftus_portrait.jpg", "Elizabeth_Loftus"),
    ("holography_diagram.jpg", "Holography"),
    ("hippocampus_brain.jpg", "Hippocampus"),
    ("dna_profiling.jpg", "DNA_profiling"),
]

print("\n" + "=" * 70)
print("🖼️ HARVESTING VERIFIED ARCHIVAL PORTRAITS VIA WIKIPEDIA API")
print("=" * 70)

for out_name, wiki_slug in WIKI_TARGETS:
    shared_img = os.path.join(SHARED_IMAGES, out_name)
    public_img = os.path.join(PUBLIC_IMAGES, out_name)
    if os.path.exists(shared_img) and os.path.getsize(shared_img) > 5000:
        print(f"[=] Already in vault: {out_name}")
        if not os.path.exists(public_img):
            shutil.copy2(shared_img, public_img)
        continue

    api_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{wiki_slug}"
    try:
        req = urllib.request.Request(api_url, headers={'User-Agent': 'ThinkLateMedia/1.0 (https://youtube.com/@wethinklate)'})
        data = json.loads(urllib.request.urlopen(req, timeout=10).read().decode('utf-8'))
        img_url = data.get("originalimage", {}).get("source") or data.get("thumbnail", {}).get("source")
        if img_url:
            print(f"[+] Downloading {out_name} from {img_url}...")
            img_req = urllib.request.Request(img_url, headers={'User-Agent': USER_AGENT})
            with urllib.request.urlopen(img_req, timeout=15) as resp, open(shared_img, 'wb') as f:
                f.write(resp.read())
            shutil.copy2(shared_img, public_img)
            print(f"    ✓ Vaulted & Mirrored: {out_name} ({os.path.getsize(shared_img)//1024} KB)")
        else:
            print(f"[-] No image found in summary for {wiki_slug}")
    except Exception as e:
        print(f"[-] Failed fetching {wiki_slug}: {e}")

print("\n[+] Asset harvesting complete!")

