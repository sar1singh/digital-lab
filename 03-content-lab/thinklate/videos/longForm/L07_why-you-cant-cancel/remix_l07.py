#!/usr/bin/env python3
"""
Remix L07 Audio with voice-forward broadcast balance:
- BGM lowered to -25dB (subtle, non-intrusive cinematic mood)
- Deep parametric vocal pocket EQ (-8dB at 1.5kHz, -6dB at 3kHz)
- Voice kept at 100% full authority (0dB)
- Fast remux into Master MP4 with NVENC
"""
import json
import os
import pathlib
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

L07_DIR = pathlib.Path(__file__).resolve().parent
PROJECT_ROOT = L07_DIR.parents[5]
CINEMA_SFX = PROJECT_ROOT / "digital-lab" / "03-content-lab" / "shared" / "assets" / "sfx" / "cinema_vault"
BGM_SRC = PROJECT_ROOT / "digital-lab" / "03-content-lab" / "shared" / "assets" / "bgm_vault" / "bgm_dark_tension_free-stock-music_atmospheres.mp3"

VOICE_WAV = L07_DIR / "assets" / "audio" / "voiceover_clean.wav"
MIXED_AUDIO = L07_DIR / "assets" / "audio" / "full_mix_master.wav"
CONCAT_RAW = L07_DIR / "assets" / "segments" / "concat_visual_raw.mp4"
ASS_SUBS = L07_DIR / "subtitles_l07_master.ass"
FINAL_MASTER_MP4 = L07_DIR / "ThinkLate_L07_Why_You_Cant_Cancel_1080p_MASTER.mp4"

CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0

sfx_click = CINEMA_SFX / "camera_classic_click.mp3"
sfx_slam = CINEMA_SFX / "sub_impact_warm_knocking.mp3"
sfx_paper = CINEMA_SFX / "paper_slide_document.mp3"
sfx_shutter = CINEMA_SFX / "camera_vintage_shutter.mp3"

filter_complex = (
    "[0:a]volume=1.0[v];"
    "[1:a]volume=-25dB,equalizer=f=1500:t=q:w=1.5:g=-8,equalizer=f=3000:t=q:w=1.5:g=-6,highpass=f=80,lowpass=f=7500,atrim=0:325[bgm];"
    "[2:a]adelay=100|100,volume=0.20[sfx_c1];"
    "[3:a]adelay=37000|37000,volume=0.25[sfx_s1];"
    "[4:a]adelay=138000|138000,volume=0.25[sfx_s2];"
    "[5:a]adelay=180000|180000,volume=0.22[sfx_shut];"
    "[6:a]adelay=226000|226000,volume=0.25[sfx_p1];"
    "[7:a]adelay=270000|270000,volume=0.28[sfx_s3];"
    "[8:a]adelay=312000|312000,volume=0.32[sfx_climax];"
    "[v][bgm][sfx_c1][sfx_s1][sfx_s2][sfx_shut][sfx_p1][sfx_s3][sfx_climax]amix=inputs=9:duration=first:dropout_transition=0:normalize=0,"
    "loudnorm=I=-16:TP=-1.0:LRA=7[out_a]"
)

cmd = [
    "ffmpeg", "-y",
    "-i", str(VOICE_WAV),
    "-stream_loop", "-1", "-i", str(BGM_SRC),
    "-i", str(sfx_click),
    "-i", str(sfx_slam),
    "-i", str(sfx_slam),
    "-i", str(sfx_shutter),
    "-i", str(sfx_paper),
    "-i", str(sfx_slam),
    "-i", str(sfx_slam),
    "-filter_complex", filter_complex,
    "-map", "[out_a]",
    "-ar", "48000",
    "-c:a", "pcm_s16le",
    str(MIXED_AUDIO)
]
print("[*] Mixing L07 audio with voice-forward -25dB BGM...")
subprocess.run(cmd, check=True, creationflags=CREATE_NO_WINDOW)
print("[+] Mixed audio successfully:", MIXED_AUDIO)

print("[*] Remuxing final L07 video with burned subtitles...")
ass_escaped = str(ASS_SUBS).replace("\\", "/").replace(":", "\\:")
final_cmd = [
    "ffmpeg", "-y",
    "-i", str(CONCAT_RAW),
    "-i", str(MIXED_AUDIO),
    "-vf", f"ass='{ass_escaped}'",
    "-map", "0:v",
    "-map", "1:a",
    "-c:v", "h264_nvenc",
    "-preset", "p5",
    "-cq", "19",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-b:a", "192k",
    "-ar", "48000",
    "-movflags", "+faststart",
    "-shortest",
    str(FINAL_MASTER_MP4)
]
res = subprocess.run(final_cmd, creationflags=CREATE_NO_WINDOW)
if res.returncode != 0:
    final_cmd[final_cmd.index("h264_nvenc")] = "libx264"
    final_cmd[final_cmd.index("-cq")] = "-crf"
    subprocess.run(final_cmd, check=True, creationflags=CREATE_NO_WINDOW)

print("[+] Master L07 MP4 remuxed successfully:", FINAL_MASTER_MP4)

# Quick QC check
probe = json.loads(subprocess.check_output(
    ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", str(FINAL_MASTER_MP4)],
    creationflags=CREATE_NO_WINDOW
))
v = [s for s in probe["streams"] if s["codec_type"] == "video"][0]
a = [s for s in probe["streams"] if s["codec_type"] == "audio"][0]
v_dur = float(v.get("duration", probe["format"]["duration"]))
a_dur = float(a.get("duration", probe["format"]["duration"]))
drift = abs(v_dur - a_dur) * 1000.0

ebu = subprocess.run(
    ["ffmpeg", "-hide_banner", "-i", str(FINAL_MASTER_MP4), "-af", "ebur128=peak=true", "-f", "null", "-"],
    capture_output=True, text=True, creationflags=CREATE_NO_WINDOW
).stderr
i_lufs = re.findall(r"I:\s*([-\d.]+)\s*LUFS", ebu)
tp = re.findall(r"Peak:\s*([-\d.]+)\s*dBFS", ebu)

sz_mb = os.path.getsize(FINAL_MASTER_MP4) / (1024 * 1024)
print(f"\n=== L07 VOICE-FORWARD AUDIO AUDIT ===")
print(f"  File:               {FINAL_MASTER_MP4.name} ({sz_mb:.2f} MB)")
print(f"  Video / Audio Dur:  {v_dur:.2f}s / {a_dur:.2f}s (Sync Drift: {drift:.1f} ms)")
print(f"  Integrated LUFS:    {i_lufs[-1] if i_lufs else 'N/A'} LUFS (Target: -16.0)")
print(f"  True Peak:          {tp[-1] if tp else 'N/A'} dBFS")
print("✅ L07 REMIX COMPLETE!")
