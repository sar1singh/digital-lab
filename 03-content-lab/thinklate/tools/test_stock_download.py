import urllib.request
import json
import os

# Test fetching a free stock video from Pexels direct download
# Video ID: 853889 (luxury car driving) or similar
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

test_url = "https://www.pexels.com/video/853889/download/"
req = urllib.request.Request(test_url, headers=headers)

out_file = r"digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/assets/test_pexels.mp4"

try:
    print("Testing Pexels video download...")
    with urllib.request.urlopen(req) as resp:
        final_url = resp.geturl()
        print(f"Redirected to: {final_url[:80]}...")
        content_type = resp.headers.get('Content-Type')
        print(f"Content-Type: {content_type}")
        # Read first 1MB to verify
        chunk = resp.read(1024 * 1024)
        with open(out_file, "wb") as f:
            f.write(chunk)
        print(f"Success! Read {len(chunk)} bytes.")
except Exception as e:
    print(f"Error: {e}")

