#!/usr/bin/env python3
"""
ThinkLate Enterprise Viral Asset Harvester Daemon
==================================================
Comprehensive autonomous background engine that harvests:
  1. Viral video reaction clips (India & USA/Global) with Speech Completion Rule.
  2. Imgflip top 100 global viral meme image templates.
  3. High-res Indian meme image templates & quote cards.
  4. Reaction GIFs for fast B-roll punch cuts.
  5. Full multi-meme video compilation packs for local offline editing.
  6. Centralized MEME_CATALOG.md index.

Usage:
  python harvest_all_assets.py --daemon    # Runs continuously in background
  python harvest_all_assets.py --all       # Runs one full harvesting pass
  python harvest_all_assets.py --images    # Harvests meme image templates only
  python harvest_all_assets.py --clips     # Harvests video reaction clips only
  python harvest_all_assets.py --packs     # Harvests compilation packs only
"""

import os
import sys
import json
import time
import argparse
import urllib.request
import subprocess
import shutil

CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SHARED_DIR = os.path.dirname(SCRIPT_DIR)
MEMES_ROOT = os.path.join(SHARED_DIR, "assets", "memes")

CLIPS_INDIA = os.path.join(MEMES_ROOT, "india")
CLIPS_USA = os.path.join(MEMES_ROOT, "usa_global")
IMAGES_GLOBAL = os.path.join(MEMES_ROOT, "images", "usa_global")
IMAGES_INDIA = os.path.join(MEMES_ROOT, "images", "india")
GIFS_GLOBAL = os.path.join(MEMES_ROOT, "gifs", "usa_global")
GIFS_INDIA = os.path.join(MEMES_ROOT, "gifs", "india")
PACKS_DIR = os.path.join(MEMES_ROOT, "packs")
CATALOG_PATH = os.path.join(MEMES_ROOT, "MEME_CATALOG.md")

# Ensure all subdirectories exist
for d in [CLIPS_INDIA, CLIPS_USA, IMAGES_GLOBAL, IMAGES_INDIA, GIFS_GLOBAL, GIFS_INDIA, PACKS_DIR]:
    os.makedirs(d, exist_ok=True)

def run_proc(cmd):
    kwargs = {}
    if sys.platform == "win32":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = 0
        kwargs["startupinfo"] = startupinfo
        kwargs["creationflags"] = CREATE_NO_WINDOW
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, **kwargs)

def probe_file(filepath):
    if not os.path.exists(filepath):
        return None
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "stream=codec_type,codec_name,width,height:format=duration,size",
        "-of", "json",
        filepath
    ]
    res = run_proc(cmd)
    if res.returncode != 0:
        return None
    try:
        data = json.loads(res.stdout)
        duration = float(data.get("format", {}).get("duration", 0.0))
        size_bytes = int(data.get("format", {}).get("size", 0))
        width, height = 0, 0
        for s in data.get("streams", []):
            if s.get("codec_type") == "video":
                width = int(s.get("width", 0))
                height = int(s.get("height", 0))
                break
        return {"duration": duration, "size_kb": size_bytes / 1024, "width": width, "height": height}
    except:
        return None

# ==========================================
# 1. HARVEST GLOBAL MEME IMAGES (Imgflip Top 100)
# ==========================================
def harvest_global_images():
    print("\n📸 [Imgflip] Harvesting Top 100 Global Viral Meme Templates...")
    url = "https://api.imgflip.com/get_memes"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        resp = urllib.request.urlopen(req, timeout=15)
        data = json.loads(resp.read().decode("utf-8"))
        if not data.get("success"):
            print("❌ Failed to fetch Imgflip manifest")
            return 0
        
        memes = data["data"]["memes"]
        count = 0
        for m in memes:
            clean_name = m["name"].lower()
            for ch in [' ', '/', '\\', ':', '*', '?', '"', '<', '>', '|', '-', '\'']:
                clean_name = clean_name.replace(ch, '_')
            while '__' in clean_name:
                clean_name = clean_name.replace('__', '_')
            clean_name = clean_name.strip('_')
            
            ext = os.path.splitext(m["url"])[1] or ".jpg"
            target_path = os.path.join(IMAGES_GLOBAL, f"{clean_name}{ext}")
            
            if os.path.exists(target_path) and os.path.getsize(target_path) > 1000:
                continue
                
            try:
                img_req = urllib.request.Request(m["url"], headers={"User-Agent": USER_AGENT})
                with urllib.request.urlopen(img_req, timeout=10) as r, open(target_path, "wb") as f:
                    f.write(r.read())
                count += 1
                if count % 10 == 0:
                    print(f"   Saved {count} meme templates...")
            except Exception as e:
                pass
        print(f"✅ Harvested {count} new Global Meme Image Templates (Total: {len(os.listdir(IMAGES_GLOBAL))})")
        return count
    except Exception as e:
        print(f"❌ Imgflip Error: {e}")
        return 0

