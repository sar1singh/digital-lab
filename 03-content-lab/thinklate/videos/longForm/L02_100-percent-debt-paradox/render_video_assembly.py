"""
ThinkLate Video 2: Master Automated Video Assembly & Rendering Pipeline
SYNCHRONIZED STRICTLY TO REAL SPOKEN AUDIO TIMESTAMPS (faster-whisper extraction)
Compiles all 24 semantic scenes, Ken Burns camera glide, High-DPI Evidence Cards,
Kinetic Typography Plates, Broadcast Lower Thirds, and Synchronized SFX
into the final 10:50.31 broadcast video.
"""

import os
import sys
import wave
import array
import time
import subprocess
import shutil

VIDEO_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\100_percent_debt_paradox"
ASSETS_DIR = os.path.join(VIDEO_DIR, "assets")
AUDIO_DIR  = os.path.join(VIDEO_DIR, "audio_takes")
SFX_DIR    = os.path.join(ASSETS_DIR, "sfx")
CACHE_DIR  = os.path.join(VIDEO_DIR, "render_cache")

MASTER_AUDIO_IN  = os.path.join(AUDIO_DIR, "full_mix_ambiment_drone.wav")
AUDIO_WITH_SFX   = os.path.join(AUDIO_DIR, "full_mix_with_sfx.wav")
CONCAT_LIST_FILE = os.path.join(CACHE_DIR, "concat_segments.txt")
FINAL_OUTPUT_MP4 = os.path.join(VIDEO_DIR, "ThinkLate_Video02_The_100_Percent_Debt_Paradox.mp4")

# 24 Real Audio-Synchronized Scene Definitions:
# (Scene_ID, Base_Image, Duration_Sec, Overlays_List, Fade_In, Fade_Out)
# Overlay item format: (relative_asset_path, local_start_sec, local_end_sec)
SCENES = [
    # --- ACT 1: The Macro Hook (00:00 - 01:29.68 | 89.68s) ---
    (1,  "scene01_city_debt_ticker.jpg",   12.80, [], True, False),
    (2,  "scene02_medieval_castle.jpg",     21.84, [("card_act1_realestate_paradox.png", 1.20, 19.50)], False, False),
    (3,  "scene03_bank_loan.png",           21.52, [], False, False),
    (4,  "scene05_debt_mountain.png",       15.88, [("kt_act1_what_if_nation.png", 0.50, 14.50)], False, False),
    (5,  "scene04_podcast_studio.png",      17.64, [("kt_act1_debt_con.png", 1.40, 16.00)], False, False),

    # --- ACT 2: The Stakes & The Data (01:29.68 - 02:51.08 | 81.40s) ---
    (6,  "scene05_debt_mountain.png",       35.48, [("card_act2_debt_benchmarks.png", 1.30, 28.00), ("lt_us_treasury.png", 13.30, 25.30)], False, False),
    (7,  "scene06_villain_dilution.png",    13.16, [("kt_act2_villain_dilution.png", 0.35, 11.80)], False, False),
    (8,  "scene07_two_apples_inflation.jpg", 21.92, [], False, False),
    (9,  "scene06_villain_dilution.png",    10.84, [("kt_act2_who_touches_first.png", 0.75, 9.80)], False, False),

    # --- ACT 3: The Historical Pattern (02:51.08 - 06:42.44 | 231.36s) ---
    (10, "scene08_roman_legion.png",        40.92, [("card_act3_denarius_purity.png", 23.90, 39.50)], False, False),
    (11, "scene09_coin_foundry.png",        32.00, [("lt_roman_debasement.png", 10.00, 26.00)], False, False),
    (12, "scene09_coin_foundry.png",        37.36, [("kt_act3_same_coins_half_meal.png", 20.00, 35.50)], False, False),
    (13, "scene10_paris_1720.png",          52.80, [], False, False),
    (14, "scene11_cantillon_study.png",     39.84, [("kt_act3_cantillon_effect.png", 0.80, 20.00), ("lt_cantillon_essay.png", 20.80, 37.80)], False, False),
    (15, "scene12_historical_con.png",      28.44, [("kt_act3_same_con.png", 12.00, 27.00)], False, False),

    # --- ACT 4: The Modern Machinery (06:42.44 - 09:29.48 | 167.04s) ---
    (16, "scene13_digital_mint.png",        40.56, [("kt_act4_trillions_created.png", 15.50, 37.50)], False, False),
    (17, "scene16_capital_flow.png",        32.60, [("lt_iif_global.png", 12.00, 29.00)], False, False),
    (18, "scene14_private_equity.png",      32.40, [("card_act4_institutional_housing.png", 0.40, 19.50), ("kt_act4_money_flows_up.png", 20.40, 31.40)], False, False),
    (19, "scene15_startup_pipeline.png",    47.00, [("kt_act4_startup_dies.png", 28.00, 45.50)], False, False),
    (20, "scene12_historical_con.png",      14.48, [], False, False),

    # --- ACT 5: The Individual Resolution (09:29.48 - 10:50.31 | 80.83s) ---
    (21, "scene17_generational_contrast.png", 40.52, [("card_act5_median_home_vs_income.png", 4.50, 38.50)], False, False),
    (22, "scene18_melting_vault.png",         20.68, [], False, False),
    (23, "scene11_cantillon_study.png",       11.76, [("kt_act5_own_tangible_assets.png", 0.30, 10.30)], False, False),
    (24, "scene19_build_boat.png",             7.87, [("kt_act5_build_a_boat.png", 0.50, 6.00)], False, True),
]

