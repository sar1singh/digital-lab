import urllib.request
import json
import urllib.parse

def search_archive_org(query):
    url = (
        "https://archive.org/advancedsearch.php?"
        f"q={urllib.parse.quote(query)}+AND+mediatype:movies&"
        "fl[]=identifier,title,description,downloads&"
        "sort[]=downloads+desc&rows=3&page=1&output=json"
    )
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            docs = data.get('response', {}).get('docs', [])
            print(f"\n--- Archive.org results for '{query}' ({len(docs)}) ---")
            for d in docs:
                ident = d.get('identifier')
                title = d.get('title')
                print(f"- {title} (ID: {ident}) -> https://archive.org/details/{ident}")
    except Exception as e:
        print(f"Error for {query}: {e}")

search_archive_org("tractor farming")
search_archive_org("assembly line factory")
search_archive_org("light bulb")

