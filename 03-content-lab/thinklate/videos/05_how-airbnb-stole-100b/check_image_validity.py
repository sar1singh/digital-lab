import glob
import os
from PIL import Image

broll_dir = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b\assets\documentary_broll"

for f in glob.glob(os.path.join(broll_dir, "*.*")):
    ext = os.path.splitext(f)[1].lower()
    if ext in ['.jpg', '.jpeg', '.png']:
        header = open(f, "rb").read(8)
        try:
            im = Image.open(f)
            print(f"VALID: {os.path.basename(f)} -> {im.size} {im.format}")
        except Exception as e:
            print(f"INVALID: {os.path.basename(f)} -> header: {header} error: {e}")

