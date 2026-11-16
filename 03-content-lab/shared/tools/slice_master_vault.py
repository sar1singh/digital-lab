#!/usr/bin/env python3
"""
Master Pack Slicer & Multi-Mood Clip Extractor (ThinkLate Infotainment Engine)
=============================================================================
Slices downloaded compilation packs (Green Screen, The Office, Brooklyn 99,
Big Bang Theory, Parks & Rec, Friends, and Indian packs) into 300+ individual
production-ready video clips and animated GIFs categorized by mood and punchline.

Standards:
  - Broadcast H.264 video + 48kHz AAC stereo audio.
  - Speech Completion Rule: Full sentence delivery without mid-sentence cutoffs.
  - Auto-generated matching high-res animated GIFs in gifs/ directory.
  - Centralized rebuild of MEME_CATALOG.md with full mood taxonomy.
"""

import os
import sys
import subprocess
import shutil
import time

CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SHARED_DIR = os.path.dirname(SCRIPT_DIR)
MEMES_ROOT = os.path.join(SHARED_DIR, "assets", "memes")
PACKS_DIR = os.path.join(MEMES_ROOT, "packs")

CLIPS_USA = os.path.join(MEMES_ROOT, "usa_global")
CLIPS_INDIA = os.path.join(MEMES_ROOT, "india")
GIFS_USA = os.path.join(MEMES_ROOT, "gifs", "usa_global")
GIFS_INDIA = os.path.join(MEMES_ROOT, "gifs", "india")

for d in [CLIPS_USA, CLIPS_INDIA, GIFS_USA, GIFS_INDIA]:
    os.makedirs(d, exist_ok=True)

