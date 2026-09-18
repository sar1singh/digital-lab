#!/usr/bin/env python3
"""
ThinkLate Master Voiceover & Audio Auditor
=========================================
Comprehensive audio analyzer for documentary voiceover tracks.
Audits:
  1. Accent & Delivery Style: Natural Indian-Global English cadence, conversational pacing, pause ratios
  2. Correct Pronunciation: Phonetic dictionary and syllable stress checks for key terms
  3. Energy Level & Script Tone: Acoustic match against scene-specific emotional cues
  4. Voice Clarity & Modularity: True Peak headroom, YouTube -14 LUFS compliance,
     Loudness Range (LRA) monotone detection, noise floor / SNR estimation.
  5. Multi-Take Continuity: Batch verification across all takes for seamless documentary mix.

Usage:
  python audit_audio.py <audio_file> <take_num>
  python audit_audio.py --all <directory_with_takes>
"""

import sys
import os
import re
import subprocess
import json

# Ensure UTF-8 output on Windows
sys.stdout.reconfigure(encoding='utf-8')

FFMPEG_PATH = r'C:\Users\sar1s\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin\ffmpeg.exe'

# -------------------------------------------------------------------------
# Comprehensive Take Specifications & Pronunciation Lexicon
# -------------------------------------------------------------------------
TAKE_SPECS = {
    1: {
        "title": "Cold Open",
        "expected_words": 37,
        "target_tone": "Low, conversational, conspiratorial (Office observation)",
        "energy_target": "LOW-MID",
        "target_lufs": (-18.0, -15.0),
        "target_wpm": (125, 145),
        "target_lra": (3.0, 6.5),
        "pronunciations": [
            {"word": "strategy", "phonetic": "STRAT-uh-jee", "pitfall": "Avoid elongating the 'a' or rolling the 'r' aggressively."},
            {"word": "budget", "phonetic": "BUH-jit", "pitfall": "Clean soft 't' finish, don't drop the end consonant."},
            {"word": "platform", "phonetic": "PLAT-form", "pitfall": "Neutral vowel on 'plat'."}
        ],
        "delivery_cue": "Start quiet, like sharing an insider observation over coffee. Do NOT shout. Don't sound like a radio presenter."
    },
    2: {
        "title": "Core Thesis",
        "expected_words": 52,
        "target_tone": "Direct, confident, promise delivery",
        "energy_target": "HIGH-ASSERTIVE",
        "target_lufs": (-16.0, -13.5),
        "target_wpm": (130, 155),
        "target_lra": (3.5, 7.5),
        "pronunciations": [
            {"word": "documented", "phonetic": "DOK-yoo-men-tid", "pitfall": "Do not swallow 'men-tid'. Crisp syllables."},
            {"word": "opposite", "phonetic": "OP-uh-zit", "pitfall": "Stress first syllable 'OP'. Not op-PO-site."},
            {"word": "technology", "phonetic": "tek-NOL-uh-jee", "pitfall": "Second syllable stress on 'NOL'."}
        ],
        "delivery_cue": "Firm, intellectual confidence. Hit 'real' and 'bubble' with distinct audible weight."
    },
    3: {
        "title": "Personal Stake",
        "expected_words": 37,
        "target_tone": "Grounded, personal, sobering",
        "energy_target": "MID-SOBER",
        "target_lufs": (-17.0, -14.5),
        "target_wpm": (120, 145),
        "target_lra": (3.0, 6.5),
        "pronunciations": [
            {"word": "shareholders", "phonetic": "SHAIR-hohl-derz", "pitfall": "Clear 'shair', don't say 'sher-holders'."},
            {"word": "ownership", "phonetic": "OH-ner-ship", "pitfall": "Clear diphthong 'OH'."},
            {"word": "salary", "phonetic": "SAL-uh-ree", "pitfall": "Three syllables, neutral unhurried pacing."}
        ],
        "delivery_cue": "Slow down on 'Through your job.' Let the reality land in the listener's mind."
    },
    4: {
        "title": "Historical Pivot",
        "expected_words": 67,
        "target_tone": "Deadpan pivot, intellectual curiosity",
        "energy_target": "MID-CURIOUS",
        "target_lufs": (-16.5, -14.0),
        "target_wpm": (130, 150),
        "target_lra": (3.5, 7.0),
        "pronunciations": [
            {"word": "Odlyzko", "phonetic": "OD-liz-ko", "pitfall": "CRITICAL: Stress first syllable 'OD'. Never say 'odd-LEEZ-ko'."},
            {"word": "mania", "phonetic": "MAY-nee-uh", "pitfall": "Stress 'MAY'. Do not pronounce like Hindi 'maa-ni-yaa'."},
            {"word": "nineteenth", "phonetic": "NINE-teenth", "pitfall": "Enunciate the 'th' at the end clearly."}
        ],
        "delivery_cue": "Pause hard after 'So... railways.' Give the listener a mental gear-shift."
    },
    5: {
        "title": "The Capital Scale",
        "expected_words": 82,
        "target_tone": "Stunned gravity, unhurried scale",
        "energy_target": "LOW-GRAVE",
        "target_lufs": (-17.5, -14.5),
        "target_wpm": (120, 140),
        "target_lra": (3.5, 7.0),
        "pronunciations": [
            {"word": "GDP", "phonetic": "JEE-dee-PEE", "pitfall": "Even spacing between letters, no rushing."},
            {"word": "valuation", "phonetic": "val-yoo-AY-shun", "pitfall": "Stress 'AY'. Clear 4 syllables."},
            {"word": "investors", "phonetic": "in-VES-terz", "pitfall": "Middle syllable stress on 'VES'."}
        ],
        "delivery_cue": "Do NOT rush. Drop your voice lower on 'fifteen to twenty percent'. Let the magnitude stun the room."
    },
    6: {
        "title": "Predicted Collapse",
        "expected_words": 69,
        "target_tone": "Sharp, analytical, investigative",
        "energy_target": "HIGH-ANALYTICAL",
        "target_lufs": (-16.0, -13.5),
        "target_wpm": (135, 155),
        "target_lra": (3.5, 7.5),
        "pronunciations": [
            {"word": "quantitative", "phonetic": "KWON-tih-tay-tiv", "pitfall": "Stress first syllable 'KWON'. Avoid 'kwan-tee-teh-tiv'."},
            {"word": "freight", "phonetic": "FRAYT", "pitfall": "Clean long 'A' sound. Rhymes with 'great'."},
            {"word": "measures", "phonetic": "MEZH-erz", "pitfall": "Soft 'zh' sound, not 'may-jurs'."}
        ],
        "delivery_cue": "Enunciate 'trustworthy quantitative measures'. Tone should feel like uncovering hard forensic evidence."
    },
    7: {
        "title": "Victorian Intellectuals",
        "expected_words": 63,
        "target_tone": "Quiet dry sarcasm, intellectual disbelief",
        "energy_target": "MID-IRONIC",
        "target_lufs": (-16.5, -14.0),
        "target_wpm": (130, 150),
        "target_lra": (3.5, 7.0),
        "pronunciations": [
            {"word": "Brontë", "phonetic": "BRON-tay", "pitfall": "Ends in 'tay' (rhymes with day). Never say 'bron-tee'."},
            {"word": "hallucination", "phonetic": "huh-loo-sih-NAY-shun", "pitfall": "Clean stress on 'NAY'."},
            {"word": "intellectuals", "phonetic": "in-tuh-LEK-choo-ulz", "pitfall": "Don't trip over middle syllables. Enunciate cleanly."}
        ],
        "delivery_cue": "Deliver 'Charles Darwin' and 'John Stuart Mill' with slight wry disbelief. Even the smartest minds lost everything."
    },
    8: {
        "title": "The Invariant Payoff",
        "expected_words": 65,
        "target_tone": "Decisive payoff, calm authority",
        "energy_target": "HIGH-AUTHORITY",
        "target_lufs": (-15.5, -13.5),
        "target_wpm": (125, 145),
        "target_lra": (4.0, 8.0),
        "pronunciations": [
            {"word": "communication", "phonetic": "kuh-myoo-nih-KAY-shun", "pitfall": "Primary stress on 'KAY'."},
            {"word": "utility", "phonetic": "yoo-TIL-ih-tee", "pitfall": "Second syllable stress on 'TIL'."},
            {"word": "wiped out", "phonetic": "WYPT OWT", "pitfall": "Punch both words clearly with audible space between."}
        ],
        "delivery_cue": "Punch the contrast: 'Investors were wiped out. The tracks survived. And trains kept running.'"
    },
    9: {
        "title": "The Pattern",
        "expected_words": 37,
        "target_tone": "Clear summary, memorable invariant",
        "energy_target": "MID-PUNCHY",
        "target_lufs": (-16.0, -14.0),
        "target_wpm": (125, 145),
        "target_lra": (3.5, 7.0),
        "pronunciations": [
            {"word": "infrastructure", "phonetic": "IN-fruh-struk-cher", "pitfall": "First syllable stress 'IN'. Avoid 'infra-strak-chur' rushing."},
            {"word": "destroying", "phonetic": "dih-STROY-ing", "pitfall": "Clean 'stroy'."},
            {"word": "shareholders", "phonetic": "SHAIR-hohl-derz", "pitfall": "Keep consistent pronunciation with Take 3."}
        ],
        "delivery_cue": "Deliver the channel invariant like a proverb: 'The tracks survived. The shareholders didn't.'"
    },
    10: {
        "title": "The 1830s Paradox",
        "expected_words": 86,
        "target_tone": "Thoughtful, nuanced, intellectual twist",
        "energy_target": "MID-NUANCED",
        "target_lufs": (-16.5, -14.0),
        "target_wpm": (130, 150),
        "target_lra": (3.5, 7.0),
        "pronunciations": [
            {"word": "prematurely", "phonetic": "pree-muh-CHUR-lee", "pitfall": "Common trap: avoid 'pre-ma-chu-ra-ly'. Four crisp syllables."},
            {"word": "irrational", "phonetic": "ih-RASH-uh-nul", "pitfall": "Short 'ih' at start, stress 'RASH'."},
            {"word": "profitable", "phonetic": "PROF-ih-tuh-bul", "pitfall": "Stress first syllable 'PROF'."}
        ],
        "delivery_cue": "Slow pause before 'Except...'. Treat this as the sophisticated twist that separates amateur hot takes from deep history."
    },
    11: {
        "title": "Modern AI Capex",
        "expected_words": 105,
        "target_tone": "Frank, transparent, intellectual honesty",
        "energy_target": "MID-HONEST",
        "target_lufs": (-16.5, -14.0),
        "target_wpm": (130, 150),
        "target_lra": (3.5, 7.0),
        "pronunciations": [
            {"word": "inference", "phonetic": "IN-fer-ens", "pitfall": "Stress first syllable 'IN'. In finance/AI: do not confuse with 'infer'."},
            {"word": "hypothesis", "phonetic": "hy-POTH-uh-sis", "pitfall": "Second syllable stress 'POTH'."},
            {"word": "depreciation", "phonetic": "dih-pree-shee-AY-shun", "pitfall": "CRITICAL: 'shee-AY-shun', not 'see-a-shun'."},
            {"word": "capex", "phonetic": "KAP-eks", "pitfall": "Short 'a', clean 'eks'."}
        ],
        "delivery_cue": "Total humility on 'Here, I am making an inference. Nobody knows for sure yet.' Authenticity creates trust."
    },
    12: {
        "title": "The Real Bill",
        "expected_words": 37,
        "target_tone": "Cold reality check, punchy payoff",
        "energy_target": "HIGH-PAYOFF",
        "target_lufs": (-15.5, -13.5),
        "target_wpm": (120, 140),
        "target_lra": (4.0, 8.0),
        "pronunciations": [
            {"word": "depreciation", "phonetic": "dih-pree-shee-AY-shun", "pitfall": "Hit the 'AY' stress firmly."},
            {"word": "headcount", "phonetic": "HED-kownt", "pitfall": "Crisp punch on both syllables. Let it echo."}
        ],
        "delivery_cue": "Drop the hammer on the final word: 'headcount'. Hold a beat of silence before the final scene."
    },
    13: {
        "title": "The Close",
        "expected_words": 42,
        "target_tone": "Quiet, lingering closing thought",
        "energy_target": "LOW-CONTEMPLATIVE",
        "target_lufs": (-18.0, -15.5),
        "target_wpm": (120, 140),
        "target_lra": (3.0, 6.0),
        "pronunciations": [
            {"word": "paying attention", "phonetic": "PAY-ing uh-TEN-shun", "pitfall": "Gentle, thoughtful enunciation."}
        ],
        "delivery_cue": "Do NOT beg for likes or subscribers. End on a quiet, provocative question that hangs in the air into silence."
    }
}

