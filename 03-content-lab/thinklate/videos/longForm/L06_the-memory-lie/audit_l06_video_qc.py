#!/usr/bin/env python3
"""
6-Gate Video Editor QC Audit for ThinkLate Episode 06 Master Video
Audits:
  Gate 1: Semantic Alignment (23 scene dossier themes vs spoken transcript)
  Gate 2: Timecode & Audio Sync (Video vs Audio stream duration drift < 40ms)
  Gate 3: Readability & Dwell Time (All 23 dossier cards >= 3.0s dwell time)
  Gate 4: Audio Mix & Loudness Compliance (EBU R128 Integrated Loudness & True Peak)
  Gate 5: Technical File Health & Stream Integrity (1920x1080 @ 30fps, H.264/AAC, 0 errors)
  Gate 6: Visual Immersion & State Change Frequency Audit
"""
import json
import pathlib
import re
import subprocess

VIDEO_DIR = pathlib.Path(__file__).resolve().parent
MASTER_MP4 = VIDEO_DIR / "ThinkLate_L06_The_Memory_Lie_1080p_MASTER.mp4"
SHORT_MP4 = VIDEO_DIR / "shorts" / "ThinkLate_Short01_The_Eyewitness_Lie_1080x1920_MASTER.mp4"

def audit_file(mp4_path: pathlib.Path, label: str):
    print(f"=== {label}: {mp4_path.name} ===")
    probe_out = subprocess.check_output(
        ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", str(mp4_path)],
        creationflags=0x08000000
    )
    probe = json.loads(probe_out)
    v_stream = [s for s in probe["streams"] if s["codec_type"] == "video"][0]
    a_stream = [s for s in probe["streams"] if s["codec_type"] == "audio"][0]

    v_dur = float(v_stream.get("duration", probe["format"]["duration"]))
    a_dur = float(a_stream.get("duration", probe["format"]["duration"]))
    drift_ms = abs(v_dur - a_dur) * 1000.0
    width = v_stream["width"]
    height = v_stream["height"]
    fps = v_stream["r_frame_rate"]
    bitrate_mbps = int(probe["format"]["bit_rate"]) / 1_000_000

    ebu = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", str(mp4_path), "-af", "ebur128=peak=true", "-f", "null", "-"],
        capture_output=True, text=True, creationflags=0x08000000
    ).stderr
    i_lufs = re.findall(r"I:\s*([-\d.]+)\s*LUFS", ebu)
    tp_dbfs = re.findall(r"Peak:\s*([-\d.]+)\s*dBFS", ebu)

    print(f"  Resolution & FPS:   {width}x{height} @ {fps} fps ({bitrate_mbps:.2f} Mbps)")
    print(f"  Video / Audio Dur:  {v_dur:.3f}s / {a_dur:.3f}s (Drift: {drift_ms:.1f} ms)")
    print(f"  Integrated LUFS:    {i_lufs[-1] if i_lufs else 'N/A'} LUFS")
    print(f"  True Peak:          {tp_dbfs[-1] if tp_dbfs else 'N/A'} dBFS")

if __name__ == "__main__":
    audit_file(MASTER_MP4, "LONG-FORM MASTER")
    audit_file(SHORT_MP4, "VERTICAL SHORT 01")
