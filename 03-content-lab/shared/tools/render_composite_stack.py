#!/usr/bin/env python3
"""
Shared Multi-Layer Visual Composite Engine (Rule 23)
=====================================================
Assembles multi-layer broadcast composites where every single frame contains
3+ simultaneous, complex motion layers:
  - Layer 1 (Base): Living gameplay or stock video canvas
  - Layer 2 (Focus): Selective Gaussian blur (sigma 10-16)
  - Layer 3 (Primary Card): Animated Remotion evidence card / chart / radar
  - Layer 4 (Micro-Motion): Concurrent Remotion typography slam or metric badge

Ensures ZERO static frames across all video pipelines.
"""

import os
import sys
import json
import shutil
import argparse
import subprocess

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
if sys.stderr.encoding != 'utf-8':
    try:
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0

def get_headless_kwargs():
    kwargs = {}
    if sys.platform == "win32":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = 0  # SW_HIDE
        kwargs["startupinfo"] = startupinfo
        kwargs["creationflags"] = CREATE_NO_WINDOW
    return kwargs

DEFAULT_GAMEPLAY = r"C:\Users\sar1s\Documents\MyWork\YOUTUBE\#final_videos\ACBF_Gameplay_2.mp4"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RENDER_MOTION = os.path.join(SCRIPT_DIR, "render_motion.py")

def render_remotion_element(template, props, out_path, frame=None):
    cmd = [
        sys.executable, RENDER_MOTION,
        "--template", template,
        "--out", out_path,
        "--props", json.dumps(props)
    ]
    if frame is not None:
        cmd.extend(["--frame", str(frame)])
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **get_headless_kwargs())
    return res.returncode == 0

def composite_layers(background_path, primary_path, secondary_path, output_path, blur_sigma=12.0, duration=4.0):
    output_path = os.path.abspath(output_path)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    is_video = output_path.lower().endswith((".mp4", ".mov", ".mkv"))

    inputs = []
    # Input 0: Background
    if background_path.lower().endswith((".mp4", ".mov", ".mkv")):
        inputs.extend(["-ss", "180", "-t", str(duration), "-i", background_path])
    else:
        if is_video:
            inputs.extend(["-loop", "1", "-t", str(duration), "-i", background_path])
        else:
            inputs.extend(["-i", background_path])

    # Input 1: Primary Motion Card (PNG or MP4)
    if is_video and primary_path.lower().endswith((".png", ".jpg")):
        inputs.extend(["-loop", "1", "-t", str(duration), "-i", primary_path])
    else:
        inputs.extend(["-i", primary_path])

    # Input 2: Secondary Micro-Motion Card (if present)
    if secondary_path and os.path.exists(secondary_path):
        if is_video and secondary_path.lower().endswith((".png", ".jpg")):
            inputs.extend(["-loop", "1", "-t", str(duration), "-i", secondary_path])
        else:
            inputs.extend(["-i", secondary_path])

    # Filter graph construction:
    filter_parts = [
        f"[0:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,gblur=sigma={blur_sigma}[bg]"
    ]

    if secondary_path and os.path.exists(secondary_path):
        filter_parts.append("[bg][1:v]overlay=0:0:shortest=1[layer1]")
        filter_parts.append("[layer1][2:v]overlay=0:0:shortest=1[outv]")
        map_out = "[outv]"
    else:
        filter_parts.append("[bg][1:v]overlay=0:0:shortest=1[outv]")
        map_out = "[outv]"

    filter_complex = ";".join(filter_parts)

    cmd = ["ffmpeg", "-y"] + inputs + [
        "-filter_complex", filter_complex,
        "-map", map_out
    ]

    if is_video:
        cmd.extend([
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            "-preset", "veryfast",
            "-crf", "18",
            "-r", "30",
            output_path
        ])
    else:
        cmd.extend([
            "-vframes", "1",
            output_path
        ])

    print(f"🎬 Compiling Multi-Layer Composite -> {os.path.basename(output_path)}...")
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **get_headless_kwargs())
    if res.returncode == 0 and os.path.exists(output_path):
        print(f"✅ Multi-Layer Composite Complete: {output_path}")
        return True
    else:
        print(f"❌ FFmpeg Composite Failed:\n{res.stderr.decode('utf-8', errors='ignore')[:400]}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Multi-Layer 3+ Motion Stack Composite Builder")
    parser.add_argument("--primary", required=True, help="Primary Remotion Template ID")
    parser.add_argument("--primary-props", default="{}", help="JSON props for primary template")
    parser.add_argument("--secondary", default=None, help="Secondary concurrent Remotion Template ID")
    parser.add_argument("--secondary-props", default="{}", help="JSON props for secondary template")
    parser.add_argument("--background", default=DEFAULT_GAMEPLAY, help="Track 1 Living Background path")
    parser.add_argument("--blur", type=float, default=12.0, help="Track 2 Gaussian blur sigma (default: 12)")
    parser.add_argument("--duration", type=float, default=4.0, help="Duration in seconds (default: 4)")
    parser.add_argument("--out", required=True, help="Output file path (.mp4 or .png)")
    parser.add_argument("--channel", default="thinklate", help="Channel theme (thinklate, offscript, sarwanology)")
    args = parser.parse_args()

    temp_dir = os.path.join(SCRIPT_DIR, ".tmp_composite")
    os.makedirs(temp_dir, exist_ok=True)

    is_video = args.out.lower().endswith((".mp4", ".mov", ".mkv"))
    layer_ext = ".mov" if is_video else ".png"
    layer_frame = None if is_video else 45

    try:
        p_props = json.loads(args.primary_props)
    except Exception:
        p_props = {}
    p_props["channel"] = args.channel

    primary_tmp = os.path.join(temp_dir, f"primary_{args.primary}{layer_ext}")
    print(f"Rendering Primary Layer: {args.primary} ({'Animated ProRes 4444' if is_video else 'Still Frame'})...")
    if not render_remotion_element(args.primary, p_props, primary_tmp, frame=layer_frame):
        print(f"Failed to render primary layer {args.primary}")
        sys.exit(1)

    secondary_tmp = None
    if args.secondary:
        try:
            s_props = json.loads(args.secondary_props)
        except Exception:
            s_props = {}
        s_props["channel"] = args.channel
        secondary_tmp = os.path.join(temp_dir, f"secondary_{args.secondary}{layer_ext}")
        print(f"Rendering Secondary Layer: {args.secondary} ({'Animated ProRes 4444' if is_video else 'Still Frame'})...")
        if not render_remotion_element(args.secondary, s_props, secondary_tmp, frame=layer_frame):
            print(f"Failed to render secondary layer {args.secondary}")
            sys.exit(1)

    success = composite_layers(
        background_path=args.background,
        primary_path=primary_tmp,
        secondary_path=secondary_tmp,
        output_path=args.out,
        blur_sigma=args.blur,
        duration=args.duration
    )

    try:
        shutil.rmtree(temp_dir, ignore_errors=True)
    except Exception:
        pass

    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