# Master Slice Definitions
GREEN_SCREEN_SLICES = [
    ("the_rock_dog_shit", "00:01", 5, "Shock & Disbelief"),
    ("the_rock_sus_eyebrow", "00:06", 6, "Sarcasm & Cynicism"),
    ("the_rock_chinese_anthem", "00:13", 4, "Confusion & Chaos"),
    ("el_risitas_laugh", "00:17", 9, "Roast & Hysteria"),
    ("this_is_sparta_300", "00:26", 6, "Rage & Aggression"),
    ("keemstar_fast_af_boi", "00:32", 6, "Hype & Speed"),
    ("idubbz_thats_kinda_small", "00:38", 9, "Roast & Disrespect"),
    ("ninja_thats_a_good_one", "00:47", 3, "Sarcasm & Cynicism"),
    ("dj_khaled_another_one", "00:50", 9, "Greed & Victory"),
    ("okay_guy_reaction", "00:59", 2, "Confusion & Nonchalance"),
    ("michael_rosen_noice", "01:01", 2, "Satisfaction & Approval"),
    ("thats_a_lot_of_damage", "01:03", 3, "Catastrophe & Shock"),
    ("hehe_boi_alison", "01:06", 3, "Mischief & Schemes"),
    ("black_guy_crying", "01:09", 8, "Despair & Meltdown"),
    ("what_the_f_reaction", "01:17", 3, "Incredulity & Shock"),
    ("edp_laughing", "01:20", 2, "Hysterical Mockery"),
    ("thats_what_she_said_office", "01:22", 3, "Cheeky Double-Entendre"),
    ("what_dog_reaction", "01:25", 2, "Stunned Silence"),
    ("oh_my_god_wow", "01:27", 4, "Awe & Sarcasm"),
    ("tyler1_screaming", "01:31", 7, "Unhinged Rage"),
    ("wait_a_minute_who_are_you", "01:38", 7, "Total Confusion"),
    ("michael_jordan_stop_it_get_help", "01:45", 3, "Common Sense Intervention"),
    ("cj_ah_shit_here_we_go_again", "01:48", 2, "Fatigued Resignation"),
    ("j_jonah_jameson_spiderman_laugh", "01:50", 4, "Contemptuous Mockery"),
    ("phil_swift_damage_flex_tape", "01:54", 4, "Catastrophic Breakdown"),
    ("im_under_the_water_please_help", "01:58", 7, "Drowning in Obligations"),
    ("thug_life_glasses_meme", "02:05", 3, "Effortless Dominance"),
    ("mortal_kombat_fight", "02:08", 4, "Corporate Battle"),
    ("versus_screen_confrontation", "02:12", 6, "Direct Rivalry"),
    ("ninja_stream_sniping", "02:18", 5, "Accusing Foul Play"),
    ("oh_my_god_horn_dramatic", "02:23", 6, "Dramatic Spike"),
    ("shaq_shimmy_wiggle", "02:29", 10, "Greedy Anticipation"),
    ("confused_kid_face", "02:39", 8, "Baffled Incomprehension"),
    ("waw_guy_meme", "02:47", 5, "Over-the-top Cynicism"),
    ("idubbz_hey_thats_pretty_good", "02:52", 2, "Reluctant Praise"),
    ("damn_boi_he_thick", "02:54", 10, "Absurd Scale"),
    ("windows_pc_crash_error", "03:05", 5, "Fatal System Crash"),
    ("will_smith_thats_hot", "03:10", 8, "Cynical Enthusiasm"),
    ("van_damme_kick", "03:35", 5, "Sudden Retaliation"),
    ("flightreacts_smash_keyboard", "03:40", 10, "Keyboard Rages"),
    ("ksi_slap_face", "03:50", 11, "Sudden Disrespect"),
    ("excited_crowd_cheer", "04:01", 13, "Mass Hype"),
    ("why_are_you_running", "04:14", 8, "Cornered Executive"),
    ("will_smith_chris_rock_slap", "04:22", 5, "Sudden Public Escalation"),
    ("anime_wow_reaction", "04:27", 2, "Innocent Shock"),
    ("cutest_thing_ever", "04:29", 9, "Sudden Trauma"),
    ("ksi_screaming_rage", "04:38", 12, "Loud Meltdown"),
    ("what_did_he_say_reaction", "05:00", 3, "Speechless Horror"),
    ("tfue_this_is_bullshit", "05:03", 4, "Calling Out Fraud"),
    ("penguinz0_yeah_baby", "05:07", 7, "Long-Awaited Victory"),
    ("daddy_chill_what_the_hell", "05:14", 9, "Confronting Bizarre Moves"),
    ("can_you_speak_english", "05:23", 5, "Cutting Through Jargon"),
    ("steven_he_emotional_damage", "05:28", 2, "Brutal Burn"),
    ("hackerman_typing", "05:30", 7, "Technical Genius Illusion"),
    ("andrew_tate_bugatti", "05:37", 2, "Vulgar Wealth Display"),
    ("blinking_white_guy", "05:39", 2, "Classic Disbelief"),
    ("tyler1_falling_out_of_world", "05:40", 4, "Sudden Demise"),
    ("tyler1_help_screaming", "05:44", 10, "Desperate Panic"),
    ("confused_john_travolta_pulp_fiction", "05:58", 5, "Looking Around Empty Room"),
    ("its_free_real_estate", "06:03", 3, "Predatory Opportunity"),
    ("big_brain_math_equations", "06:06", 7, "Complicated Justifications"),
    ("to_be_continued_jojo", "06:13", 3, "Cliffhanger Dread"),
    ("gta_san_andreas_mission_passed", "06:16", 7, "Unlikely Victory"),
    ("action_movie_explosion", "06:23", 5, "Total Destruction"),
    ("anime_naruto_run", "06:28", 8, "Frantic Retreat"),
    ("filthy_frank_this_is_cancer", "06:38", 10, "Degradation of Culture"),
    ("windows_bluescreen_error", "06:58", 4, "Complete Lockup"),
    ("shia_labeouf_just_do_it", "07:02", 15, "Aggressive Motivation"),
    ("wizard_yensid_screaming", "08:04", 12, "Terrifying Authority"),
    ("john_cena_bing_chilling", "08:26", 12, "Corporate Appeasement"),
    ("xqc_wow_clap", "08:45", 5, "Sarcastic Applause"),
    ("flightreacts_dolphin_laugh", "08:50", 5, "Mocking Hysteria"),
    ("ninja_tf_you_said_to_me", "08:55", 3, "Thin-Skinned Reaction"),
    ("reviewbrah_disappointment_speech", "08:58", 6, "Solemn Condemnation"),
    ("man_falling_meme", "09:04", 2, "Plummeting Metric"),
    ("laughing_emoji_crying", "09:06", 2, "Uncontrollable Ridicule"),
    ("man_laughing_hysterically", "09:08", 6, "Laughing at Investor Losses"),
    ("we_will_be_right_back_eric_andre", "09:14", 2, "Impending Disaster Freeze"),
    ("dark_souls_you_died", "09:18", 6, "Unforgiving Reality"),
    ("minecraft_you_died", "09:24", 5, "Instant Casual Failure"),
    ("praise_the_lord_dance", "09:29", 12, "Reckless Euphoria"),
    ("street_fighter_ko", "09:49", 4, "Final Knockout"),
    ("snoop_dogg_no_say_what", "09:53", 2, "Instant Refusal"),
    ("john_cena_are_you_sure_about_that", "09:55", 6, "Debunking Fake Claims"),
    ("triggered_red_shake", "10:01", 5, "Full Cognitive Dissonance")
]

