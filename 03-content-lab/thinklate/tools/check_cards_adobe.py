import os

for f in ["card_cue34_job_hostage.png", "card_cue35_ftc_lawsuit.png", "card_cue36_bmw_drops_rent.png", "card_cue37_repair_wins.png"]:
    p = os.path.join(r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\04_the-subscription-trap\brand_assets", f)
    print(f, "exists:", os.path.exists(p))
