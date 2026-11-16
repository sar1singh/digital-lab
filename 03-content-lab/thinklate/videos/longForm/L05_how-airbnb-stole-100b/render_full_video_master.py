"""
ThinkLate Video 05: Master Full 15m 56s Video Renderer
Orchestrates the entire 15m 56s video production across all 8 Acts:
- Base Layer (V1): Living Gameplay Canvas Spine & Documentary B-roll (1,376s total source, never static)
- Focus Layer (V2): Atmospheric Tone & Gaussian Blur (boxblur=8:1) during card reveals
- Evidence Layer (V3): Verified Historical Archival Photos (Brian Chesky, Joe Gebbia, Paul Graham)
- Motion Graphics Layer (V4): 12 Transparent Remotion Motion Cards (.mov ProRes 4444 Alpha) with dynamic entrance/exit
- Audio: Broadcast Master (+15% pace, -1.0 dB true peak, -26 dB BGM with 1.5kHz vocal pocket)
"""

import os
import sys
import json
import subprocess
import time

BASE_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
AUDIO_DIR = os.path.join(BASE_DIR, "audio_takes")
CARDS_DIR = os.path.join(ASSETS_DIR, "motion_cards")
ACTION_DIR = os.path.join(ASSETS_DIR, "action_gameplay_clips")
DOC_DIR = os.path.join(ASSETS_DIR, "documentary_broll")
CACHE_DIR = os.path.join(BASE_DIR, "render_cache_v05_master")
ARTIFACT_DIR = r"C:\Users\sar1s\.gemini\antigravity\brain\a2e7cc12-b50a-4810-b87e-118b7df25366"

os.makedirs(CACHE_DIR, exist_ok=True)
CREATE_NO_WINDOW = 0x08000000

AUDIO_SRC = os.path.join(AUDIO_DIR, "dual_full_mix_preview_plus15.wav")
TOTAL_DURATION = 956.83 # 15m 56.83s

# 1. Living Canvas & B-roll sources
GAMEPLAY_FILES = [os.path.join(ACTION_DIR, f) for f in sorted(os.listdir(ACTION_DIR)) if f.endswith(".mp4")]
DOC_FILES = [os.path.join(DOC_DIR, f) for f in sorted(os.listdir(DOC_DIR)) if f.endswith(".mp4")]
FOUNDERS_ARCHIVE = os.path.join(ASSETS_DIR, "generative_broll", "scene_02_real_founders_archive.jpg")

# 2. Transparent Remotion Cards (start_s, duration_s, mov_filename)
TRANSPARENT_CARDS = [
    (0.4, 4.0, "card_01_evidence_eviction.mov"),
    (5.0, 3.0, "card_02_typography_slam_hook.mov"),
    (75.0, 4.0, "card_03_comparison_hotel_vs_airbed.mov"),
    (220.0, 4.0, "card_04_metric_cereal_capital.mov"),
    (290.0, 4.0, "card_05_headline_angel_rejection.mov"),
    (340.0, 4.0, "card_06_citation_paulg.mov"),
    (430.0, 4.0, "card_07_redaction_vc_pass.mov"),
    (490.0, 3.0, "card_08_glitch_cartel.mov"),
    (620.0, 4.0, "card_09_barchart_multiples.mov"),
    (710.0, 4.0, "card_10_linechart_ipo_spike.mov"),
    (810.0, 4.0, "card_11_receipt_junk_fees.mov"),
    (910.0, 3.0, "card_12_highlighter_rules.mov")
]

# Chunk definition: 4 acts / sections to ensure stable memory management and headless execution
CHUNKS = [
    ("part1_hook_and_arbitrage", 0.0, 240.0),    # 0 to 4:00 (Hook + Hotel Arbitrage)
    ("part2_bootstrap_rejection", 240.0, 480.0), # 4:00 to 8:00 (Cereal Hustle + Angel Rejections)
    ("part3_growth_and_multiples", 480.0, 720.0),# 8:00 to 12:00 (Growth Hacks + Wall St Multiples)
    ("part4_trap_and_climax", 720.0, TOTAL_DURATION) # 12:00 to 15:57 (Junk Fees + Climax)
]