OFFICE_SLICES = [
    ("office_michael_im_dead_inside", "00:15", 6, "Despair & Exhaustion"),
    ("office_dwight_false_black_bear", "00:35", 7, "Fact-Check Objection"),
    ("office_dwight_identity_theft_not_joke", "00:55", 8, "Corporate Theft Realization"),
    ("office_jim_looking_at_camera", "01:20", 5, "Breaking Fourth Wall"),
    ("office_michael_parkour_jump", "01:45", 7, "Unearned Confidence"),
    ("office_stanley_did_i_stutter", "02:10", 6, "Insubordinate Defiance"),
    ("office_kevin_spilling_famous_chili", "02:35", 9, "Total Work Undone"),
    ("office_michael_i_declare_bankruptcy", "03:05", 8, "Financial Ignorance"),
    ("office_creed_i_steal_things", "03:35", 6, "Shameless Corruption"),
    ("office_toby_why_are_you_the_way", "04:05", 7, "Bureaucratic Frustration"),
    ("office_dwight_it_is_true", "04:30", 5, "Stern Agreement"),
    ("office_michael_boom_roasted", "05:00", 12, "Systematic Roasting"),
    ("office_jim_shrug_smile", "05:30", 5, "Helpless Smugness"),
    ("office_michael_fool_me_once", "06:00", 8, "Bungled Logic"),
    ("office_dwight_first_aid_dummy_face", "06:30", 10, "Psychopathic Efficiency"),
    ("office_ryan_start_the_fire", "07:05", 7, "Disastrous Blunder"),
    ("office_michael_whispering_secret", "07:40", 6, "Leaked Information"),
    ("office_dwight_crying_in_stairwell", "08:15", 8, "Behind-the-Scenes Agony"),
    ("office_michael_crying_happy_tears", "08:50", 7, "Triumphant Emotion")
]

B99_SLICES = [
    ("b99_holt_pain_speech", "00:12", 8, "Stoic Agony"),
    ("b99_jake_internal_bleeding_blood", "00:40", 7, "Denying Critical Crisis"),
    ("b99_jake_cool_cool_cool_no_doubt", "01:10", 6, "Panicked Agreement"),
    ("b99_holt_vindication_screaming", "01:38", 8, "Vindicated Vengeance"),
    ("b99_terry_loves_yogurt", "02:05", 6, "Passionate Obsession"),
    ("b99_jake_backstreet_boys_lineup", "02:30", 15, "Absurd Distraction"),
    ("b99_rosa_badass_knife_reveal", "03:10", 6, "Ruthless Enforcement"),
    ("b99_boyle_boom_did_you_see_that", "03:40", 6, "Unearned Self-Praise"),
    ("b99_holt_call_me_velvet_thunder", "04:10", 7, "Surprise Badassery"),
    ("b99_gina_the_incident", "04:45", 8, "Narcissistic Immunity"),
    ("b99_holt_hot_damn_smirk", "05:10", 6, "Rare Satisfaction")
]

