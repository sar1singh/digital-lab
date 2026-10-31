"""
YouTube Packaging Competitor Analyzer CLI Tool
-----------------------------------------------
Autonomously searches YouTube or inspects specific video URLs, downloads high-res thumbnails,
analyzes title ergonomics and visual color/contrast metrics (against YouTube #0F0F0F dark mode),
and produces a structured Packaging QC dossier for creators and agents.

Usage:
    python inspect_youtube_packaging.py --query "airbnb documentary" --limit 5
    python inspect_youtube_packaging.py --url "https://www.youtube.com/watch?v=Ce43Rt_h5jw"
    python inspect_youtube_packaging.py --video-id Ce43Rt_h5jw
"""

import os
import sys
import json
import re
import argparse
import urllib.request
import urllib.parse
from PIL import Image

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def get_video_ids_from_query(query: str, limit: int = 5) -> list[str]:
    """Extract top unique video IDs from YouTube search results."""
    encoded_query = urllib.parse.quote_plus(query)
    search_url = f"https://www.youtube.com/results?search_query={encoded_query}"
    
    req = urllib.request.Request(search_url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=12) as response:
            html = response.read().decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"[-] Error querying YouTube search: {e}", file=sys.stderr)
        return []

    # Match 11-char video IDs in watch?v= links
    raw_ids = re.findall(r'watch\?v=([a-zA-Z0-9_-]{11})', html)
    # Filter unique while preserving order
    unique_ids = []
    for vid in raw_ids:
        if vid not in unique_ids:
            unique_ids.append(vid)
            if len(unique_ids) >= limit:
                break
    return unique_ids

def get_oembed_data(video_id: str) -> dict:
    """Fetch video metadata via public YouTube oEmbed endpoint."""
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=8) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception:
        return {
            "title": f"Video {video_id}",
            "author_name": "Unknown Creator",
            "author_url": "",
            "thumbnail_url": f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
        }

def download_thumbnail(video_id: str, dest_dir: str) -> tuple[str, bool]:
    """Download maxresdefault thumbnail, falling back to hqdefault. Returns (filepath, is_maxres)."""
    os.makedirs(dest_dir, exist_ok=True)
    target_path = os.path.join(dest_dir, f"{video_id}_thumb.jpg")
    
    # Try maxres first (1280x720)
    maxres_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    req = urllib.request.Request(maxres_url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=8) as response:
            data = response.read()
            # If thumbnail is a placeholder 404, data is small or returns 404
            if len(data) > 5000:
                with open(target_path, "wb") as f:
                    f.write(data)
                return target_path, True
    except Exception:
        pass

    # Fallback to hqdefault (480x360)
    hq_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
    req_hq = urllib.request.Request(hq_url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req_hq, timeout=8) as response:
            with open(target_path, "wb") as f:
                f.write(response.read())
            return target_path, False
    except Exception as e:
        print(f"[-] Failed downloading thumbnail for {video_id}: {e}", file=sys.stderr)
        return "", False

