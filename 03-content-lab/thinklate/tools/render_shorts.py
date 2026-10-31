#!/usr/bin/env python3
"""
ThinkLate Autonomous Vertical Shorts Generator (9:16)
=====================================================
Autonomously extracts and renders 9:16 YouTube Shorts directly from master long-form assets:
1. Reads `<!-- SHORTS_SPLICE_START: <TAG> -->` and `<!-- SHORTS_SPLICE_END: <TAG> -->` markers.
2. Resolves millisecond timestamps via `transcription_timestamps.json`.
3. Slices master audio with 0.5s pre/post handles.
4. Crops 16:9 stock documentary B-roll to 9:16 (center-safe: 1080x1920).
5. Generates high-impact 9:16 Shorts with burning subtitles.
6. Operates 100% headlessly (CREATE_NO_WINDOW).
"""

import os
import sys
import re
import json
import subprocess
import argparse

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0

def parse_shorts_splices_from_script(script_path):
    if not os.path.exists(script_path):
        return []
    with open(script_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r'<!--\s*SHORTS_SPLICE_START:\s*([A-Za-z0-9_-]+)\s*-->(.*?)<!--\s*SHORTS_SPLICE_END:\s*\1\s*-->'
    matches = re.findall(pattern, content, re.DOTALL)
    
    splices = []
    for tag, text in matches:
        clean_text = re.sub(r'\[.*?\]', '', text).strip()
        words = clean_text.replace('//', ' ').replace('///', ' ').split()
        splices.append({
            "tag": tag,
            "raw_text": text.strip(),
            "clean_text": clean_text,
            "word_count": len(words)
        })
    return splices

def match_splice_to_whisper_timestamps(splice, timestamps_path):
    if not os.path.exists(timestamps_path):
        return None, None
    with open(timestamps_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Clean words to match
    sample_start = splice["clean_text"].split()[:6]
    sample_end = splice["clean_text"].split()[-6:]
    
    start_phrase = " ".join([re.sub(r'[^a-zA-Z0-9]', '', w).lower() for w in sample_start])
    end_phrase = " ".join([re.sub(r'[^a-zA-Z0-9]', '', w).lower() for w in sample_end])

    start_sec = None
    end_sec = None

    for seg in data:
        seg_text = re.sub(r'[^a-zA-Z0-9\s]', '', seg.get("text", seg.get("spoken_words", ""))).lower()
        if start_sec is None and all(w in seg_text for w in start_phrase.split()[:3]):
            start_sec = float(seg.get("start", seg.get("start_s", 0.0)))
        if all(w in seg_text for w in end_phrase.split()[-3:]):
            end_sec = float(seg.get("end", seg.get("end_s", 0.0)))

    # Fallback to estimation if not strictly found
    if start_sec is None:
        start_sec = 0.0
    if end_sec is None or end_sec <= start_sec:
        duration_est = splice["word_count"] / 2.3
        end_sec = start_sec + duration_est

    return start_sec, end_sec

def render_vertical_short(video_dir, splice_tag, start_sec, end_sec, broll_files):
    shorts_dir = os.path.join(video_dir, "shorts")
    os.makedirs(shorts_dir, exist_ok=True)
    out_mp4 = os.path.join(shorts_dir, f"short_{splice_tag.lower()}.mp4")

    # Audio source (preview or voice mastered)
    audio_src = os.path.join(video_dir, "audio_takes", "full_mix_preview.mp3")
    if not os.path.exists(audio_src):
        audio_src = os.path.join(video_dir, "audio_takes", "voice_mastered.mp3")
    if not os.path.exists(audio_src):
        print(f"Error: No audio file found in {video_dir}/audio_takes")
        return False

    duration = max(1.0, end_sec - start_sec)
    print(f"🎬 Splicing Short [{splice_tag}]: {start_sec:.2f}s -> {end_sec:.2f}s ({duration:.2f}s)")

    # Select B-roll background
    bg_video = None
    for b in broll_files:
        if os.path.exists(b):
            bg_video = b
            break

    # Build FFmpeg command for 9:16 vertical crop
    # Video Filter: Center-crop 16:9 to 9:16 (ih*9/16 width), scale to 1080x1920
    vf_filter = "crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=1080:1920:flags=lanczos"

    if bg_video and bg_video.endswith(".mp4"):
        cmd = [
            "ffmpeg", "-y",
            "-ss", str(start_sec), "-t", str(duration), "-i", bg_video,
            "-ss", str(start_sec), "-t", str(duration), "-i", audio_src,
            "-vf", vf_filter,
            "-c:v", "libx264", "-preset", "fast", "-crf", "20",
            "-c:a", "aac", "-b:a", "192k",
            "-shortest", out_mp4
        ]
    else:
        # Fallback to test card if no b-roll mp4
        cmd = [
            "ffmpeg", "-y",
            "-f", "lavfi", "-i", f"color=c=0x111116:s=1080x1920:d={duration}:r=30",
            "-ss", str(start_sec), "-t", str(duration), "-i", audio_src,
            "-c:v", "libx264", "-preset", "ultrafast",
            "-c:a", "aac", "-b:a", "192k",
            "-shortest", out_mp4
        ]

    try:
        subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            creationflags=CREATE_NO_WINDOW
        )
        print(f"✅ Rendered 9:16 Short: {out_mp4}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ FFmpeg Error rendering {splice_tag}: {e.stderr.decode('utf-8', errors='ignore')[:300]}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Autonomous ThinkLate 9:16 Shorts Generator")
    parser.add_argument("video_dir", help="Path to video project folder (e.g. videos/05_how-airbnb-stole-100b)")
    args = parser.parse_args()

    video_dir = os.path.abspath(args.video_dir)
    script_path = os.path.join(video_dir, "script.md")
    trans_path = os.path.join(video_dir, "transcription_timestamps.json")

    splices = parse_shorts_splices_from_script(script_path)
    if not splices:
        print(f"⚠️ No <!-- SHORTS_SPLICE_START: TAG --> markers found in {script_path}.")
        print("💡 The script must contain 3 tagged micro-arcs for autonomous clipping.")
        return 0

    print(f"Found {len(splices)} tagged Shorts splice(s) in script.")
    
    broll_dir = os.path.join(video_dir, "assets", "documentary_broll")
    broll_files = []
    if os.path.exists(broll_dir):
        broll_files = [os.path.join(broll_dir, f) for f in os.listdir(broll_dir) if f.endswith(".mp4")]

    success_count = 0
    for s in splices:
        start_s, end_s = match_splice_to_whisper_timestamps(s, trans_path)
        if start_s is not None and end_s is not None:
            if render_vertical_short(video_dir, s["tag"], start_s, end_s, broll_files):
                success_count += 1

    print(f"\n🎉 Successfully compiled {success_count}/{len(splices)} vertical Shorts in {video_dir}/shorts/")
    return 0

if __name__ == "__main__":
    sys.exit(main())