# Exact Spoken-Audio Synchronized SFX Cue Events: (timestamp_sec, sfx_filename, volume_scale)
SFX_CUES = [
    # Act 1
    (0.0,    "sfx_sub_boom.wav",  0.55),   # 00:00 Opening Hook
    (12.8,   "sfx_whoosh.wav",    0.40),   # 00:12 Castle cut
    (14.0,   "sfx_data_blip.wav", 0.35),   # 00:14 Real estate card reveal
    (34.6,   "sfx_whoosh.wav",    0.40),   # 00:34 Bank loan cut
    (47.0,   "sfx_sub_boom.wav",  0.50),   # 00:47 "Done. Finis."
    (56.5,   "sfx_sub_boom.wav",  0.55),   # 00:56 What if a nation does it
    (72.0,   "sfx_whoosh.wav",    0.40),   # 01:12 Host intro cut
    (73.5,   "sfx_data_blip.wav", 0.35),   # 01:13 Debt con title

    # Act 2
    (89.7,   "sfx_sub_boom.wav",  0.55),   # 01:29 Act 2 start / Debt data
    (91.0,   "sfx_data_blip.wav", 0.35),   # 01:31 Debt benchmarks card reveal
    (103.0,  "sfx_data_blip.wav", 0.35),   # 01:43 US Treasury citation reveal
    (125.2,  "sfx_whoosh.wav",    0.40),   # 02:05 Villain is dilution cut
    (126.0,  "sfx_sub_boom.wav",  0.50),   # 02:06 Dilution text punch
    (138.3,  "sfx_whoosh.wav",    0.40),   # 02:18 Two apples cut
    (160.2,  "sfx_sub_boom.wav",  0.50),   # 02:40 Who touches money first punch

    # Act 3
    (171.1,  "sfx_sub_boom.wav",  0.55),   # 02:51 Act 3 start / Roman empire
    (195.0,  "sfx_data_blip.wav", 0.35),   # 03:15 Denarius purity card reveal
    (212.0,  "sfx_whoosh.wav",    0.40),   # 03:32 Coin foundry cut
    (222.0,  "sfx_data_blip.wav", 0.35),   # 03:42 Roman debasement lower third
    (264.0,  "sfx_sub_boom.wav",  0.50),   # 04:24 Same coins half meal punch
    (281.4,  "sfx_whoosh.wav",    0.40),   # 04:41 Paris 1720 cut
    (334.2,  "sfx_whoosh.wav",    0.40),   # 05:34 Cantillon cut
    (335.0,  "sfx_sub_boom.wav",  0.50),   # 05:35 Cantillon effect title
    (355.0,  "sfx_data_blip.wav", 0.35),   # 05:55 Cantillon essay lower third
    (374.0,  "sfx_whoosh.wav",    0.40),   # 06:14 Bubble popped cut
    (386.0,  "sfx_sub_boom.wav",  0.50),   # 06:26 Same con different millennium

    # Act 4
    (402.4,  "sfx_whoosh.wav",    0.40),   # 06:42 Digital mint cut
    (418.0,  "sfx_sub_boom.wav",  0.55),   # 06:58 Trillions created text punch
    (443.0,  "sfx_whoosh.wav",    0.40),   # 07:23 Capital flow cut
    (455.0,  "sfx_data_blip.wav", 0.35),   # 07:35 IIF lower third reveal
    (475.6,  "sfx_whoosh.wav",    0.40),   # 07:55 Private equity housing cut
    (476.0,  "sfx_data_blip.wav", 0.35),   # 07:56 Institutional card reveal
    (496.0,  "sfx_sub_boom.wav",  0.50),   # 08:16 Money flows up text punch
    (508.0,  "sfx_whoosh.wav",    0.40),   # 08:28 Speculative tech cut
    (536.0,  "sfx_sub_boom.wav",  0.50),   # 08:56 Startup dies plant wins
    (555.0,  "sfx_sub_boom.wav",  0.50),   # 09:15 Pipeline identical punch

    # Act 5
    (569.5,  "sfx_sub_boom.wav",  0.55),   # 09:29 Act 5 start / 1970s contrast
    (574.0,  "sfx_data_blip.wav", 0.35),   # 09:34 Median home vs income card
    (610.0,  "sfx_whoosh.wav",    0.40),   # 10:10 Melting vault cut
    (630.7,  "sfx_sub_boom.wav",  0.50),   # 10:30 Own tangible assets punch
    (642.4,  "sfx_sub_boom.wav",  0.55),   # 10:42 Build a boat climax punch
]

