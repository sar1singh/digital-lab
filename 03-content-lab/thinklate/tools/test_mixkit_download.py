import urllib.request
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Test Mixkit HD video download (e.g., 720p or 1080p)
# URL: https://assets.mixkit.co/videos/16033/16033-720.mp4 or 16033-1080.mp4
out_file = r"digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/assets/test_mixkit_tractor.mp4"

for res in ["720", "1080", "360"]:
    url = f"https://assets.mixkit.co/videos/16033/16033-{res}.mp4"
    print(f"Trying Mixkit {res}p: {url}...")
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = resp.read()
            with open(out_file, "wb") as f:
                f.write(data)
            print(f"SUCCESS! Downloaded {len(data)} bytes ({len(data)//(1024*1024)} MB) to {out_file}")
            break
    except Exception as e:
        print(f"Failed {res}p: {e}")

