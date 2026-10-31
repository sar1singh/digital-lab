#!/usr/bin/env python3
"""
ThinkLate Video 05 — DaVinci Resolve Timeline Exporter (FCPXML 1.8 & CMX 3600 EDL)
==================================================================================
Episode: "How An $80 Airbed Stole An Entire Industry" (05_how-airbnb-stole-100b)
Runtime: 17m 26s (1,046.00s) | Audio: Andrew Multilingual Neural (Pure Crisp 90%) + Ambient Bed (30%)
4-Track Architecture:
  V1: 100% Real-World Documentary Stock Video & Archival B-Roll
  V2: Scoped Gaussian Blur (0.15) & 35mm Film Grain (8%)
  V3: Programmatic Data Charts & Anchor Plates (3% Ken Burns push)
  V4: Kinetic Typography Slams & Evidence Badges (Text+)
  A1: Master Dialogue Voiceover (90% volume)
  A2: Cinematic Ambient BGM Bed (30% volume)
  A3: Sub-Bass Impact Booms & Drops (-12 dB)
  A4: Diegetic Foley Soundscapes (-16 dB)
"""

import os
import sys
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

VIDEO_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(VIDEO_DIR, "assets")
BROLL_DIR = os.path.join(ASSETS_DIR, "documentary_broll")
AUDIO_DIR = os.path.join(VIDEO_DIR, "audio_takes")
SFX_DIR = os.path.join(ASSETS_DIR, "sfx")

FCPXML_OUT = os.path.join(VIDEO_DIR, "ThinkLate_Video05_DaVinci.fcpxml")
EDL_OUT = os.path.join(VIDEO_DIR, "ThinkLate_Video05.edl")

FPS = 30
FRAME_DUR = f"1/{FPS}s"

def sec_to_frames(sec):
    return int(round(sec * FPS))