def step1_mix_sfx_audio():
    """Load master audio and layer SFX cues at exact timecodes using Python arrays."""
    print("\n--- STEP 1: Building Synchronized Audio + SFX Stem ---")
    t0 = time.time()

    with wave.open(MASTER_AUDIO_IN, 'rb') as wf:
        params = wf.getparams()
        framerate = params.framerate
        n_frames = params.nframes
        audio_samples = array.array('h', wf.readframes(n_frames))

    print(f"Loaded master track: {n_frames} frames ({n_frames/framerate:.2f}s) @ {framerate}Hz mono")

    # Cache SFX audio buffers
    sfx_buffers = {}
    for filename in ["sfx_sub_boom.wav", "sfx_whoosh.wav", "sfx_data_blip.wav"]:
        sfx_path = os.path.join(SFX_DIR, filename)
        with wave.open(sfx_path, 'rb') as swf:
            sfx_buffers[filename] = array.array('h', swf.readframes(swf.getnframes()))

    # Mix SFX onto master array
    for timestamp, sfx_file, scale in SFX_CUES:
        start_idx = int(timestamp * framerate)
        sfx_data = sfx_buffers.get(sfx_file)
        if not sfx_data:
            continue
        for i in range(len(sfx_data)):
            target_idx = start_idx + i
            if target_idx >= len(audio_samples):
                break
            val = audio_samples[target_idx] + int(sfx_data[i] * scale)
            if val > 32767:
                val = 32767
            elif val < -32768:
                val = -32768
            audio_samples[target_idx] = val

    with wave.open(AUDIO_WITH_SFX, 'wb') as out_wf:
        out_wf.setparams(params)
        out_wf.writeframes(audio_samples.tobytes())

    print(f"Successfully generated: {AUDIO_WITH_SFX} (mixed in {time.time()-t0:.2f}s)")

