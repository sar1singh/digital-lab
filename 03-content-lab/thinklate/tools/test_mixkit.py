import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def search_mixkit(query):
    url = f"https://mixkit.co/free-stock-video/{query}/"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Look for direct video MP4 URLs or video links
            mp4s = re.findall(r'https://assets\.mixkit\.co/videos/[a-zA-Z0-9_\-\.\/]+', html)
            print(f"Mixkit search '{query}': Found {len(mp4s)} assets")
            for m in list(set(mp4s))[:5]:
                print(" -", m)
    except Exception as e:
        print(f"Error {query}: {e}")

search_mixkit("car")
search_mixkit("printer")
search_mixkit("tractor")
search_mixkit("technology")

