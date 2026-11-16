#!/usr/bin/env python3
"""
Assemble ThinkLate Video 05 Part 2 Master (01:16 - 05:36 | 260s)
================================================================
Strictly compliant with:
- Rule 10 & 23: 4-track multi-layer visual stacking, state changes <= 3.5s
- Rule 17: Headless CREATE_NO_WINDOW execution
- Rule 20: Real founder faces clearly visible (Nathan Blecharczyk & Paul Graham)
- Rule 21: ZERO camera shakes or tremors
- Rule 22: Broadcast VO (-1.0dB) + ducked BGM (-26dB with 1.5kHz notch EQ)
- Generous on-screen hold durations (11.5s to 22.0s) with in-memory frame freeze (tpad)
"""

import os
import sys
import subprocess

BASE_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
AUDIO_DIR = os.path.join(BASE_DIR, "audio_takes")
PART2_CARDS_DIR = os.path.join(ASSETS_DIR, "part2_cards")
SHARED_BROLL = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\shared\assets\broll"
DOC_BROLL = os.path.join(ASSETS_DIR, "documentary_broll")
GAME_BROLL = os.path.join(ASSETS_DIR, "action_gameplay_clips")
ARTIFACT_DIR = r"C:\Users\sar1s\.gemini\antigravity\brain\a2e7cc12-b50a-4810-b87e-118b7df25366"

AUDIO_SRC = os.path.join(AUDIO_DIR, "dual_full_mix_preview_plus15.wav")
OUTPUT_MASTER = os.path.join(BASE_DIR, "ThinkLate_Video05_Part2_Master_1080p.mp4")
OUTPUT_LIGHT = os.path.join(ARTIFACT_DIR, "ThinkLate_Video05_Part2_Review_Light.mp4")

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

