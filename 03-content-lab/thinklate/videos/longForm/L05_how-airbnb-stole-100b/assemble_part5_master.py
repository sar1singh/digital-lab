#!/usr/bin/env python3
"""
Assemble ThinkLate Video 05 Part 5 Master (13:27 - 15:57 | 150s)
================================================================
Strictly calibrated segment durations (zero duration clipping).
Incorporating diverse gameplay sequences:
(naval broadside fire, jungle waterfalls, deck sword combat, white sand beach walk, stormy sailing).
"""

import os
import sys
import subprocess

BASE_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
AUDIO_DIR = os.path.join(BASE_DIR, "audio_takes")
PART5_CARDS_DIR = os.path.join(ASSETS_DIR, "part5_cards")
SHARED_BROLL = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\shared\assets\broll"
DOC_BROLL = os.path.join(ASSETS_DIR, "documentary_broll")
GAME_BROLL = os.path.join(ASSETS_DIR, "action_gameplay_clips")
ARTIFACT_DIR = r"C:\Users\sar1s\.gemini\antigravity\brain\a2e7cc12-b50a-4810-b87e-118b7df25366"

AUDIO_SRC = os.path.join(AUDIO_DIR, "dual_full_mix_preview_plus15.wav")
OUTPUT_MASTER = os.path.join(BASE_DIR, "ThinkLate_Video05_Part5_Master_1080p.mp4")
OUTPUT_LIGHT = os.path.join(ARTIFACT_DIR, "ThinkLate_Video05_Part5_Review_Light.mp4")

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

