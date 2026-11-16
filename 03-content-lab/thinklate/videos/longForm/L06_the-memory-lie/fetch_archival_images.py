import os
import re
import json
import urllib.request
import urllib.parse

IMAGES_DIR = os.path.abspath("digital-lab/03-content-lab/shared/motion_engine/public/images/memory_lie")
os.makedirs(IMAGES_DIR, exist_ok=True)

def search_wikimedia(query, limit=5):
    encoded = urllib.parse.quote(query)
    url = f"https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrsearch={encoded}&gsrnamespace=6&gsrlimit={limit}&prop=imageinfo&iiprop=url|mime|size"
    req = urllib.request.Request(url, headers={'User-Agent': 'ThinkLateBot/1.0 (educational research)'})
    try:
        data = json.loads(urllib.request.urlopen(req, timeout=10).read().decode('utf-8'))
        pages = data.get("query", {}).get("pages", {})
        results = []
        for p in pages.values():
            info = p.get("imageinfo", [{}])[0]
            if "url" in info:
                results.append((p.get("title", ""), info["url"]))
        return results
    except Exception as e:
        print(f"Error searching {query}: {e}")
        return []

queries = [
    "Ronald Cotton",
    "Jennifer Thompson Cannino",
    "courtroom docket",
    "DNA gel electrophoresis",
    "Innocence Project"
]

for q in queries:
    print(f"[*] Searching Wikimedia for '{q}'...")
    res = search_wikimedia(q, limit=3)
    for title, url in res:
        print(f"  -> {title}: {url}")
        clean_name = re.sub(r'[^a-zA-Z0-9_\.]', '_', title.replace("File:", ""))[:40] + ".jpg"
        target = os.path.join(IMAGES_DIR, clean_name)
        if not os.path.exists(target):
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=15) as resp, open(target, 'wb') as f:
                    f.write(resp.read())
                print(f"     ✓ Downloaded {clean_name}")
            except Exception as e:
                print(f"     ✗ Download error: {e}")