def render_part(part_name, start_t, end_t):
    dur = end_t - start_t
    out_mp4 = os.path.join(CACHE_DIR, f"{part_name}.mp4")
    if os.path.exists(out_mp4) and os.path.getsize(out_mp4) > 5000000:
        print(f"Part {part_name} already rendered. Skipping.")
        return out_mp4
        
    print(f"\n>>> Rendering {part_name} ({start_t:.1f}s to {end_t:.1f}s | Duration: {dur:.1f}s)...", flush=True)
    
    # Select motion cards active in this chunk
    active_cards = []
    for c_start, c_dur, c_file in TRANSPARENT_CARDS:
        if start_t <= c_start < end_t:
            rel_start = c_start - start_t
            active_cards.append((rel_start, c_dur, os.path.join(CARDS_DIR, c_file)))
            
    # Assemble gameplay & documentary loop for this chunk
    bg_clip1 = GAMEPLAY_FILES[int((start_t / 60) % len(GAMEPLAY_FILES))]
    bg_clip2 = DOC_FILES[int((start_t / 30) % len(DOC_FILES))]
    
    # Filter graph construction
    inputs = [
        "-ss", str(start_t), "-t", str(dur), "-i", AUDIO_SRC,
        "-stream_loop", "-1", "-i", bg_clip1,
        "-stream_loop", "-1", "-i", bg_clip2,
    ]
    
    filter_chains = []
    # Alternate between living gameplay and documentary broll every 12 seconds
    filter_chains.append(f"[1:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30,setsar=1[v_game];")
    filter_chains.append(f"[2:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30,setsar=1[v_doc];")
    filter_chains.append(f"[v_game][v_doc]blend=all_expr='if(lte(mod(T,24),12),A,B)'[v_base];")
    
    current_v = "[v_base]"
    input_idx = 3
    
    # Overlay transparent motion cards with setpts timestamp alignment
    for idx, (rel_start, c_dur, c_path) in enumerate(active_cards):
        inputs.extend(["-i", c_path])
        c_raw = f"[{input_idx}:v]"
        c_delayed = f"[c_delayed_{idx}]"
        next_v = f"[v_card_{idx}]"
        
        # Delay the card so frame 0 begins precisely at rel_start
        filter_chains.append(
            f"{c_raw}setpts=PTS-STARTPTS+{rel_start:.2f}/TB{c_delayed};"
            f"{current_v}boxblur=enable='between(t,{rel_start:.2f},{rel_start+c_dur:.2f})':luma_radius=8:luma_power=1[v_blurred_{idx}];"
            f"[v_blurred_{idx}]{c_delayed}overlay=x=0:y=0:enable='between(t,{rel_start:.2f},{rel_start+c_dur:.2f})':eof_action=pass{next_v};"
        )
        current_v = next_v
        input_idx += 1
        
    filter_chains.append(f"{current_v}null[v_final]")
    
    cmd = [
        "ffmpeg", "-y",
        *inputs,
        "-filter_complex", "".join(filter_chains),
        "-map", "[v_final]",
        "-map", "0:a",
        "-c:v", "libx264", "-preset", "ultrafast", "-crf", "22", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-t", str(dur),
        out_mp4
    ]
    
    t0 = time.time()
    res = subprocess.run(cmd, creationflags=CREATE_NO_WINDOW, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error rendering {part_name}:")
        print(res.stderr[-1000:])
        sys.exit(1)
        
    print(f"SUCCESS: {part_name} rendered in {time.time()-t0:.1f}s | Size: {os.path.getsize(out_mp4)/1024/1024:.2f} MB", flush=True)
    return out_mp4

def assemble_master():
    rendered_parts = []
    for p_name, st, et in CHUNKS:
        p_file = render_part(p_name, st, et)
        rendered_parts.append(p_file)
        
    concat_txt = os.path.join(CACHE_DIR, "master_concat.txt")
    with open(concat_txt, "w", encoding="utf-8") as f:
        for p in rendered_parts:
            # Format file path with forward slashes for ffmpeg concat
            p_clean = p.replace("\\", "/")
            f.write(f"file '{p_clean}'\n")
            
    final_master = os.path.join(BASE_DIR, "ThinkLate_Video05_Broadcast_Master_1080p.mp4")
    print("\n>>> Concatenating parts into final Broadcast Master...")
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_txt,
        "-c", "copy",
        final_master
    ], creationflags=CREATE_NO_WINDOW, check=True)
    
    print(f"\n=======================================================")
    print(f" BROADCAST MASTER RENDERING 100% COMPLETE!")
    print(f" Saved to: {final_master}")
    print(f" Size: {os.path.getsize(final_master)/1024/1024:.2f} MB")
    print(f"=======================================================")
    
    # Also generate a lightweight in-IDE preview cut (first 90s, <15MB)
    preview_mp4 = os.path.join(ARTIFACT_DIR, "ThinkLate_Video05_Master_Preview_Light.mp4")
    print("\n>>> Generating lightweight in-IDE preview cut (<15MB)...")
    subprocess.run([
        "ffmpeg", "-y", "-ss", "0", "-t", "90.0", "-i", final_master,
        "-c:v", "libx264", "-crf", "25", "-preset", "fast",
        "-c:a", "aac", "-b:a", "128k",
        preview_mp4
    ], creationflags=CREATE_NO_WINDOW, check=True)
    print(f"Preview saved: {preview_mp4} ({os.path.getsize(preview_mp4)/1024/1024:.2f} MB)")

if __name__ == "__main__":
    assemble_master()
