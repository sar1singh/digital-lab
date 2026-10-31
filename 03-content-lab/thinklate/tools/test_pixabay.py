import urllib.request
import json

# Pixabay API has a public demo key 'anonymous' or standard free key
# Let's test searching Pixabay videos
query = "tractor"
url = f"https://pixabay.com/api/videos/?key=anonymous&q={query}&per_page=3"

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode())
        print("Pixabay results:", len(data.get('hits', [])))
        for hit in data.get('hits', []):
            print(f"Hit ID: {hit.get('id')}, tags: {hit.get('tags')}")
            videos = hit.get('videos', {})
            for size, info in videos.items():
                print(f"  {size}: {info.get('url')} ({info.get('width')}x{info.get('height')})")
except Exception as e:
    print(f"Error: {e}")

