#!/usr/bin/env python3
"""
ThinkLate Episode 06 ("The Memory Lie") — GPU-Accelerated 4-Track Widescreen Master Compiler
=============================================================================================
Compiles all 23 widescreen (1920x1080 @ 30fps) documentary scenes using:
  - Layer 1: Real curated documentary stock B-roll (`shared/assets/broll/`) with smooth cinematic pan
  - Layer 2: 35mm dark noir grade & selective focus blur (`boxblur=10:1`)
  - Layer 3: Remotion-rendered 1920x1080 RGBA forensic dossiers, real archival photos, Raptor Syndicate
             co-host sprites (`element-00.png` .. `element-22.png`), plus viral vault PiP cuts
  - Layer 4: Word-accurate ASS kinetic subtitles (`subtitles_l06_master.ass`)
  - Audio:   Full 23-scene Foley-enriched broadcast master (`full_mix_master.wav`, -16.5 LUFS)
"""

import os
import sys
import time
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(".")
SHARED_ASSETS = os.path.join(PROJECT_ROOT, "digital-lab", "03-content-lab", "shared", "assets")
BROLL_DIR = os.path.join(SHARED_ASSETS, "broll")
MEMES_USA = os.path.join(SHARED_ASSETS, "memes", "usa_global")
POP_CULTURE = os.path.join(SHARED_ASSETS, "pop_culture")

L06_DIR = os.path.join(PROJECT_ROOT, "digital-lab", "03-content-lab", "thinklate", "videos", "longForm", "L06_the-memory-lie")
PLATES_DIR = os.path.join(L06_DIR, "assets", "remotion_plates")
SEGMENTS_DIR = os.path.join(L06_DIR, "assets", "video_segments")
os.makedirs(SEGMENTS_DIR, exist_ok=True)

AUDIO_MASTER = os.path.join(L06_DIR, "assets", "audio", "full_mix_master.wav")
ASS_SUBS = os.path.join(L06_DIR, "subtitles_l06_master.ass")
FINAL_MASTER_MP4 = os.path.join(L06_DIR, "ThinkLate_L06_The_Memory_Lie_1080p_MASTER.mp4")

CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0

# Exact 23 scenes mapped to the 427.96s timeline:
# (scene_id, start_sec, end_sec, broll_filename, optional_pip_video)
SCENES = [
    # Take 01 (0.00 -> 37.41s) split into 3 scenes:
    (1,   0.00,  12.00, "courtroom.mp4",                  None),
    (2,  12.00,  22.00, "prison_bars.mp4",                None),
    (3,  22.00,  37.41, "dna_lab.mp4",                    None),
    # Take 02 (37.41 -> 55.65s)
    (4,  37.41,  55.65, "broll_eye_macro.mp4",            None),
    # Take 03 (55.65 -> 73.67s) + Leonardo Pointing PiP pattern interrupt
    (5,  55.65,  73.67, "broll_birthday_candles.mp4",     os.path.join(POP_CULTURE, "once_upon_a_time_leo_pointing.mp4")),
    # Take 04 (73.67 -> 94.41s)
    (6,  73.67,  94.41, "broll_lightbulb_filament.mp4",   None),
    # Take 05 (94.41 -> 118.59s)
    (7,  94.41, 118.59, "broll_vintage_camcorder.mp4",    None),
    # Take 06 (118.59 -> 145.42s)
    (8, 118.59, 145.42, "broll_laser_optics.mp4",         None),
    # Take 07 (145.42 -> 180.07s) + Kurt Angle Stare PiP pattern interrupt
    (9, 145.42, 180.07, "broll_shattered_glass.mp4",      os.path.join(MEMES_USA, "kurt_angle_thousand_yard_stare.mp4")),
    # Take 08 (180.07 -> 202.34s)
    (10, 180.07, 202.34, "broll_neurosurgery_mri.mp4",    None),
    # Take 09 (202.34 -> 218.88s)
    (11, 202.34, 218.88, "broll_servers.mp4",             None),
    # Take 10 (218.88 -> 237.66s)
    (12, 218.88, 237.66, "broll_psych_notebook.mp4",      None),
    # Take 11 (237.66 -> 255.38s) + Big Short Bragging PiP pattern interrupt
    (13, 237.66, 255.38, "broll_shopping_mall.mp4",       os.path.join(POP_CULTURE, "the_big_short_bragging.mp4")),
    # Take 12 (255.38 -> 278.72s)
    (14, 255.38, 278.72, "broll_smartphone_scrolling.mp4", None),
    # Take 13 (278.72 -> 294.88s)
    (15, 278.72, 294.88, "brain_synapse.mp4",             None),
    # Take 14 (294.88 -> 301.60s) + Kurt Angle Stare PiP pattern interrupt
    (16, 294.88, 301.60, "broll_protein_molecules.mp4",   os.path.join(MEMES_USA, "kurt_angle_thousand_yard_stare.mp4")),
    # Take 15 (301.60 -> 337.36s)
    (17, 301.60, 337.36, "broll_protein_molecules.mp4",   None),
    # Take 16 (337.36 -> 358.43s) + The Big Short Bragging PiP pattern interrupt
    (18, 337.36, 358.43, "broll_soccer_sunset.mp4",       os.path.join(POP_CULTURE, "the_big_short_bragging.mp4")),
    # Take 17 (358.43 -> 367.70s)
    (19, 358.43, 367.70, "broll_photocopier_scan.mp4",    None),
    # Take 18 (367.70 -> 386.17s)
    (20, 367.70, 386.17, "broll_savanna_lion.mp4",        None),
    # Take 19 (386.17 -> 405.21s)
    (21, 386.17, 405.21, "broll_laser_optics.mp4",        None),
    # Take 20 (405.21 -> 421.04s) + Kurt Angle Stare PiP pattern interrupt
    (22, 405.21, 421.04, "broll_couple_argument.mp4",     os.path.join(MEMES_USA, "kurt_angle_thousand_yard_stare.mp4")),
    # Take 21 (421.04 -> 427.96s)
    (23, 421.04, 427.96, "broll_eye_macro.mp4",           None),
]