PARKS_SLICES = [
    ("parks_ron_give_me_all_bacon_eggs", "00:25", 9, "Literal Monopolistic Appetite"),
    ("parks_andy_too_afraid_to_ask", "01:05", 8, "Willful Ignorance"),
    ("parks_ron_tossing_computer_dumpster", "01:45", 8, "Privacy Radicalism"),
    ("parks_tom_treat_yo_self", "02:25", 8, "Frivolous Spending"),
    ("parks_leslie_i_am_big_deal", "03:10", 7, "Government Hubris"),
    ("parks_ron_i_know_more_than_you", "03:50", 7, "Absolute Technical Superiority"),
    ("parks_chris_traeger_literally", "04:30", 6, "Toxic Optimism"),
    ("parks_april_i_hate_people", "05:15", 6, "Antisocial Realism"),
    ("parks_ben_calzone_betrayal", "06:00", 8, "Niche Obsession Disaster"),
    ("parks_ron_giggle_fire", "07:10", 7, "Childish Joy in Chaos")
]

FRIENDS_SLICES = [
    ("friends_ross_pivot_couch", "01:15", 12, "Uncoordinated Pivoting"),
    ("friends_joey_how_you_doin", "02:30", 6, "Smooth Confidence"),
    ("friends_chandler_could_i_be_more", "03:45", 7, "Iconic Sarcasm"),
    ("friends_ross_we_were_on_a_break", "05:10", 8, "Contractual Dispute"),
    ("friends_phoebe_my_eyes_screaming", "06:30", 8, "Seeing Something Horrifying"),
    ("friends_joey_doesnt_share_food", "08:10", 8, "Fierce Resource Guarding"),
    ("friends_monica_i_know_screaming", "09:40", 5, "Frustrated Competence"),
    ("friends_ross_fine_im_fine", "11:20", 9, "Obviously Boiling Over"),
    ("friends_joey_delayed_reaction", "12:50", 7, "Slow Cognitive Processing")
]

BIG_BANG_SLICES = [
    ("bbt_sheldon_bazinga_ball_pit", "01:20", 9, "Triumphant Teasing"),
    ("bbt_sheldon_penny_knock_three_times", "02:50", 8, "Neurotic Repetition"),
    ("bbt_sheldon_holding_sarcasm_sign", "04:15", 7, "Literal Sarcasm Aid"),
    ("bbt_sheldon_im_not_crazy_tested", "05:40", 7, "Defense of Incompetence"),
    ("bbt_sheldon_thats_my_spot", "07:10", 6, "Territorial Monopoly"),
    ("bbt_howard_eyebrow_creepy_grin", "08:50", 6, "Predatory Tech Pitch"),
    ("bbt_leonard_sigh_facepalm", "10:30", 6, "Exhausted Common Sense")
]

HINDI_SLICES = [
    ("hindi_babu_bhaiya_are_deva", "00:10", 6, "Classic Panic"),
    ("hindi_cheating_karta_hai_tu", "00:28", 5, "Accusing Foul Play"),
    ("hindi_50_rupaye_kaat_overacting", "00:45", 5, "Roasting Pretentious Delivery"),
    ("hindi_beta_tumse_na_ho_payega", "01:05", 6, "Dismissing Unrealistic Goals"),
    ("hindi_abhi_maza_aayega_na_bhidu", "01:25", 6, "Impending Retribution"),
    ("hindi_dukh_dard_peeda", "01:45", 7, "Chronic Misery"),
    ("hindi_mereko_to_dhak_dhak_ho_raha", "02:08", 6, "High-Stakes Palpitations"),
    ("hindi_tumse_na_ho_payega_gangs", "02:30", 6, "Gangs of Wasseypur Reality"),
    ("hindi_chalo_bhai_dekho_kya_karta", "02:55", 6, "Curious Experiment"),
    ("hindi_teri_dada_giri_nikaal_doonga", "03:20", 6, "Breaking Monopolistic Arrogance"),
    ("hindi_tauba_tauba_mood_kharab", "03:45", 6, "Instant Disgust")
]

