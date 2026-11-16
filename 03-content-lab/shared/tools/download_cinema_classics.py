#!/usr/bin/env python3
"""
Evergreen Cinema & TV Staples Harvester
=======================================
Harvests iconic evergreen cinema & TV clips with full sentence delivery.
"""

import os
import sys
import subprocess
import shutil

CREATE_NO_WINDOW = 0x08000000

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SHARED_DIR = os.path.dirname(SCRIPT_DIR)
MEMES_ROOT = os.path.join(SHARED_DIR, "assets", "memes")
CLIPS_USA = os.path.join(MEMES_ROOT, "usa_global")
CLIPS_INDIA = os.path.join(MEMES_ROOT, "india")
GIFS_USA = os.path.join(MEMES_ROOT, "gifs", "usa_global")
GIFS_INDIA = os.path.join(MEMES_ROOT, "gifs", "india")

CLASSICS = [
    # USA / GLOBAL CINEMA & TV ICONS
    {
        "id": "bb_walter_i_am_the_one_who_knocks",
        "category": "usa_global",
        "query": "ytsearch1:i am the one who knocks full scene 1080p",
        "dur": 8,
        "mood": "Ruthless Threat"
    },
    {
        "id": "bb_gus_fring_we_are_not_the_same",
        "category": "usa_global",
        "query": "ytsearch1:we are not the same meme template 1080p",
        "dur": 6,
        "mood": "Elitism & Hierarchy"
    },
    {
        "id": "batman_joker_why_so_serious",
        "category": "usa_global",
        "query": "ytsearch1:why so serious heath ledger 1080p clip",
        "dur": 9,
        "mood": "Psychotic Menace"
    },
    {
        "id": "gatsby_dicaprio_champagne_toast",
        "category": "usa_global",
        "query": "ytsearch1:leonardo dicaprio toast the great gatsby 1080p",
        "dur": 6,
        "mood": "Wealth & Smug Triumph"
    },
    {
        "id": "pulp_fiction_say_what_again",
        "category": "usa_global",
        "query": "ytsearch1:say what again samuel l jackson 1080p clip",
        "dur": 8,
        "mood": "Interrogation Terror"
    },
    {
        "id": "american_psycho_business_card_sweat",
        "category": "usa_global",
        "query": "ytsearch1:american psycho business card scene 1080p clip",
        "dur": 8,
        "mood": "Status Insecurity"
    },
    {
        "id": "star_wars_hello_there_kenobi",
        "category": "usa_global",
        "query": "ytsearch1:hello there general kenobi 1080p clip",
        "dur": 5,
        "mood": "Iconic Arrival"
    },
    {
        "id": "spider_man_bully_maguire_dance",
        "category": "usa_global",
        "query": "ytsearch1:bully maguire dance 1080p green screen",
        "dur": 6,
        "mood": "Arrogant Strut"
    },
    {
        "id": "godfather_massacred_my_boy",
        "category": "usa_global",
        "query": "ytsearch1:look how they massacred my boy 1080p clip",
        "dur": 7,
        "mood": "Grief over Ruined Work"
    },
    {
        "id": "wwe_vince_mcmahon_smelling_money",
        "category": "usa_global",
        "query": "ytsearch1:vince mcmahon smelling money meme 1080p",
        "dur": 6,
        "mood": "Gross Capitalist Greed"
    },
    {
        "id": "homelander_blank_stare_smiling",
        "category": "usa_global",
        "query": "ytsearch1:homelander staring meme template 1080p",
        "dur": 7,
        "mood": "Psychopathic Restraint"
    },
    {
        "id": "community_troy_pizza_room_on_fire",
        "category": "usa_global",
        "query": "ytsearch1:community troy walking in with pizza fire clip 1080p",
        "dur": 6,
        "mood": "Walking into Disaster"
    },
    {
        "id": "curb_larry_david_stare_music",
        "category": "usa_global",
        "query": "ytsearch1:larry david staring meme music clip 1080p",
        "dur": 8,
        "mood": "Suspicious Audit"
    },
    {
        "id": "always_sunny_pepe_silvia_conspiracy",
        "category": "usa_global",
        "query": "ytsearch1:charlie kelly pepe silvia 1080p clip",
        "dur": 10,
        "mood": "Schizo Research & Chaos"
    },
    {
        "id": "seinfeld_no_soup_for_you",
        "category": "usa_global",
        "query": "ytsearch1:no soup for you seinfeld 1080p clip",
        "dur": 6,
        "mood": "Arbitrary Vendor Ban"
    },

    # INDIA CLASSICS
    {
        "id": "gow_faizal_badla_lega_sabka",
        "category": "india",
        "query": "ytsearch1:baap ka dada ka sabka badla lega re tera faizal clip",
        "dur": 7,
        "mood": "Vow of Vengeance"
    },
    {
        "id": "dhamaal_waha_ek_laal_button_hai",
        "category": "india",
        "query": "ytsearch1:dhamaal red button helicopter scene clip",
        "dur": 8,
        "mood": "Catastrophic Misclick"
    },
    {
        "id": "chup_chup_ke_mujhe_sab_aata_hai",
        "category": "india",
        "query": "ytsearch1:mujhe sab aata hai rajpal yadav clip",
        "dur": 6,
        "mood": "Over-promising Incompetence"
    },
    {
        "id": "welcome_meri_ek_taang_nakli_hai",
        "category": "india",
        "query": "ytsearch1:meri ek taang nakli hai nana patekar clip",
        "dur": 7,
        "mood": "Absurd Sympathy Play"
    },
    {
        "id": "andaz_crime_master_gogo_aankhein",
        "category": "india",
        "query": "ytsearch1:aankhein nikaal ke gotiyan khelunga crime master gogo",
        "dur": 7,
        "mood": "Comic Villainy"
    }
]

