#!/usr/bin/env python3
"""
Build Master DaVinci Timeline Guide for Video 05 using Whisper Ground Truth
"""

import json
import os

VIDEO_DIR = os.path.dirname(os.path.abspath(__file__))
TRANS_JSON = os.path.join(VIDEO_DIR, "transcription_timestamps.json")
OUT_MD = os.path.join(VIDEO_DIR, "MASTER_DAVINCI_TIMELINE_GUIDE.md")

with open(TRANS_JSON, "r", encoding="utf-8") as f:
    segments = json.load(f)

# Scene breakdown mapping to Whisper segments
scenes = [
    {
        "id": 1,
        "title": "Cold Open: The Three-Day Vision",
        "start_seg": 1,
        "end_seg": 10,
        "anchor": "thumbnail_option_a.jpg",
        "broll": "Documentary Stock: Dilapidated San Francisco apartment exterior + Target receipt",
        "text_slam": "OCTOBER 2007: $1,150 OVERDUE RENT // 3 AIR MATTRESSES ON THE FLOOR",
        "sfx": "A4: Wooden door knock (-16dB) at 00:00 -> A4: Paper eviction rip (-18dB) at 00:08 -> A3: Sub-bass drop (-12dB) at 00:55"
    },
    {
        "id": 2,
        "title": "The $20,000 Debt Trap & The Cereal Stunt",
        "start_seg": 11,
        "end_seg": 28,
        "anchor": "anchor_01_cereal_heist.jpg",
        "broll": "Archival photo of maxed-out credit card binders + DNC Denver 2008 crowd",
        "text_slam": "SUMMER 2008: $20,000 CREDIT DEBT // 1,000 BOXES AT $40 = $30,000 CASH",
        "sfx": "A4: Credit card decline beep (-16dB) at 01:25 -> A4: Cereal rattle (-18dB) at 02:00 -> A3: Sub-bass impact (-12dB) at 02:35"
    },
    {
        "id": 3,
        "title": "The Y Combinator Cereal Pitch",
        "start_seg": 29,
        "end_seg": 39,
        "anchor": "anchor_02_paul_graham_pitch.jpg",
        "broll": "Archival Paul Graham Y Combinator 2009 boardroom + flatline revenue chart",
        "text_slam": "JANUARY 2009: PAUL GRAHAM PITCH // IF YOU CAN SELL $4 CEREAL FOR $40, YOU'RE IN",
        "sfx": "A4: Backpack zipper slide (-18dB) at 02:55 -> A4: Stamp slamming APPROVED (-16dB) at 03:20 -> A4: Heart monitor flatline (-18dB) at 03:37"
    },
    {
        "id": 4,
        "title": "The Ground War: Knocking on Doors in New York",
        "start_seg": 40,
        "end_seg": 51,
        "anchor": "anchor_03_nyc_photography_war.jpg",
        "broll": "Documentary Brooklyn street walk + side-by-side flip-phone vs DSLR interior comparison",
        "text_slam": "SUMMER 2009: DO THINGS THAT DON'T SCALE // FREE $500 DSLR PHOTOS 3X BOOKINGS",
        "sfx": "A4: Subway train screech (-18dB) at 03:40 -> A4: Knuckles knocking on door (-16dB) at 03:52 -> A4: Camera shutter burst (-16dB) at 04:30"
    },
    {
        "id": 5,
        "title": "The Craigslist Growth Hack",
        "start_seg": 52,
        "end_seg": 63,
        "anchor": "anchor_04_craigslist_bot.jpg",
        "broll": "CRT terminal green python code + Craigslist 2010 interface overlay",
        "text_slam": "2010: THE CRAIGSLIST HIJACK // REVERSE-ENGINEERED FORMS = 50M USERS FOR $0",
        "sfx": "A4: Mechanical keyboard clatter (-18dB) at 04:45 -> A4: Resonant mouse click (-16dB) at 05:15 -> A3: Rocket rumble cut (-12dB) at 05:40"
    },
    {
        "id": 6,
        "title": "The COVID Near-Death & The $100B IPO",
        "start_seg": 64,
        "end_seg": 77,
        "anchor": "anchor_05_covid_crash_ipo.jpg",
        "broll": "March 2020 empty airport departure boards + NASDAQ opening bell ceremony December 2020",
        "text_slam": "MARCH 2020: 80% BOOKING CRASH ($1B REFUNDS) // DEC 2020: $100B NASDAQ IPO",
        "sfx": "A4: Airport PA chime (-18dB) at 05:50 -> A3: Stock sell-off alarm (-12dB) at 06:10 -> A4: NASDAQ bell ringing (-16dB) at 07:05"
    },
    {
        "id": 7,
        "title": "The Backlash: $300 Chore Fees & City Bans",
        "start_seg": 78,
        "end_seg": 92,
        "anchor": "anchor_06_chore_fee_backlash.jpg",
        "broll": "Laminated host chore checklist + NYC Local Law 18 protest + Barcelona street march",
        "text_slam": "2023-2024: $180 CLEANING FEE + CHORES // NYC & BARCELONA ELIMINATE LISTINGS",
        "sfx": "A4: Cash register ring (-16dB) at 07:35 -> A3: Sub-bass dead-air drop (-12dB) at 08:05 -> A4: Street protest chants (-20dB) at 08:35"
    },
    {
        "id": 8,
        "title": "The Re-Invention: Fixing Mistakes & Pivoting to Hotels",
        "start_seg": 93,
        "end_seg": 107,
        "anchor": "anchor_07_chesky_reinvention.jpg",
        "broll": "Brian Chesky 2025/2026 keynote demo + slow camera pull-back to 2007 air mattress",
        "text_slam": "2026 REALITY: $12.2B REVENUE // THE ULTIMATE IRONY: PIVOTING TO BOUTIQUE HOTELS",
        "sfx": "A4: Keynote slide click (-18dB) at 09:05 -> A2: Warm synth fade-in at 09:40 -> A3: Final cinematic sub-bass impact at 10:00"
    }
]

