"""
Off Script Episode 01 — GPU Master Video Render Engine
Renders the perfectly synced 41-minute master video using NVIDIA NVENC.
Handles seamless bridging between ACBF_Full_GamePlay_1.mp4 and ACBF_Gameplay_2.mp4.
"""

import os
import sys
import json
import time
import subprocess
from pathlib import Path

V1_PATH = Path(r"C:\Users\sar1s\Documents\MyWork\YOUTUBE\#final_videos\ACBF_Full_GamePlay_1.mp4")
V2_PATH = Path(r"C:\Users\sar1s\Documents\MyWork\YOUTUBE\#final_videos\ACBF_Gameplay_2.mp4")
AUDIO_PATH = Path(r"03-content-lab/off-script/episodes/01_acbf_havana/audio/take1_trimmed.mp3")
MASTER_OUT = Path(r"C:\Users\sar1s\Documents\MyWork\YOUTUBE\#final_videos\ACBF_OffScript_Ep01_41M_Master.mp4")

SEG_DIR = Path(r"03-content-lab/off-script/episodes/01_acbf_havana/analysis/render_segments")
SEG_DIR.mkdir(parents=True, exist_ok=True)

CSV_PATH = Path(r"03-content-lab/off-script/episodes/01_acbf_havana/analysis/ep01_timeline_cuts.csv")

def main():
    t0 = time.time()
    print("=== OFF SCRIPT EPISODE 01 GPU RENDER PIPELINE ===")
    print(f"Target Master: {MASTER_OUT}")
    print(f"Master Audio:  {AUDIO_PATH}")
    print(f"Source 1:      {V1_PATH}")
    print(f"Source 2:      {V2_PATH}")

    with open(CSV_PATH, "r", encoding="utf-8") as f:
        rows = [line.strip().split(",") for line in f if line.strip()][1:]

    v1_limit = 3671.701
    segment_files = []

    print(f"\nPhase 1: Generating {len(rows)} synchronized video slices with NVENC...")
    
    # Process segments 1 to 23 from V1
    for row in rows:
        seg_id = int(row[0])
        s = float(row[1])
        e = float(row[2])
        dur = float(row[4])
        
        seg_file = SEG_DIR / f"seg_{seg_id:02d}.ts"
        segment_files.append(seg_file)

        if e <= v1_limit:
            # Segment comes entirely from V1
            cmd = [
                "ffmpeg", "-y", "-v", "error",
                "-ss", f"{s:.3f}",
                "-to", f"{e:.3f}",
                "-i", str(V1_PATH),
                "-c:v", "h264_nvenc",
                "-preset", "p4",
                "-b:v", "14M",
                "-r", "60",
                "-an",
                "-f", "mpegts",
                str(seg_file)
            ]
            print(f"Rendering Seg {seg_id:02d} from V1 ({s:.1f}s -> {e:.1f}s, dur {dur:.1f}s)...")
            subprocess.run(cmd, check=True)
            
        elif s < v1_limit and e > v1_limit:
            # Split segment across V1 and V2
            v1_part = SEG_DIR / f"seg_{seg_id:02d}_v1.ts"
            v2_part = SEG_DIR / f"seg_{seg_id:02d}_v2.ts"
            
            # V1 piece
            cmd1 = [
                "ffmpeg", "-y", "-v", "error",
                "-ss", f"{s:.3f}",
                "-to", f"{v1_limit:.3f}",
                "-i", str(V1_PATH),
                "-c:v", "h264_nvenc",
                "-preset", "p4",
                "-b:v", "14M",
                "-r", "60",
                "-an",
                "-f", "mpegts",
                str(v1_part)
            ]
            subprocess.run(cmd1, check=True)
            
            # V2 piece (scale 1080p to 2048x1152 for exact resolution match)
            v2_needed = e - v1_limit
            cmd2 = [
                "ffmpeg", "-y", "-v", "error",
                "-ss", "0.000",
                "-to", f"{v2_needed:.3f}",
                "-i", str(V2_PATH),
                "-vf", "scale=2048:1152:flags=lanczos",
                "-c:v", "h264_nvenc",
                "-preset", "p4",
                "-b:v", "14M",
                "-r", "60",
                "-an",
                "-f", "mpegts",
                str(v2_part)
            ]
            subprocess.run(cmd2, check=True)
            
            # Concat the two subparts
            concat_txt = SEG_DIR / f"seg_{seg_id:02d}_concat.txt"
            with open(concat_txt, "w", encoding="utf-8") as cf:
                cf.write(f"file '{v1_part.resolve().as_posix()}'\nfile '{v2_part.resolve().as_posix()}'\n")
            
            cmd_merge = [
                "ffmpeg", "-y", "-v", "error",
                "-f", "concat", "-safe", "0",
                "-i", str(concat_txt),
                "-c", "copy",
                "-f", "mpegts",
                str(seg_file)
            ]
            subprocess.run(cmd_merge, check=True)
            print(f"Rendered Split Seg {seg_id:02d} (V1 + V2 bridge, dur {dur:.1f}s)...")
            
        else:
            # Segment comes from V2
            v2_offset = s - v1_limit
            v2_end = e - v1_limit
            cmd = [
                "ffmpeg", "-y", "-v", "error",
                "-ss", f"{v2_offset:.3f}",
                "-to", f"{v2_end:.3f}",
                "-i", str(V2_PATH),
                "-vf", "scale=2048:1152:flags=lanczos",
                "-c:v", "h264_nvenc",
                "-preset", "p4",
                "-b:v", "14M",
                "-r", "60",
                "-an",
                "-f", "mpegts",
                str(seg_file)
            ]
            print(f"Rendering Seg {seg_id:02d} from V2 ({v2_offset:.1f}s -> {v2_end:.1f}s, dur {dur:.1f}s)...")
            subprocess.run(cmd, check=True)

    print(f"\nPhase 2: Concatenating all 26 slices and muxing with master audio ({AUDIO_PATH})...")
    list_file = SEG_DIR / "concat_list.txt"
    with open(list_file, "w", encoding="utf-8") as lf:
        for sf in segment_files:
            lf.write(f"file '{sf.resolve().as_posix()}'\n")

    cmd_final = [
        "ffmpeg", "-y", "-v", "warning",
        "-f", "concat", "-safe", "0",
        "-i", str(list_file),
        "-i", str(AUDIO_PATH),
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-movflags", "+faststart",
        str(MASTER_OUT)
    ]
    subprocess.run(cmd_final, check=True)

    elapsed = time.time() - t0
    print(f"\n[SUCCESS] Final 41-Minute Master Video Rendered in {elapsed:.1f}s ({elapsed/60:.2f} mins)!")
    print(f"Master Video Path: {MASTER_OUT}")

if __name__ == "__main__":
    main()