def render_scene_segment(scene_tuple):
    scene_id, st, en, broll_name, pip_path = scene_tuple
    dur = round(en - st, 2)
    broll_path = os.path.join(BROLL_DIR, broll_name)
    plate_path = os.path.join(PLATES_DIR, f"element-{scene_id-1:02d}.png")
    out_seg = os.path.join(SEGMENTS_DIR, f"seg_{scene_id:02d}.mp4")
    if os.path.exists(out_seg) and os.path.getsize(out_seg) > 100_000:
        print(f"  ✓ Cached Scene {scene_id:02d} ({st:6.2f}s -> {en:6.2f}s | {broll_name})")
        return out_seg

    if not os.path.exists(broll_path):
        broll_path = os.path.join(BROLL_DIR, "brain_synapse.mp4")

    # Dynamic mid-scene punch-in (every 6 seconds toggles a 1.06x focal punch-in on long scenes)
    punch_expr = (
        ",crop=w='if(gt(mod(t,12),6),1810,1920)':h='if(gt(mod(t,12),6),1018,1080)',scale=1920:1080"
        if dur > 14.0 else ""
    )

    cmd = [
        "ffmpeg", "-y",
        "-stream_loop", "-1", "-t", f"{dur:.2f}", "-i", broll_path,
        "-loop", "1", "-t", f"{dur:.2f}", "-i", plate_path,
    ]

    if pip_path and os.path.exists(pip_path):
        cmd.extend(["-t", "3.0", "-i", pip_path])
        filter_complex = (
            "[0:v]scale=2112:1188:force_original_aspect_ratio=increase,"
            "crop=1920:1080:x='(iw-ow)/2+sin(t*0.4)*55':y='(ih-oh)/2+cos(t*0.3)*30',"
            "fps=30,setsar=1,eq=brightness=-0.10:contrast=1.18:saturation=0.88,boxblur=8:1[bg];"
            f"[1:v]format=yuva420p,fade=t=in:st=0:d=0.4:alpha=1,fade=t=out:st={max(0.5, dur-0.35):.2f}:d=0.35:alpha=1[plate];"
            "[bg][plate]overlay=0:0[v_plated];"
            "[2:v]scale=460:258:force_original_aspect_ratio=decrease,pad=468:266:4:4:color=#E2FF00,fps=30,setsar=1[pip];"
            f"[v_plated][pip]overlay=W-w-64:H-h-205:enable='between(t,0.3,3.1)'{punch_expr}[outv]"
        )
    else:
        filter_complex = (
            "[0:v]scale=2112:1188:force_original_aspect_ratio=increase,"
            "crop=1920:1080:x='(iw-ow)/2+sin(t*0.4)*55':y='(ih-oh)/2+cos(t*0.3)*30',"
            "fps=30,setsar=1,eq=brightness=-0.10:contrast=1.18:saturation=0.88,boxblur=8:1[bg];"
            f"[1:v]format=yuva420p,fade=t=in:st=0:d=0.4:alpha=1,fade=t=out:st={max(0.5, dur-0.35):.2f}:d=0.35:alpha=1[plate];"
            f"[bg][plate]overlay=0:0{punch_expr}[outv]"
        )

    cmd.extend([
        "-filter_complex", filter_complex,
        "-map", "[outv]",
        "-c:v", "h264_nvenc",
        "-preset", "p4",
        "-cq", "19",
        "-pix_fmt", "yuv420p",
        "-r", "30",
        "-t", f"{dur:.2f}",
        out_seg
    ])

    res = subprocess.run(cmd, creationflags=CREATE_NO_WINDOW, capture_output=True, text=True)
    if res.returncode != 0:
        # Fallback to libx264 if nvenc session limit reached
        idx = cmd.index("h264_nvenc")
        cmd[idx] = "libx264"
        cmd[cmd.index("-preset") + 1] = "fast"
        cmd[cmd.index("-cq")] = "-crf"
        res = subprocess.run(cmd, creationflags=CREATE_NO_WINDOW, capture_output=True, text=True)
        if res.returncode != 0:
            raise RuntimeError(f"Failed rendering scene {scene_id}: {res.stderr}")

    print(f"  ✓ Rendered Scene {scene_id:02d} ({st:6.2f}s -> {en:6.2f}s | {broll_name})")
    return out_seg