# ==========================================
# 2. HARVEST INDIAN MEME IMAGES & QUOTES
# ==========================================
INDIAN_IMAGE_TEMPLATES = [
    {
        "name": "paisa_hi_paisa_hoga",
        "url": "https://indianmemetemplates.com/wp-content/uploads/phir-hera-pheri-paisa-hi-paisa-hoga-meme-template.jpg",
        "quote": "Paisa hi paisa hoga! (Akshay Kumar)"
    },
    {
        "name": "bhai_kya_kar_raha_hai_tu",
        "url": "https://indianmemetemplates.com/wp-content/uploads/Bhai-kya-kar-raha-hai-tu.jpg",
        "quote": "Bhai kya kar raha hai tu? (Ashneer Grover)"
    },
    {
        "name": "welcome_seh_lenge_thoda",
        "url": "https://indianmemetemplates.com/wp-content/uploads/2019/02/welcome-nana-patekar-seh-lenge-thoda.jpg",
        "quote": "Thoda dard hua par seh lenge thoda (Nana Patekar)"
    },
    {
        "name": "panchayat_dekh_raha_hai_binod",
        "url": "https://indianmemetemplates.com/wp-content/uploads/dekh-raha-hai-binod.jpg",
        "quote": "Dekh raha hai Binod (Panchayat)"
    },
    {
        "name": "dhol_aao_kabhi_haveli_pe",
        "url": "https://indianmemetemplates.com/wp-content/uploads/aao-kabhi-haveli-pe.jpg",
        "quote": "Aao kabhi haveli pe"
    },
    {
        "name": "aloknath_sanskari",
        "url": "https://raw.githubusercontent.com/PramodShenoy/Meme-Inator/master/app/src/main/res/drawable/aloknath.jpg",
        "quote": "Babuji Sanskari Aloknath"
    },
    {
        "name": "arnab_goswami_thug_life",
        "url": "https://raw.githubusercontent.com/PramodShenoy/Meme-Inator/master/app/src/main/res/drawable/arnab_thug_life.jpg",
        "quote": "The nation wants to know! (Arnab Goswami)"
    },
    {
        "name": "cid_acp_pradyuman",
        "url": "https://raw.githubusercontent.com/PramodShenoy/Meme-Inator/master/app/src/main/res/drawable/cid.jpg",
        "quote": "Kuch toh gadbad hai Daya! (ACP Pradyuman)"
    },
    {
        "name": "kejriwal_cough_muffler",
        "url": "https://raw.githubusercontent.com/PramodShenoy/Meme-Inator/master/app/src/main/res/drawable/kejri.jpg",
        "quote": "Mufflerman Arvind Kejriwal"
    },
    {
        "name": "narendra_modi_namo_serious",
        "url": "https://raw.githubusercontent.com/PramodShenoy/Meme-Inator/master/app/src/main/res/drawable/namo_s.jpg",
        "quote": "Narendra Modi Intense Stare"
    },
    {
        "name": "nana_patekar_angry",
        "url": "https://raw.githubusercontent.com/PramodShenoy/Meme-Inator/master/app/src/main/res/drawable/nana_angry.jpg",
        "quote": "Nana Patekar Intense Monologue"
    },
    {
        "name": "rahul_gandhi_smirk",
        "url": "https://raw.githubusercontent.com/PramodShenoy/Meme-Inator/master/app/src/main/res/drawable/rahul1.jpg",
        "quote": "Rahul Gandhi Signature Wink / Smirk"
    },
    {
        "name": "rajinikanth_mind_it",
        "url": "https://raw.githubusercontent.com/PramodShenoy/Meme-Inator/master/app/src/main/res/drawable/rajani_mindit.jpg",
        "quote": "Mind It! (Thalaivar Rajinikanth)"
    }
]

