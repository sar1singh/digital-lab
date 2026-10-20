"""
Off Script Episode 01 — Automated Audio & Video Trimming Timeline Engine
Trims all silence gaps > 20s down to a balanced 20-second Game Audio Breathing Gap
(10s natural room tone decay + 10s pre-speech anticipation).

Outputs:
1. take1_trimmed.mp3 — Master 41-minute voiceover track.
2. ep01_timeline_cuts.edl — Standard EDL for DaVinci Resolve / Premiere.
3. ep01_timeline_cuts.csv — Human-readable cut list with original vs trimmed timecodes.
4. render_trimmed_video.ps1 — 1-click FFmpeg script to render the matching trimmed 41m video.
5. updated_chapters_trimmed.md — Recalculated YouTube chapter markers.
"""

import os
import sys
import json
import subprocess
from pathlib import Path

BASE_DIR = Path("03-content-lab/off-script/episodes/01_acbf_havana")
AUDIO_FILE = BASE_DIR / "audio" / "take1.mp3"
VIDEO_FILE = Path(r"C:\Users\sar1s\Documents\MyWork\YOUTUBE\#final_videos\ACBF_Full_GamePlay_1.mp4")
METRICS_FILE = BASE_DIR / "analysis" / "speech_audit_metrics.json"

OUT_AUDIO = BASE_DIR / "audio" / "take1_trimmed.mp3"
OUT_EDL = BASE_DIR / "analysis" / "ep01_timeline_cuts.edl"
OUT_CSV = BASE_DIR / "analysis" / "ep01_timeline_cuts.csv"
OUT_SCRIPT = BASE_DIR / "analysis" / "render_trimmed_video.ps1"
OUT_CHAPTERS = BASE_DIR / "analysis" / "chapters_trimmed.md"

