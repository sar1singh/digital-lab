"""
ThinkLate Audio Quality Control (QC) & Acoustic Auditor
Usage:
    python qc_audio.py <audio_file.wav> [--words <word_count>]
    python qc_audio.py --dir <directory_of_takes>
"""

import sys
import os
import wave
import array
import math
import argparse

def analyze_take(wav_path, word_count=None):
    if not os.path.exists(wav_path):
        print(f"Error: File not found: {wav_path}")
        return None

    with wave.open(wav_path, "rb") as wf:
        sr = wf.getframerate()
        ch = wf.getnchannels()
        nframes = wf.getnframes()
        dur = nframes / float(sr)
        raw = wf.readframes(nframes)
        
    # Ultra-fast unpack with array
    samples = array.array("h")
    samples.frombytes(raw)

    # Convert to mono if stereo
    if ch > 1:
        samples = samples[::ch]

    # Peak & RMS
    peak = max(abs(s) for s in samples) if samples else 0
    peak_db = 20 * math.log10(peak / 32768.0) if peak > 0 else -99
    
    # Subsample for fast RMS if file is large (> 1 min)
    step = 1 if len(samples) < 2000000 else 2
    sum_sq = sum(s * s for s in samples[::step])
    rms = math.sqrt(sum_sq / (len(samples) // step)) if samples else 0
    rms_db = 20 * math.log10(rms / 32768.0) if rms > 0 else -99

    # Pause detection (windows of 50ms)
    win_len = int(sr * 0.05)
    hop_len = int(sr * 0.025)
    silence_thresh = 32768.0 * (10 ** (-32 / 20)) # -32 dBFS

    silent_windows = 0
    total_windows = 0
    pauses = []
    curr_pause = 0

    for pos in range(0, len(samples) - win_len, hop_len):
        chunk = samples[pos : pos + win_len]
        p = max(abs(s) for s in chunk)
        total_windows += 1
        if p < silence_thresh:
            silent_windows += 1
            curr_pause += 1
        else:
            if curr_pause > 0:
                p_sec = curr_pause * (hop_len / sr)
                if p_sec >= 0.4:
                    pauses.append(p_sec)
                curr_pause = 0
    if curr_pause > 0:
        p_sec = curr_pause * (hop_len / sr)
        if p_sec >= 0.4:
            pauses.append(p_sec)

    silence_pct = (silent_windows / total_windows * 100) if total_windows > 0 else 0
    max_pause = max(pauses) if pauses else 0.0
    long_hesitations = [p for p in pauses if p >= 1.4]

    # WPM
    wpm = (word_count / (dur / 60.0)) if word_count and dur > 0 else None

    # Score calculation (100 base)
    score = 100
    penalties = []

    # Headroom check
    if peak_db > -0.5:
        score -= 25
        penalties.append(f"Clipping Danger! Peak is {peak_db:.1f} dBFS (Target: -1.5 dBFS)")
    elif peak_db < -6.0:
        score -= 15
        penalties.append(f"Low Input Gain. Peak is {peak_db:.1f} dBFS (Too quiet)")

    # RMS check
    if rms_db < -22.0:
        score -= 15
        penalties.append(f"Low Vocal Energy. RMS is {rms_db:.1f} dBFS (Target: -15 to -18 dBFS)")
    elif rms_db > -13.0:
        score -= 15
        penalties.append(f"Over-compressed or Too Loud. RMS is {rms_db:.1f} dBFS")

    # Hesitation check
    if len(long_hesitations) > 2:
        score -= 10 * len(long_hesitations)
        penalties.append(f"{len(long_hesitations)} long pauses/hesitations (>1.4s) detected! Momentum is draining.")

    # WPM check
    if wpm:
        if wpm > 165:
            score -= 15
            penalties.append(f"Pacing Rushed! {wpm:.0f} WPM (Target: 130-145 WPM)")
        elif wpm < 115:
            score -= 15
            penalties.append(f"Pacing Dragging! {wpm:.0f} WPM (Target: 130-145 WPM)")

    score = max(0, score)
    return {
        "file": os.path.basename(wav_path),
        "duration": dur,
        "peak_db": peak_db,
        "rms_db": rms_db,
        "silence_pct": silence_pct,
        "pauses_count": len(pauses),
        "max_pause": max_pause,
        "long_hesitations": len(long_hesitations),
        "wpm": wpm,
        "score": score,
        "penalties": penalties
    }

def print_report(res):
    print("=" * 70)
    print(f" THINKLATE AUDIO QC REPORT: {res['file']}")
    print("=" * 70)
    print(f" Duration:            {res['duration']:.2f} seconds ({res['duration']/60:.2f} min)")
    print(f" True Peak Ceiling:   {res['peak_db']:.1f} dBFS  (Target: -1.5 dBFS)")
    print(f" Average Vocal RMS:   {res['rms_db']:.1f} dBFS  (Target: -16.0 dBFS)")
    print(f" Silence / Pause %:   {res['silence_pct']:.1f}%")
    print(f" Meaningful Pauses:   {res['pauses_count']} (Max pause: {res['max_pause']:.2f}s)")
    if res['wpm']:
        print(f" Cadence (WPM):       {res['wpm']:.1f} WPM  (Target: 130-145 WPM)")
    print("-" * 70)
    
    if res['score'] >= 85:
        grade = "PASSED (Broadcast Grade)"
    elif res['score'] >= 70:
        grade = "WARNING (Review Hesitations / EQ)"
    else:
        grade = "FAILED (Re-take or Heavy Edit Required)"
        
    print(f" QC Overall Score:    {res['score']} / 100  ->  {grade}")
    
    if res['penalties']:
        print("\n Actionable Flags:")
        for p in res['penalties']:
            print(f"   * {p}")
    else:
        print("\n Clean Take: Ready for timeline assembly!")
    print("=" * 70)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ThinkLate Audio QC")
    parser.add_argument("file", nargs="?", help="Path to .wav file")
    parser.add_argument("--words", type=int, help="Optional word count for WPM verification")
    parser.add_argument("--dir", help="Audit all .wav files in a directory")
    args = parser.parse_args()

    if args.dir:
        files = [os.path.join(args.dir, f) for f in os.listdir(args.dir) if f.endswith(".wav")]
        files.sort()
        print(f"Auditing {len(files)} takes in {args.dir}...\n")
        for f in files:
            res = analyze_take(f)
            if res:
                print(f"[{res['score']:3d}/100] {res['file']:<25} Peak: {res['peak_db']:5.1f}dB | RMS: {res['rms_db']:5.1f}dB | MaxPause: {res['max_pause']:4.1f}s")
    elif args.file:
        res = analyze_take(args.file, args.words)
        if res:
            print_report(res)
    else:
        parser.print_help()
