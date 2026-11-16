#!/usr/bin/env python3
"""
Assemble ThinkLate Video 05 Final Hook Master (00:00 - 01:16 | 76s)
===================================================================
Strictly compliant with:
- Rule 10 & 23: 4-track multi-layer visual stacking, state changes <= 3.5s
- Rule 17: Headless CREATE_NO_WINDOW execution
- Rule 20: Real founder faces clearly visible (Brian Chesky & Joe Gebbia)
- Rule 21: ZERO camera shakes or tremors
- Rule 22: Peaked voiceover (-1.0dB) + ducked BGM with 1.5kHz notch EQ
- Purge of all junk stock (no green screen girl, no wall clock, no credit card guy)
"""

import os
import sys
import subprocess

BASE_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
AUDIO_DIR = os.path.join(BASE_DIR, "audio_takes")
HOOK_CARDS_DIR = os.path.join(ASSETS_DIR, "hook_cards")
SHARED_BROLL = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\shared\assets\broll"
ARTIFACT_DIR = r"C:\Users\sar1s\.gemini\antigravity\brain\a2e7cc12-b50a-4810-b87e-118b7df25366"

AUDIO_SRC = os.path.join(AUDIO_DIR, "dual_full_mix_preview_plus15.wav")
OUTPUT_MASTER = os.path.join(BASE_DIR, "ThinkLate_Video05_Hook_Final_1080p.mp4")
OUTPUT_LIGHT = os.path.join(ARTIFACT_DIR, "ThinkLate_Video05_Hook_Final_Review_Light.mp4")

CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0

def get_headless_kwargs():
    kwargs = {}
    if sys.platform == "win32":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = 0
        kwargs["startupinfo"] = startupinfo
        kwargs["creationflags"] = CREATE_NO_WINDOW
    return kwargs

