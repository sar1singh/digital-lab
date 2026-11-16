"""
ThinkLate Video 05: Master Video Assembly & Rendering Pipeline
Built strictly on the proven Video 04 Architectural Standard.
- Track 1 (V1): Continuous Living Gameplay Canvas (Assassin's Creed Black Flag: naval action, broadsides, pirating)
- Track 2 (V2): Scoped Blur (gblur=sigma=12, dark vignette) under text cards
- Track 4 (V4): High-DPI Evidence Badges & Kinetic Typography Slams (smooth alpha fade-in/out)
- Master Audio: Andrew 90% voice + BGM 30% + J-Cut SFX (whooshes, sub-bass booms, data blips)
- Zero DSP distortion, zero PPT full-screen slides, zero thumbnail cuts in video.
"""

import os
import sys
import wave
import array
import time
import subprocess
import shutil
from build_timeline_cues_v05 import CUES_DEF, total_dur

NO_WINDOW = subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0

VIDEO_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b"
ASSETS_DIR = os.path.join(VIDEO_DIR, "assets")
BRAND_DIR  = os.path.join(VIDEO_DIR, "brand_assets")
AUDIO_DIR  = os.path.join(VIDEO_DIR, "audio_takes")
SFX_DIR    = os.path.join(ASSETS_DIR, "sfx")
CACHE_DIR  = os.path.join(VIDEO_DIR, "render_cache_v05")
ACTION_DIR = os.path.join(ASSETS_DIR, "action_gameplay_clips")
VAULT_DIR  = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\reusable_vault\gameplay_broll\ac_black_flag"

VOICE_AND_BGM_IN = os.path.join(AUDIO_DIR, "full_mix_preview.wav")
AUDIO_WITH_SFX   = os.path.join(AUDIO_DIR, "master_soundtrack_with_sfx.wav")
CONCAT_LIST_FILE = os.path.join(CACHE_DIR, "concat_segments.txt")
FINAL_OUTPUT_MP4 = os.path.join(VIDEO_DIR, "ThinkLate_Video05_Broadcast_Master.mp4")

def step1_mix_master_audio():
    """
    Combines the approved Andrew 90% + BGM 30% master mix with J-cut SFX cues.
    All SFX are rendered at 48kHz stereo with precise -100ms J-cut positioning.
    """
    print("\n=======================================================")
    print(" STEP 1: Building Synchronized Master Audio with SFX")
    print(f" Master Audio Duration: {total_dur:.2f}s (~{int(total_dur//60)}m {int(total_dur%60)}s)")
    print("=======================================================")
    t0 = time.time()
    os.makedirs(CACHE_DIR, exist_ok=True)

    # Convert voice+BGM to standard 16-bit PCM WAV to avoid WAVE_FORMAT_EXTENSIBLE issue
    temp_pcm16 = os.path.join(CACHE_DIR, "temp_voice_bgm_16bit.wav")
    subprocess.run(
        ["ffmpeg", "-y", "-i", VOICE_AND_BGM_IN, "-c:a", "pcm_s16le", "-ar", "48000", "-ac", "2", temp_pcm16],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, creationflags=NO_WINDOW
    )

    with wave.open(temp_pcm16, 'rb') as wf:
        params = wf.getparams()
        framerate = params.framerate
        n_frames = params.nframes
        master_samples = array.array('h', wf.readframes(n_frames))

    print(f"Loaded master voice+BGM: {n_frames} frames ({n_frames/framerate:.2f}s) @ {framerate}Hz")

    # Cache SFX
    sfx_cache = {}
    for fname in ["sfx_sub_boom.wav", "sfx_whoosh.wav", "sfx_data_blip.wav"]:
        p = os.path.join(SFX_DIR, fname)
        if os.path.exists(p):
            sfx_temp = os.path.join(CACHE_DIR, f"temp_{fname}")
            subprocess.run(
                ["ffmpeg", "-y", "-i", p, "-ar", str(framerate), "-ac", "2", sfx_temp],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, creationflags=NO_WINDOW
            )
            with wave.open(sfx_temp, 'rb') as swf:
                sfx_cache[fname] = array.array('h', swf.readframes(swf.getnframes()))

    # Apply SFX cues
    sfx_applied_count = 0
    for cue in CUES_DEF:
        cue_id, st, et, v1_broll, v2_blur, v4_card, sfx_cue = cue
        if not sfx_cue:
            continue
        sfx_file, sfx_timestamp, sfx_scale = sfx_cue
        sfx_data = sfx_cache.get(sfx_file)
        if not sfx_data:
            continue

        # J-Cut: start SFX 100ms before timestamp
        actual_start_sec = max(0.0, sfx_timestamp - 0.10)
        start_idx = int(actual_start_sec * framerate) * 2

        for k in range(len(sfx_data)):
            target_idx = start_idx + k
            if target_idx >= len(master_samples):
                break
            v = master_samples[target_idx] + int(sfx_data[k] * sfx_scale)
            if v > 32767: v = 32767
            elif v < -32768: v = -32768
            master_samples[target_idx] = v
        sfx_applied_count += 1

    with wave.open(AUDIO_WITH_SFX, 'wb') as out_wf:
        out_wf.setparams(params)
        out_wf.writeframes(master_samples.tobytes())

    print(f"Master Soundtrack with {sfx_applied_count} SFX Hits Mixed: {AUDIO_WITH_SFX} ({time.time()-t0:.2f}s)")

