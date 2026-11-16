#!/usr/bin/env python3
"""
ThinkLate L06 Full 23-Scene Cinema Foley & Broadcast Audio Mixer
================================================================
Mixes `full_dialogue_master.wav` (427.96s) with:
  - Ducked ambient BGM (-25 dB with -6 dB @ 1.5 kHz vocal clarity notch)
  - 18 timed Cinema Vault Foley cues synchronized to the 23 documentary scenes
  - Broadcast EBU R128 loudness mastering (-16.5 LUFS, -1.0 dBFS true peak)
"""

import os
import sys
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(BASE_DIR, "assets", "audio")
DIALOGUE_WAV = os.path.join(AUDIO_DIR, "full_dialogue_master.wav")
BGM_SRC = os.path.abspath("digital-lab/03-content-lab/thinklate/videos/shortForm/S01_ai-energy-shock/assets/audio/ambient_music_dark_fog.mp3")
CINEMA_SFX_DIR = os.path.abspath("digital-lab/03-content-lab/shared/assets/sfx/cinema_vault")
MASTER_MIX_WAV = os.path.join(AUDIO_DIR, "full_mix_master.wav")

def get_duration(file_path):
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        file_path
    ]
    res = subprocess.run(cmd, creationflags=0x08000000, capture_output=True, text=True)
    return float(res.stdout.strip())

def main():
    print("=" * 70)
    print("🎛️ MIXING FULL 23-SCENE CINEMA FOLEY & BROADCAST MASTER AUDIO")
    print("=" * 70)

    duration = get_duration(DIALOGUE_WAV)
    print(f"[*] Master dialogue duration: {duration:.2f}s (~{int(duration//60)}m {int(duration%60)}s)")

    # Timed SFX schedule (seconds, filename, volume_db)
    SFX_SCHEDULE = [
        (3.5,   "sub_impact_deep_cinematic.mp3", -11),
        (12.2,  "camera_vintage_shutter.mp3",    -13),
        (22.0,  "paper_slide_document.mp3",      -13),
        (37.4,  "whoosh_tunnel_smooth.mp3",      -14),
        (55.7,  "camera_classic_click.mp3",      -13),
        (74.0,  "sub_impact_warm_knocking.mp3",  -12),
        (94.5,  "paper_page_turn.mp3",           -13),
        (118.6, "paper_slide_document.mp3",      -13),
        (145.5, "whoosh_tunnel_smooth.mp3",      -13),
        (180.1, "sub_impact_warm_knocking.mp3",  -12),
        (202.4, "typewriter_soft_keystroke.mp3", -12),
        (218.9, "camera_vintage_shutter.mp3",    -13),
        (237.7, "paper_slide_document.mp3",      -13),
        (255.4, "sub_impact_deep_cinematic.mp3", -12),
        (278.8, "whoosh_air_soft.mp3",           -14),
        (294.9, "sub_impact_deep_cinematic.mp3", -11),
        (302.0, "tape_rewind_cinematic.mp3",     -14),
        (337.4, "camera_classic_click.mp3",      -13),
        (358.5, "whoosh_tunnel_smooth.mp3",      -14),
        (367.8, "sub_impact_warm_knocking.mp3",  -12),
        (386.2, "paper_slide_document.mp3",      -13),
        (405.3, "whoosh_air_soft.mp3",           -14),
        (422.5, "camera_vintage_shutter.mp3",    -11),
    ]

    cmd = [
        "ffmpeg", "-y",
        "-i", DIALOGUE_WAV,
        "-stream_loop", "-1", "-i", BGM_SRC,
    ]

    for _, fname, _ in SFX_SCHEDULE:
        cmd.extend(["-i", os.path.join(CINEMA_SFX_DIR, fname)])

    filter_parts = [
        "[0:a]volume=1.0[vocal]",
        f"[1:a]atrim=0:{duration:.2f},volume=-24dB,equalizer=f=1500:t=q:w=1.5:g=-6,afade=t=out:st={duration-4:.2f}:d=4[bgm]"
    ]

    sfx_tags = []
    for idx, (ts, _, vol_db) in enumerate(SFX_SCHEDULE):
        inp_idx = idx + 2
        delay_ms = int(ts * 1000)
        tag = f"[sfx{idx}]"
        sfx_tags.append(tag)
        filter_parts.append(
            f"[{inp_idx}:a]adelay={delay_ms}|{delay_ms},volume={vol_db}dB,lowpass=f=8000{tag}"
        )

    all_inputs_str = "[vocal][bgm]" + "".join(sfx_tags)
    total_inputs = 2 + len(SFX_SCHEDULE)
    filter_parts.append(
        f"{all_inputs_str}amix=inputs={total_inputs}:duration=first:dropout_transition=2:normalize=0[mixed]"
    )
    filter_parts.append(
        "[mixed]loudnorm=I=-16.5:TP=-1.0:LRA=7[out]"
    )

    cmd.extend([
        "-filter_complex", ";".join(filter_parts),
        "-map", "[out]",
        "-ar", "48000", "-ac", "2",
        MASTER_MIX_WAV
    ])

    res = subprocess.run(cmd, creationflags=0x08000000, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"[+] Full 23-scene master audio mix written: {MASTER_MIX_WAV}")
        print(f"    Duration: {get_duration(MASTER_MIX_WAV):.2f}s | Size: {os.path.getsize(MASTER_MIX_WAV)//1024:,} KB")
    else:
        print(f"[-] FFmpeg error:\n{res.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    main()
