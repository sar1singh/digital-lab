import os
import glob
from PIL import Image, ImageStat

sample_dir = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b\assets\gameplay_samples"

for f in sorted(glob.glob(os.path.join(sample_dir, "*.jpg"))):
    im = Image.open(f)
    stat = ImageStat.Stat(im)
    r, g, b = stat.mean[:3]
    # Check if ocean/sky (high blue/cyan) or combat
    print(f"{os.path.basename(f)}: Mean RGB=({r:.1f}, {g:.1f}, {b:.1f})")

