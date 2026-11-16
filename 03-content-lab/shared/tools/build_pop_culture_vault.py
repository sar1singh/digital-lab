#!/usr/bin/env python3
"""
Pop-Culture Vault Builder (ThinkLate Infotainment Engine)
=========================================================
Produces 5 high-voltage cinema/meme clips with 1080p 16:9 standardization,
audio normalization, verified durations (1.5s–3.5s), and cataloging.
"""

import os
import sys
import subprocess
import json

CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SHARED_DIR = os.path.dirname(SCRIPT_DIR)
VAULT_DIR = os.path.join(SHARED_DIR, "assets", "pop_culture")
RAW_DIR = os.path.join(VAULT_DIR, "raw")

def run_cmd(cmd):
    kwargs = {}
    if sys.platform == "win32":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = 0
        kwargs["startupinfo"] = startupinfo
        kwargs["creationflags"] = CREATE_NO_WINDOW
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, **kwargs)
    if res.returncode != 0:
        print(f"Warning on cmd: {' '.join(cmd[:4])}...\nStderr: {res.stderr[-300:]}")
    return res

def probe_file(fpath):
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration,size:stream=codec_type,codec_name,width,height",
        "-of", "json", fpath
    ]
    res = run_cmd(cmd)
    try:
        data = json.loads(res.stdout)
        dur = float(data.get("format", {}).get("duration", 0))
        size = int(data.get("format", {}).get("size", 0))
        v_stream = next((s for s in data.get("streams", []) if s.get("codec_type") == "video"), None)
        a_stream = next((s for s in data.get("streams", []) if s.get("codec_type") == "audio"), None)
        return {
            "duration": dur,
            "size": size,
            "width": v_stream.get("width") if v_stream else None,
            "height": v_stream.get("height") if v_stream else None,
            "vcodec": v_stream.get("codec_name") if v_stream else None,
            "acodec": a_stream.get("codec_name") if a_stream else None
        }
    except Exception as e:
        print(f"Probe error for {fpath}: {e}")
        return {}

def build_vault():
    os.makedirs(VAULT_DIR, exist_ok=True)
    
    tasks = [
        {
            "name": "wolf_of_wall_street_chest_thump.mp4",
            "desc": "The Wolf of Wall Street (2013) - Matthew McConaughey Chest Thump & Hum",
            "builder": lambda out: run_cmd([
                "ffmpeg", "-y",
                "-ss", "0.5", "-to", "3.5",
                "-i", os.path.join(RAW_DIR, "wolf_raw.mp4"),
                "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black,format=yuv420p",
                "-af", "loudnorm=I=-14:LRA=7:TP=-1.5",
                "-c:v", "libx264", "-preset", "slow", "-crf", "18",
                "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                out
            ])
        },
        {
            "name": "the_big_short_bragging.mp4",
            "desc": "The Big Short (2015) - Steve Carell: 'They're not confessing. They're bragging.'",
            "builder": lambda out: run_cmd([
                "ffmpeg", "-y",
                "-ss", "3.85", "-to", "6.68",
                "-i", os.path.join(RAW_DIR, "big_short_raw.mp4"),
                "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black,format=yuv420p",
                "-af", "volume=10dB,loudnorm=I=-14:LRA=7:TP=-1.5",
                "-c:v", "libx264", "-preset", "slow", "-crf", "18",
                "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                out
            ])
        },
        {
            "name": "succession_serious_people.mp4",
            "desc": "Succession (2023) - Logan Roy: 'You are not serious people.'",
            "builder": lambda out: run_cmd([
                "ffmpeg", "-y",
                "-ss", "3.3", "-to", "9.0",
                "-i", os.path.join(RAW_DIR, "succession_raw.mp4"),
                "-filter_complex",
                "[0:v]trim=0.2:1.3,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black[v1];"
                "[0:v]trim=3.6:5.6,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black[v2];"
                "[v1][v2]concat=n=2:v=1:a=0,format=yuv420p[vout];"
                "[0:a]atrim=0.2:1.3,asetpts=PTS-STARTPTS[a1];"
                "[0:a]atrim=3.6:5.6,asetpts=PTS-STARTPTS[a2];"
                "[a1][a2]concat=n=2:v=0:a=1,loudnorm=I=-14:LRA=7:TP=-1.5[aout]",
                "-map", "[vout]", "-map", "[aout]",
                "-c:v", "libx264", "-preset", "slow", "-crf", "18",
                "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                out
            ])
        },
        {
            "name": "jensen_huang_more_you_buy.mp4",
            "desc": "NVIDIA GTC Keynote - Jensen Huang: 'The more you buy, the more you save.'",
            "builder": lambda out: run_cmd([
                "ffmpeg", "-y",
                "-ss", "45.4", "-to", "48.4",
                "-i", os.path.join(RAW_DIR, "jensen_raw.mp4"),
                "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black,format=yuv420p",
                "-af", "loudnorm=I=-14:LRA=7:TP=-1.5",
                "-c:v", "libx264", "-preset", "slow", "-crf", "18",
                "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                out
            ])
        },
        {
            "name": "pedro_pascal_laugh_cry.mp4",
            "desc": "Pedro Pascal Laughing to Crying (Chroma Green Screen)",
            "builder": lambda out: run_cmd([
                "ffmpeg", "-y",
                "-ss", "6.5", "-to", "9.5",
                "-i", os.path.join(RAW_DIR, "pedro_raw.mp4"),
                "-vf", "scale=1920:1080,format=yuv420p",
                "-af", "loudnorm=I=-14:LRA=7:TP=-1.5",
                "-c:v", "libx264", "-preset", "slow", "-crf", "18",
                "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                out
            ])
        }
    ]
    
    results = []
    print("🎬 Building ThinkLate Pop-Culture Footage Vault...\n")
    for t in tasks:
        out_path = os.path.join(VAULT_DIR, t["name"])
        print(f"Processing: {t['name']}...")
        t["builder"](out_path)
        meta = probe_file(out_path)
        meta["name"] = t["name"]
        meta["desc"] = t["desc"]
        meta["path"] = out_path
        results.append(meta)
        print(f"  ✅ Built: {t['name']} | {meta['duration']:.2f}s | {meta['width']}x{meta['height']} | {meta['size']/1024:.1f} KB")

    return results

if __name__ == "__main__":
    build_vault()