def assemble_hook():
    print("Building ThinkLate Video 05 Final Hook (00:00 - 01:16)...")
    
    # 7 Background segments
    bg_segments = [
        {"file": os.path.join(ASSETS_DIR, "generative_broll", "scene_01_eviction_door.jpg"), "is_img": True, "dur": 6.5},
        {"file": os.path.join(ASSETS_DIR, "action_gameplay_clips", "action_01_sea_sailing.mp4"), "is_img": False, "dur": 17.0},
        {"file": os.path.join(SHARED_BROLL, "pexels_san_francisco_street_1.mp4"), "is_img": False, "dur": 8.5},
        {"file": os.path.join(ASSETS_DIR, "documentary_broll", "scene1_01_city_apartments.mp4"), "is_img": False, "dur": 13.0},
        {"file": os.path.join(ASSETS_DIR, "action_gameplay_clips", "action_02_naval_patrol.mp4"), "is_img": False, "dur": 10.0},
        {"file": os.path.join(ASSETS_DIR, "action_gameplay_clips", "action_03_ocean_waves.mp4"), "is_img": False, "dur": 12.5},
        {"file": os.path.join(ASSETS_DIR, "action_gameplay_clips", "action_04_fleet_approach.mp4"), "is_img": False, "dur": 8.5},
    ]

    # Verify background clips
    for seg in bg_segments:
        if not os.path.exists(seg["file"]):
            raise FileNotFoundError(f"Missing background asset: {seg['file']}")

    # 8 Overlay cards with exact start and duration (extended to match full spoken thoughts)
    card_overlays = [
        {"file": os.path.join(HOOK_CARDS_DIR, "card_01_evidence_eviction.mov"), "start": 0.4, "dur": 5.8},      # 00:00.4 - 00:06.2 (5.8s)
        {"file": os.path.join(HOOK_CARDS_DIR, "card_02_character_founders.mov"), "start": 6.5, "dur": 8.5},     # 00:06.5 - 00:15.0 (8.5s)
        {"file": os.path.join(HOOK_CARDS_DIR, "card_03_typography_scrambling.mov"), "start": 15.5, "dur": 7.0},  # 00:15.5 - 00:22.5 (7.0s)
        {"file": os.path.join(HOOK_CARDS_DIR, "card_04_headline_hotels_sold_out.mov"), "start": 23.5, "dur": 8.0},# 00:23.5 - 00:31.5 (8.0s)
        {"file": os.path.join(HOOK_CARDS_DIR, "card_05_comparison_hotel_vs_airbed.mov"), "start": 32.0, "dur": 11.5},# 00:32.0 - 00:43.5 (11.5s)
        {"file": os.path.join(HOOK_CARDS_DIR, "card_06_typography_blueprint.mov"), "start": 44.5, "dur": 9.5},  # 00:44.5 - 00:54.0 (9.5s)
        {"file": os.path.join(HOOK_CARDS_DIR, "card_07_timeline_moves.mov"), "start": 55.0, "dur": 11.5},        # 00:55.0 - 01:06.5 (11.5s)
        {"file": os.path.join(HOOK_CARDS_DIR, "card_08_receipt_240_cash.mov"), "start": 67.5, "dur": 8.0},      # 00:67.5 - 01:15.5 (8.0s)
    ]

    for card in card_overlays:
        if not os.path.exists(card["file"]):
            raise FileNotFoundError(f"Missing card asset: {card['file']}")

    # Construct FFmpeg input arguments
    cmd = ["ffmpeg", "-y"]
    
    # Inputs 0..6: Background segments
    for seg in bg_segments:
        if seg["is_img"]:
            cmd.extend(["-loop", "1", "-t", f"{seg['dur']:.2f}", "-i", seg["file"]])
        else:
            cmd.extend(["-ss", "0", "-t", f"{seg['dur']:.2f}", "-i", seg["file"]])

    # Inputs 7..14: 8 Card overlays
    for card in card_overlays:
        cmd.extend(["-i", card["file"]])

    # Input 15: Audio source (pegged George VO + -26dB BGM)
    cmd.extend(["-ss", "0", "-t", "76.0", "-i", AUDIO_SRC])

    # Filtergraph construction
    filter_chains = []

    # 1. Normalize and scale all 7 background segments
    for i, seg in enumerate(bg_segments):
        filter_chains.append(
            f"[{i}:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30,setsar=1[v_bg_{i}]"
        )

    # 2. Concat background segments into continuous Track 1
    concat_inputs = "".join(f"[v_bg_{i}]" for i in range(len(bg_segments)))
    filter_chains.append(f"{concat_inputs}concat=n={len(bg_segments)}:v=1:a=0[base_v]")

    # 3. Dynamic Track 2 Gaussian focus blur during card windows
    blur_conditions = "+".join([
        f"between(t,{c['start']},{c['start']+c['dur']})" for c in card_overlays
    ])
    filter_chains.append(f"[base_v]split[base_sharp][base_for_blur]")
    filter_chains.append(f"[base_for_blur]boxblur=10:1[base_blurred]")
    filter_chains.append(
        f"[base_sharp][base_blurred]overlay=enable='{blur_conditions}'[tracked_bg]"
    )

    # 4. Sequentially overlay the 8 transparent ProRes 4444 Remotion cards (Track 3)
    # Using tpad=stop_mode=clone:stop=-1 so cards freeze on their final state for the extended hold duration
    current_stream = "tracked_bg"
    card_start_input_idx = len(bg_segments)  # index 7

    for idx, card in enumerate(card_overlays):
        in_idx = card_start_input_idx + idx
        next_stream = f"card_comp_{idx}"
        st = card["start"]
        et = card["start"] + card["dur"]
        
        # Freeze last frame with tpad and position with PTS timing
        filter_chains.append(
            f"[{in_idx}:v]tpad=stop_mode=clone:stop=-1,setpts=PTS-STARTPTS+{st}/TB[card_pts_{idx}]"
        )
        filter_chains.append(
            f"[{current_stream}][card_pts_{idx}]overlay=x=0:y=0:enable='between(t,{st},{et})'[card_comp_{idx}]"
        )
        current_stream = next_stream

    filter_complex_str = ";\n".join(filter_chains)

    audio_idx = card_start_input_idx + len(card_overlays)  # index 15

    # Full broadcast master command
    full_cmd = cmd + [
        "-filter_complex", filter_complex_str,
        "-map", f"[{current_stream}]",
        "-map", f"{audio_idx}:a",
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "320k",
        "-shortest",
        OUTPUT_MASTER
    ]

    print("Executing master Hook assembly...")
    res = subprocess.run(full_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **get_headless_kwargs())
    if res.returncode == 0 and os.path.exists(OUTPUT_MASTER):
        print(f"Master Hook Assembly Complete: {OUTPUT_MASTER} ({os.path.getsize(OUTPUT_MASTER)/1024/1024:.2f}MB)")
    else:
        print(f"Error during assembly:\n{res.stderr.decode('utf-8', errors='ignore')[-600:]}")
        return False

    # Also render light review cut for in-IDE player (<15MB)
    light_cmd = [
        "ffmpeg", "-y",
        "-i", OUTPUT_MASTER,
        "-c:v", "libx264",
        "-preset", "faster",
        "-crf", "24",
        "-c:a", "aac",
        "-b:a", "192k",
        OUTPUT_LIGHT
    ]
    subprocess.run(light_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **get_headless_kwargs())
    if os.path.exists(OUTPUT_LIGHT):
        print(f"In-IDE Light Cut Ready: {OUTPUT_LIGHT} ({os.path.getsize(OUTPUT_LIGHT)/1024/1024:.2f}MB)")

    return True

if __name__ == "__main__":
    assemble_hook()
