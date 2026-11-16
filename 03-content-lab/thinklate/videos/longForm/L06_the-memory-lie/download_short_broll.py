import os
import re
import urllib.request

BROLL_DIR = os.path.abspath("digital-lab/03-content-lab/shared/motion_engine/public/broll")
os.makedirs(BROLL_DIR, exist_ok=True)

TARGETS = [
    ("courtroom.mp4", ["court", "courtroom", "gavel", "law", "judge"]),
    ("prison_bars.mp4", ["jail", "prison", "bars", "prison-bars", "cage"]),
    ("dna_lab.mp4", ["dna", "laboratory", "microscope", "science", "chemistry"]),
    ("archive_files.mp4", ["files", "documents", "paperwork", "office", "investigation"]),
    ("brain_synapse.mp4", ["brain", "medical", "neurology", "abstract-technology", "scan"])
]

def find_mixkit_video(keywords):
    for kw in keywords:
        url = f"https://mixkit.co/free-stock-video/{kw}/"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
            matches = re.findall(r'https://assets\.mixkit\.co/videos/[0-9]+/[0-9]+-720\.mp4', html)
            if not matches:
                matches = re.findall(r'https://assets\.mixkit\.co/videos/preview/mixkit-[a-zA-Z0-9_-]+-large\.mp4', html)
            if matches:
                return matches[0]
        except Exception as e:
            pass
    return None

for out_name, kws in TARGETS:
    out_path = os.path.join(BROLL_DIR, out_name)
    if os.path.exists(out_path) and os.path.getsize(out_path) > 100000:
        print(f"[=] Already exists: {out_name} ({os.path.getsize(out_path):,} bytes)")
        continue
    url = find_mixkit_video(kws)
    if url:
        print(f"[+] Downloading {out_name} from {url}...")
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=30) as resp, open(out_path, 'wb') as f:
                f.write(resp.read())
            print(f"    ✓ Saved {out_name} ({os.path.getsize(out_path):,} bytes)")
        except Exception as e:
            print(f"    ✗ Download error for {out_name}: {e}")
    else:
        print(f"[-] Could not find URL for {out_name}")
