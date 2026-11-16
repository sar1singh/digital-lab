#!/usr/bin/env python3
"""
Assemble ThinkLate Video 05 Part 4 Master (10:15 - 13:27 | 192s)
================================================================
Strictly calibrated segment durations (zero duration clipping).
Incorporating 5 distinct, diverse gameplay scenes:
(galleon deck sword combat, naval cannon broadsides, white sand beach stroll, jungle waterfalls, stormy sailing).
"""

import os
import sys
import subprocess

BASE_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
AUDIO_DIR = os.path.join(BASE_DIR, "audio_takes")
PART4_CARDS_DIR = os.path.join(ASSETS_DIR, "part4_cards")
SHARED_BROLL = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\shared\assets\broll"
DOC_BROLL = os.path.join(ASSETS_DIR, "documentary_broll")
GAME_BROLL = os.path.join(ASSETS_DIR, "action_gameplay_clips")
ARTIFACT_DIR = r"C:\Users\sar1s\.gemini\antigravity\brain\a2e7cc12-b50a-4810-b87e-118b7df25366"

AUDIO_SRC = os.path.join(AUDIO_DIR, "dual_full_mix_preview_plus15.wav")
OUTPUT_MASTER = os.path.join(BASE_DIR, "ThinkLate_Video05_Part4_Master_1080p.mp4")
OUTPUT_LIGHT = os.path.join(ARTIFACT_DIR, "ThinkLate_Video05_Part4_Review_Light.mp4")

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

