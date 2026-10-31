import urllib.request
import json
import urllib.parse

def search_commons_videos(query):
    # Wikimedia Commons API
    url = (
        "https://commons.wikimedia.org/w/api.php?"
        "action=query&format=json&generator=search&"
        f"gsrsearch={urllib.parse.quote(query)}+filetype:video&"
        "gsrlimit=5&prop=imageinfo&iiprop=url|mime|size"
    )
    req = urllib.request.Request(url, headers={'User-Agent': 'ThinkLateBot/1.0 (contact: team@thinklate.com)'})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            print(f"\n--- Commons Videos for '{query}' ({len(pages)} results) ---")
            for pid, page in pages.items():
                title = page.get('title')
                info = page.get('imageinfo', [{}])[0]
                media_url = info.get('url')
                mime = info.get('mime')
                size = info.get('size', 0)
                print(f"Title: {title}\n  MIME: {mime}, Size: {size//1024} KB\n  URL: {media_url}")
    except Exception as e:
        print(f"Error for {query}: {e}")

search_commons_videos("combine harvester")
search_commons_videos("light bulb filament")
search_commons_videos("server room")

