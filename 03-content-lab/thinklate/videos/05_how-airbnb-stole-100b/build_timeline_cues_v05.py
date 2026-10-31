"""
ThinkLate Video 05: Master Timeline Cues (1046.00s Broadcast Audio)
Mapped strictly to Whisper speech timestamps.
Continuous High-Action Living Gameplay Canvas (Assassin's Creed Black Flag: naval combat, pirating, broadside cannons).
Scoped Blur + Kinetic Typography & Evidence Badges (Track 4).
Audio: Completely muted game audio (-an); Andrew 90% + BGM 30% + J-Cut SFX.
"""

import os
import json

SCRIPT_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b"
TIMESTAMPS_FILE = os.path.join(SCRIPT_DIR, "transcription_timestamps.json")

with open(TIMESTAMPS_FILE, "r", encoding="utf-8") as f:
    segments = json.load(f)

total_dur = segments[-1]["end"]

# Cue format:
# (cue_id, start_sec, end_sec, v1_broll, v2_blur, v4_card, sfx_cue)

CUES_DEF = [
    # =========================================================================
    # ACT 1: THE THREE-DAY COUNTDOWN & THE AIRBED (0:00 - 164.16)
    # =========================================================================
    ( 1,   0.00,   6.32, "action_01_sea_sailing.mp4",        True,  "card_cue01_overdue_rent.png",          ("sfx_whoosh.wav", 0.0, 0.40)),
    ( 2,   6.32,  12.56, "action_02_naval_patrol.mp4",       True,  "card_cue02_broke_founders.png",        ("sfx_data_blip.wav", 6.5, 0.35)),
    ( 3,  12.56,  23.04, "action_03_ocean_waves.mp4",        False, None,                                   None),
    ( 4,  23.04,  33.12, "action_04_fleet_approach.mp4",     True,  "card_cue03_hotels_sold_out.png",       ("sfx_sub_boom.wav", 23.1, 0.50)),
    ( 5,  33.12,  50.72, "action_07_broadside_run.mp4",      True,  "card_cue04_the_airbed_hustle.png",     ("sfx_whoosh.wav", 33.2, 0.40)),
    ( 6,  50.72,  56.72, "action_08_cannon_barrage.mp4",     True,  "card_cue05_empire_transformation.png", ("sfx_sub_boom.wav", 50.8, 0.55)),
    ( 7,  56.72,  74.96, "action_05_naval_maneuver.mp4",     True,  "card_cue06_solo_blueprint.png",        ("sfx_whoosh.wav", 57.0, 0.40)),
    ( 8,  74.96,  87.44, "action_06_combat_ready.mp4",       True,  "card_cue07_rent_paid_cash.png",        ("sfx_data_blip.wav", 75.2, 0.35)),
    ( 9,  87.44,  98.88, "action_09_ship_chase.mp4",         True,  "card_cue08_the_lightbulb.png",         ("sfx_whoosh.wav", 88.0, 0.40)),
    (10,  98.88, 110.40, "action_10_boarding_prep.mp4",      True,  "card_cue09_no_code_problem.png",       ("sfx_sub_boom.wav", 99.0, 0.50)),
    (11, 110.40, 122.40, "action_11_high_seas_piracy.mp4",   True,  "card_cue10_airbed_launch.png",         ("sfx_whoosh.wav", 110.5, 0.40)),
    (12, 122.40, 139.84, "action_12_deck_combat.mp4",        False, None,                                   None),
    (13, 139.84, 164.16, "action_13_sunny_caribbean.mp4",    False, None,                                   ("sfx_data_blip.wav", 140.0, 0.35)),

    # =========================================================================
    # ACT 2: THE $20,000 DEBT TRAP & THE CEREAL STUNT (164.16 - 254.00)
    # =========================================================================
    (14, 164.16, 182.24, "action_14_island_raid.mp4",        True,  "card_cue11_twenty_k_debt.png",         ("sfx_sub_boom.wav", 164.5, 0.55)),
    (15, 182.24, 212.56, "action_15_storm_sailing.mp4",      False, None,                                   None),
    (16, 212.56, 235.00, "action_16_final_broadside.mp4",    True,  "card_cue12_cereal_arbitrage.png",      ("sfx_whoosh.wav", 212.8, 0.40)),
    (17, 235.00, 254.00, "blackflag_jackdaw_broadside_fire_v55.mp4", False, None,                            ("sfx_sub_boom.wav", 235.5, 0.50)),

    # =========================================================================
    # ACT 3: THE Y COMBINATOR CRUCIBLE (254.00 - 350.40)
    # =========================================================================
    (18, 254.00, 280.00, "action_01_sea_sailing.mp4",        True,  "card_cue13_paul_graham_quote.png",     ("sfx_whoosh.wav", 254.5, 0.40)),
    (19, 280.00, 310.00, "action_02_naval_patrol.mp4",       False, None,                                   None),
    (20, 310.00, 325.00, "action_03_ocean_waves.mp4",        False, None,                                   ("sfx_data_blip.wav", 310.5, 0.35)),
    (21, 325.00, 350.40, "action_04_fleet_approach.mp4",     True,  "card_cue14_trough_of_sorrow.png",      ("sfx_sub_boom.wav", 325.5, 0.50)),

    # =========================================================================
    # ACT 4: THE BROOKLYN GROUND WAR (350.40 - 438.40)
    # =========================================================================
    (22, 350.40, 361.04, "action_05_naval_maneuver.mp4",     True,  "card_cue15_dont_scale.png",            ("sfx_whoosh.wav", 350.8, 0.40)),
    (23, 361.04, 400.00, "action_06_combat_ready.mp4",       True,  "card_cue16_brooklyn_photos.png",       ("sfx_data_blip.wav", 361.5, 0.35)),
    (24, 400.00, 420.00, "action_07_broadside_run.mp4",      False, None,                                   None),
    (25, 420.00, 438.40, "action_08_cannon_barrage.mp4",     False, None,                                   ("sfx_sub_boom.wav", 420.5, 0.50)),

    # =========================================================================
    # ACT 5: THE CRAIGSLIST HIJACK & VALUATION (438.40 - 547.12)
    # =========================================================================
    (26, 438.40, 475.00, "action_09_ship_chase.mp4",         True,  "card_cue17_craigslist_hijack.png",     ("sfx_whoosh.wav", 438.8, 0.40)),
    (27, 475.00, 500.00, "action_10_boarding_prep.mp4",      False, None,                                   None),
    (28, 500.00, 520.00, "action_11_high_seas_piracy.mp4",   False, None,                                   ("sfx_data_blip.wav", 500.5, 0.35)),
    (29, 520.00, 547.12, "action_12_deck_combat.mp4",        True,  "card_cue18_valuation_multiplier.png",  ("sfx_sub_boom.wav", 520.5, 0.50)),

    # =========================================================================
    # ACT 6: COVID CRASH & THE $100B IPO (547.12 - 701.76)
    # =========================================================================
    (30, 547.12, 580.00, "action_15_storm_sailing.mp4",      True,  "card_cue19_covid_collapse.png",        ("sfx_sub_boom.wav", 547.5, 0.55)),
    (31, 580.00, 605.00, "blackflag_naval_night_combat_v36.mp4", False, None,                                None),
    (32, 605.00, 629.28, "action_13_sunny_caribbean.mp4",    False, None,                                   ("sfx_whoosh.wav", 605.5, 0.40)),
    (33, 629.28, 670.00, "action_14_island_raid.mp4",        True,  "card_cue20_nasdaq_ipo.png",            ("sfx_sub_boom.wav", 629.8, 0.55)),
    (34, 670.00, 701.76, "action_16_final_broadside.mp4",    False, None,                                   None),

    # =========================================================================
    # ACT 7: THE $180 CLEANING FEE TAX & CITY BANS (701.76 - 878.96)
    # =========================================================================
    (35, 701.76, 735.00, "action_01_sea_sailing.mp4",        True,  "card_cue21_cleaning_fee_tax.png",      ("sfx_whoosh.wav", 702.0, 0.40)),
    (36, 735.00, 768.96, "action_02_naval_patrol.mp4",       False, None,                                   None),
    (37, 768.96, 805.00, "action_03_ocean_waves.mp4",        True,  "card_cue22_city_bans.png",             ("sfx_sub_boom.wav", 769.5, 0.50)),
    (38, 805.00, 840.00, "action_04_fleet_approach.mp4",     False, None,                                   None),
    (39, 840.00, 878.96, "action_05_naval_maneuver.mp4",     False, None,                                   ("sfx_data_blip.wav", 840.5, 0.35)),

    # =========================================================================
    # ACT 8: THE SOLO-FOUNDER PLAYBOOK & THE VERDICT (878.96 - 1046.00)
    # =========================================================================
    (40, 878.96, 913.92, "action_06_combat_ready.mp4",       True,  "card_cue23_rule1.png",                 ("sfx_whoosh.wav", 879.5, 0.40)),
    (41, 913.92, 946.00, "action_07_broadside_run.mp4",      True,  "card_cue24_rule2.png",                 ("sfx_sub_boom.wav", 914.5, 0.50)),
    (42, 946.00, 976.00, "action_08_cannon_barrage.mp4",     True,  "card_cue25_rule3.png",                 ("sfx_whoosh.wav", 946.5, 0.40)),
    (43, 976.00, 1010.00,"action_09_ship_chase.mp4",         False, None,                                   None),
    (44,1010.00, 1040.16,"action_10_boarding_prep.mp4",       False, None,                                   ("sfx_sub_boom.wav", 1010.5, 0.50)),
    (45,1040.16, 1046.00,"action_11_high_seas_piracy.mp4",   True,  "card_cue26_stay_curious.png",          ("sfx_data_blip.wav", 1040.5, 0.35)),
]

print(f"Loaded {len(CUES_DEF)} cues spanning 0.00s to {total_dur:.2f}s.")