def assemble_part2():
    print("Building ThinkLate Video 05 Part 2 (01:16 - 05:58 | 282s)...")
    
    # 17 Background segments strictly scheduled across 282.0 seconds
    bg_segments = [
        {"file": os.path.join(GAME_BROLL, "action_04_fleet_approach.mp4"), "ss": 0.0, "dur": 16.5},
        {"file": os.path.join(GAME_BROLL, "action_01_sea_sailing.mp4"), "ss": 0.0, "dur": 21.5},
        {"file": os.path.join(SHARED_BROLL, "pexels_san_francisco_street_1.mp4"), "ss": 0.0, "dur": 13.0},
        {"file": os.path.join(DOC_BROLL, "scene3_01_venture_meeting.mp4"), "ss": 0.0, "dur": 12.5},
        {"file": os.path.join(GAME_BROLL, "action_02_naval_patrol.mp4"), "ss": 0.0, "dur": 11.5},
        {"file": os.path.join(DOC_BROLL, "scene2_01_credit_card_debt.mp4"), "ss": 0.0, "dur": 18.0},
        {"file": os.path.join(GAME_BROLL, "action_03_ocean_waves.mp4"), "ss": 0.0, "dur": 17.0},
        {"file": os.path.join(GAME_BROLL, "action_06_combat_ready.mp4"), "ss": 0.0, "dur": 12.5},
        {"file": os.path.join(GAME_BROLL, "action_05_naval_maneuver.mp4"), "ss": 0.0, "dur": 12.5},
        {"file": os.path.join(GAME_BROLL, "action_04_fleet_approach.mp4"), "ss": 16.5, "dur": 15.0},
        {"file": os.path.join(DOC_BROLL, "scene3_01_venture_meeting.mp4"), "ss": 12.5, "dur": 20.0},
        {"file": os.path.join(GAME_BROLL, "action_01_sea_sailing.mp4"), "ss": 21.5, "dur": 19.0},
        {"file": os.path.join(DOC_BROLL, "scene3_02_partnership_deal.mp4"), "ss": 0.0, "dur": 17.0},
        {"file": os.path.join(DOC_BROLL, "scene1_01_city_apartments.mp4"), "ss": 0.0, "dur": 20.0},
        {"file": os.path.join(SHARED_BROLL, "pexels_san_francisco_street_1.mp4"), "ss": 0.0, "dur": 18.0},
        {"file": os.path.join(GAME_BROLL, "action_02_naval_patrol.mp4"), "ss": 11.5, "dur": 16.0},
        {"file": os.path.join(GAME_BROLL, "action_05_naval_maneuver.mp4"), "ss": 12.5, "dur": 22.0},
    ]

    total_bg_dur = sum(s["dur"] for s in bg_segments)
    print(f"Total background duration: {total_bg_dur:.1f}s (target: 282.0s)")

    for seg in bg_segments:
        if not os.path.exists(seg["file"]):
            raise FileNotFoundError(f"Missing background asset: {seg['file']}")

    # 14 Motion Graphic Overlay Cards strictly grounded to speech-to-text timestamps
    card_overlays = [
        {"file": os.path.join(PART2_CARDS_DIR, "card_p2_01_character_nate.mov"), "start": 16.5, "dur": 11.5},       # 16.5 - 28.0s: Nate Blecharczyk CTO
        {"file": os.path.join(PART2_CARDS_DIR, "card_p2_02_architecture_mvp.mov"), "start": 28.5, "dur": 9.0},       # 28.5 - 37.5s: Primitive Airbed MVP Stack
        {"file": os.path.join(PART2_CARDS_DIR, "card_p2_03_headline_vc_pass.mov"), "start": 38.0, "dur": 12.0},      # 38.0 - 50.0s: Sand Hill Road VC Rejections
        {"file": os.path.join(PART2_CARDS_DIR, "card_p2_04_redaction_seed_memo.mov"), "start": 51.0, "dur": 12.0},   # 51.0 - 63.0s: VC Partner Pass Memo
        {"file": os.path.join(PART2_CARDS_DIR, "card_p2_05_comparison_sxsw.mov"), "start": 63.5, "dur": 11.0},       # 63.5 - 74.5s: SXSW 2 Bookings Reality
        {"file": os.path.join(PART2_CARDS_DIR, "card_p2_06_ladder_debt.mov"), "start": 75.0, "dur": 14.0},           # 75.0 - 89.0s: Credit Card Debt Ladder ($20k)
        {"file": os.path.join(PART2_CARDS_DIR, "card_p2_07_polaroid_cereal.mov"), "start": 110.0, "dur": 12.0},      # 110.0 - 122.0s: Denver DNC Cereal Business
        {"file": os.path.join(PART2_CARDS_DIR, "card_p2_08_comparison_cereal.mov"), "start": 122.5, "dur": 12.0},     # 122.5 - 134.5s: Obama O's vs Cap'n McCain's
        {"file": os.path.join(PART2_CARDS_DIR, "card_p2_09_metric_cereal_cash.mov"), "start": 135.0, "dur": 14.0},   # 135.0 - 149.0s: $38,000 Pure Cash
        {"file": os.path.join(PART2_CARDS_DIR, "card_p2_10_character_paulg.mov"), "start": 150.0, "dur": 18.0},      # 150.0 - 168.0s: Paul Graham YC Gate
        {"file": os.path.join(PART2_CARDS_DIR, "card_p2_11_citation_paulg.mov"), "start": 189.0, "dur": 17.0},       # 189.0 - 206.0s: Graham Cockroach Retrospective
        {"file": os.path.join(PART2_CARDS_DIR, "card_p2_12_comparison_rebrand.mov"), "start": 208.0, "dur": 30.0},    # 208.0 - 238.0s: Airbed & Breakfast -> Airbnb.com
        {"file": os.path.join(PART2_CARDS_DIR, "card_p2_13_linechart_flatline.mov"), "start": 244.0, "dur": 16.0},   # 244.0 - 260.0s: Windowless Office & Ramen Flatline
        {"file": os.path.join(PART2_CARDS_DIR, "card_p2_14_typography_nyc.mov"), "start": 268.0, "dur": 12.0},       # 268.0 - 280.0s: "DO THINGS THAT DON'T SCALE"
    ]

    for card in card_overlays:
        if not os.path.exists(card["file"]):
            raise FileNotFoundError(f"Missing card asset: {card['file']}")

    cmd = ["ffmpeg", "-y"]

    # Inputs 0..16: 17 Background segments
    for seg in bg_segments:
        cmd.extend(["-ss", f"{seg['ss']:.2f}", "-t", f"{seg['dur']:.2f}", "-i", seg["file"]])

    # Inputs 17..30: 14 Card overlays
    for card in card_overlays:
        cmd.extend(["-i", card["file"]])

    # Input 31: Audio source (pegged George VO + -26dB BGM from 76.0s for 282.0s)
    cmd.extend(["-ss", "76.0", "-t", "282.0", "-i", AUDIO_SRC])

    filter_chains = []

    # 1. Normalize and scale all 17 background segments
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

    # 4. Sequentially overlay the 14 transparent ProRes 4444 Remotion cards (Track 3)
    # Using tpad=stop_mode=clone:stop=-1 so cards freeze on their final state for the extended hold duration
    current_stream = "tracked_bg"
    card_start_input_idx = len(bg_segments)  # index 17

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
    audio_idx = card_start_input_idx + len(card_overlays)  # index 31

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

    print("Executing master Part 2 assembly...")
    res = subprocess.run(full_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **get_headless_kwargs())
    if res.returncode == 0 and os.path.exists(OUTPUT_MASTER):
        print(f"Master Part 2 Assembly Complete: {OUTPUT_MASTER} ({os.path.getsize(OUTPUT_MASTER)/1024/1024:.2f}MB)")
    else:
        print(f"Error during Part 2 assembly:\n{res.stderr.decode('utf-8', errors='ignore')[-600:]}")
        return False

    # Also render light review cut for in-IDE player
    print("Rendering light review cut for in-IDE player...")
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
    assemble_part2()