def main():
    t0 = time.time()
    print("=" * 70)
    print("🚀 COMPILING THINKLATE EPISODE 06 FULL WIDESCREEN MASTER (1920x1080)")
    print("=" * 70)

    # 1. Render all 23 segments in parallel (max 3 workers to respect NVENC concurrent session limit)
    seg_files = []
    with ThreadPoolExecutor(max_workers=3) as pool:
        seg_files = list(pool.map(render_scene_segment, SCENES))

    # 2. Concatenate all 23 segments
    concat_txt = os.path.join(SEGMENTS_DIR, "concat_list.txt")
    with open(concat_txt, "w", encoding="utf-8") as f:
        for sf in seg_files:
            f.write(f"file '{sf.replace(os.sep, '/')}'\n")

    concat_raw = os.path.join(SEGMENTS_DIR, "concat_visual_raw.mp4")
    print("\n[*] Concatenating 23 widescreen scenes...")
    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_txt, "-c", "copy", concat_raw],
        creationflags=CREATE_NO_WINDOW, check=True
    )

    # 3. Burn in Word-Synced ASS Subtitles & Mux with Master Broadcast Audio (full_mix_master.wav)
    print("[*] Burning in word-synced ASS broadcast subtitles & muxing master audio...")
    ass_escaped = ASS_SUBS.replace("\\", "/").replace(":", "\\:")
    final_cmd = [
        "ffmpeg", "-y",
        "-i", concat_raw,
        "-i", AUDIO_MASTER,
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
        FINAL_MASTER_MP4
    ]
    res = subprocess.run(final_cmd, creationflags=CREATE_NO_WINDOW, capture_output=True, text=True)
    if res.returncode != 0:
        print("[-] NVENC final pass fallback to libx264:", res.stderr)
        idx = final_cmd.index("h264_nvenc")
        final_cmd[idx] = "libx264"
        final_cmd[final_cmd.index("-preset") + 1] = "fast"
        final_cmd[final_cmd.index("-cq")] = "-crf"
        subprocess.run(final_cmd, creationflags=CREATE_NO_WINDOW, check=True)

    # Copy to artifact directory for instant user preview
    artifact_dir = r"C:\Users\sar1s\.gemini\antigravity\brain\d8895c41-3403-4f18-9410-6e0368cec188"
    if os.path.exists(artifact_dir):
        shutil.copy2(FINAL_MASTER_MP4, os.path.join(artifact_dir, "ThinkLate_L06_The_Memory_Lie_1080p_MASTER.mp4"))

    elapsed = time.time() - t0
    sz_mb = os.path.getsize(FINAL_MASTER_MP4) / (1024 * 1024)
    print("=" * 70)
    print(f"✅ EPISODE 06 WIDESCREEN MASTER COMPLETE in {elapsed:.1f}s!")
    print(f"   Master File: {FINAL_MASTER_MP4}")
    print(f"   File Size:   {sz_mb:.2f} MB (1920x1080 @ 30fps, H.264/AAC)")
    print("=" * 70)

if __name__ == "__main__":
    main()