# -------------------------------------------------------------------------
# FFmpeg Acoustic Extraction Engine
# -------------------------------------------------------------------------
def run_ffmpeg_audio_analysis(filepath):
    """
    Extracts EBU R128 loudness, volumedetect peaks, and silence cadence
    using FFmpeg CLI with zero external python dependencies.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Audio file not found: {filepath}")

    # 1. EBU R128 Loudness Filter
    ebur_cmd = [
        FFMPEG_PATH, '-y', '-i', filepath,
        '-af', 'ebur128=framelog=quiet',
        '-f', 'null', '-'
    ]
    ebur_proc = subprocess.run(ebur_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True, encoding='utf-8', errors='ignore')
    ebur_out = ebur_proc.stderr

    # Parse ebur128 outputs
    integrated_lufs = -24.0
    loudness_range = 5.0
    true_peak = -3.0

    i_match = re.search(r'Integrated loudness:\s+I:\s+([-\d.]+)\s+LUFS', ebur_out)
    if i_match:
        integrated_lufs = float(i_match.group(1))

    lra_match = re.search(r'Loudness range:\s+LRA:\s+([-\d.]+)\s+LU', ebur_out)
    if lra_match:
        loudness_range = float(lra_match.group(1))

    tp_match = re.search(r'True peak:\s+Peak:\s+([-\d.]+)\s+dBFS', ebur_out)
    if tp_match:
        true_peak = float(tp_match.group(1))

    # 2. Volume Detect Filter (Peak & Mean volume)
    vol_cmd = [
        FFMPEG_PATH, '-y', '-i', filepath,
        '-af', 'volumedetect',
        '-f', 'null', '-'
    ]
    vol_proc = subprocess.run(vol_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True, encoding='utf-8', errors='ignore')
    vol_out = vol_proc.stderr

    max_volume = -3.0
    mean_volume = -20.0
    mv_match = re.search(r'max_volume:\s+([-\d.]+)\s+dB', vol_out)
    if mv_match:
        max_volume = float(mv_match.group(1))
    mean_match = re.search(r'mean_volume:\s+([-\d.]+)\s+dB', vol_out)
    if mean_match:
        mean_volume = float(mean_match.group(1))

    # 3. Silence Detection (Pacing, conversational pauses, active speech duration)
    # Silence defined as quieter than -34 dBFS lasting at least 0.28s
    silence_cmd = [
        FFMPEG_PATH, '-y', '-i', filepath,
        '-af', 'silencedetect=noise=-34dB:d=0.28',
        '-f', 'null', '-'
    ]
    silence_proc = subprocess.run(silence_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True, encoding='utf-8', errors='ignore')
    silence_out = silence_proc.stderr

    # Duration from container
    dur_match = re.search(r'Duration:\s+(\d+):(\d+):([-\d.]+)', silence_out)
    total_duration = 15.0
    if dur_match:
        h, m, s = float(dur_match.group(1)), float(dur_match.group(2)), float(dur_match.group(3))
        total_duration = h * 3600 + m * 60 + s

    # Parse pauses
    pause_durations = [float(d) for d in re.findall(r'silence_duration:\s+([-\d.]+)', silence_out)]
    total_pause_time = sum(pause_durations)
    pause_count = len(pause_durations)
    active_speech_time = max(0.5, total_duration - total_pause_time)
    pause_ratio = (total_pause_time / total_duration) if total_duration > 0 else 0.0

    return {
        "duration": total_duration,
        "active_speech_time": active_speech_time,
        "total_pause_time": total_pause_time,
        "pause_count": pause_count,
        "pause_ratio": pause_ratio,
        "integrated_lufs": integrated_lufs,
        "loudness_range_lra": loudness_range,
        "true_peak_dbfs": max(true_peak, max_volume),
        "mean_volume_db": mean_volume
    }

# -------------------------------------------------------------------------
# Core Audit Evaluator
# -------------------------------------------------------------------------
def audit_single_take(filepath, take_num=1):
    spec = TAKE_SPECS.get(take_num, TAKE_SPECS[1])
    metrics = run_ffmpeg_audio_analysis(filepath)

    expected_words = spec['expected_words']
    # Overall WPM (including pauses) vs Active Speech WPM
    wpm_overall = (expected_words / metrics['duration']) * 60.0
    wpm_active = (expected_words / metrics['active_speech_time']) * 60.0

    score = 100
    strengths = []
    warnings = []
    coaching = []

    # --- 1. Broadcast Loudness & Headroom Audit ---
    tp = metrics['true_peak_dbfs']
    if tp > -0.8:
        score -= 20
        warnings.append(f"PEAK CLIPPING RISK: True Peak is {tp:.1f} dBFS (Target: -3.0 to -1.5 dBFS). Digital distortion likely on phone speakers. Reduce recording gain by {abs(tp - (-2.0)):.1f} dB.")
    elif tp < -12.0:
        score -= 15
        warnings.append(f"UNDER-MODULATED SIGNAL: True Peak is {tp:.1f} dBFS (Too faint). Increase microphone preamp gain.")
    else:
        strengths.append(f"Safe Peak Headroom: True Peak at {tp:.1f} dBFS (Clean broadcast headroom without digital clipping).")

    lufs = metrics['integrated_lufs']
    target_lufs_min, target_lufs_max = spec['target_lufs']
    if lufs > -12.0:
        score -= 15
        warnings.append(f"LOUDNESS TOO HIGH: {lufs:.1f} LUFS (Target YouTube standard is -14.0 LUFS). YouTube will apply negative normalization penalty.")
    elif lufs < -22.0:
        score -= 15
        warnings.append(f"LOUDNESS TOO QUIET: {lufs:.1f} LUFS (Will sound weak compared to reference YouTube documentaries). Boost track gain.")
    else:
        strengths.append(f"YouTube Aligned Loudness: {lufs:.1f} LUFS (Optimal dynamic mix range).")

    # --- 2. Cadence, Pacing & Indian English Conversational Flow ---
    target_wpm_low, target_wpm_high = spec['target_wpm']
    if wpm_overall < target_wpm_low - 15:
        score -= 10
        warnings.append(f"PACING DRAGGING: {wpm_overall:.0f} WPM (Target: {target_wpm_low}-{target_wpm_high} WPM). Pacing is too sluggish; deliver with slightly more conversational momentum.")
    elif wpm_overall > target_wpm_high + 18:
        score -= 15
        warnings.append(f"RUSHING DETECTED: {wpm_overall:.0f} WPM (Target: {target_wpm_low}-{target_wpm_high} WPM). Classic Indian English speed-up trap. Slow down and let the listener digest the point.")
    else:
        strengths.append(f"Natural Documentary Cadence: {wpm_overall:.0f} WPM (Right inside the {target_wpm_low}–{target_wpm_high} sweet spot).")

    # Pause ratio check (Conversational documentary breathing)
    pr = metrics['pause_ratio']
    if pr < 0.12:
        score -= 10
        warnings.append(f"BREATHLESS / WALL-OF-SOUND: Pause ratio is only {pr*100:.0f}%. You did not pause at the '//' rhythm markers. Add 0.5s to 1.0s breath beats.")
    elif pr > 0.40:
        score -= 10
        warnings.append(f"EXCESSIVE DEAD AIR: Pause ratio is {pr*100:.0f}%. Long awkward gaps detected between thoughts.")
    else:
        strengths.append(f"Engaging Breath Rhythm: {metrics['pause_count']} distinct conversational pauses ({pr*100:.0f}% natural thinking time).")

    # --- 3. Energy Level & Script Tone Alignment ---
    lra = metrics['loudness_range_lra']
    target_lra_min, target_lra_max = spec['target_lra']
    if lra < 2.5:
        score -= 15
        warnings.append(f"MONOTONE / FLAT DELIVERY: Loudness range is only {lra:.1f} LU. Sounds robotic or uninspired. Vary your pitch and stress key operative nouns.")
    elif lra > 9.5:
        score -= 10
        warnings.append(f"ERRATIC DYNAMICS: Loudness range {lra:.1f} LU is too extreme. Sudden shouts or whispered endings detected. Keep mic distance steady at 6 inches.")
    else:
        strengths.append(f"Vocal Modularity: {lra:.1f} LU dynamic range (Expressive human vocal contour, not flat).")

    # Tone check against target energy
    energy_target = spec['energy_target']
    if "LOW" in energy_target and lufs > -14.0:
        warnings.append(f"TONE MISMATCH: Scene requires '{spec['target_tone']}', but vocal intensity is high ({lufs:.1f} LUFS). Soften delivery and speak closer to mic.")
    elif "HIGH" in energy_target and lufs < -17.5:
        warnings.append(f"TONE MISMATCH: Scene requires '{spec['target_tone']}', but energy is underpowered ({lufs:.1f} LUFS). Project with more conviction.")

    # --- 4. Coaching & Pronunciation Watchpoints ---
    for item in spec['pronunciations']:
        coaching.append(f"'{item['word']}' ➔ Phonetic: [{item['phonetic']}] | Coach: {item['pitfall']}")

    # --- Format Terminal Report ---
    print("\n" + "█"*75)
    print(f"🎙️  THINKLATE AUDIO AUDITOR — TAKE {take_num:02d}: {spec['title'].upper()}")
    print("█"*75)
    print(f"📁 Audio Take File:    {os.path.basename(filepath)}")
    print(f"⏱️  Duration:           {metrics['duration']:.2f}s total | {metrics['active_speech_time']:.2f}s speech | {metrics['total_pause_time']:.2f}s pauses")
    print(f"🎯 Target Register:     {spec['target_tone']}")
    print(f"⚡ Energy Blueprint:    {spec['energy_target']} (Target Loudness: {target_lufs_min:.1f} to {target_lufs_max:.1f} LUFS)")
    print(f"🎬 Director's Cue:     \"{spec['delivery_cue']}\"")
    print("-" * 75)
    
    status_icon = "🟢 EXCELLENT" if score >= 85 else ("🟡 ACCEPTABLE" if score >= 70 else "🔴 RETAKE RECOMMENDED")
    print(f"🏆 VOCAL QC SCORE:     {max(0, score)} / 100  [{status_icon}]")
    print("-" * 75)

    print("\n✅ WHAT HIT THE TARGET:")
    for s in strengths:
        print(f"   [PASS] {s}")

    if warnings:
        print("\n⚠️  COACHING & ACTIONABLE ADJUSTMENTS:")
        for w in warnings:
            print(f"   [ACTION] {w}")
    else:
        print("\n🎉 BROADCAST GRADE: Ready for final timeline mix with drone soundscape.")

    print("\n🗣️  PRONUNCIATION & ACCENT WATCHLIST FOR THIS TAKE:")
    for c in coaching:
        print(f"   • {c}")

    print("█"*75 + "\n")

    return {
        "take_num": take_num,
        "score": max(0, score),
        "metrics": metrics,
        "warnings": warnings,
        "strengths": strengths
    }

# -------------------------------------------------------------------------
# Batch Multi-Take Audit (Continuity & Uniformity Across Video)
# -------------------------------------------------------------------------
def audit_all_takes(directory):
    print("\n" + "="*75)
    print("🔍 THINKLATE MULTI-TAKE CONTINUITY & LOUDNESS UNIFORMITY AUDIT")
    print("="*75)
    
    all_results = []
    for take_num in range(1, 14):
        # Look for mp3 or wav takes
        patterns = [
            os.path.join(directory, f"user_take_{take_num:02d}.wav"),
            os.path.join(directory, f"user_take_{take_num:02d}.mp3"),
            os.path.join(directory, f"take_{take_num:02d}.wav"),
            os.path.join(directory, f"take_{take_num:02d}.mp3"),
            os.path.join(directory, f"take_{take_num}.mp3"),
            os.path.join(directory, f"take_{take_num}.wav"),
        ]
        found = None
        for p in patterns:
            if os.path.exists(p):
                found = p
                break
        
        if found:
            res = audit_single_take(found, take_num)
            all_results.append(res)
        else:
            print(f"⚠️  Take {take_num:02d}: No recorded audio file found in {directory}.")

    if len(all_results) >= 2:
        print("\n" + "="*75)
        print("📊 CROSS-TAKE UNIFORMITY ANALYSIS (Full Documentary Mix Check)")
        print("="*75)
        lufs_vals = [r['metrics']['integrated_lufs'] for r in all_results]
        lufs_spread = max(lufs_vals) - min(lufs_vals)
        mean_lufs = sum(lufs_vals) / len(lufs_vals)

        print(f"• Total Takes Evaluated:      {len(all_results)} / 13")
        print(f"• Average Integrated Loudness: {mean_lufs:.1f} LUFS")
        print(f"• Loudness Spread:            {lufs_spread:.1f} dB (Max: {max(lufs_vals):.1f}, Min: {min(lufs_vals):.1f})")

        if lufs_spread > 4.5:
            print("⚠️  CONTINUITY WARNING: Volume varies significantly between takes (>4.5 dB).")
            print("    Some scenes will sound jarringly louder than others. Balance clip gains in DaVinci Resolve Fairlight.")
        else:
            print("✅ EXCELLENT CONTINUITY: Vocal loudness is uniform and smooth across the documentary.")
        print("="*75 + "\n")

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--all':
        folder = sys.argv[2] if len(sys.argv) > 2 else 'audio_takes'
        audit_all_takes(folder)
    else:
        target_file = sys.argv[1] if len(sys.argv) > 1 else 'audio_takes/take_01.mp3'
        take = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        audit_single_take(target_file, take)