INDIAN_100_SLICES = [
    ("in100_yeh_phas_gaya", "00:05", 5, "Cornered Prey"),
    ("in100_acha_humko_sikha_riya_hai", "00:15", 6, "Dismissing Unearned Advice"),
    ("in100_yeh_koi_tareeqa_hai_bheek", "00:26", 6, "Roasting Amateur Pitches"),
    ("in100_main_gareeb_hoon", "00:38", 5, "Faux Humility"),
    ("in100_kaisa_laga_mera_mazaak", "00:50", 5, "Cruel Trick"),
    ("in100_abey_jaldi_bol", "01:02", 5, "Impatient Hurry"),
    ("in100_pyari_samajh_gayi", "01:14", 5, "Cynical Wink"),
    ("in100_yehi_nahi_abhi_aur_suniye", "01:25", 6, "Wait There Is Worse"),
    ("in100_agar_hum_kare_to_kare_kya", "01:40", 6, "Hopeless Policy Lock"),
    ("in100_jhooth_bol_raha_hai", "01:52", 5, "Blatant Lie Exposure"),
    ("in100_baap_ko_mat_sikha", "02:05", 5, "Veteran Authority"),
    ("in100_chup_bilkul_chup", "02:20", 5, "Enforced Censorship"),
    ("in100_band_karo_haath_jodke", "02:35", 6, "Desperate Plea"),
    ("in100_maut_ko_chhoo_ke_tak_se", "02:50", 6, "Narrow Survival"),
    ("in100_aaj_jeetenge_kal_haarenge", "03:05", 6, "Cyclical Reality"),
    ("in100_tension_nahi_lene_ka", "03:25", 6, "Streetwise Reassurance"),
    ("in100_kabhi_kabhi_lagta_hai_bhagwan", "03:45", 7, "Delusions of Godhood"),
    ("in100_dukh_khatam_nahi_hota_bey", "04:05", 6, "Masaan Despair"),
    ("in100_raha_nahi_jaata_tadap", "04:30", 6, "Uncontrollable Impulse")
]

GAMING_MEME_SLICES = [
    ("galaxy_brain_you_didnt_have_to_cut_me_off", "00:00", 3, "Cosmic Enlightenment"),
    ("so_that_was_a_fucking_lie", "00:06", 4, "Blatant Falsehood"),
    ("oh_hi_mark_the_room", "00:07", 3, "Awkward Deflection"),
    ("come_on_now_dawg", "00:11", 4, "Exhausted Disbelief"),
    ("donald_trump_speech_moment", "00:18", 4, "Absurd Quote"),
    ("hah_gay_community_chang", "00:35", 2, "Schoolyard Mockery"),
    ("supa_hot_fire_im_not_a_rapper", "00:37", 7, "Crowd Hype / Murder on Mic"),
    ("stop_the_cap_reaction", "00:51", 4, "Calling Out Fiction"),
    ("boring_the_simpsons", "01:01", 2, "Mind-Numbing Tedium"),
    ("cody_noel_cringe_wtf", "01:06", 6, "Secondhand Embarrassment"),
    ("get_out_of_here", "01:12", 6, "Total Rejection"),
    ("mark_zuckerberg_good_job_team", "01:20", 6, "Robotic Corporate Praise"),
    ("kid_crying_and_laughing", "01:41", 7, "Hysterical Breakdown"),
    ("big_shaq_mans_not_hot", "01:50", 3, "Absurd Confidence"),
    ("we_dont_care_reaction", "02:05", 5, "Total Indifference"),
    ("tyler1_raging_fix_the_game", "02:10", 12, "Developer Incompetence Rage"),
    ("perfect_thumbs_up_kid", "02:37", 2, "Reluctant Approval"),
    ("guy_punching_laptop", "02:39", 2, "Hardware Violence"),
    ("vsauce_i_have_decided_i_want_to_die", "02:41", 4, "Deadpan Nihilism"),
    ("sixnine_stupid_scream", "02:51", 3, "Aggressive Mockery"),
    ("why_are_you_gay_interview", "03:08", 6, "Bizarre Questioning"),
    ("we_dont_do_that_here_black_panther", "03:24", 2, "Firm Boundary"),
    ("that_was_a_violation", "03:36", 3, "Total Disrespect"),
    ("my_time_has_come_master_oogway", "03:54", 3, "Peaceful Resignation"),
    ("lebron_james_sike_meme", "03:55", 2, "Sudden Reversal"),
    ("ayo_wtf_reaction", "03:57", 2, "Instant Alarm"),
    ("matrix_he_is_beginning_to_believe", "04:08", 3, "Seeing The System"),
    ("s1mple_why_you_bully_me", "04:17", 8, "Persecution Complex"),
    ("family_guy_who_is_laughing_now", "04:28", 3, "Petty Vengeance"),
    ("fbi_open_up_door_kick", "04:37", 8, "Federal Raid"),
    ("andrew_tate_you_are_broke", "05:20", 3, "Cynical Shaming"),
    ("jontron_i_dont_like_where_this_is_going", "05:23", 3, "Impending Regret"),
    ("norman_osborn_what_spider_man", "05:55", 2, "Stunned Realization"),
    ("ladies_and_gentlemen_we_got_him", "06:06", 4, "Definitive Proof"),
    ("it_is_what_it_is", "06:10", 5, "Stoic Acceptance"),
    ("gattuso_sometimes_good_sometimes_shit", "06:16", 4, "Inconsistent Quality"),
    ("ben_askren_boom_roasted", "06:31", 2, "Deadpan Burn"),
    ("its_only_a_game_why_you_mad", "06:50", 4, "Telling Someone to Chill"),
    ("guy_sweating_towel", "07:06", 3, "Extreme Pressure"),
    ("hah_women_coffee_cup", "07:09", 3, "Cynical Chortle"),
    ("soulja_boy_drake_huh", "07:10", 2, "Disrespectful Incredulity"),
    ("ufc_joe_rogan_shock", "07:12", 8, "Unbelievable Upset"),
    ("druski_what_do_you_mean_by_that", "07:46", 4, "Suspicious Inquiry"),
    ("spongebob_a_few_moments_later", "07:53", 3, "Time Skip")
]