def frames_to_timecode(frames, fps=30):
    total_sec = frames // fps
    f = frames % fps
    s = total_sec % 60
    m = (total_sec // 60) % 60
    h = total_sec // 3600
    return f"{h:02d}:{m:02d}:{s:02d}:{f:02d}"

def sec_to_timecode(sec, fps=30):
    return frames_to_timecode(sec_to_frames(sec), fps)

# 8 Narrative Scenes mapped with Whisper Ground-Truth boundaries
TIMELINE_CUES = [
    {
        "id": 1,
        "name": "Scene 01: Eviction & Airbed Hook",
        "start": 0.00,
        "end": 164.16,
        "v1_broll": "scene1_01_city_apartments.mp4",
        "v1_broll_2": "scene1_02_apartment_keys.mp4",
        "v1_archive": "san_francisco_exterior.jpg",
        "v3_anchor": "thumbnail_option_a.jpg",
        "v4_text": "OCTOBER 2007: $1,150 OVERDUE RENT // 3 AIRBEDS ON BARE FLOOR",
        "sfx": ("sfx_sub_boom.wav", 0.00, -12.0)
    },
    {
        "id": 2,
        "name": "Scene 02: $20K Debt & Cereal Heist",
        "start": 164.16,
        "end": 259.52,
        "v1_broll": "scene2_01_credit_card_debt.mp4",
        "v1_broll_2": "scene2_02_convention_crowd.mp4",
        "v1_archive": "brian_chesky_archive.jpg",
        "v3_anchor": None,
        "v4_text": "SUMMER 2008: $20,000 CREDIT DEBT // 1,000 CEREAL BOXES = $30,000 RUNWAY",
        "sfx": ("sfx_whoosh.wav", 164.50, -16.0)
    },
    {
        "id": 3,
        "name": "Scene 03: YC Crucible & Paul Graham",
        "start": 259.52,
        "end": 367.12,
        "v1_broll": "scene3_01_venture_meeting.mp4",
        "v1_broll_2": "scene3_02_partnership_deal.mp4",
        "v1_archive": "paul_graham_archive.jpg",
        "v3_anchor": None,
        "v4_text": "JANUARY 2009: PAUL GRAHAM INTERVIEW // IF YOU CAN SELL $40 CEREAL, YOU'RE IN",
        "sfx": ("sfx_sub_boom.wav", 260.00, -12.0)
    },
    {
        "id": 4,
        "name": "Scene 04: Brooklyn Photography Ground War",
        "start": 367.20,
        "end": 445.52,
        "v1_broll": "scene4_01_dslr_camera.mp4",
        "v1_broll_2": "scene4_02_bright_interior.mp4",
        "v1_archive": "brooklyn_apartments.jpg",
        "v3_anchor": None,
        "v4_text": "DO THINGS THAT DON'T SCALE // FREE $500 DSLR PHOTOS = 3X BOOKINGS",
        "sfx": ("sfx_data_blip.wav", 368.00, -16.0)
    },
    {
        "id": 5,
        "name": "Scene 05: Craigslist Hijack Growth Hack",
        "start": 445.52,
        "end": 567.20,
        "v1_broll": "scene5_01_python_coding.mp4",
        "v1_broll_2": "scene5_02_laptop_terminal.mp4",
        "v1_archive": None,
        "v3_anchor": "CHART_VALUATION_ARBITRAGE.png",
        "v4_text": "2010: THE CRAIGSLIST HIJACK // REVERSE-ENGINEERED FORMS = 50M USERS FOR $0",
        "sfx": ("sfx_whoosh.wav", 446.00, -16.0)
    },
    {
        "id": 6,
        "name": "Scene 06: COVID Crash & $100B IPO",
        "start": 567.20,
        "end": 671.68,
        "v1_broll": "scene6_01_empty_airport.mp4",
        "v1_broll_2": "scene6_02_wall_street_ticker.mp4",
        "v1_archive": "nasdaq_times_square_billboards.jpg",
        "v3_anchor": "CHART_AIRBNB_REVENUE_GROWTH.png",
        "v4_text": "MARCH 2020: 80% CRASH ($1B REFUNDS) // DEC 2020: $100B NASDAQ IPO",
        "sfx": ("sfx_sub_boom.wav", 568.00, -12.0)
    },
    {
        "id": 7,
        "name": "Scene 07: Corporate Greed & City Bans",
        "start": 671.68,
        "end": 884.08,
        "v1_broll": "scene7_01_house_chores.mp4",
        "v1_broll_2": "scene7_02_city_protest.mp4",
        "v1_archive": "barcelona_housing_protest.jpg",
        "v3_anchor": None,
        "v4_text": "2023-2024: $180 CLEANING FEE + CHORES // NYC & BARCELONA BAN LISTINGS",
        "sfx": ("sfx_sub_boom.wav", 672.00, -12.0)
    },
    {
        "id": 8,
        "name": "Scene 08: 3 Entrepreneur Rules & Outro",
        "start": 884.08,
        "end": 1046.00,
        "v1_broll": "scene8_01_boutique_hotel.mp4",
        "v1_broll_2": "scene8_02_luggage_journey.mp4",
        "v1_archive": "nasdaq_stock_market.jpg",
        "v3_anchor": "CHART_AIRBNB_REVENUE_GROWTH.png",
        "v4_text": "THE PLAYBOOK: 1. BORROW DISTRIBUTION // 2. ANSWER IS IN KITCHEN // 3. KEEP THE SOUL",
        "sfx": ("sfx_whoosh.wav", 885.00, -16.0)
    }
]

total_dur = TIMELINE_CUES[-1]["end"]

def generate_fcpxml():
    root = ET.Element("fcpxml", version="1.8")
    resources = ET.SubElement(root, "resources")

    # Format resource
    ET.SubElement(resources, "format", id="r1", name="FFVideoFormat1080p30", frameDuration=FRAME_DUR, width="1920", height="1080")

    # Audio Master resource (A1 Dialogue)
    voice_path = os.path.join(AUDIO_DIR, "voice_mastered.wav").replace("\\", "/")
    ET.SubElement(resources, "asset", id="r_audio", name="voice_mastered", src=f"file:///{voice_path}", duration=f"{sec_to_frames(total_dur)}/{FPS}s", hasAudio="1")

    # Ambient BGM resource (A2 Bed)
    bgm_path = os.path.join(AUDIO_DIR, "ambient_bed_track.wav").replace("\\", "/")
    ET.SubElement(resources, "asset", id="r_bgm", name="ambient_bed_track", src=f"file:///{bgm_path}", duration=f"{sec_to_frames(total_dur)}/{FPS}s", hasAudio="1")

    # SFX resources
    sfx_files = ["sfx_sub_boom.wav", "sfx_whoosh.wav", "sfx_data_blip.wav"]
    for idx, sfx in enumerate(sfx_files):
        s_id = f"r_sfx_{idx}"
        p = os.path.join(SFX_DIR, sfx).replace("\\", "/")
        ET.SubElement(resources, "asset", id=s_id, name=sfx, src=f"file:///{p}", hasAudio="1")

    library = ET.SubElement(root, "library")
    event = ET.SubElement(library, "event", name="ThinkLate_Video05_Event")
    project = ET.SubElement(event, "project", name="ThinkLate_Video05_How_Airbnb_Stole_100B")

    sequence = ET.SubElement(project, "sequence", format="r1", duration=f"{sec_to_frames(total_dur)}/{FPS}s")
    spine = ET.SubElement(sequence, "spine")

    # Master timeline primary spine (V1 / V3 base)
    for cue in TIMELINE_CUES:
        st = cue["start"]
        et = cue["end"]
        dur_sec = et - st
        dur_frames = sec_to_frames(dur_sec)
        offset_frames = sec_to_frames(st)

        clip_name = cue["v3_anchor"] if cue["v3_anchor"] else cue["v1_broll"]
        asset_node = ET.SubElement(spine, "clip", name=clip_name, offset=f"{offset_frames}/{FPS}s", duration=f"{dur_frames}/{FPS}s", start="0/1s")

        # Markers for blur & text
        ET.SubElement(asset_node, "marker", start="0/1s", duration=f"{dur_frames}/{FPS}s", value=f"V2_SCOPED_BLUR: Active under text")
        if cue["v4_text"]:
            ET.SubElement(asset_node, "marker", start="10/30s", duration=f"{max(dur_frames - 20, 10)}/{FPS}s", value=f"V4_TEXT: {cue['v4_text']}")
        if cue["sfx"]:
            sfx_name, sfx_time, sfx_vol = cue["sfx"]
            ET.SubElement(asset_node, "marker", start="0/1s", duration="1/1s", value=f"SFX: {sfx_name} (vol {sfx_vol}dB)")

    # Prettify XML
    xml_str = ET.tostring(root, encoding="utf-8")
    parsed = minidom.parseString(xml_str)
    pretty_xml = parsed.toprettyxml(indent="  ")

    with open(FCPXML_OUT, "w", encoding="utf-8") as f:
        f.write(pretty_xml)
    print(f"✅ Generated DaVinci FCPXML: {FCPXML_OUT}")

def generate_edl():
    lines = [
        "TITLE: ThinkLate_Video05_How_Airbnb_Stole_100B",
        "FCM: NON-DROP FRAME",
        ""
    ]

    for cue in TIMELINE_CUES:
        st_tc = sec_to_timecode(cue["start"], FPS)
        et_tc = sec_to_timecode(cue["end"], FPS)
        dur_tc = sec_to_timecode(cue["end"] - cue["start"], FPS)

        reel = f"AX{cue['id']:02d}"
        clip_name = cue["v3_anchor"] if cue["v3_anchor"] else cue["v1_broll"]
        lines.append(f"{cue['id']:03d}  {reel}       V     C        00:00:00:00 {dur_tc} {st_tc} {et_tc}")
        lines.append(f"* FROM CLIP NAME: {clip_name}")
        lines.append(f"* COMMENT: SCENE = {cue['name']}")
        if cue["v4_text"]:
            lines.append(f"* COMMENT: V4 TEXT OVERLAY = {cue['v4_text']}")
        if cue["sfx"]:
            lines.append(f"* COMMENT: SFX CUE = {cue['sfx'][0]} at {cue['sfx'][1]}s ({cue['sfx'][2]}dB)")
        lines.append("")

    with open(EDL_OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"✅ Generated CMX 3600 EDL: {EDL_OUT}")

def main():
    print(f"🎬 Compiling DaVinci Resolve Timeline for Video 05 ({total_dur:.2f}s | {total_dur/60:.2f} min)...")
    generate_fcpxml()
    generate_edl()
    print("\n🎉 DaVinci Resolve Timeline Package ready for 1-click import into DaVinci Resolve Studio!")

if __name__ == "__main__":
    main()