def assemble_part5():
    print("Building ThinkLate Video 05 Part 5 (13:27 - 15:57 | 150.0s)...")
    
    # 11 Background segments strictly scheduled across 150.0 seconds
    bg_segments = [
        {"file": os.path.join(DOC_BROLL, "scene3_04_whiteboard_strategy.mp4"), "ss": 0.0, "dur": 12.0},      # 0.0 - 12.0s: Strategy blueprint (3 brutal rules)
        {"file": os.path.join(GAME_BROLL, "gameplay_02_naval_broadside_fire.mp4"), "ss": 0.0, "dur": 14.0}, # 12.0 - 26.0s: Naval broadside combat (Law 1 hijack!)
        {"file": os.path.join(DOC_BROLL, "scene5_01_python_coding.mp4"), "ss": 0.0, "dur": 12.0},          # 26.0 - 38.0s: Rogue python script
        {"file": os.path.join(DOC_BROLL, "scene4_04_doorway_entry.mp4"), "ss": 0.0, "dur": 14.0},          # 38.0 - 52.0s: Doorway entry (Law 2 kitchen doctrine)
        {"file": os.path.join(GAME_BROLL, "gameplay_04_jungle_waterfall_run.mp4"), "ss": 0.0, "dur": 14.0}, # 52.0 - 66.0s: Jungle waterfalls run (unscalable legwork)
        {"file": os.path.join(DOC_BROLL, "scene6_04_financial_trading.mp4"), "ss": 0.0, "dur": 14.0},      # 66.0 - 80.0s: Wall Street trading (Law 3 spreadsheet extraction)
        {"file": os.path.join(GAME_BROLL, "gameplay_03_galleon_deck_combat.mp4"), "ss": 0.0, "dur": 14.0}, # 80.0 - 94.0s: Deck sword fighting (competitors destroying you)
        {"file": os.path.join(GAME_BROLL, "gameplay_05_caribbean_beach_stalk.mp4"), "ss": 0.0, "dur": 14.0},# 94.0 - 108.0s: White sand beach walk (humble founder back to wall)
        {"file": os.path.join(DOC_BROLL, "scene8_02_luggage_journey.mp4"), "ss": 0.0, "dur": 14.0},         # 108.0 - 122.0s: Pack bag and travel / step outside routine
        {"file": os.path.join(GAME_BROLL, "action_13_sunny_caribbean.mp4"), "ss": 0.0, "dur": 14.0},        # 122.0 - 136.0s: Atop church looking at harbor ($80 airbed into $100B)
        {"file": os.path.join(GAME_BROLL, "gameplay_01_ocean_storm_sailing.mp4"), "ss": 0.0, "dur": 14.0}, # 136.0 - 150.0s: High seas storm sailing (Stay curious outro)
    ]

    total_bg_dur = sum(s["dur"] for s in bg_segments)
    print(f"Total background duration: {total_bg_dur:.1f}s (target: 150.0s)")
    assert abs(total_bg_dur - 150.0) < 0.01, f"Background duration mismatch: {total_bg_dur} != 150.0"

    for seg in bg_segments:
        if not os.path.exists(seg["file"]):
            raise FileNotFoundError(f"Missing background asset: {seg['file']}")

    # 7 Motion Graphic Overlay Cards strictly grounded to Whisper speech-to-text timestamps
    card_overlays = [
        {"file": os.path.join(PART5_CARDS_DIR, "card_p5_01_ladder_3laws.mov"), "start": 1.0, "dur": 21.0},        # 1.0 - 22.0s: The 3 Brutal Laws of Solo Entrepreneurship
        {"file": os.path.join(PART5_CARDS_DIR, "card_p5_02_comparison_distribution.mov"), "start": 24.0, "dur": 20.0},# 24.0 - 44.0s: Law 1: Borrow Distribution Before You Own It
        {"file": os.path.join(PART5_CARDS_DIR, "card_p5_03_comparison_kitchen.mov"), "start": 46.0, "dur": 20.0},     # 46.0 - 66.0s: Law 2: The Kitchen Doctrine (Do things that don't scale)
        {"file": os.path.join(PART5_CARDS_DIR, "card_p5_04_evidence_soul.mov"), "start": 68.0, "dur": 20.0},       # 68.0 - 88.0s: Law 3: Never Optimize The Soul Out Of Product
        {"file": os.path.join(PART5_CARDS_DIR, "card_p5_05_character_chesky.mov"), "start": 90.0, "dur": 20.0},    # 90.0 - 110.0s: Brian Chesky: Resourceful, Stubborn, Humble
        {"file": os.path.join(PART5_CARDS_DIR, "card_p5_06_typography_action.mov"), "start": 112.0, "dur": 20.0},  # 112.0 - 132.0s: "FIND AN ANNOYING PROBLEM. DO UNGLAMOROUS WORK."
        {"file": os.path.join(PART5_CARDS_DIR, "card_p5_07_headline_outro.mov"), "start": 134.0, "dur": 15.0},     # 134.0 - 149.0s: From $80 Airbed to $100B / Stay Curious Outro
    ]

    for card in card_overlays:
        if not os.path.exists(card["file"]):
            raise FileNotFoundError(f"Missing card asset: {card['file']}")

    cmd = ["ffmpeg", "-y"]

    # Inputs 0..10: 11 Background segments
    for seg in bg_segments:
        cmd.extend(["-ss", f"{seg['ss']:.2f}", "-t", f"{seg['dur']:.2f}", "-i", seg["file"]])

    # Inputs 11..17: 7 Card overlays
    for card in card_overlays:
        cmd.extend(["-i", card["file"]])

    # Input 18: Audio source (voiceover + -26dB BGM from 807.0s for 150.0s)
    cmd.extend(["-ss", "807.0", "-t", "150.0", "-i", AUDIO_SRC])

    filter_chains = []

    # 1. Normalize and scale all 11 background segments
    for i, seg in enumerate(bg_segments):
        filter_chains.append(
            f"[{i}:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30,setsar=1[v_bg_{i}]"
        )

    # 2. Concat background segments into continuous Track 1 base video
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

    # 4. Sequentially overlay the 7 transparent ProRes 4444 Remotion cards (Track 3)
    current_stream = "tracked_bg"
    card_start_input_idx = len(bg_segments)  # index 11

    for idx, card in enumerate(card_overlays):
        in_idx = card_start_input_idx + idx
        next_stream = f"card_comp_{idx}"
        st = card["start"]
        et = card["start"] + card["dur"]

        filter_chains.append(
            f"[{in_idx}:v]tpad=stop_mode=clone:stop=-1,setpts=PTS-STARTPTS+{st}/TB[card_pts_{idx}]"
        )
        filter_chains.append(
            f"[{current_stream}][card_pts_{idx}]overlay=x=0:y=0:enable='between(t,{st},{et})'[card_comp_{idx}]"
        )
        current_stream = next_stream

    filter_complex_str = ";\n".join(filter_chains)
    audio_idx = card_start_input_idx + len(card_overlays)  # index 18

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

    print("Executing master Part 5 assembly (CRF 18)...")
    res = subprocess.run(full_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **get_headless_kwargs())
    if res.returncode == 0 and os.path.exists(OUTPUT_MASTER):
        print(f"Master Part 5 Assembly Complete: {OUTPUT_MASTER} ({os.path.getsize(OUTPUT_MASTER)/1024/1024:.2f}MB)")
    else:
        print(f"Error during Part 5 assembly:\n{res.stderr.decode('utf-8', errors='ignore')[-600:]}")
        return False

    # Also render light review cut for in-IDE player
    print("Rendering light review cut for in-IDE player (CRF 24)...")
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
    assemble_part5()

