import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

video_url = "https://www.pexels.com/video/5309351/"
req = urllib.request.Request(video_url, headers=headers)

try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        # Find video source URLs (e.g., https://videos.pexels.com/video-files/...)
        mp4_links = re.findall(r'https://videos\.pexels\.com/video-files/[a-zA-Z0-9_\-\.\/]+', html)
        print(f"Found {len(mp4_links)} MP4 links for video 5309351:")
        for link in set(mp4_links):
            print(" -", link)
except Exception as e:
    print(f"Error: {e}")

