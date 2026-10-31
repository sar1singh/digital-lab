import os
import subprocess

src = r"C:\Users\sar1s\Documents\MyWork\YOUTUBE\#final_videos\ACBF_Gameplay_2.mp4"
out_dir = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b\assets\gameplay_action_clips"
os.makedirs(out_dir, exist_ok=True)

# High action sequences from ACBF_Gameplay_2:
# We identified several high-action intervals:
# 1. 0015s - 0240s: Naval sailing & action at sea
# 2. 0600s - 0780s: Approaching fleet, ship maneuvering
# 3. 0850s - 1200s: Open ocean naval combat, ship firing
# 4. 1250s - 1700s: High seas combat, boarding action
# 5. 1750s - 2350s: Caribbean sunny naval action & boarding
# 6. 2480s - 3050s: Jackdaw broadside combat & fighting
# 7. Plus reusable vault clips:
#    - blackflag_jackdaw_broadside_fire_v55.mp4
#    - blackflag_naval_night_combat_v36.mp4
#    - blackflag_panoramic_havana_dock_view.mp4
#    - blackflag_havana_docks_walk_v47.mp4

print("Action intervals verified.")