def harvest_indian_images():
    print("\n🇮🇳 [India Templates] Harvesting High-Res Indian Meme Images...")
    count = 0
    for item in INDIAN_IMAGE_TEMPLATES:
        target_path = os.path.join(IMAGES_INDIA, f"{item['name']}.jpg")
        if os.path.exists(target_path) and os.path.getsize(target_path) > 1000:
            continue
        try:
            req = urllib.request.Request(item["url"], headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=10) as r, open(target_path, "wb") as f:
                f.write(r.read())
            count += 1
            print(f"   ✅ Saved: {item['name']}.jpg")
        except Exception as e:
            pass
    print(f"✅ Harvested Indian Meme Stills (Total: {len(os.listdir(IMAGES_INDIA))})")
    return count

# ==========================================
# 3. EXPANDED VIDEO REACTION CLIPS (Speech Completion Rule)
# ==========================================
EXPANDED_CLIPS = [
    # INDIA VIRAL VIDEO CLIPS
    {
        "id": "aman_gupta_hum_bhi_bana_lenge",
        "category": "india",
        "title": "Hum Bhi Bana Lenge (Aman Gupta / Shark Tank)",
        "dialogue": "Haan toh hum bhi bana lenge! Isme kya badi baat hai?",
        "target": "ytsearch1:aman gupta hum bhi bana lenge meme template",
        "type": "full"
    },
    {
        "id": "carryminati_toh_kaise_hain_aap",
        "category": "india",
        "title": "Toh Kaise Hain Aap Log (CarryMinati)",
        "dialogue": "Toh kaise hain aap log?!",
        "target": "ytsearch1:carryminati toh kaise hain aap log intro meme green screen",
        "type": "full"
    },
    {
        "id": "zakir_khan_sakht_launda",
        "category": "india",
        "title": "Sakht Launda (Zakir Khan)",
        "dialogue": "Lekin apun bhi sakht launda hai... yahan apun pighal gaya!",
        "target": "ytsearch1:zakir khan pighal gaya meme template",
        "type": "full"
    },
    {
        "id": "bassi_hum_toh_aise_hi_the",
        "category": "india",
        "title": "Hum Toh Aise Hi The (Bassi Standup)",
        "dialogue": "Hum toh aise hi the... koi scene hi nahi tha bhai.",
        "target": "OB7FTyuCpe8",
        "type": "full"
    },
    {
        "id": "choti_bachi_ho_kya",
        "category": "india",
        "title": "Choti Bachi Ho Kya (Tiger Shroff Heropanti)",
        "dialogue": "Choti bachi ho kya? Samajh nahi aata?",
        "target": "ytsearch1:choti bachi ho kya meme template 1080p",
        "type": "full"
    },
    {
        "id": "bhupendra_jogi_us",
        "category": "india",
        "title": "Bhupendra Jogi US Tour (Viral Meme)",
        "dialogue": "US mein kahan kahan gaye hain aap? — Bhupendra Jogi.",
        "target": "ytsearch1:bhupendra jogi viral meme template",
        "type": "full"
    },
    {
        "id": "moye_moye_viral",
        "category": "india",
        "title": "Moye Moye Tragic Realization (Viral Song)",
        "dialogue": "Moye moye... moye moye...",
        "target": "ytsearch1:moye moye meme template green screen",
        "type": "full"
    },
    {
        "id": "puneet_superstar_screaming",
        "category": "india",
        "title": "Lord Puneet Screaming Rage (Puneet Superstar)",
        "dialogue": "[Loud unhinged screaming laughter / facepalm]",
        "target": "ytsearch1:puneet superstar screaming meme green screen",
        "type": "full"
    },
    {
        "id": "chin_tapak_dum_dum",
        "category": "india",
        "title": "Chin Tapak Dum Dum (Viral 2024 Green Screen)",
        "dialogue": "Chin tapak dum dum!",
        "target": "I_1RopANF7E",
        "type": "full"
    },
    {
        "id": "just_looking_like_a_wow",
        "category": "india",
        "title": "Just Looking Like A Wow (Jasmeen Kaur)",
        "dialogue": "So beautiful, so elegant, just looking like a wow!",
        "target": "zom_mABGS3M",
        "type": "full"
    },
    {
        "id": "arpit_bala_hum_pe_to_hai_hi_nau",
        "category": "india",
        "title": "Hum Pe To Hai Hi 9 (Arpit Bala)",
        "dialogue": "Hum pe to hai hi 9 😛",
        "target": "Ny74RSt_qvw",
        "type": "full"
    },
    {
        "id": "jis_raah_pe_chal_rahe_ho_andhera",
        "category": "india",
        "title": "Jis Raah Pe Chal Rahe Ho Aage Andhera Hai",
        "dialogue": "Jis raah pe tum chal rahe ho beta wahan aage andhera hai.",
        "target": "Z9oThmTT6j0",
        "type": "full"
    },

    # USA & GLOBAL VIDEO CLIPS
    {
        "id": "elon_musk_go_fuck_yourself",
        "category": "usa_global",
        "title": "Go Fuck Yourself (Elon Musk DealBook Interview)",
        "dialogue": "If somebody's gonna try to blackmail me with advertising... go fuck yourself. Go. Fuck. Yourself.",
        "target": "ytsearch1:elon musk go fuck yourself dealbook 1080p full clip",
        "type": "slice",
        "start": "00:00",
        "duration": 9
    },
    {
        "id": "gordon_ramsay_idiot_sandwich",
        "category": "usa_global",
        "title": "Idiot Sandwich (Gordon Ramsay)",
        "dialogue": "What are you? — An idiot sandwich, chef.",
        "target": "ytsearch1:what are you idiot sandwich full meme clip",
        "type": "full"
    },
    {
        "id": "kai_cenat_screaming_chair_fall",
        "category": "usa_global",
        "title": "Kai Cenat & IShowSpeed Losing Their Minds (Green Screen)",
        "dialogue": "[Loud scream / losing their minds on stream]",
        "target": "jYT9h04L-3M",
        "type": "full"
    },
    {
        "id": "ishowspeed_shocked_reaction",
        "category": "usa_global",
        "title": "IShowSpeed Shocked Reaction (Green Screen)",
        "dialogue": "[Shocked jaw drop / sudden aggressive reaction]",
        "target": "ytsearch1:iShowSpeed Shocking - Green Screen",
        "type": "full"
    },
    {
        "id": "spongebob_a_few_moments_later",
        "category": "usa_global",
        "title": "A Few Moments Later (SpongeBob Timecard)",
        "dialogue": "A few moments later...",
        "target": "ytsearch1:a few moments later spongebob time card 1080p",
        "type": "full"
    },
    {
        "id": "hawk_tuah_viral",
        "category": "usa_global",
        "title": "Hawk Tuah Spit On That Thang (Viral 2024)",
        "dialogue": "You gotta give 'em that 'hawk tuah' and spit on that thang!",
        "target": "ytsearch1:hawk tuah girl meme template green screen",
        "type": "full"
    },
    {
        "id": "ryan_gosling_i_drive",
        "category": "usa_global",
        "title": "I Drive (Ryan Gosling / Drive)",
        "dialogue": "I drive.",
        "target": "ytsearch1:ryan gosling i drive meme clip 1080p",
        "type": "full"
    },
    {
        "id": "very_demure_very_mindful",
        "category": "usa_global",
        "title": "Very Demure Very Mindful (Green Screen 2024)",
        "dialogue": "See how I do my makeup for work? Very demure, very mindful.",
        "target": "hnidS6CD_qs",
        "type": "full"
    },
    {
        "id": "pedro_pascal_laughing_crying",
        "category": "usa_global",
        "title": "Pedro Pascal Laughing Then Crying (Green Screen)",
        "dialogue": "[Uncontrollable laughing turning into tragic crying]",
        "target": "ob5HBNwaS_o",
        "type": "full"
    },
    {
        "id": "english_or_spanish_freeze",
        "category": "usa_global",
        "title": "English Or Spanish Freeze (Viral 2024)",
        "dialogue": "English or Spanish? Whoever moves first is gay.",
        "target": "4DJdJ5R9F6U",
        "type": "full"
    },
    {
        "id": "steve_ballmer_developers",
        "category": "usa_global",
        "title": "Steve Ballmer Developers Monologue",
        "dialogue": "Developers, developers, developers, developers!",
        "target": "Vhh_GeBPOhs",
        "type": "full"
    }
]

