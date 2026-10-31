"""
Updated Master Timeline Cues for ThinkLate Video 04 (400.12s ElevenLabs Master Audio)
Maps all 39 narrative cues strictly to Whisper speech timestamps.
Replaces all legacy gameplay with curated 1080p Documentary B-Roll footage.
"""

import os
import json

SCRIPT_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\04_the-subscription-trap"
TIMESTAMPS_FILE = os.path.join(SCRIPT_DIR, "transcription_timestamps.json")

with open(TIMESTAMPS_FILE, "r", encoding="utf-8") as f:
    segments = json.load(f)

total_dur = segments[-1]["end"]

# 39 Cues:
# (cue_id, start_sec, end_sec, v1_broll, v2_blur, v3_anchor, v4_card, sfx_cue)
CUES_DEF = [
    # --- ACT 1: THE FROSTED COCKPIT (0:00 - 56.28) ---
    (1,   0.00,  10.24, "broll_01_bmw_car.mp4",        True,  None,                             "card_cue01_60k_car.png",          ("sfx_whoosh.wav", 0.0, 0.40)),
    (2,  10.24,  18.44, "broll_02_car_driving.mp4",    True,  None,                             "card_cue02_global_rollout.png",   None),
    (3,  18.44,  27.08, "broll_01_bmw_car.mp4",        False, "anchor_01_frosted_dashboard.jpg", None,                             ("sfx_data_blip.wav", 20.0, 0.35)),
    (4,  27.08,  32.88, "broll_02_car_driving.mp4",    True,  None,                             "card_cue04_bolted_factory.png",   ("sfx_sub_boom.wav", 27.08, 0.55)),
    (5,  32.88,  37.08, "broll_01_bmw_car.mp4",        True,  None,                             "card_cue05_cloud_lock.png",       ("sfx_data_blip.wav", 33.0, 0.35)),
    (6,  37.08,  43.12, "broll_02_car_driving.mp4",    True,  None,                             "card_cue06_hostage_seat.png",     ("sfx_sub_boom.wav", 37.08, 0.55)),
    (7,  43.12,  47.64, "broll_01_bmw_car.mp4",        False, None,                             None,                              None),
    (8,  47.64,  56.28, "broll_02_car_driving.mp4",    True,  None,                             "card_cue08_not_a_prank.png",      ("sfx_sub_boom.wav", 47.64, 0.50)),

    # --- ACT 2: THE PRINTER AUDIT (56.28 - 124.40) ---
    (9,   56.28,  64.12, "broll_03_hp_printer.mp4",    False, "anchor_02_hp_printer_kill.jpg",  None,                              ("sfx_whoosh.wav", 56.5, 0.40)),
    (10,  64.12,  75.64, "broll_04_office_corp.mp4",   True,  None,                             "card_cue10_overnight_brick.png",  ("sfx_data_blip.wav", 65.0, 0.35)),
    (11,  75.64,  82.36, "broll_03_hp_printer.mp4",    True,  None,                             "card_cue11_audits_ink.png",       ("sfx_sub_boom.wav", 76.0, 0.50)),
    (12,  82.36,  91.24, "broll_04_office_corp.mp4",   True,  None,                             "card_cue12_fine_penalty.png",     ("sfx_whoosh.wav", 83.0, 0.40)),
    (13,  91.24, 100.72, "broll_03_hp_printer.mp4",    False, "evidence_hp_ceo_quote.jpg",     None,                              ("sfx_data_blip.wav", 92.0, 0.35)),
    (14, 100.72, 112.68, "broll_04_office_corp.mp4",   True,  None,                             "card_cue14_hp_investment.png",    ("sfx_sub_boom.wav", 102.0, 0.50)),
    (15, 112.68, 118.16, "broll_03_hp_printer.mp4",    True,  None,                             "card_cue15_cheap_ink_target.png", None),
    (16, 118.16, 124.40, "broll_04_office_corp.mp4",   True,  None,                             "card_cue16_cold_seat_tractor.png",("sfx_sub_boom.wav", 119.0, 0.50)),

    # --- ACT 3: THE NEBRASKA HARVEST & UKRAINIAN FIRMWARE (124.40 - 186.56) ---
    (17, 124.40, 136.52, "broll_05_nebraska_tractor.mp4",False,"anchor_03_nebraska_combine.jpg", "card_cue17_nebraska_testimony.png", ("sfx_whoosh.wav", 125.0, 0.40)),
    (18, 136.52, 148.52, "broll_06_farm_combine.mp4",    True, None,                             "card_cue18_john_deere_trip.png",   ("sfx_data_blip.wav", 138.0, 0.35)),
    (19, 148.52, 154.60, "broll_05_nebraska_tractor.mp4",True, None,                             "card_cue19_whose_tractor.png",     None),
    (20, 154.60, 165.08, "broll_07_hacker_firmware.mp4", False,"hacker_noir_plate.jpg",          None,                                ("sfx_whoosh.wav", 155.0, 0.40)),
    (21, 165.08, 177.60, "broll_08_diagnostic_code.mp4", True, None,                             "card_cue21_copyright_weapon.png",  ("sfx_sub_boom.wav", 166.0, 0.50)),
    (22, 177.60, 186.56, "broll_07_hacker_firmware.mp4", True, None,                             "card_cue22_spreadsheet_villain.png",("sfx_sub_boom.wav", 178.0, 0.50)),

    # --- ACT 4: THE SAAS MULTIPLIER (186.56 - 252.52) ---
    (23, 186.56, 201.60, "broll_09_wall_street_finance.mp4",False,"CHART_VALUATION_MULTIPLIER_animated.mp4", None,                  ("sfx_data_blip.wav", 188.0, 0.35)),
    (24, 201.60, 214.84, "broll_10_server_room.mp4",         False,"CHART_VALUATION_MULTIPLIER_animated.mp4", None,                  ("sfx_sub_boom.wav", 202.0, 0.55)),
    (25, 214.84, 228.00, "broll_09_wall_street_finance.mp4",True, None,                             "card_cue25_cannot_leave.png",     ("sfx_sub_boom.wav", 216.0, 0.50)),
    (26, 228.00, 240.00, "broll_10_server_room.mp4",         True, None,                             "card_cue26_valuation_surge.png",  ("sfx_data_blip.wav", 230.0, 0.35)),
    (27, 240.00, 252.52, "broll_09_wall_street_finance.mp4",True, None,                             "card_cue27_ceo_scoreboard.png",   None),

    # --- ACT 5: THE PHOEBUS CARTEL (252.52 - 314.80) ---
    (28, 252.52, 270.88, "broll_11_tungsten_bulb.mp4",   False, "anchor_05_geneva_cartel_1924.jpg",None,                              ("sfx_whoosh.wav", 253.0, 0.40)),
    (29, 270.88, 280.00, "broll_11_tungsten_bulb.mp4",   True,  None,                             "card_cue29_secret_pact.png",      ("sfx_sub_boom.wav", 272.0, 0.50)),
    (30, 280.00, 290.60, "broll_11_tungsten_bulb.mp4",   False, "centennial_light_1901.jpg",      "card_cue30_livermore_bulb.png",   ("sfx_data_blip.wav", 282.0, 0.35)),
    (31, 290.60, 302.00, "broll_11_tungsten_bulb.mp4",   True,  None,                             "card_cue31_phoebus_limit.png",    ("sfx_sub_boom.wav", 292.0, 0.50)),
    (32, 302.00, 314.80, "broll_11_tungsten_bulb.mp4",   True,  None,                             "card_cue32_same_incentive.png",   ("sfx_whoosh.wav", 303.0, 0.40)),

    # --- ACT 6: THE SMARTPHONE PADLOCK & THE TAKEAWAY (314.80 - 400.12) ---
    (33, 314.80, 331.48, "broll_12_delivery_rider.mp4",  False, "anchor_06_phone_lock_delivery.jpg",None,                              ("sfx_whoosh.wav", 315.0, 0.40)),
    (34, 331.48, 344.00, "broll_13_phone_lock.mp4",      True,  None,                             "card_cue34_job_hostage.png",      ("sfx_sub_boom.wav", 332.0, 0.55)),
    (35, 344.00, 355.00, "broll_13_phone_lock.mp4",      True,  None,                             "card_cue35_ftc_lawsuit.png",       ("sfx_data_blip.wav", 346.0, 0.35)),
    (36, 355.00, 365.00, "broll_01_bmw_car.mp4",         True,  None,                             "card_cue36_bmw_drops_rent.png",   ("sfx_whoosh.wav", 355.5, 0.40)),
    (37, 365.00, 375.00, "broll_05_nebraska_tractor.mp4",True,  None,                             "card_cue37_repair_wins.png",      ("sfx_data_blip.wav", 366.0, 0.35)),
    (38, 375.00, 388.44, "broll_01_bmw_car.mp4",         True,  None,                             "card_cue38_one_update_lease.png", ("sfx_sub_boom.wav", 376.0, 0.50)),
    (39, 388.44, 400.12, "broll_02_car_driving.mp4",     True,  None,                             "card_cue39_holding_key.png",       ("sfx_whoosh.wav", 389.0, 0.40)),
]

print(f"Loaded {len(CUES_DEF)} cues spanning 0.00s to {total_dur:.2f}s.")
