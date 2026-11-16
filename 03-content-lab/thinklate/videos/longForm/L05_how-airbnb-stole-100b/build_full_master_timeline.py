"""
ThinkLate Video 05: Master Full 15m 56s Video Assembly Engine
Multi-Track Visual Stacking Standard:
- Track 1 (V1): Living Gameplay Canvas Spine (Continuous 60fps high-retention movement)
- Track 2 (V2): Atmospheric Tone & Selective Blur (0.16 boxblur when evidence cards trigger)
- Track 3 (V3): Documentary B-roll / Real Founder Archival Plates (Wikimedia Commons verified, rock-solid dead-steady)
- Track 4 (V4): Transparent Alpha WebM Remotion Motion Cards + Dynamic Center-Screen Progressive Typography
- Master Audio: Approved +15% Voiceover Master (George Act 1 + Andrew Acts 2-8) with -1.0 dB vocal peak and -26 dB BGM with 1.5kHz pocket.
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
os.makedirs(CACHE_DIR, exist_ok=True)

CREATE_NO_WINDOW = 0x08000000

AUDIO_SRC = os.path.join(AUDIO_DIR, "dual_full_mix_preview_plus15.wav")
TOTAL_DURATION = 956.83 # 15m 56.83s

# Load Whisper segments
with open(os.path.join(BASE_DIR, "transcription_timestamps.json"), "r", encoding="utf-8") as f:
    WHISPER_SEGS = json.load(f)

# Action clips bank for living canvas spine
ACTION_CLIPS = [os.path.join(ACTION_DIR, f) for f in sorted(os.listdir(ACTION_DIR)) if f.endswith(".mp4")]

# Documentary broll bank
DOC_CLIPS = [os.path.join(DOC_DIR, f) for f in sorted(os.listdir(DOC_DIR)) if f.endswith(".mp4")]

# 12 Transparent Remotion Motion Cards mapping to story chapters
MOTION_CARDS_MAP = [
    (0.4, 4.4, "card_01_evidence_eviction.webm", "Eviction Notice"),
    (5.0, 8.0, "card_02_typography_slam_hook.webm", "Hook Typography Slam"),
    (75.0, 79.0, "card_03_comparison_hotel_vs_airbed.webm", "Hotel vs Airbed Spread"),
    (220.0, 224.0, "card_04_metric_cereal_capital.webm", "Cereal Box Capital Counter"),
    (290.0, 294.0, "card_05_headline_angel_rejection.webm", "Angel Rejection Headline"),
    (340.0, 344.0, "card_06_citation_paulg.webm", "Paul Graham Citation"),
    (430.0, 434.0, "card_07_redaction_vc_pass.webm", "Redacted VC Exhibit"),
    (490.0, 493.0, "card_08_glitch_cartel.webm", "Glitch Decoded Cartel"),
    (620.0, 624.0, "card_09_barchart_multiples.webm", "Valuation Multiples Bar Chart"),
    (710.0, 714.0, "card_10_linechart_ipo_spike.webm", "$100B IPO Spike Curve"),
    (810.0, 814.0, "card_11_receipt_junk_fees.webm", "Torn Paper Junk Fee Receipt"),
    (910.0, 913.0, "card_12_highlighter_rules.webm", "Highlighter Climax Wipe")
]

print("Master Video Assembly Pipeline configured.")
print(f"Total Duration: {TOTAL_DURATION}s | Segments: {len(WHISPER_SEGS)} | Transparent Motion Cards: {len(MOTION_CARDS_MAP)}")

