#!/usr/bin/env python3
import os
import subprocess
import re

CREATE_NO_WINDOW = 0x08000000

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SHARED_DIR = os.path.dirname(SCRIPT_DIR)
MEMES_ROOT = os.path.join(SHARED_DIR, "assets", "memes")
PACK_PATH = os.path.join(MEMES_ROOT, "packs", "top_40_indian_memes_pack.mp4")
CLIPS_INDIA = os.path.join(MEMES_ROOT, "india")
GIFS_INDIA = os.path.join(MEMES_ROOT, "gifs", "india")

TITLES_40 = [
    "in40_01_gajab_beizzati_yaar",
    "in40_02_yeh_phas_gaya",
    "in40_03_acha_humko_sikha_riya_hai",
    "in40_04_yeh_koi_tareeqa_hai_bheek",
    "in40_05_mai_gareeb_hoon",
    "in40_06_kaisa_laga_mera_mazaak",
    "in40_07_abey_jaldi_bol_kal_subah",
    "in40_08_pyari_samajh_gayi",
    "in40_09_yehi_nahi_abhi_aur_suniye",
    "in40_10_cheating_karta_hai_tu",
    "in40_11_utha_le_re_baba",
    "in40_12_agar_hum_kare_to_kare_kya",
    "in40_13_jhooth_bol_raha_hai",
    "in40_14_tere_baap_ko_mat_sikha",
    "in40_15_arey_kehna_kya_chahte_ho",
    "in40_16_chup_bilkul_chup",
    "in40_17_band_karo_haath_jodke",
    "in40_18_maut_ko_chhoo_ke_tak_se",
    "in40_19_aaj_jeetenge_kal_haarenge",
    "in40_20_50_rupaye_kaat_overacting",
    "in40_21_abhi_maza_aayega_na_bhidu",
    "in40_22_beta_tumse_na_ho_payega",
    "in40_23_babu_bhaiya_phone_call",
    "in40_24_tension_nahi_lene_ka_apun",
    "in40_25_kabhi_kabhi_lagta_hai",
    "in40_26_teri_dada_giri_nikaal_doonga",
    "in40_27_mereko_to_dhak_dhak_ho_raha",
    "in40_28_dukh_khatam_kaahe_nahi_hota",
    "in40_29_i_am_sorry_babu",
    "in40_30_chalo_bhai_dekho_kya_karta",
    "in40_31_tum_rehne_do_tauba_tauba",
    "in40_32_nice_clip",
    "in40_33_oh_noob_reaction",
    "in40_34_nani_anime_sound",
    "in40_35_bro_what_are_you_talking_about",
    "in40_36_i_am_rich_meme",
    "in40_37_salman_khan_laughing",
    "in40_38_samajh_rahe_ho_na",
    "in40_39_raha_nahi_jata_tadap",
    "in40_40_big_guy_laughing"
]

def main():
    if not os.path.exists(PACK_PATH):
        print("Pack not found")
        return

    # Probe duration
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", PACK_PATH]
    total_dur = float(subprocess.check_output(cmd, creationflags=CREATE_NO_WINDOW).decode().strip())
    print(f"Total pack duration: {total_dur:.1f}s")
    
    # Run scene detect
    detect_cmd = ["ffmpeg", "-i", PACK_PATH, "-filter:v", "select=gt(scene\\,0.22),showinfo", "-f", "null", "-"]
    res = subprocess.run(detect_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=CREATE_NO_WINDOW)
    cuts = [0.0] + [float(t) for t in re.findall(r"pts_time:([0-9.]+)", res.stderr)]
    # Filter cuts that are too close (< 2.5s)
    clean_cuts = [0.0]
    for c in cuts[1:]:
        if c - clean_cuts[-1] >= 2.5:
            clean_cuts.append(c)
    clean_cuts.append(total_dur)
    
    print(f"Detected {len(clean_cuts)-1} scene segments in pack.")
    
    count = 0
    num_to_slice = min(len(TITLES_40), len(clean_cuts) - 1)
    for i in range(num_to_slice):
        title = TITLES_40[i]
        start = clean_cuts[i]
        end = clean_cuts[i+1]
        dur = max(2.0, end - start)
        
        out_mp4 = os.path.join(CLIPS_INDIA, f"{title}.mp4")
        out_gif = os.path.join(GIFS_INDIA, f"{title}.gif")
        
        if not os.path.exists(out_mp4) or os.path.getsize(out_mp4) < 5000:
            slice_cmd = [
                "ffmpeg", "-y", "-ss", f"{start:.2f}", "-i", PACK_PATH, "-t", f"{dur:.2f}",
                "-c:v", "libx264", "-preset", "ultrafast", "-crf", "20",
                "-c:a", "aac", "-b:a", "128k", out_mp4
            ]
            subprocess.run(slice_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=CREATE_NO_WINDOW)
            if os.path.exists(out_mp4) and os.path.getsize(out_mp4) > 1000:
                count += 1
                
        if os.path.exists(out_mp4) and (not os.path.exists(out_gif) or os.path.getsize(out_gif) < 1000):
            gif_cmd = [
                "ffmpeg", "-y", "-i", out_mp4, "-t", f"{min(dur, 5):.2f}",
                "-vf", "fps=10,scale=360:-1", out_gif
            ]
            subprocess.run(gif_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=CREATE_NO_WINDOW)
            
    print(f"✅ Successfully sliced {count} new Indian video clips and GIFs!")

if __name__ == "__main__":
    main()