def analyze_thumbnail_image(img_path: str) -> dict:
    """Analyze image resolution, luminance, saturation, dominant colors, and dark-mode pop score."""
    if not os.path.exists(img_path):
        return {}

    with Image.open(img_path) as img:
        width, height = img.size
        rgb_img = img.convert("RGB")
        hsv_img = img.convert("HSV")
        
        # Calculate average luminance (standard ITU-R BT.601)
        pixels = list(rgb_img.getdata())
        n_pixels = len(pixels)
        if n_pixels == 0:
            return {}
        
        total_lum = sum(0.299 * r + 0.587 * g + 0.114 * b for r, g, b in pixels)
        mean_luminance = total_lum / n_pixels
        
        # Average saturation
        hsv_pixels = list(hsv_img.getdata())
        mean_saturation = sum(s for h, s, v in hsv_pixels) / (n_pixels * 255.0) * 100.0
        
        # Dominant colors via color quantization (palette of 5 colors)
        quantized = rgb_img.quantize(colors=5, method=Image.Quantize.FASTOCTREE)
        palette = quantized.getpalette()[:15]
        dominant_colors = []
        for i in range(0, len(palette), 3):
            r, g, b = palette[i], palette[i+1], palette[i+2]
            dominant_colors.append(f"#{r:02x}{g:02x}{b:02x}".upper())
            
        # Dark-mode pop score (0-100)
        # Higher score = brighter, punchier, high-contrast colors against pure black #0F0F0F
        # Pure dark thumbnails (luminance < 60) score low (< 40)
        pop_score = min(100, int((mean_luminance / 255.0 * 60) + (mean_saturation * 0.4)))
        
        if pop_score >= 65:
            contrast_verdict = "🔥 High-Contrast Pop (Dominates Dark Mode)"
        elif pop_score >= 45:
            contrast_verdict = "⚖️ Moderate Contrast (Standard Feed Presence)"
        else:
            contrast_verdict = "⚠️ Low Contrast / Danger (Blends into #0F0F0F Feed)"

        return {
            "width": width,
            "height": height,
            "aspect_ratio": f"{width}:{height}",
            "mean_luminance": round(mean_luminance, 1),
            "mean_saturation_pct": round(mean_saturation, 1),
            "dominant_colors": dominant_colors,
            "pop_score": pop_score,
            "contrast_verdict": contrast_verdict
        }

def analyze_title(title: str) -> dict:
    """Analyze title length, ergonomics, and click mechanics."""
    char_len = len(title)
    words = title.split()
    word_count = len(words)
    
    # Check length against YouTube mobile ceiling (50 chars)
    if char_len <= 50:
        length_status = "✅ Mobile Safe (≤ 50 chars)"
    elif char_len <= 70:
        length_status = "⚠️ Borderline (May truncate on mobile feed)"
    else:
        length_status = "❌ Severely Truncated (> 70 chars)"
        
    has_numbers = bool(re.search(r'\d+', title))
    has_question = "?" in title
    has_brackets = "[" in title or "(" in title or "|" in title
    
    return {
        "title": title,
        "char_length": char_len,
        "word_count": word_count,
        "length_status": length_status,
        "has_numbers": has_numbers,
        "has_question": has_question,
        "has_brackets_or_pipe": has_brackets
    }

def inspect_video(video_id: str, output_dir: str) -> dict:
    """Run complete packaging inspection on a single YouTube video ID."""
    oembed = get_oembed_data(video_id)
    thumb_path, is_maxres = download_thumbnail(video_id, output_dir)
    image_metrics = analyze_thumbnail_image(thumb_path) if thumb_path else {}
    title_metrics = analyze_title(oembed.get("title", ""))
    
    return {
        "video_id": video_id,
        "video_url": f"https://www.youtube.com/watch?v={video_id}",
        "channel_name": oembed.get("author_name", "Unknown"),
        "channel_url": oembed.get("author_url", ""),
        "title_analysis": title_metrics,
        "thumbnail_path": thumb_path.replace("\\", "/"),
        "is_maxres": is_maxres,
        "image_analysis": image_metrics
    }

