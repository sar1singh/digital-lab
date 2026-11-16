#!/usr/bin/env python3
"""
ThinkLate Short 05 Audio Re-Master (V3 Ultra-Clean Voice-Forward)
===============================================================
Key fixes:
1. Replaced dramatic film score with pure warm ambient drone (bgm_cinematic_free-stock-music_ambient.mp3)
   - Zero violin screeching, zero piano arpeggios, zero percussion
2. Lowered BGM to -32dB (completely transparent background tension)
3. Deep vocal pocket EQ: -10dB @ 1500Hz, -8dB @ 3000Hz, lowpassed at 3500Hz
4. Softened Cinema SFX hits (0.15 to 0.22)
5. Removed secondary loudnorm from amix to prevent dynamic amplification of music during speech pauses
6. Fast NVENC 1080x1920 remux with burned subtitles
"""
import json
import os
import pathlib
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

SHORT_DIR = pathlib.Path(__file__).resolve().parent
PROJECT_ROOT = SHORT_DIR.parents[5]
CINEMA_SFX = PROJECT_ROOT / "digital-lab" / "03-content-lab" / "shared" / "assets" / "sfx" / "cinema_vault"
BGM_SRC = PROJECT_ROOT / "digital-lab" / "03-content-lab" / "shared" / "assets" / "bgm_vault" / "bgm_cinematic_free-stock-music_ambient.mp3"

VOICE_WAV = SHORT_DIR / "audio" / "voiceover_clean.wav"
MIXED_AUDIO = SHORT_DIR / "audio" / "full_mix_s05.wav"
CONCAT_RAW = SHORT_DIR / "segments" / "concat_visual_raw.mp4"
ASS_SUBS = SHORT_DIR / "subtitles_s05.ass"
FINAL_MASTER_MP4 = SHORT_DIR / "ThinkLate_Short05_The_Shelf_Price_Is_Fake_1080x1920_MASTER.mp4"

CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0

sfx_shutter = CINEMA_SFX / "camera_vintage_shutter.mp3"
sfx_paper = CINEMA_SFX / "paper_slide_document.mp3"
sfx_click = CINEMA_SFX / "camera_classic_click.mp3"
sfx_knock = CINEMA_SFX / "sub_impact_warm_knocking.mp3"

# Voice at 1.0 (100% full presence)
# BGM at -32dB (barely noticeable psychological bed)
# Bandpassed 90Hz - 3500Hz with massive 1.5kHz dip
filter_complex = (
    "[0:a]volume=1.0[v];"
    "[1:a]volume=-32dB,lowpass=f=3500,highpass=f=90,equalizer=f=1500:t=q:w=1.5:g=-10,equalizer=f=3000:t=q:w=1.5:g=-8,atrim=0:43[bgm];"
    "[2:a]adelay=100|100,volume=0.14[s_shut];"
    "[3:a]adelay=3500|3500,volume=0.16[s_pap];"
    "[4:a]adelay=11800|11800,volume=0.15[s_clk];"
    "[5:a]adelay=25500|25500,volume=0.18[s_knk1];"
    "[6:a]adelay=33300|33300,volume=0.18[s_knk2];"
    "[7:a]adelay=40500|40500,volume=0.20[s_climax];"
    "[v][bgm][s_shut][s_pap][s_clk][s_knk1][s_knk2][s_climax]amix=inputs=8:duration=first:dropout_transition=0:normalize=0[out_a]"
)

cmd = [
    "ffmpeg", "-y",
    "-i", str(VOICE_WAV),
    "-i", str(BGM_SRC),
    "-i", str(sfx_shutter),
    "-i", str(sfx_paper),
    "-i", str(sfx_click),
    "-i", str(sfx_knock),
    "-i", str(sfx_knock),
    "-i", str(sfx_knock),
    "-filter_complex", filter_complex,
    "-map", "[out_a]",
    "-ar", "48000",
    "-c:a", "pcm_s16le",
    str(MIXED_AUDIO)
]
print("[*] Mixing audio with -32dB non-intrusive ambient bed...")
subprocess.run(cmd, check=True, creationflags=CREATE_NO_WINDOW)
print("[+] Mixed audio successfully:", MIXED_AUDIO)

print("[*] Remuxing final video with burned subtitles...")
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
    "-cq", "18",
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

print("[+] Master MP4 remuxed successfully:", FINAL_MASTER_MP4)

# Audit
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
print(f"\n=== S05 V3 AUDIO AUDIT (ULTRA-CLEAN VOICE-FORWARD) ===")
print(f"  File:               {FINAL_MASTER_MP4.name} ({sz_mb:.2f} MB)")
print(f"  Video / Audio Dur:  {v_dur:.2f}s / {a_dur:.2f}s (Sync Drift: {drift:.1f} ms)")
print(f"  Integrated LUFS:    {i_lufs[-1] if i_lufs else 'N/A'} LUFS (Target: -16.0)")
print(f"  True Peak:          {tp[-1] if tp else 'N/A'} dBFS")
print("✅ S05 V3 RE-MASTER COMPLETE!")
