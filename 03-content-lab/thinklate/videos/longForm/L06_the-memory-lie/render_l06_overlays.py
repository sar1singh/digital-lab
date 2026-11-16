import os
import sys
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(".")
MOTION_ENGINE = os.path.join(PROJECT_ROOT, "digital-lab", "03-content-lab", "shared", "motion_engine")
L06_DIR = os.path.join(PROJECT_ROOT, "digital-lab", "03-content-lab", "thinklate", "videos", "longForm", "L06_the-memory-lie")
PLATES_DIR = os.path.join(L06_DIR, "assets", "remotion_plates")
os.makedirs(PLATES_DIR, exist_ok=True)

cmd = [
    "npx.cmd", "remotion", "render",
    "src/index.ts", "L06ForensicOverlay",
    PLATES_DIR,
    "--sequence",
    "--image-format=png",
    "--gl=angle"
]

print("[*] Rendering 23 Widescreen 1920x1080 RGBA Documentary Plates via Remotion...")
res = subprocess.run(cmd, cwd=MOTION_ENGINE, creationflags=0x08000000, capture_output=True, text=True)
if res.returncode == 0:
    files = sorted(os.listdir(PLATES_DIR))
    print(f"[+] Successfully rendered {len(files)} RGBA plates in {PLATES_DIR}:")
    for f in files[:5]:
        print("   ->", f)
else:
    print("[-] Error:", res.stderr or res.stdout)
    sys.exit(1)