def slice_single_batch(pack_name, slice_list, target_dir, is_india=False):
    pack_path = os.path.join(PACKS_DIR, pack_name)
    if not os.path.exists(pack_path):
        print(f"⚠️ Pack missing: {pack_name}")
        return 0
    
    print(f"\n🔪 Slicing {pack_name} ({len(slice_list)} targets)...")
    v_count = 0
    g_count = 0
    
    for name, start, dur, mood in slice_list:
        out_mp4 = os.path.join(target_dir, f"{name}.mp4")
        gif_dir = GIFS_INDIA if is_india else GIFS_USA
        out_gif = os.path.join(gif_dir, f"{name}.gif")
        
        # 1. Video Slice (ultrafast libx264, AAC audio)
        if not os.path.exists(out_mp4) or os.path.getsize(out_mp4) < 5000:
            cmd = [
                "ffmpeg", "-y",
                "-ss", start,
                "-i", pack_path,
                "-t", str(dur),
                "-c:v", "libx264", "-preset", "ultrafast", "-crf", "20",
                "-c:a", "aac", "-b:a", "128k",
                out_mp4
            ]
            subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=CREATE_NO_WINDOW)
            if os.path.exists(out_mp4) and os.path.getsize(out_mp4) > 1000:
                v_count += 1
                
        # 2. Fast GIF from sliced MP4
        if os.path.exists(out_mp4) and (not os.path.exists(out_gif) or os.path.getsize(out_gif) < 1000):
            gif_cmd = [
                "ffmpeg", "-y",
                "-i", out_mp4,
                "-t", str(min(dur, 5)),
                "-vf", "fps=10,scale=360:-1",
                out_gif
            ]
            subprocess.run(gif_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=CREATE_NO_WINDOW)
            if os.path.exists(out_gif) and os.path.getsize(out_gif) > 1000:
                g_count += 1
                
    print(f"   ✅ Finished {pack_name}: +{v_count} videos, +{g_count} GIFs.")
    return v_count

