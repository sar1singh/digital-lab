#!/usr/bin/env python3
"""
Assemble ThinkLate Video 05 Part 3 Master (05:58 - 10:15 | 257s)
================================================================
Strictly compliant with:
- Rule 10 & 23: 4-track multi-layer visual stacking, state changes <= 3.5s
- Rule 17: Headless CREATE_NO_WINDOW execution
- Rule 20: Grounded historical archival assets
- Rule 21: ZERO camera shakes or tremors
- Rule 22: Broadcast VO (-1.0dB) + ducked BGM (-26dB with 1.5kHz notch EQ)
- Generous on-screen hold durations (14.5s to 25.0s) with in-memory frame freeze (tpad)
- Audio master clock from 358.0s to 615.0s (dual_full_mix_preview_plus15.wav)
"""

import os
import sys
import subprocess

BASE_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
AUDIO_DIR = os.path.join(BASE_DIR, "audio_takes")
PART3_CARDS_DIR = os.path.join(ASSETS_DIR, "part3_cards")
SHARED_BROLL = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\shared\assets\broll"
DOC_BROLL = os.path.join(ASSETS_DIR, "documentary_broll")
GAME_BROLL = os.path.join(ASSETS_DIR, "action_gameplay_clips")
ARTIFACT_DIR = r"C:\Users\sar1s\.gemini\antigravity\brain\a2e7cc12-b50a-4810-b87e-118b7df25366"

AUDIO_SRC = os.path.join(AUDIO_DIR, "dual_full_mix_preview_plus15.wav")
OUTPUT_MASTER = os.path.join(BASE_DIR, "ThinkLate_Video05_Part3_Master_1080p.mp4")
OUTPUT_LIGHT = os.path.join(ARTIFACT_DIR, "ThinkLate_Video05_Part3_Review_Light.mp4")

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