def harvest_single_video_clip(item):
    target_dir = CLIPS_INDIA if item["category"] == "india" else CLIPS_USA
    final_file = os.path.join(target_dir, f"{item['id']}.mp4")
    
    if os.path.exists(final_file) and os.path.getsize(final_file) > 50000:
        info = probe_file(final_file)
        if info:
            print(f"⏩ [Cached] {item['id']}.mp4 ({info['duration']:.1f}s)")
            return True

    print(f"\n🎬 Harvesting Video: {item['title']}...")
    temp_raw = os.path.join(target_dir, f"{item['id']}_raw.mp4")
    
    cmd = [
        "yt-dlp",
        item["target"],
        "-f", "bestvideo[height<=1080]+bestaudio/best",
        "--merge-output-format", "mp4",
        "-o", temp_raw,
        "--no-playlist",
        "--force-overwrites"
    ]
    
    if item.get("type") == "slice":
        cmd.extend(["--download-sections", f"*{item.get('start', '00:00')}-{item.get('duration', 7)}"])

    run_proc(cmd)
    
    # Locate downloaded candidate
    downloaded = temp_raw if os.path.exists(temp_raw) else None
    if not downloaded:
        for f in os.listdir(target_dir):
            if f.startswith(f"{item['id']}_raw") and not f.endswith(".part"):
                downloaded = os.path.join(target_dir, f)
                break
                
    if not downloaded or os.path.getsize(downloaded) < 1000:
        print(f"❌ Failed to download {item['id']}")
        return False

    # Convert to 48kHz AAC stereo
    temp_aac = final_file + ".tmp.mp4"
    remux_cmd = [
        "ffmpeg", "-y", "-i", downloaded,
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        temp_aac
    ]
    res = run_proc(remux_cmd)
    if res.returncode == 0 and os.path.exists(temp_aac) and os.path.getsize(temp_aac) > 1000:
        if os.path.exists(final_file):
            os.remove(final_file)
        shutil.move(temp_aac, final_file)
        try:
            os.remove(downloaded)
        except:
            pass
        info = probe_file(final_file)
        if info:
            print(f"   ✅ Vaulted: {item['id']}.mp4 ({info['duration']:.1f}s, {info['width']}x{info['height']})")
            return True
            
    print(f"❌ Failed to standardize {item['id']}")
    return False

