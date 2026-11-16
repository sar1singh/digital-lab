import os
import glob
import json
import subprocess

takes_dir = "digital-lab/03-content-lab/thinklate/videos/longForm/L06_the-memory-lie/assets/audio/takes"
files = sorted(glob.glob(os.path.join(takes_dir, "*.wav")))

cum = 0.0
manifest = []
for f in files:
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", f]
    dur = float(subprocess.check_output(cmd, creationflags=0x08000000).decode().strip())
    bname = os.path.basename(f)
    print(f"{bname:25s} | {cum:6.2f}s -> {cum+dur:6.2f}s | ({dur:5.2f}s)")
    manifest.append({
        "file": bname,
        "start": round(cum, 2),
        "end": round(cum + dur, 2),
        "duration": round(dur, 2)
    })
    cum += dur

with open("digital-lab/03-content-lab/thinklate/videos/longForm/L06_the-memory-lie/takes_timing.json", "w") as out:
    json.dump(manifest, out, indent=2)