def assemble_part3():
    print("Building ThinkLate Video 05 Part 3 (05:58 - 10:15 | 257.0s)...")
    
    # 18 Background segments strictly scheduled across 257.0 seconds
    # Alternating curated documentary B-roll and living canvas gameplay spine
    bg_segments = [
        {"file": os.path.join(DOC_BROLL, "scene4_01_dslr_camera.mp4"), "ss": 0.0, "dur": 15.0},         # 0.0 - 15.0s: Flying to Brooklyn, DSLR camera
        {"file": os.path.join(DOC_BROLL, "scene4_04_doorway_entry.mp4"), "ss": 0.0, "dur": 13.0},       # 15.0 - 28.0s: Doorway entry, knocking on doors
        {"file": os.path.join(DOC_BROLL, "scene4_02_bright_interior.mp4"), "ss": 0.0, "dur": 15.0},     # 28.0 - 43.0s: Bright interior wide angle
        {"file": os.path.join(GAME_BROLL, "action_01_sea_sailing.mp4"), "ss": 0.0, "dur": 13.0},        # 43.0 - 56.0s: Living canvas - Caribbean sailing
        {"file": os.path.join(DOC_BROLL, "scene5_04_web_browsing.mp4"), "ss": 0.0, "dur": 12.0},       # 56.0 - 68.0s: Web browsing, hitting nationwide marketing wall
        {"file": os.path.join(DOC_BROLL, "scene5_03_server_datacenter.mp4"), "ss": 0.0, "dur": 18.0},   # 68.0 - 86.0s: Craigslist classified monopoly / servers
        {"file": os.path.join(DOC_BROLL, "scene5_01_python_coding.mp4"), "ss": 0.0, "dur": 16.0},       # 86.0 - 102.0s: Python code reverse engineering
        {"file": os.path.join(DOC_BROLL, "scene5_02_laptop_terminal.mp4"), "ss": 0.0, "dur": 13.0},     # 102.0 - 115.0s: Terminal bot syndication logs
        {"file": os.path.join(GAME_BROLL, "action_05_naval_maneuver.mp4"), "ss": 0.0, "dur": 17.0},     # 115.0 - 132.0s: Living canvas - aggressive naval maneuver ($0 siphon)
        {"file": os.path.join(DOC_BROLL, "scene3_01_venture_meeting.mp4"), "ss": 0.0, "dur": 13.0},     # 132.0 - 145.0s: Sequoia venture capital flood
        {"file": os.path.join(DOC_BROLL, "scene8_01_boutique_hotel.mp4"), "ss": 0.0, "dur": 17.0},      # 145.0 - 162.0s: Boutique hotel cartel vs 7M rooms
        {"file": os.path.join(DOC_BROLL, "scene6_01_empty_airport.mp4"), "ss": 0.0, "dur": 13.0},       # 162.0 - 175.0s: March 2020 COVID empty airport
        {"file": os.path.join(DOC_BROLL, "scene6_03_airplane_tarmac.mp4"), "ss": 0.0, "dur": 10.0},     # 175.0 - 185.0s: Grounded planes, $1B cash refunds
        {"file": os.path.join(DOC_BROLL, "scene3_04_whiteboard_strategy.mp4"), "ss": 0.0, "dur": 19.0}, # 185.0 - 204.0s: Executive restructuring memo / 1,900 layoffs
        {"file": os.path.join(DOC_BROLL, "scene8_02_luggage_journey.mp4"), "ss": 0.0, "dur": 14.0},     # 204.0 - 218.0s: Packed car escaping city
        {"file": os.path.join(GAME_BROLL, "action_13_sunny_caribbean.mp4"), "ss": 0.0, "dur": 12.0},    # 218.0 - 230.0s: Living canvas - mountain drive / cabin boom
        {"file": os.path.join(DOC_BROLL, "scene6_02_wall_street_ticker.mp4"), "ss": 0.0, "dur": 14.0},  # 230.0 - 244.0s: Wall Street NASDAQ ticker
        {"file": os.path.join(DOC_BROLL, "scene6_04_financial_trading.mp4"), "ss": 0.0, "dur": 13.0},   # 244.0 - 257.0s: Trading floor cheering, $100B IPO victory
    ]

    total_bg_dur = sum(s["dur"] for s in bg_segments)
    print(f"Total background duration: {total_bg_dur:.1f}s (target: 257.0s)")
    assert abs(total_bg_dur - 257.0) < 0.01, f"Background duration mismatch: {total_bg_dur} != 257.0"

    for seg in bg_segments:
        if not os.path.exists(seg["file"]):
            raise FileNotFoundError(f"Missing background asset: {seg['file']}")

    # 11 Motion Graphic Overlay Cards strictly grounded to speech-to-text timestamps
    card_overlays = [
        {"file": os.path.join(PART3_CARDS_DIR, "card_p3_01_polaroid_camera.mov"), "start": 1.0, "dur": 19.0},       # 1.0 - 20.0s: Brooklyn $500 Rented DSLR Hack
        {"file": os.path.join(PART3_CARDS_DIR, "card_p3_02_comparison_photos.mov"), "start": 24.5, "dur": 18.5},    # 24.5 - 43.0s: 2008 Flip Phone Crime Scene vs DSLR
        {"file": os.path.join(PART3_CARDS_DIR, "card_p3_03_metric_nyc_spike.mov"), "start": 43.5, "dur": 12.5},     # 43.5 - 56.0s: +300% NYC Bookings Surge
        {"file": os.path.join(PART3_CARDS_DIR, "card_p3_04_headline_craigslist.mov"), "start": 68.0, "dur": 18.0},  # 68.0 - 86.0s: Craigslist Controls 50M Seekers, Zero API
        {"file": os.path.join(PART3_CARDS_DIR, "card_p3_05_terminal_bot.mov"), "start": 87.0, "dur": 21.0},         # 87.0 - 108.0s: Terminal Code Block: Craigslist Auto Poster
        {"file": os.path.join(PART3_CARDS_DIR, "card_p3_06_comparison_siphon.mov"), "start": 112.0, "dur": 20.0},   # 112.0 - 132.0s: $100k Traditional Ad Spend vs $0 Bot
        {"file": os.path.join(PART3_CARDS_DIR, "card_p3_07_barchart_supply.mov"), "start": 138.0, "dur": 24.0},     # 138.0 - 162.0s: Hotel Cartel vs Airbnb (7.0M Rooms)
        {"file": os.path.join(PART3_CARDS_DIR, "card_p3_08_headline_covid.mov"), "start": 165.0, "dur": 19.0},     # 165.0 - 184.0s: March 2020: 80% Collapse & $1B Cash Refund
        {"file": os.path.join(PART3_CARDS_DIR, "card_p3_09_redaction_layoffs.mov"), "start": 184.5, "dur": 19.5},   # 184.5 - 204.0s: Confidential Restructuring Memo: 1,900 Layoffs
        {"file": os.path.join(PART3_CARDS_DIR, "card_p3_10_comparison_staycation.mov"), "start": 206.0, "dur": 24.0},# 206.0 - 230.0s: Flights 0% vs Drive-to Cabins Record Cash
        {"file": os.path.join(PART3_CARDS_DIR, "card_p3_11_linechart_ipo.mov"), "start": 231.0, "dur": 25.0},       # 231.0 - 256.0s: Valuation Line Chart: $0 to $100B NASDAQ IPO
    ]

    for card in card_overlays:
        if not os.path.exists(card["file"]):
            raise FileNotFoundError(f"Missing card asset: {card['file']}")

    cmd = ["ffmpeg", "-y"]

    # Inputs 0..17: 18 Background segments
    for seg in bg_segments:
        cmd.extend(["-ss", f"{seg['ss']:.2f}", "-t", f"{seg['dur']:.2f}", "-i", seg["file"]])

    # Inputs 18..28: 11 Card overlays
    for card in card_overlays:
        cmd.extend(["-i", card["file"]])

    # Input 29: Audio source (voiceover + -26dB BGM from 358.0s for 257.0s)
    cmd.extend(["-ss", "358.0", "-t", "257.0", "-i", AUDIO_SRC])

    filter_chains = []

    # 1. Normalize and scale all 18 background segments
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

    # 4. Sequentially overlay the 11 transparent ProRes 4444 Remotion cards (Track 3)
    # Using tpad=stop_mode=clone:stop=-1 so cards freeze on their final state for the extended hold duration
    current_stream = "tracked_bg"
    card_start_input_idx = len(bg_segments)  # index 18

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
    audio_idx = card_start_input_idx + len(card_overlays)  # index 29

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

    print("Executing master Part 3 assembly (CRF 18)...")
    res = subprocess.run(full_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **get_headless_kwargs())
    if res.returncode == 0 and os.path.exists(OUTPUT_MASTER):
        print(f"Master Part 3 Assembly Complete: {OUTPUT_MASTER} ({os.path.getsize(OUTPUT_MASTER)/1024/1024:.2f}MB)")
    else:
        print(f"Error during Part 3 assembly:\n{res.stderr.decode('utf-8', errors='ignore')[-600:]}")
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
    assemble_part3()