lines = [
    "# ThinkLate Video 05 — Master DaVinci Resolve Timeline Guide",
    "",
    "> **Episode:** *\"How An $80 Airbed Stole An Entire Industry\"* (`05_how-airbnb-stole-100b`)  ",
    "> **Channel:** ThinkLate (`@wethinklate`) | **Runtime:** 10m 01s  ",
    "> **Master Audio:** `audio_takes/voice_mastered.wav` (48kHz 24-bit PCM | -16.6 LUFS)  ",
    "> **Whisper Ground Truth:** `transcription_timestamps.json` (107 segments)  ",
    "",
    "---",
    "",
    "## 🎛️ 1. DaVinci Resolve 4-Track Audio & Video Architecture",
    "",
    "```",
    "┌────────────────────────────────────────────────────────────────────────┐",
    "│ VIDEO TRACK 4 (V4): Kinetic Typography Slams (DaVinci Text+) & Badges  │",
    "├────────────────────────────────────────────────────────────────────────┤",
    "│ VIDEO TRACK 3 (V3): 16:9 Cinematic Graphic Noir Anchor Plates (3% Push)│",
    "├────────────────────────────────────────────────────────────────────────┤",
    "│ VIDEO TRACK 2 (V2): Scoped Gaussian Blur (0.15) & 35mm Film Grain (8%) │",
    "├────────────────────────────────────────────────────────────────────────┤",
    "│ VIDEO TRACK 1 (V1): 1080p Documentary Stock Footage / Historical B-Roll│",
    "└────────────────────────────────────────────────────────────────────────┘",
    "",
    "┌────────────────────────────────────────────────────────────────────────┐",
    "│ AUDIO TRACK 1 (A1): Master Dialogue Voiceover [FADER: -5.0 dB]         │",
    "├────────────────────────────────────────────────────────────────────────┤",
    "│ AUDIO TRACK 2 (A2): Cinematic Ambient BGM Bed [FADER: -23.0 dB]        │",
    "├────────────────────────────────────────────────────────────────────────┤",
    "│ AUDIO TRACK 3 (A3): Sub-Bass Impact Booms & Dead-Air Slams [-12.0 dB]  │",
    "├────────────────────────────────────────────────────────────────────────┤",
    "│ AUDIO TRACK 4 (A4): Diegetic Foley Soundscapes & Clicks [-16.0 dB]     │",
    "└────────────────────────────────────────────────────────────────────────┘",
    "```",
    "",
    "---",
    "",
    "## 🎬 2. Master Spoken Timeline Schedule (Whisper Ground Truth)",
    "",
    "| Scene | Timecode Range | Narrative Arc & Spoken Segment Range | Video Track 1 & 3 Assets | Video Track 4 Kinetic Typography Copy | Audio Track & Exact SFX Cue |",
    "| :---: | :--- | :--- | :--- | :--- | :--- |"
]

for sc in scenes:
    s_seg = segments[sc["start_seg"] - 1]
    e_seg = segments[sc["end_seg"] - 1]
    tc_start = f"{int(s_seg['start']//60):02d}:{int(s_seg['start']%60):02d}"
    tc_end   = f"{int(e_seg['end']//60):02d}:{int(e_seg['end']%60):02d}"
    lines.append(
        f"| **{sc['id']:02d}** | `{tc_start} – {tc_end}` | **{sc['title']}**<br>*(Segments #{sc['start_seg']}–{sc['end_seg']})* | "
        f"**V3:** `{sc['anchor']}` *(3% Push)*<br>**V1:** {sc['broll']} | "
        f"**V4:** `{sc['text_slam']}` | "
        f"{sc['sfx']} |"
    )

with open(OUT_MD, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Generated: {OUT_MD}")