def assemble_part4():
    print("Building ThinkLate Video 05 Part 4 (10:15 - 13:27 | 192.0s)...")
    
    # 15 Background segments calibrated to exact source lengths (192.0s total)
    bg_segments = [
        {"file": os.path.join(DOC_BROLL, "scene1_01_city_apartments.mp4"), "ss": 0.0, "dur": 16.0},         # 0.0 - 16.0s: Dense urban apartments (shadow hotels)
        {"file": os.path.join(DOC_BROLL, "scene3_03_business_contract.mp4"), "ss": 0.0, "dur": 10.0},       # 16.0 - 26.0s: Private equity contracts
        {"file": os.path.join(DOC_BROLL, "scene5_04_web_browsing.mp4"), "ss": 0.0, "dur": 12.0},           # 26.0 - 38.0s: Browsing Airbnb site
        {"file": os.path.join(SHARED_BROLL, "mixkit_money_18296-1080.mp4"), "ss": 0.0, "dur": 8.0},        # 38.0 - 46.0s: Cash explosion ($180 cleaning fee)
        {"file": os.path.join(DOC_BROLL, "scene7_03_cleaning_chores.mp4"), "ss": 0.0, "dur": 10.0},        # 46.0 - 56.0s: Mopping floors, cleaning chores
        {"file": os.path.join(DOC_BROLL, "scene7_01_house_chores.mp4"), "ss": 0.0, "dur": 6.0},            # 56.0 - 62.0s: Dishwasher, dump run
        {"file": os.path.join(GAME_BROLL, "gameplay_03_galleon_deck_combat.mp4"), "ss": 0.0, "dur": 22.0}, # 62.0 - 84.0s: Deck sword combat (viral backlash clash!)
        {"file": os.path.join(DOC_BROLL, "scene7_04_city_protest_street.mp4"), "ss": 0.0, "dur": 7.0},     # 84.0 - 91.0s: Street protests / government guillotine
        {"file": os.path.join(DOC_BROLL, "scene7_02_city_protest.mp4"), "ss": 0.0, "dur": 7.0},            # 91.0 - 98.0s: Anti-tourism crowds / Local Law 18
        {"file": os.path.join(GAME_BROLL, "gameplay_02_naval_broadside_fire.mp4"), "ss": 0.0, "dur": 22.0},# 98.0 - 120.0s: Explosive cannon broadside (regulatory war)
        {"file": os.path.join(GAME_BROLL, "gameplay_05_caribbean_beach_stalk.mp4"), "ss": 0.0, "dur": 16.0},# 120.0 - 136.0s: White sand beach & palm trees walk (doing nothing)
        {"file": os.path.join(DOC_BROLL, "scene6_04_financial_trading.mp4"), "ss": 0.0, "dur": 16.0},      # 136.0 - 152.0s: $12B revenue trading floor
        {"file": os.path.join(GAME_BROLL, "gameplay_04_jungle_waterfall_run.mp4"), "ss": 0.0, "dur": 14.0},# 152.0 - 166.0s: Lush jungle waterfalls & pristine stream
        {"file": os.path.join(DOC_BROLL, "scene8_01_boutique_hotel.mp4"), "ss": 0.0, "dur": 14.0},         # 166.0 - 180.0s: Boutique hotel lobby
        {"file": os.path.join(GAME_BROLL, "gameplay_01_ocean_storm_sailing.mp4"), "ss": 0.0, "dur": 12.0}, # 180.0 - 192.0s: High seas storm sailing (solo war)
    ]

    total_bg_dur = sum(s["dur"] for s in bg_segments)
    print(f"Total background duration: {total_bg_dur:.1f}s (target: 192.0s)")
    assert abs(total_bg_dur - 192.0) < 0.01, f"Background duration mismatch: {total_bg_dur} != 192.0"

    for seg in bg_segments:
        if not os.path.exists(seg["file"]):
            raise FileNotFoundError(f"Missing background asset: {seg['file']}")

    # 8 Motion Graphic Overlay Cards strictly grounded to Whisper speech-to-text timestamps
    card_overlays = [
        {"file": os.path.join(PART4_CARDS_DIR, "card_p4_01_headline_shadow_hotels.mov"), "start": 1.0, "dur": 21.0},        # 1.0 - 22.0s: Private Equity & Shadow Hotels
        {"file": os.path.join(PART4_CARDS_DIR, "card_p4_02_receipt_exploding_bill.mov"), "start": 28.0, "dur": 18.0},        # 28.0 - 46.0s: $150 to $400 Exploding Bill ($180 cleaning fee)
        {"file": os.path.join(PART4_CARDS_DIR, "card_p4_03_redaction_chore_list.mov"), "start": 48.0, "dur": 24.0},          # 48.0 - 72.0s: Laminated Chore Contract & Dump Run
        {"file": os.path.join(PART4_CARDS_DIR, "card_p4_04_citation_hotels_won.mov"), "start": 74.0, "dur": 13.0},          # 74.0 - 87.0s: TikTok #HotelsWon Backlash (14.2M views)
        {"file": os.path.join(PART4_CARDS_DIR, "card_p4_05_redaction_nyc_law18.mov"), "start": 92.0, "dur": 16.0},          # 92.0 - 108.0s: NYC Local Law 18 Hammer (80% wiped out)
        {"file": os.path.join(PART4_CARDS_DIR, "card_p4_06_comparison_global_bans.mov"), "start": 110.0, "dur": 18.0},       # 110.0 - 128.0s: Barcelona 2028 Total Ban vs NYC Law 18
        {"file": os.path.join(PART4_CARDS_DIR, "card_p4_07_barchart_mature_machine.mov"), "start": 132.0, "dur": 20.0},       # 132.0 - 152.0s: $12B Revenue / $2.5B Profit / 8M Listings
        {"file": os.path.join(PART4_CARDS_DIR, "card_p4_08_comparison_boutique_hotels.mov"), "start": 158.0, "dur": 32.0},   # 158.0 - 190.0s: Comedic Full Circle: Boutique Hotels #1 Category
    ]

    for card in card_overlays:
        if not os.path.exists(card["file"]):
            raise FileNotFoundError(f"Missing card asset: {card['file']}")

    cmd = ["ffmpeg", "-y"]

    # Inputs 0..14: 15 Background segments
    for seg in bg_segments:
        cmd.extend(["-ss", f"{seg['ss']:.2f}", "-t", f"{seg['dur']:.2f}", "-i", seg["file"]])

    # Inputs 15..22: 8 Card overlays
    for card in card_overlays:
        cmd.extend(["-i", card["file"]])

    # Input 23: Audio source (voiceover + -26dB BGM from 615.0s for 192.0s)
    cmd.extend(["-ss", "615.0", "-t", "192.0", "-i", AUDIO_SRC])

    filter_chains = []

    # 1. Normalize and scale all 15 background segments
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

    # 4. Sequentially overlay the 8 transparent ProRes 4444 Remotion cards (Track 3)
    current_stream = "tracked_bg"
    card_start_input_idx = len(bg_segments)  # index 15

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
    audio_idx = card_start_input_idx + len(card_overlays)  # index 23

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

    print("Executing master Part 4 assembly (CRF 18)...")
    res = subprocess.run(full_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **get_headless_kwargs())
    if res.returncode == 0 and os.path.exists(OUTPUT_MASTER):
        print(f"Master Part 4 Assembly Complete: {OUTPUT_MASTER} ({os.path.getsize(OUTPUT_MASTER)/1024/1024:.2f}MB)")
    else:
        print(f"Error during Part 4 assembly:\n{res.stderr.decode('utf-8', errors='ignore')[-600:]}")
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
    assemble_part4()