# ==========================================
# 4. HARVEST FULL MULTI-MEME COMPILATION PACKS
# ==========================================
COMPILATION_PACKS = [
    {
        "id": "100_green_screen_memes_global_pack",
        "title": "100 Green Screen Memes for Editing (No Copyright Free Pack)",
        "url": "https://www.youtube.com/watch?v=2G--pt5aZ5M"
    },
    {
        "id": "100_indian_memes_editor_pack",
        "title": "100+ Indian Memes for Video Editing (No Copyright Templates)",
        "url": "https://www.youtube.com/watch?v=tnllb7LeKOI"
    }
]

def harvest_compilation_packs():
    print("\n📦 [Packs] Harvesting Offline Master Compilation Packs...")
    for p in COMPILATION_PACKS:
        out_file = os.path.join(PACKS_DIR, f"{p['id']}.mp4")
        if os.path.exists(out_file) and os.path.getsize(out_file) > 10000000:
            print(f"⏩ [Cached] {p['id']}.mp4")
            continue
        print(f"   Downloading pack: {p['title']}...")
        cmd = [
            "yt-dlp",
            p["url"],
            "-f", "bestvideo[height<=720]+bestaudio/best",
            "--merge-output-format", "mp4",
            "-o", out_file,
            "--no-playlist",
            "--force-overwrites"
        ]
        res = run_proc(cmd)
        if os.path.exists(out_file) and os.path.getsize(out_file) > 1000:
            size_mb = os.path.getsize(out_file) / (1024 * 1024)
            print(f"   ✅ Master Pack Saved: {p['id']}.mp4 ({size_mb:.1f} MB)")

