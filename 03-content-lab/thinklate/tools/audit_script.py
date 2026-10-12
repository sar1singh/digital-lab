#!/usr/bin/env python3
"""
ThinkLate Automated Script QC Gate
Audits script markdown files against ThinkLate vocal profile:
- Maximum 12 words per sentence/breath chunk
- Banned phrases & academic jargon check
- Breath markers presence (// and ///)
- Spoken word count and runtime estimation (target: 130-140 WPM)
"""

import sys
import os
import re

# Ensure UTF-8 output on Windows consoles
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BANNED_PHRASES = [
    # Regional / culturally specific slang
    'repo man', 'tow truck', 'foreclose', 'foreclosure', 'credit score',
    # Jargon / academic constructs
    'quantitative easing', 'quote-unquote', 'quote unquote', 'illusion',
    'mechanic', 'leverage', 'fiscal', 'monetary', 'sovereign', 'gross domestic',
    'fiat', 'aircraft carrier', 'groans', 'as we all know', 'in conclusion',
    # Difficult pronunciation / tongue-twisters (Video 2 finding)
    'bullion', 'cantillon', 'seigniorage', 'denarius', 'debasement'
]


def audit_script(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        sys.exit(1)

    with open(filepath, 'r', encoding='utf-8') as f:
        raw_lines = f.readlines()

    raw_text = "".join(raw_lines)

    # Clean text for speech analysis
    clean_text = re.sub(r'\[.*?\]', '', raw_text)      # remove stage directions [VISUAL: ...]
    clean_text = re.sub(r'#.*', '', clean_text)          # remove markdown headers
    clean_text = re.sub(r'\*[^*]*\*', '', clean_text)    # remove italics/metadata notes
    
    # Calculate spoken words
    spoken_words = [w for w in clean_text.replace('//', ' ').replace('///', ' ').split() if re.search(r'[a-zA-Z0-9]', w)]
    total_spoken_words = len(spoken_words)
    runtime_mins_135 = total_spoken_words / 135.0

    print("=" * 60)
    print(" THINKLATE SCRIPT AUDIT REPORT")
    print(f" File: {filepath}")
    print(f" Spoken Words: {total_spoken_words}")
    print(f" Estimated Runtime: {runtime_mins_135:.2f} min ({int(runtime_mins_135)}m {int((runtime_mins_135%1)*60)}s) @ 135 WPM")
    print("=" * 60)

    # 1. Banned words check
    banned_violations = []
    for line_idx, line in enumerate(raw_lines, 1):
        if line.strip().startswith('#') or line.strip().startswith('['):
            continue
        line_lower = line.lower()
        for banned in BANNED_PHRASES:
            if banned in line_lower:
                banned_violations.append((line_idx, banned, line.strip()))

    print(f"\n1. BANNED PHRASE AUDIT: {len(banned_violations)} violation(s)")
    if banned_violations:
        for idx, phrase, line in banned_violations:
            print(f"   Line {idx:3d}: [{phrase}] -> \"{line}\"")
    else:
        print("   [PASS] Zero banned phrases found.")

    # 2. Sentence Length Check (Max 12 words between breath markers)
    chunks = re.split(r'///|//|\n\n+', clean_text)
    length_violations = []
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk:
            continue
        words = [w for w in chunk.split() if re.search(r'[a-zA-Z0-9]', w)]
        if len(words) > 12:
            length_violations.append((len(words), chunk))

    print(f"\n2. 12-WORD SENTENCE CAP AUDIT: {len(length_violations)} violation(s)")
    if length_violations:
        for word_count, snippet in length_violations[:10]:
            disp = snippet[:80] + '...' if len(snippet) > 80 else snippet
            print(f"   [{word_count:2d} words] \"{disp}\"")
        if len(length_violations) > 10:
            print(f"   ... and {len(length_violations) - 10} more.")
    else:
        print("   [PASS] All breath chunks are <= 12 words.")

    # 3. Breath Marker Density Check
    pause_half_count = raw_text.count('//') - raw_text.count('///') * 1  # approximate
    pause_full_count = raw_text.count('///')
    print(f"\n3. BREATH MARKER DENSITY:")
    print(f"   Half-beat pauses (//): {pause_half_count}")
    print(f"   Full stop resets (///): {pause_full_count}")
    if pause_half_count < 10 or pause_full_count < 10:
        print("   [WARNING] Low breath marker count. Ensure pauses are embedded.")
    else:
        print("   [PASS] Adequate breath marker pacing.")

    # Final verdict
    print("\n" + "=" * 60)
    passed = (len(banned_violations) == 0) and (len(length_violations) == 0)
    if passed:
        print(" [OVERALL RESULT] PASSED! Script ready for recording deck generation.")
    else:
        print(" [OVERALL RESULT] FAILED! Resolve violations before final recording.")
    print("=" * 60)

    return 0 if passed else 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python audit_script.py <path_to_script.md>")
        sys.exit(1)
    sys.exit(audit_script(sys.argv[1]))
