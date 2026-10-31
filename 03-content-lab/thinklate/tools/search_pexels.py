import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

def search_pexels_videos(query):
    url = f"https://www.pexels.com/search/videos/{urllib.parse.quote(query)}/"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Look for video URLs or IDs
            # Pexels embeds video links like /video/luxury-car-driving-1234567/ or data-video-id="1234567"
            video_ids = re.findall(r'/video/([a-zA-Z0-9\-]+)-(\d+)/', html)
            print(f"Found {len(video_ids)} videos for '{query}':")
            for slug, vid in video_ids[:5]:
                print(f"  - Title: {slug}, ID: {vid}")
            return [vid for slug, vid in video_ids[:5]]
    except Exception as e:
        print(f"Error searching {query}: {e}")
        return []

import urllib.parse
search_pexels_videos("luxury car")
search_pexels_videos("printer")
search_pexels_videos("tractor")