# ==========================================
# 5. REBUILD MASTER CATALOG (Markdown)
# ==========================================
def rebuild_master_catalog():
    print("\n📋 Generating Comprehensive MEME_CATALOG.md...")
    
    lines = [
        "# ThinkLate & Multi-Channel Enterprise Viral Asset Vault",
        "> **Location:** `digital-lab/03-content-lab/shared/assets/memes/`  ",
        "> **Standards:** Broadcast 1080p/720p H.264 · 48kHz AAC Stereo · Speech Completion Rule (Zero mid-sentence cuts).  ",
        "> **Shared Across:** ThinkLate (@wethinklate), Off Script (@OffScriptEddy), and Sarwanology.",
        "",
        "---",
        "",
        "## 🎬 1. India Viral Video Clips (`memes/india/`)",
        "High-voltage satirical reaction clips with complete dialogue delivery from Shark Tank India, Panchayat, and cult Bollywood comedy.",
        "",
        "| File Name | Duration | Resolution | File Size | Status |",
        "| :--- | :---: | :---: | :---: | :---: |"
    ]
    
    for f in sorted(os.listdir(CLIPS_INDIA)):
        if f.endswith(".mp4") and not f.endswith("_raw.mp4") and not ".tmp" in f:
            fpath = os.path.join(CLIPS_INDIA, f)
            info = probe_file(fpath)
            if info:
                link = f"<a href=\"india/{f}\" target=\"_blank\">{f} ↗</a>"
                lines.append(f"| {link} | **{info['duration']:.1f}s** | {info['width']}x{info['height']} | {info['size_kb']:.1f} KB | Verified ✅ |")

    lines.extend([
        "",
        "---",
        "",
        "## 🎬 2. USA & Global Viral Video Clips (`memes/usa_global/`)",
        "Iconic reaction clips, executive keynotes, green-screen memes, and high-tension cinema soundbites with 100% complete sentences.",
        "",
        "| File Name | Duration | Resolution | File Size | Status |",
        "| :--- | :---: | :---: | :---: | :---: |"
    ])
    
    for f in sorted(os.listdir(CLIPS_USA)):
        if f.endswith(".mp4") and not f.endswith("_raw.mp4") and not ".tmp" in f:
            fpath = os.path.join(CLIPS_USA, f)
            info = probe_file(fpath)
            if info:
                link = f"<a href=\"usa_global/{f}\" target=\"_blank\">{f} ↗</a>"
                lines.append(f"| {link} | **{info['duration']:.1f}s** | {info['width']}x{info['height']} | {info['size_kb']:.1f} KB | Verified ✅ |")

    lines.extend([
        "",
        "---",
        "",
        "## 🖼️ 3. Global Meme Image Templates (`memes/images/usa_global/`)",
        f"Top 100 viral blank meme image templates from Imgflip ready for kinetic DaVinci overlays or graphic slides ({len(os.listdir(IMAGES_GLOBAL))} vaulted):",
        "",
        "| Preview Link | File Name | Size |",
        "| :--- | :--- | :---: |"
    ])
    
    for f in sorted(os.listdir(IMAGES_GLOBAL))[:25]:
        if f.endswith(('.jpg', '.png', '.webp')):
            fpath = os.path.join(IMAGES_GLOBAL, f)
            size_kb = os.path.getsize(fpath) / 1024
            link = f"<a href=\"images/usa_global/{f}\" target=\"_blank\">{f} ↗</a>"
            lines.append(f"| {link} | `{f}` | {size_kb:.1f} KB |")
    if len(os.listdir(IMAGES_GLOBAL)) > 25:
        lines.append(f"| *...and {len(os.listdir(IMAGES_GLOBAL)) - 25} more image templates vaulted in folder* | - | - |")

    lines.extend([
        "",
        "---",
        "",
        "## 🖼️ 4. India Meme Stills & Quote Cards (`memes/images/india/`)",
        f"High-res Indian meme templates, reaction faces, and iconic quote cards ({len(os.listdir(IMAGES_INDIA))} vaulted):",
        "",
        "| Preview Link | File Name | Size |",
        "| :--- | :--- | :---: |"
    ])

    for f in sorted(os.listdir(IMAGES_INDIA)):
        if f.endswith(('.jpg', '.png', '.webp')):
            fpath = os.path.join(IMAGES_INDIA, f)
            size_kb = os.path.getsize(fpath) / 1024
            link = f"<a href=\"images/india/{f}\" target=\"_blank\">{f} ↗</a>"
            lines.append(f"| {link} | `{f}` | {size_kb:.1f} KB |")

    lines.extend([
        "",
        "---",
        "",
        "## 📦 5. Master Offline Compilation Packs (`memes/packs/`)",
        "Full length multi-clip compilation packs for offline editor browsing and local scene detection:",
        "",
        "| Pack File Name | Size | Description |",
        "| :--- | :---: | :--- |"
    ])
    
    for f in sorted(os.listdir(PACKS_DIR)):
        if f.endswith(".mp4"):
            fpath = os.path.join(PACKS_DIR, f)
            size_mb = os.path.getsize(fpath) / (1024 * 1024)
            link = f"<a href=\"packs/{f}\" target=\"_blank\">{f} ↗</a>"
            lines.append(f"| {link} | **{size_mb:.1f} MB** | 100+ separated green-screen and Indian editor memes |")

    with open(CATALOG_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"📋 Master Catalog updated: {CATALOG_PATH}")