def format_tc(sec, fps=60):
    hrs = int(sec // 3600)
    mins = int((sec % 3600) // 60)
    secs = int(sec % 60)
    frames = int(round((sec - int(sec)) * fps))
    if frames >= fps:
        frames = fps - 1
    return f"{hrs:02d}:{mins:02d}:{secs:02d}:{frames:02d}"

def format_mmss(sec):
    hrs = int(sec // 3600)
    mins = int((sec % 3600) // 60)
    secs = int(sec % 60)
    if hrs > 0:
        return f"{hrs:02d}:{mins:02d}:{secs:02d}"
    return f"{mins:02d}:{secs:02d}"

def main():
    if not AUDIO_FILE.exists():
        print(f"Error: {AUDIO_FILE} not found!")
        sys.exit(1)

    with open(METRICS_FILE, "r", encoding="utf-8") as f:
        metrics = json.load(f)

    silences = metrics["pause_statistics"]["major_silences"]
    total_dur = metrics["total_duration_sec"]

    # Calculate cuts: clamp each silence > 20s to exactly 20s
    cuts = []
    for s in silences:
        dur = s["duration"]
        if dur > 20.0:
            c_start = round(s["start"] + 10.0, 3)
            c_end = round(s["end"] - 10.0, 3)
            cuts.append({
                "start": c_start,
                "end": c_end,
                "duration": round(c_end - c_start, 3),
                "orig_timecode": s["timecode"]
            })

    # Derive keep segments
    keeps = []
    cur = 0.0
    for c in cuts:
        if c["start"] > cur:
            keeps.append({
                "start": cur,
                "end": c["start"],
                "duration": round(c["start"] - cur, 3)
            })
        cur = c["end"]
    if cur < total_dur:
        keeps.append({
            "start": cur,
            "end": total_dur,
            "duration": round(total_dur - cur, 3)
        })

    trimmed_dur = sum(k["duration"] for k in keeps)
    print(f"Original Duration: {format_mmss(total_dur)} ({total_dur:.2f}s)")
    print(f"Trimmed Duration:  {format_mmss(trimmed_dur)} ({trimmed_dur:.2f}s)")
    print(f"Excess Silence Cut: {format_mmss(total_dur - trimmed_dur)} ({total_dur - trimmed_dur:.2f}s)")
    print(f"Kept Segments:     {len(keeps)}")

    # 1. Generate CSV Cut Sheet
    csv_lines = [
        "Segment_ID,Orig_Start_Sec,Orig_End_Sec,Orig_Timecode_Range,Duration_Sec,Trimmed_Timeline_In,Trimmed_Timeline_Out"
    ]
    running_in = 0.0
    for i, k in enumerate(keeps, 1):
        s = k["start"]
        e = k["end"]
        dur = k["duration"]
        t_in = running_in
        t_out = running_in + dur
        running_in = t_out
        csv_lines.append(f"{i},{s:.3f},{e:.3f},{format_mmss(s)} - {format_mmss(e)},{dur:.3f},{format_mmss(t_in)},{format_mmss(t_out)}")

    with open(OUT_CSV, "w", encoding="utf-8") as f:
        f.write("\n".join(csv_lines))
    print(f"Saved CSV: {OUT_CSV}")

    # 2. Generate DaVinci Resolve / Premiere EDL
    edl_lines = [
        "TITLE: OFF_SCRIPT_EP01_TRIMMED",
        "FCM: NON-DROP FRAME",
        ""
    ]
    running_rec_in = 0.0
    for i, k in enumerate(keeps, 1):
        src_in = format_tc(k["start"])
        src_out = format_tc(k["end"])
        rec_in = format_tc(running_rec_in)
        rec_out = format_tc(running_rec_in + k["duration"])
        running_rec_in += k["duration"]
        edl_lines.append(f"{i:03d}  AX       AA/V  C        {src_in} {src_out} {rec_in} {rec_out}")
        edl_lines.append(f"* FROM CLIP NAME: ACBF_Full_GamePlay_1.mp4")
        edl_lines.append("")

    with open(OUT_EDL, "w", encoding="utf-8") as f:
        f.write("\n".join(edl_lines))
    print(f"Saved EDL: {OUT_EDL}")

    # 3. Recalculate YouTube Chapters
    raw_chapters = [
        (0.0, "The 3 Tiers of Identity Crisis (Personal, Societal, Civilizational)"),
        (148.0, "School Bullying: The Scars Nobody Talks About"),
        (264.0, "Arcade Era Nostalgia: Tekken 3, Mustafa & 8-Bit Cartridges"),
        (450.0, "AC Black Flag in 2026 vs Modern Gaming (One Piece Soul)"),
        (560.0, "The 1:30 AM WhatsApp Chat: Why Corporate Jobs Can't Free You"),
        (645.0, "The Unspoken Reality: Expelled from School Assembly for Fees"),
        (730.0, "Bullying Below the Poverty Line & Fetching Balls from Gutters"),
        (911.0, "Childhood Trauma as the Root of Modern Adult Crisis"),
        (1486.0, "The Corporate Rat Race, Office Gossip & Illusions of Friendship"),
        (1627.0, "Why Absolute Freedom Doesn't Exist in 2026"),
        (1958.0, "Doflamingo's Law: Whoever Wins Becomes Justice"),
        (2084.0, "Carrying Water Buckets & Sacrifices of Middle-Class Parents"),
        (2257.0, "Civilizational Trauma: Invasions & The British Mental Slavery Model"),
        (2495.0, "Macaulay's 1835 Minute on Education: Brown Skin, British Minds"),
        (2657.0, "Manufactured Social Divisions & The Ellora Kailasa Temple Truth"),
        (2769.0, "The Erosion of Indigenous Philosophy: Dharma, Karma & Moksha"),
        (3309.0, "The Professional Riot & Mob Outrage Industry"),
        (3420.0, "Who Truly Pays the Bill? The Auto Driver & Honest Taxpayer"),
        (3500.0, "Desh Sabse Pehle (Nation First)"),
        (3698.0, "Human Consciousness vs Animal Instincts"),
        (3895.0, "The Viewpoint & Off Script Sign-Off")
    ]

    def map_to_trimmed(orig_t):
        removed = 0.0
        for c in cuts:
            if orig_t >= c["end"]:
                removed += c["duration"]
            elif orig_t > c["start"]:
                removed += (orig_t - c["start"])
                break
        return orig_t - removed

    ch_lines = [
        "# Off Script Episode 01 — Recalculated YouTube Chapters (Trimmed 41m Master)",
        f"**Source Runtime:** {format_mmss(total_dur)} $\\rightarrow$ **Trimmed Runtime:** {format_mmss(trimmed_dur)}\n",
        "```text",
        "TIMESTAMPS:"
    ]
    for orig_t, title in raw_chapters:
        new_t = map_to_trimmed(orig_t)
        ch_lines.append(f"{format_mmss(new_t)} - {title}")
    ch_lines.append("```")

    with open(OUT_CHAPTERS, "w", encoding="utf-8") as f:
        f.write("\n".join(ch_lines))
    print(f"Saved Chapters: {OUT_CHAPTERS}")

    # 4. Generate FFmpeg Batch Trim Command for Video & Audio
    # Build filter_complex string for FFmpeg video + audio trimming
    v_segments = []
    a_segments = []
    for i, k in enumerate(keeps):
        v_segments.append(f"[0:v]trim=start={k['start']}:end={k['end']},setpts=PTS-STARTPTS[v{i}];")
        a_segments.append(f"[0:a]atrim=start={k['start']}:end={k['end']},asetpts=PTS-STARTPTS[a{i}];")

    concat_v = "".join(f"[v{i}]" for i in range(len(keeps))) + f"concat=n={len(keeps)}:v=1:a=0[outv];"
    concat_a = "".join(f"[a{i}]" for i in range(len(keeps))) + f"concat=n={len(keeps)}:v=0:a=1[outa]"

    ps1_content = f"""# Off Script Episode 01 — 1-Click Video & Audio Render Script
# Trims excess dead air from ACBF_Full_GamePlay_1.mp4 and take1.mp3 in exact sync

$VideoSrc = "{VIDEO_FILE}"
$AudioSrc = "{AUDIO_FILE}"
$MasterOut = "C:\\Users\\sar1s\\Documents\\MyWork\\YOUTUBE\\#final_videos\\ACBF_OffScript_Ep01_41M_Master.mp4"
$TrimmedAudioOut = "{OUT_AUDIO}"

Write-Host "Rendering Trimmed Master Video (41m 08s)..." -ForegroundColor Cyan

# 1. Render Trimmed Audio Track
ffmpeg -y -i "$AudioSrc" -filter_complex "{''.join(a_segments)}{''.join(f'[a{i}]' for i in range(len(keeps)))}concat=n={len(keeps)}:v=0:a=1[outa]" -map "[outa]" -b:a 192k "$TrimmedAudioOut"

Write-Host "Trimmed audio rendered successfully to: $TrimmedAudioOut" -ForegroundColor Green

# 2. Render Trimmed Master Video (NVENC hardware accelerated)
# Uses NVIDIA RTX GPU for ultra-fast encoding
ffmpeg -y -hwaccel cuda -i "$VideoSrc" -i "$TrimmedAudioOut" -filter_complex "{''.join(v_segments)}{concat_v}" -map "[outv]" -map 1:a -c:v h264_nvenc -preset p4 -b:v 18M -c:a aac -b:a 192k "$MasterOut"

Write-Host "Finished! Master 41-minute video rendered to: $MasterOut" -ForegroundColor Green
"""

    with open(OUT_SCRIPT, "w", encoding="utf-8") as f:
        f.write(ps1_content)
    print(f"Saved Script: {OUT_SCRIPT}")

    # 5. Execute audio trimming directly right now using FFmpeg!
    print("\nExecuting FFmpeg audio trimming now...")
    audio_concat_filter = "".join(f"[0:a]atrim=start={k['start']}:end={k['end']},asetpts=PTS-STARTPTS[a{i}];" for i, k in enumerate(keeps))
    audio_concat_filter += "".join(f"[a{i}]" for i in range(len(keeps))) + f"concat=n={len(keeps)}:v=0:a=1[outa]"

    cmd = [
        "ffmpeg", "-y", "-v", "warning",
        "-i", str(AUDIO_FILE),
        "-filter_complex", audio_concat_filter,
        "-map", "[outa]",
        "-c:a", "libmp3lame",
        "-b:a", "192k",
        str(OUT_AUDIO)
    ]
    subprocess.run(cmd, check=True)
    print(f"[SUCCESS] Trimmed audio exported: {OUT_AUDIO}")

if __name__ == "__main__":
    main()