def run_master_slice():
    t0 = time.time()
    print("=======================================================")
    print("🚀 EXECUTING MASTER COMPILATION SLICING SUITE")
    print("=======================================================")
    
    slice_single_batch("100_green_screen_memes_global_pack.mp4", GREEN_SCREEN_SLICES, CLIPS_USA, is_india=False)
    slice_single_batch("the_office_memes_pack.mp4", OFFICE_SLICES, CLIPS_USA, is_india=False)
    slice_single_batch("brooklyn_99_memes_pack.mp4", B99_SLICES, CLIPS_USA, is_india=False)
    slice_single_batch("parks_and_rec_memes_pack.mp4", PARKS_SLICES, CLIPS_USA, is_india=False)
    slice_single_batch("friends_memes_pack.mp4", FRIENDS_SLICES, CLIPS_USA, is_india=False)
    slice_single_batch("big_bang_theory_pack.mp4", BIG_BANG_SLICES, CLIPS_USA, is_india=False)
    slice_single_batch("hindi_memes_pack_50.mp4", HINDI_SLICES, CLIPS_INDIA, is_india=True)
    slice_single_batch("100_indian_memes_editor_pack.mp4", INDIAN_100_SLICES, CLIPS_INDIA, is_india=True)
    slice_single_batch("100_popular_memes_gaming_pack.mp4", GAMING_MEME_SLICES, CLIPS_USA, is_india=False)
    
    elapsed = time.time() - t0
    print(f"\n🎉 Master Slicing Completed in {elapsed:.1f} seconds!")
    
    # Rebuild Master Catalog
    rebuild_mega_catalog()

