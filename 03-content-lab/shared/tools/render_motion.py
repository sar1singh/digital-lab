#!/usr/bin/env python3
"""
ThinkLate Motion Graphics CLI Bridge (Remotion Engine)
======================================================
Renders broadcast-grade 2026 UI motion cards, animated evidence highlights, 
and typography slams headlessly via Remotion + React.

Replaces obsolete Python PIL drawing scripts permanently.

Usage Examples:
    # 1. Render still frame (PNG) of an Evidence Card
    python render_motion_card.py --template EvidenceCard \
        --props '{"title": "OCTOBER 2007", "quote": "Your rent is $1,150. You have three days before your landlord kicks you out and your bank account is empty.", "highlightWords": "three days before your landlord kicks you out"}' \
        --out ../videos/05_how-airbnb-stole-100b/assets/card_eviction.png --frame 45

    # 2. Render MP4 video of Metric Counter
    python render_motion_card.py --template MetricCounter \
        --props '{"label": "CEREAL REVENUE", "startVal": 0, "endVal": 30000, "prefix": "$"}' \
        --out ../videos/05_how-airbnb-stole-100b/assets/counter_cereal.mp4
"""

import os
import sys
import json
import shutil
import subprocess
import argparse

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

# Strict Headless Window Suppression for Windows
CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0

def get_headless_subprocess_kwargs():
    kwargs = {}
    if sys.platform == "win32":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = 0  # SW_HIDE
        kwargs["startupinfo"] = startupinfo
        kwargs["creationflags"] = CREATE_NO_WINDOW
    return kwargs

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
if os.path.exists(os.path.join(os.path.dirname(TOOLS_DIR), "motion_engine")):
    ENGINE_DIR = os.path.join(os.path.dirname(TOOLS_DIR), "motion_engine")
else:
    ENGINE_DIR = os.path.join(TOOLS_DIR, "motion_engine")
ENTRY_FILE = os.path.join(ENGINE_DIR, "src", "index.ts")

def render_motion_card(template_id, props_dict, output_path, frame=None):
    output_path = os.path.abspath(output_path)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    props_json = json.dumps(props_dict)
    
    is_still = output_path.lower().endswith((".png", ".jpg", ".jpeg")) or (frame is not None)
    
    npx_bin = shutil.which("npx.cmd") or shutil.which("npx") or "npx"

    cmd = [npx_bin, "remotion"]
    if is_still:
        target_frame = frame if frame is not None else 45
        cmd.extend(["still", ENTRY_FILE, template_id, output_path, f"--frame={target_frame}"])
    else:
        cmd.extend(["render", ENTRY_FILE, template_id, output_path])
        
    cmd.append(f"--props={props_json}")

    print(f"Rendering [{template_id}] -> {os.path.basename(output_path)}...")
    try:
        kwargs = get_headless_subprocess_kwargs()
        res = subprocess.run(
            cmd,
            cwd=ENGINE_DIR,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False,
            **kwargs
        )
        if res.returncode != 0:
            print(f"Remotion Render Failed (Code {res.returncode}):")
            print("STDOUT:", res.stdout.decode('utf-8', errors='ignore'))
            print("STDERR:", res.stderr.decode('utf-8', errors='ignore'))
            return False
        print(f"Successfully rendered: {output_path}")
        return True
    except Exception as e:
        print(f"Remotion Execution Exception: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="ThinkLate Remotion Motion Graphics Bridge")
    parser.add_argument("--template", required=True, help="Remotion Composition ID (e.g. EvidenceCard, AnimatedBarChart, AnimatedLineChart, NewspaperSlider, DocumentRedaction, SocialCitation, StatDonutGauge, TornPaperReceipt, TypographySlam, TypewriterBlink, GlitchDecoder, HighlighterWipe, WordByWordPop, SplitWordCollision, StrikethroughSlam, FloatingPillBadge, Perspective3DTilt, StaggeredWave)")
    parser.add_argument("--props", default="{}", help="JSON string of component props")
    parser.add_argument("--out", required=True, help="Output file path (.png, .mp4)")
    parser.add_argument("--frame", type=int, default=None, help="Frame number for still image render (default: 45)")
    args = parser.parse_args()

    try:
        props = json.loads(args.props)
    except Exception as e:
        print(f"Error parsing props JSON: {e}")
        sys.exit(1)

    success = render_motion_card(args.template, props, args.out, frame=args.frame)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