def main():
    print(f"🎬 Sourcing {len(CLASSICS)} Evergreen Cinema & TV Staples...")
    count = 0
    for item in CLASSICS:
        target_dir = CLIPS_INDIA if item["category"] == "india" else CLIPS_USA
        gif_dir = GIFS_INDIA if item["category"] == "india" else GIFS_USA
        
        out_mp4 = os.path.join(target_dir, f"{item['id']}.mp4")
        out_gif = os.path.join(gif_dir, f"{item['id']}.gif")
        
        if os.path.exists(out_mp4) and os.path.getsize(out_mp4) > 50000:
            continue
            
        print(f"   Downloading: {item['id']}...")
        temp_raw = out_mp4 + ".raw.mp4"
        cmd = [
            "yt-dlp", item["query"],
            "-f", "bestvideo[height<=720]+bestaudio/best",
            "--merge-output-format", "mp4",
            "-o", temp_raw,
            "--no-playlist", "--force-overwrites"
        ]
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=CREATE_NO_WINDOW)
        
        if os.path.exists(temp_raw) and os.path.getsize(temp_raw) > 1000:
            # Cut first N seconds or full
            cut_cmd = [
                "ffmpeg", "-y", "-i", temp_raw,
                "-t", str(item["dur"]),
                "-c:v", "libx264", "-preset", "ultrafast", "-crf", "20",
                "-c:a", "aac", "-b:a", "128k", out_mp4
            ]
            subprocess.run(cut_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=CREATE_NO_WINDOW)
            try:
                os.remove(temp_raw)
            except:
                pass
                
            if os.path.exists(out_mp4) and os.path.getsize(out_mp4) > 1000:
                count += 1
                print(f"   ✅ Saved video: {item['id']}.mp4")
                
                # Make matching GIF
                gif_cmd = [
                    "ffmpeg", "-y", "-i", out_mp4,
                    "-t", str(min(item["dur"], 5)),
                    "-vf", "fps=10,scale=360:-1", out_gif
                ]
                subprocess.run(gif_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=CREATE_NO_WINDOW)
                
    print(f"🎉 Harvested {count} new Evergreen Cinema & TV clips!")

if __name__ == "__main__":
    main()
