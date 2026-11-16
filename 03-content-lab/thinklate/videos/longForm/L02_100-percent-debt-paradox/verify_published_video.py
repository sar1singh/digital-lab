import json
import subprocess
import sys

def verify_youtube_video(video_url: str):
    print(f"[*] Running autonomous verification audit for: {video_url}")
    cmd = ["uv", "run", "--with", "yt-dlp", "yt-dlp", "--dump-json", video_url]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        print(f"[!] Error fetching video metadata: {res.stderr}")
        return False, None
    
    data = json.loads(res.stdout)
    
    title = data.get("title", "")
    uploader = data.get("uploader", "")
    uploader_id = data.get("uploader_id", "")
    duration = data.get("duration", 0)
    duration_str = data.get("duration_string", "")
    availability = data.get("availability", "")
    chapters = data.get("chapters") or []
    subtitles = data.get("subtitles") or {}
    auto_captions = data.get("automatic_captions") or {}
    formats = data.get("formats") or []
    thumbnail = data.get("thumbnail", "")
    thumbnails = data.get("thumbnails") or []
    description = data.get("description", "")
    tags = data.get("tags") or []
    
    # Resolutions check
    resolutions = set()
    codecs = set()
    for f in formats:
        h = f.get("height")
        if h:
            resolutions.add(h)
        vc = f.get("vcodec")
        if vc and vc != "none":
            codecs.add(vc.split(".")[0])
            
    has_1080p = 1080 in resolutions
    has_chapters = len(chapters) >= 15
    has_manual_subs = "en" in subtitles or len(subtitles) > 0
    has_auto_subs = len(auto_captions) > 0
    desc_has_timestamps = "00:00" in description or "0:00" in description
    desc_length = len(description)
    
    report = {
        "url": video_url,
        "id": data.get("id"),
        "title": title,
        "uploader": uploader,
        "uploader_id": uploader_id,
        "duration": duration,
        "duration_str": duration_str,
        "availability": availability,
        "has_1080p": has_1080p,
        "all_resolutions": sorted(list(resolutions)),
        "video_codecs": sorted(list(codecs)),
        "total_chapters": len(chapters),
        "chapters": chapters,
        "has_manual_subs": has_manual_subs,
        "manual_subs_languages": list(subtitles.keys()),
        "has_auto_subs": has_auto_subs,
        "thumbnail": thumbnail,
        "highest_res_thumbnail": thumbnails[-1] if thumbnails else None,
        "description_length": desc_length,
        "desc_has_timestamps": desc_has_timestamps,
        "description": description,
        "tags_count": len(tags),
        "tags": tags
    }
    
    return True, report

if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "https://www.youtube.com/watch?v=MjlAKKDdA8c"
    success, rep = verify_youtube_video(url)
    if success:
        with open("live_verification_report.json", "w", encoding="utf-8") as f:
            json.dump(rep, f, indent=2)
        print("=== VERIFICATION RESULTS ===")
        print(f"Title: {rep['title']}")
        print(f"Channel: {rep['uploader']} ({rep['uploader_id']})")
        print(f"Duration: {rep['duration_str']} ({rep['duration']}s)")
        print(f"Status: {rep['availability']}")
        print(f"1080p Processed: {rep['has_1080p']} (Available: {rep['all_resolutions']})")
        print(f"Codecs: {rep['video_codecs']}")
        print(f"Chapters Count: {rep['total_chapters']}")
        print(f"Description Length: {rep['description_length']} chars (Timestamps: {rep['desc_has_timestamps']})")
        print(f"Manual Subtitles: {rep['manual_subs_languages']}")
        print(f"Thumbnail URL: {rep['thumbnail']}")
        print(f"Tags Count: {rep['tags_count']}")
    else:
        sys.exit(1)