def step2_render_scenes(limit_cues=None):
    """
    Renders video segments synchronized to Whisper ground truth.
    - V1: Action Gameplay (1080p, 30fps)
    - V2: Scoped Blur (gblur=sigma=12, dark vignette) under text cards
    - V4: Kinetic typography slams & UI evidence cards with smooth alpha fades
    """
    print("\n=======================================================")
    print(f" STEP 2: Rendering Video Segments (Total Cues: {len(CUES_DEF) if not limit_cues else limit_cues})")
    print("=======================================================")
    os.makedirs(CACHE_DIR, exist_ok=True)
    cues_to_render = CUES_DEF[:limit_cues] if limit_cues else CUES_DEF
    segment_files = []

    for cue in cues_to_render:
        cue_id, st, et, v1_broll, v2_blur, v4_card, sfx_cue = cue
        dur = et - st
        seg_filename = f"seg_{cue_id:02d}.mp4"
        seg_path = os.path.join(CACHE_DIR, seg_filename)
        segment_files.append(seg_path)

        if os.path.exists(seg_path) and os.path.getsize(seg_path) > 100000:
            print(f"--> Cue {cue_id:02d} [{st:6.2f} - {et:6.2f}] already rendered ({os.path.getsize(seg_path):,} bytes), skipping...")
            continue

        # Locate broll clip
        broll_clip = os.path.join(ACTION_DIR, v1_broll)
        if not os.path.exists(broll_clip):
            broll_clip = os.path.join(VAULT_DIR, v1_broll)
        if not os.path.exists(broll_clip):
            broll_clip = os.path.join(ACTION_DIR, "action_01_sea_sailing.mp4")

        cmd = ["ffmpeg", "-y", "-stream_loop", "-1", "-i", broll_clip]

        if v2_blur and v4_card:
            # Scoped blur + 12% dark tint to make typography slam pop
            base_filter = (
                f"[0:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30,"
                f"gblur=sigma=12,colorlevels=rimax=0.88:gimax=0.88:bimax=0.88[base]"
            )
            card_path = os.path.join(BRAND_DIR, v4_card)
            cmd.extend(["-loop", "1", "-i", card_path])
            ov_filter = (
                f"[1:v]format=rgba,fade=t=in:st=0.3:d=0.35:alpha=1,fade=t=out:st={max(0.4, dur-0.4):.2f}:d=0.35:alpha=1[ov]"
            )
            composite_filter = f"[base][ov]overlay=0:0:enable='between(t,0.3,{max(0.35, dur-0.05):.2f})'[outv]"
            full_filter = f"{base_filter}; {ov_filter}; {composite_filter}"
        else:
            # Full crisp action gameplay
            full_filter = f"[0:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30[outv]"

        cmd.extend([
            "-filter_complex", full_filter,
            "-map", "[outv]",
            "-t", f"{dur:.3f}",
            "-c:v", "h264_nvenc",
            "-preset", "p4",
            "-b:v", "6M",
            "-pix_fmt", "yuv420p",
            seg_path
        ])

        t_seg = time.time()
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=NO_WINDOW)
        if res.returncode != 0:
            print(f"NVENC failed for Cue {cue_id:02d}, falling back to libx264...")
            # Fallback to libx264
            cmd[-6] = "libx264"
            cmd[-4] = "veryfast"
            subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, creationflags=NO_WINDOW)

        print(f"Rendered Cue {cue_id:02d} [{st:6.2f} - {et:6.2f} | {dur:5.2f}s] in {time.time()-t_seg:.2f}s -> {seg_filename}", flush=True)

    return segment_files

def step3_concat_and_mux(output_file, limit_cues=None):
    """
    Concatenates rendered video segments and muxes with the master soundtrack.
    """
    print("\n=======================================================")
    print(" STEP 3: Concat Video Segments and Mux Master Soundtrack")
    print("=======================================================")
    t0 = time.time()
    cues_to_concat = CUES_DEF[:limit_cues] if limit_cues else CUES_DEF

    with open(CONCAT_LIST_FILE, "w", encoding="utf-8") as f:
        for cue in cues_to_concat:
            seg_filename = f"seg_{cue[0]:02d}.mp4"
            f.write(f"file '{seg_filename}'\n")

    # Cut audio to match duration if limited
    audio_source = AUDIO_WITH_SFX
    if limit_cues:
        sub_dur = cues_to_concat[-1][2]
        temp_sub_audio = os.path.join(CACHE_DIR, f"audio_preview_{sub_dur:.0f}s.wav")
        cmd_cut_aud = ["ffmpeg", "-y", "-i", AUDIO_WITH_SFX, "-t", f"{sub_dur:.3f}", "-c", "copy", temp_sub_audio]
        subprocess.run(cmd_cut_aud, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, creationflags=NO_WINDOW)
        audio_source = temp_sub_audio

    cmd_mux = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0", "-i", CONCAT_LIST_FILE,
        "-i", audio_source,
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "320k",
        "-shortest",
        output_file
    ]
    subprocess.run(cmd_mux, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, creationflags=NO_WINDOW)
    print(f"Master Broadcast Video Assembled: {output_file} ({os.path.getsize(output_file):,} bytes) in {time.time()-t0:.2f}s")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--preview-opening", action="store_true", help="Render only first 12 cues (opening ~2.5 mins)")
    args = parser.parse_args()

    step1_mix_master_audio()

    if args.preview_opening:
        print("\n--- RENDERING OPENING PREVIEW (FIRST 12 CUES: 0:00 - 2:20) ---")
        step2_render_scenes(limit_cues=12)
        preview_out = os.path.join(VIDEO_DIR, "test_opening_2min_preview.mp4")
        step3_concat_and_mux(preview_out, limit_cues=12)
        print(f"\nOpening Preview Ready: {preview_out}")
    else:
        step2_render_scenes()
        step3_concat_and_mux(FINAL_OUTPUT_MP4)
        print(f"\nFull Master Video Ready: {FINAL_OUTPUT_MP4}")