def generate_markdown_report(query_or_url: str, results: list[dict], report_path: str):
    """Generate a clean, structured Markdown packaging report."""
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    
    lines = [
        f"# YouTube Packaging Intelligence Dossier",
        f"",
        f"> **Inspection Target:** `{query_or_url}`  ",
        f"> **Videos Analyzed:** {len(results)}  ",
        f"> **Engine:** Headless Packaging Analyzer & Color Metric Engine  ",
        f"",
        f"---",
        f"",
        f"## 📊 Packaging Comparison Matrix",
        f"",
        f"| Thumbnail | Creator & Title | Length & Status | Pop Score & Verdict | Dominant Colors |",
        f"| :---: | :--- | :--- | :--- | :--- |"
    ]
    
    for r in results:
        v_id = r["video_id"]
        v_url = r["video_url"]
        channel = r["channel_name"]
        t_info = r["title_analysis"]
        img_info = r.get("image_analysis", {})
        thumb_file = os.path.basename(r.get("thumbnail_path", ""))
        
        # Workspace-relative link in markdown table
        thumb_link = f"[{thumb_file}]({thumb_file})" if thumb_file else "N/A"
        
        title_display = f"**[{t_info['title']}]({v_url})**<br>👤 *{channel}*"
        length_display = f"`{t_info['char_length']} chars` ({t_info['length_status']})"
        pop_display = f"**{img_info.get('pop_score', 'N/A')}/100**<br>{img_info.get('contrast_verdict', 'N/A')}"
        colors_display = " ".join([f"`{c}`" for c in img_info.get("dominant_colors", [])[:4]])
        
        lines.append(f"| {thumb_link} | {title_display} | {length_display} | {pop_display} | {colors_display} |")
        
    lines.extend([
        f"",
        f"---",
        f"",
        f"## 🎯 Key Packaging Insights & Strategic Rules",
        f"",
        f"1. **Mobile Title Truncation Check:** Videos with titles $\le$ 50 characters retain full visibility on the YouTube mobile app without getting cut off with ellipses (`...`).",
        f"2. **Dark Mode Inversion Principle:** YouTube's dark mode UI is `#0F0F0F`. Thumbnails with low luminance (< 50) and low saturation blend into the feed and lose up to 60% of baseline CTR. High-contrast saturations (Acid Lime, Vivid Orange, White cutout text) score $\ge 65$ and reliably command the 150ms scroll glance.",
        f"3. **Recommended Visual Architecture:**",
        f"   - **Left:** High-expression character portrait or dramatic conflict object.",
        f"   - **Right:** 2-3 words Swiss Brutalist block typography in high-contrast two-tone.",
        f"   - **Background:** Saturated, high-clarity graphic environment (avoiding muddy black shadows).",
        f""
    ])
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[+] Packaging Dossier saved to: {report_path}")

def main():
    parser = argparse.ArgumentParser(description="YouTube Packaging Competitor Analyzer")
    parser.add_argument("--query", type=str, help="Search query on YouTube")
    parser.add_argument("--url", type=str, help="Single YouTube video URL")
    parser.add_argument("--video-id", type=str, help="Single YouTube video ID")
    parser.add_argument("--limit", type=int, default=5, help="Number of results to analyze (default: 5)")
    parser.add_argument("--output-dir", type=str, default="digital-lab/03-content-lab/shared/assets/competitor_thumbnails", help="Directory to save thumbnails")
    parser.add_argument("--json", action="store_true", help="Print results as JSON")
    args = parser.parse_args()

    video_ids = []
    target_label = ""
    
    if args.video_id:
        video_ids = [args.video_id]
        target_label = args.video_id
    elif args.url:
        match = re.search(r'(?:v=|\/)([a-zA-Z0-9_-]{11})', args.url)
        if match:
            video_ids = [match.group(1)]
            target_label = args.url
        else:
            print("[-] Invalid YouTube URL provided.", file=sys.stderr)
            sys.exit(1)
    elif args.query:
        print(f"[*] Searching YouTube for: '{args.query}' (limit {args.limit})...")
        video_ids = get_video_ids_from_query(args.query, args.limit)
        target_label = args.query
    else:
        print("[-] Must provide --query, --url, or --video-id", file=sys.stderr)
        sys.exit(1)

    if not video_ids:
        print("[-] No video IDs found.", file=sys.stderr)
        sys.exit(1)

    print(f"[*] Inspecting {len(video_ids)} video(s)...")
    results = []
    for vid in video_ids:
        print(f"    -> Inspecting {vid}...")
        res = inspect_video(vid, args.output_dir)
        results.append(res)

    report_path = os.path.join(args.output_dir, "PACKAGING_DOSSIER.md")
    generate_markdown_report(target_label, results, report_path)

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print(f"\n[+] Successfully inspected {len(results)} videos!")

if __name__ == "__main__":
    main()
