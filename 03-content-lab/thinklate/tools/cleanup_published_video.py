#!/usr/bin/env python3
"""
ThinkLate Post-Publishing Workspace Cleanup & Git Sync Engine
============================================================
Safely purges transient intermediate render caches, temporary segments,
and scratch audio takes while strictly preserving all broadcast masters,
scripts, decks, thumbnails, and metadata.

Usage:
    python tools/cleanup_published_video.py <video_slug> [--push]

Example:
    python tools/cleanup_published_video.py 100_percent_debt_paradox --push
"""

import os
import sys
import shutil
import subprocess

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

def get_dir_size(path):

    total = 0
    if not os.path.exists(path):
        return 0
    for root, dirs, files in os.walk(path):
        for f in files:
            fp = os.path.join(root, f)
            if not os.path.islink(fp):
                total += os.path.getsize(fp)
    return total

def cleanup_video(slug, auto_git=False):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_dir = os.path.join(base_dir, "videos", slug)

    if not os.path.exists(target_dir):
        print(f"[!] Error: Target video directory not found: {target_dir}")
        return False

    print(f"🧹 Commencing Post-Publishing Cleanup for: {slug}")
    initial_size = get_dir_size(target_dir)

    # 1. Purge render_cache/ (intermediate segment chunks)
    render_cache = os.path.join(target_dir, "render_cache")
    if os.path.exists(render_cache):
        rc_size = get_dir_size(render_cache)
        shutil.rmtree(render_cache)
        os.makedirs(render_cache, exist_ok=True)
        print(f"  ✓ Purged render_cache/ ({rc_size / (1024*1024):.2f} MB freed)")

    # 2. Purge temp_segments/
    temp_segs = os.path.join(target_dir, "temp_segments")
    if os.path.exists(temp_segs):
        ts_size = get_dir_size(temp_segs)
        shutil.rmtree(temp_segs)
        print(f"  ✓ Purged temp_segments/ ({ts_size / (1024*1024):.2f} MB freed)")

    # 3. Purge duplicate scratch takes while keeping master vocal & final mix
    audio_dir = os.path.join(target_dir, "audio_takes")
    if os.path.exists(audio_dir):
        for item in os.listdir(audio_dir):
            if item in ["test_synth.wav", "voice_mastered_std.wav", "full_mix_voice_and_ambient.wav"]:
                fpath = os.path.join(audio_dir, item)
                fsize = os.path.getsize(fpath)
                os.remove(fpath)
                print(f"  ✓ Purged scratch audio: {item} ({fsize / (1024*1024):.2f} MB freed)")

    # 4. Remove __pycache__ and temp files
    for root, dirs, files in os.walk(target_dir):
        for d in dirs:
            if d == "__pycache__":
                shutil.rmtree(os.path.join(root, d))
        for f in files:
            if f.endswith(".tmp") or f == "Thumbs.db":
                try:
                    os.remove(os.path.join(root, f))
                except Exception:
                    pass

    final_size = get_dir_size(target_dir)
    freed_mb = (initial_size - final_size) / (1024 * 1024)
    print(f"🎉 Cleanup Complete! Total disk space reclaimed: {freed_mb:.2f} MB")
    print(f"📦 Final Archive Size: {final_size / (1024*1024):.2f} MB")

    # 5. Git Commit & Push if requested
    if auto_git:
        git_dir = os.path.dirname(os.path.dirname(base_dir))
        print("\n🚀 Executing Git Sync...")
        subprocess.run(["git", "add", "."], cwd=base_dir, check=False)
        msg = f"chore(thinklate): post-publishing cleanup and asset sync for {slug}"
        subprocess.run(["git", "commit", "-m", msg], cwd=base_dir, check=False)
        push_res = subprocess.run(["git", "push", "origin", "main"], cwd=base_dir, capture_output=True, text=True)
        if push_res.returncode == 0:
            print("  ✓ Successfully pushed cleaned state to remote git repository!")
        else:
            print(f"  [!] Git push note: {push_res.stderr.strip()}")

    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cleanup_published_video.py <video_slug> [--push]")
        sys.exit(1)
    slug = sys.argv[1]
    push = "--push" in sys.argv
    cleanup_video(slug, auto_git=push)