def step2_render_scenes():
    """Render each of the 24 scene segments with Ken Burns motion, overlays, and NVENC."""
    print("\n--- STEP 2: Rendering 24 Audio-Synchronized Video Segments via NVENC ---")
    os.makedirs(CACHE_DIR, exist_ok=True)
    segment_files = []

    for item in SCENES:
        scene_id, base_img_name, duration, overlays, is_fade_in, is_fade_out = item
        seg_filename = f"seg_{scene_id:02d}.mp4"
        seg_path = os.path.join(CACHE_DIR, seg_filename)
        segment_files.append(seg_path)

        base_img_path = os.path.join(ASSETS_DIR, base_img_name)
        frames = int(duration * 30)
        zoom_rate = 0.07 / max(frames, 30)

        cmd = ["ffmpeg", "-y", "-loop", "1", "-i", base_img_path]

        for ov_item in overlays:
            ov_file = os.path.join(ASSETS_DIR, ov_item[0])
            cmd.extend(["-loop", "1", "-i", ov_file])

        filter_parts = []
        fade_extra = ""
        if is_fade_in:
            fade_extra += ",fade=t=in:st=0:d=1.0"
        if is_fade_out:
            fade_extra += f",fade=t=out:st={duration - 1.5:.2f}:d=1.5"

        bg_filter = (
            f"[0:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,"
            f"zoompan=z='min(zoom+{zoom_rate:.6f},1.07)':d={frames}:"
            f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=30"
            f"{fade_extra}[bg]"
        )
        filter_parts.append(bg_filter)

        curr_input_tag = "[bg]"
        for idx, ov_item in enumerate(overlays):
            ov_name, st, et = ov_item
            in_tag = f"[{idx + 1}:v]"
            ov_filter_tag = f"[ov{idx + 1}]"
            next_tag = f"[v{idx + 1}]" if idx < len(overlays) - 1 else "[outv]"

            filter_parts.append(
                f"{in_tag}format=rgba,fade=t=in:st={st:.2f}:d=0.5:alpha=1,fade=t=out:st={et:.2f}:d=0.5:alpha=1{ov_filter_tag}"
            )
            filter_parts.append(
                f"{curr_input_tag}{ov_filter_tag}overlay=0:0:enable='between(t,{st:.2f},{et + 0.5:.2f})'{next_tag}"
            )
            curr_input_tag = next_tag

        if not overlays:
            filter_parts.append(f"[bg]null[outv]")

        full_filter = "; ".join(filter_parts)
        cmd.extend([
            "-filter_complex", full_filter,
            "-map", "[outv]",
            "-t", f"{duration:.3f}",
            "-c:v", "h264_nvenc",
            "-preset", "p4",
            "-b:v", "5M",
            "-pix_fmt", "yuv420p",
            seg_path
        ])

        print(f"Rendering Scene {scene_id:02d} ({duration:.2f}s, {len(overlays)} overlays)...")
        t_start = time.time()
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if res.returncode != 0:
            print(f"ERROR rendering Scene {scene_id:02d}!")
            print(res.stderr[-800:])
            sys.exit(1)
        print(f"--> Scene {scene_id:02d} rendered in {time.time()-t_start:.2f}s")

    with open(CONCAT_LIST_FILE, "w", encoding="utf-8") as f:
        for p in segment_files:
            clean_path = p.replace("\\", "/")
            f.write(f"file '{clean_path}'\n")

    print(f"Concat list prepared: {CONCAT_LIST_FILE}")

def step3_concatenate_and_mux():
    """Concatenate all 24 segments and multiplex with final audio stem into MP4."""
    print("\n--- STEP 3: Concatenating 24 Segments & Muxing Master Audio ---")
    t0 = time.time()
    temp_concat_video = os.path.join(CACHE_DIR, "video_track_full.mp4")

    concat_cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", CONCAT_LIST_FILE,
        "-c", "copy",
        temp_concat_video
    ]
    print("Concatenating video tracks...")
    res = subprocess.run(concat_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print("ERROR during video concatenation!")
        print(res.stderr[-800:])
        sys.exit(1)

    mux_cmd = [
        "ffmpeg", "-y",
        "-i", temp_concat_video,
        "-i", AUDIO_WITH_SFX,
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "320k",
        "-shortest",
        FINAL_OUTPUT_MP4
    ]
    print("Multiplexing master audio stem...")
    res_mux = subprocess.run(mux_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res_mux.returncode != 0:
        print("ERROR during multiplexing!")
        print(res_mux.stderr[-800:])
        sys.exit(1)

    print(f"Final MP4 Video Rendered: {FINAL_OUTPUT_MP4}")
    print(f"Total mux time: {time.time()-t0:.2f}s")

def step4_verify_output():
    """Verify stream health, duration, and file size using ffprobe."""
    print("\n--- STEP 4: Quality Control & File Verification ---")
    if not os.path.exists(FINAL_OUTPUT_MP4):
        print("FAILED: Output file does not exist!")
        sys.exit(1)

    file_size_mb = os.path.getsize(FINAL_OUTPUT_MP4) / (1024 * 1024)
    probe_cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration,bit_rate:stream=codec_name,width,height,r_frame_rate",
        "-of", "default=noprint_wrappers=1",
        FINAL_OUTPUT_MP4
    ]
    res = subprocess.run(probe_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(f"File Size: {file_size_mb:.2f} MB")
    print("FFprobe Stream Analysis:")
    print(res.stdout)

if __name__ == '__main__':
    t_global = time.time()
    print("=========================================================")
    print(" THINKLATE VIDEO 2: REAL-AUDIO SYNCHRONIZED COMPILATION  ")
    print("=========================================================")
    # Clean cache so all 24 segments re-render with new exact timecodes
    if os.path.exists(CACHE_DIR):
        for f in os.listdir(CACHE_DIR):
            if f.endswith(".mp4") or f.endswith(".txt"):
                try:
                    os.remove(os.path.join(CACHE_DIR, f))
                except Exception:
                    pass
    step1_mix_sfx_audio()
    step2_render_scenes()
    step3_concatenate_and_mux()
    step4_verify_output()
    print(f"\n[DONE] Full 10:50 audio-synchronized video completed in {time.time()-t_global:.2f}s!")