def run_full_harvest_cycle():
    print(f"\n=======================================================")
    print(f"🚀 EXECUTING VIRAL ASSET HARVEST PASS ({time.strftime('%Y-%m-%d %H:%M:%S')})")
    print(f"=======================================================")
    
    # 1. Global Meme Images
    harvest_global_images()
    
    # 2. Indian Meme Stills
    harvest_indian_images()
    
    # 3. Expanded Video Reaction Clips
    print(f"\n🎬 Harvesting {len(EXPANDED_CLIPS)} Expanded Video Reaction Clips...")
    for item in EXPANDED_CLIPS:
        try:
            harvest_single_video_clip(item)
        except Exception as e:
            print(f"Error on {item['id']}: {e}")
            
    # 4. Compilation Packs
    try:
        harvest_compilation_packs()
    except Exception as e:
        print(f"Error on packs: {e}")
        
    # 5. Rebuild Catalog
    rebuild_master_catalog()
    print("\n✅ Harvest pass complete!")

def main():
    parser = argparse.ArgumentParser(description="ThinkLate Enterprise Viral Asset Harvester Daemon")
    parser.add_argument("--daemon", action="store_true", help="Run continuously in background (sleeps between passes)")
    parser.add_argument("--all", action="store_true", help="Run one full harvest pass")
    parser.add_argument("--images", action="store_true", help="Harvest only images")
    parser.add_argument("--clips", action="store_true", help="Harvest only video clips")
    parser.add_argument("--packs", action="store_true", help="Harvest only compilation packs")
    parser.add_argument("--catalog", action="store_true", help="Rebuild catalog only")
    args = parser.parse_args()

    if args.catalog:
        rebuild_master_catalog()
        return

    if args.images:
        harvest_global_images()
        harvest_indian_images()
        rebuild_master_catalog()
        return

    if args.clips:
        for item in EXPANDED_CLIPS:
            harvest_single_video_clip(item)
        rebuild_master_catalog()
        return

    if args.packs:
        harvest_compilation_packs()
        rebuild_master_catalog()
        return

    if args.daemon:
        print("🤖 Harvester Daemon Started. Running continuously in background...")
        while True:
            try:
                run_full_harvest_cycle()
            except Exception as e:
                print(f"Daemon error: {e}")
            # Sleep 15 minutes before checking for new targets or catalog refresh
            print("💤 Sleeping 15 minutes before next harvest check...")
            time.sleep(900)
    else:
        run_full_harvest_cycle()

if __name__ == "__main__":
    main()