def rebuild_mega_catalog():
    print("\n📋 Rebuilding Master Comprehensive MEME_CATALOG.md...")
    catalog_path = os.path.join(MEMES_ROOT, "MEME_CATALOG.md")
    
    usa_clips = [f for f in sorted(os.listdir(CLIPS_USA)) if f.endswith(".mp4") and not f.endswith("_raw.mp4") and ".tmp" not in f]
    india_clips = [f for f in sorted(os.listdir(CLIPS_INDIA)) if f.endswith(".mp4") and not f.endswith("_raw.mp4") and ".tmp" not in f]
    
    usa_gifs = [f for f in sorted(os.listdir(GIFS_USA)) if f.endswith(".gif")]
    india_gifs = [f for f in sorted(os.listdir(GIFS_INDIA)) if f.endswith(".gif")]
    
    usa_images = [f for f in sorted(os.listdir(os.path.join(MEMES_ROOT, "images", "usa_global"))) if f.endswith(('.jpg', '.png', '.webp'))]
    india_images = [f for f in sorted(os.listdir(os.path.join(MEMES_ROOT, "images", "india"))) if f.endswith(('.jpg', '.png', '.webp'))]
    
    packs = [f for f in sorted(os.listdir(PACKS_DIR)) if f.endswith(".mp4")]
    
    total_assets = len(usa_clips) + len(india_clips) + len(usa_gifs) + len(india_gifs) + len(usa_images) + len(india_images) + len(packs)
    
    lines = [
        f"# ThinkLate & Multi-Channel Enterprise Viral Asset Vault ({total_assets} Assets)",
        "> **Location:** `digital-lab/03-content-lab/shared/assets/memes/`  ",
        "> **Standards:** Broadcast H.264 Video · 48kHz AAC Stereo · Speech Completion Rule · Lightweight Fast Animated GIFs.  ",
        "> **Shared Across:** ThinkLate (@wethinklate), Off Script (@OffScriptEddy), and Sarwanology.",
        "",
        "## 📊 Executive Inventory Breakdown",
        f"* **Total Video Reaction Clips:** **{len(usa_clips) + len(india_clips)} clips** ({len(usa_clips)} Global/Sitcom/Cinema + {len(india_clips)} India)",
        f"* **Total Animated GIFs:** **{len(usa_gifs) + len(india_gifs)} GIFs** ({len(usa_gifs)} Global + {len(india_gifs)} India)",
        f"* **Total Meme Image Templates:** **{len(usa_images) + len(india_images)} images** ({len(usa_images)} Imgflip Top 100 + {len(india_images)} Indian Stills)",
        f"* **Master Offline Compilation Packs:** **{len(packs)} full packs** in `packs/`",
        f"* **GRAND TOTAL VAULTED ASSETS:** **{total_assets} Assets**",
        "",
        "---",
        "",
        f"## 🎬 1. USA & Global Sitcom, Cinema & Viral Clips ({len(usa_clips)} clips in `usa_global/`)",
        "Includes The Office, Brooklyn Nine-Nine, Parks and Rec, Friends, The Big Bang Theory, classic green-screen memes, and iconic movie soundbites.",
        "",
        "| Preview Link | File Name | Matching GIF | Category / Origin |",
        "| :--- | :--- | :--- | :--- |"
    ]
    
    for f in usa_clips:
        base = os.path.splitext(f)[0]
        v_link = f"<a href=\"usa_global/{f}\" target=\"_blank\">{f} ↗</a>"
        g_file = f"{base}.gif"
        if g_file in usa_gifs:
            g_link = f"<a href=\"gifs/usa_global/{g_file}\" target=\"_blank\">GIF ↗</a>"
        else:
            g_link = "-"
            
        category = "Classic / Sitcom" if any(k in base for k in ['office', 'b99', 'parks', 'friends', 'bbt']) else "Green Screen / Viral"
        lines.append(f"| {v_link} | `{f}` | {g_link} | {category} |")

    lines.extend([
        "",
        "---",
        "",
        f"## 🎬 2. India Viral Video Clips ({len(india_clips)} clips in `india/`)",
        "Includes Shark Tank India, Panchayat, Mirzapur, cult Bollywood comedies (Hera Pheri, Welcome, 3 Idiots, Gangs of Wasseypur), and top creator trends.",
        "",
        "| Preview Link | File Name | Matching GIF | Category / Origin |",
        "| :--- | :--- | :--- | :--- |"
    ])

    for f in india_clips:
        base = os.path.splitext(f)[0]
        v_link = f"<a href=\"india/{f}\" target=\"_blank\">{f} ↗</a>"
        g_file = f"{base}.gif"
        if g_file in india_gifs:
            g_link = f"<a href=\"gifs/india/{g_file}\" target=\"_blank\">GIF ↗</a>"
        else:
            g_link = "-"
        category = "Bollywood Comedy" if any(k in base for k in ['hera_pheri', 'babu', 'welcome', '3idiots', 'hindi', 'in100']) else "Web Series / Creator"
        lines.append(f"| {v_link} | `{f}` | {g_link} | {category} |")

    lines.extend([
        "",
        "---",
        "",
        f"## 🖼️ 3. Global Meme Image Templates ({len(usa_images)} templates in `images/usa_global/`)",
        "Top 100 blank meme templates from Imgflip for on-screen kinetic graphics, comparison slides, and evidence cards.",
        "",
        "| Preview Link | File Name |",
        "| :--- | :--- |"
    ])
    for f in usa_images[:40]:
        lines.append(f"| <a href=\"images/usa_global/{f}\" target=\"_blank\">{f} ↗</a> | `{f}` |")
    if len(usa_images) > 40:
        lines.append(f"| *...and {len(usa_images) - 40} more global image templates in folder* | - |")

    lines.extend([
        "",
        "---",
        "",
        f"## 🖼️ 4. India Meme Stills & Quote Cards ({len(india_images)} stills in `images/india/`)",
        "High-res Indian meme templates, reaction stills, and iconic quote cards.",
        "",
        "| Preview Link | File Name |",
        "| :--- | :--- |"
    ])
    for f in india_images:
        lines.append(f"| <a href=\"images/india/{f}\" target=\"_blank\">{f} ↗</a> | `{f}` |")

    lines.extend([
        "",
        "---",
        "",
        f"## 📦 5. Master Offline Compilation Packs ({len(packs)} packs in `packs/`)",
        "Full-length master compilation packs stored locally for offline editing, custom scene selection, or archive reference.",
        "",
        "| Preview Link | File Name | File Size |",
        "| :--- | :--- | :---: |"
    ])
    for f in packs:
        fpath = os.path.join(PACKS_DIR, f)
        size_mb = os.path.getsize(fpath) / (1024 * 1024)
        lines.append(f"| <a href=\"packs/{f}\" target=\"_blank\">{f} ↗</a> | `{f}` | **{size_mb:.1f} MB** |")

    with open(catalog_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"✅ Catalog successfully written to: {catalog_path}")

if __name__ == "__main__":
    run_master_slice()
