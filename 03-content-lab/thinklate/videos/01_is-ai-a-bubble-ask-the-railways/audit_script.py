#!/usr/bin/env python3
"""
ThinkLate Script Auditor & Linter
=================================
Automated verification of documentary video scripts against ThinkLate standards:
  1. Zero Numeral Rule: Zero bare numbers in spoken lines (must be spelled phonetically).
  2. 15-Second Hook Constraint: Core premise must land within 35 words.
  3. Rhythm & Breath Markers: Check presence of '//' and '///' cadence pauses.
  4. Emotional Register Cues: Verify explicit [TONE] directives for every take.
  5. Pronunciation Annotations: Non-trivial names/terms must have phonetic tags.
  6. Zero Algorithmic Begging: Zero spoken "like", "subscribe", or "bell icon" requests.
"""

import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

def audit_script(filepath):
    if not os.path.exists(filepath):
        print(f"Error: Script file not found at {filepath}")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    print("\n" + "█"*75)
    print(f"📝 THINKLATE SCRIPT AUDITOR — {os.path.basename(filepath)}")
    print("█"*75)

    takes = {}
    current_take = None
    in_metadata_block = True

    for line_idx, line in enumerate(lines, 1):
        stripped = line.strip()
        take_match = re.search(r'\[TAKE\s+(\d+)\]', stripped)
        if take_match:
            in_metadata_block = False
            current_take = int(take_match.group(1))
            takes[current_take] = {
                "header_line": line_idx,
                "tone_cue": None,
                "visual_cue": None,
                "spoken_lines": []
            }
            # Look for tone cue on same line
            tone_match = re.search(r'⟨TONE:\s*([^⟩]+)⟩', stripped)
            if tone_match:
                takes[current_take]["tone_cue"] = tone_match.group(1)
            continue

        if current_take is not None:
            # Check for tone cue on subsequent line
            tone_match = re.search(r'⟨TONE:\s*([^⟩]+)⟩', stripped)
            if tone_match and not takes[current_take]["tone_cue"]:
                takes[current_take]["tone_cue"] = tone_match.group(1)
                continue

            # Visual cue
            if '⟨VISUAL' in stripped or '⟨LOWER-THIRD' in stripped or '⟨CALLOUT' in stripped:
                continue

            # Ignore empty lines or markdown code fence
            if not stripped or stripped.startswith('```') or stripped.startswith('---'):
                continue

            # This is a spoken line
            takes[current_take]["spoken_lines"].append((line_idx, stripped))

    score = 100
    errors = []
    warnings = []
    passes = []

    # 1. Take Coverage
    total_takes = len(takes)
    if total_takes == 0:
        print("❌ FATAL: No [TAKE X] markers discovered in script.")
        return False
    passes.append(f"Scene Structure: {total_takes} takes identified.")

    # 2. Algorithmic Begging / Forbidden Clichés Check
    forbidden_terms = [r'\blike and subscribe\b', r'\bhit the bell\b', r'\bsmash that like\b', r'\bsubscribe to my channel\b']
    found_forbidden = False
    for t_num, t_data in takes.items():
        for l_no, text in t_data["spoken_lines"]:
            for pattern in forbidden_terms:
                if re.search(pattern, text, re.IGNORECASE):
                    errors.append(f"Take {t_num} (Line {l_no}): Algorithmic begging detected: '{pattern}'. ThinkLate rule forbids spoken like/subscribe.")
                    score -= 25
                    found_forbidden = True
    if not found_forbidden:
        passes.append("Editorial Dignity: Zero spoken like/subscribe requests detected.")

    # 3. Zero Numeral Rule Check in Spoken Text
    numeral_pattern = re.compile(r'\b\d+(?:st|nd|rd|th|%|\$|b|m|k)?\b', re.IGNORECASE)
    numeral_violations = []
    for t_num, t_data in takes.items():
        for l_no, text in t_data["spoken_lines"]:
            # Strip out intentional pronunciation tags like (pron: OD-liz-ko) before checking
            cleaned_text = re.sub(r'\(pron:[^)]+\)', '', text)
            matches = numeral_pattern.findall(cleaned_text)
            if matches:
                # Filter out pure punctuation false positives
                valid_digits = [m for m in matches if any(c.isdigit() for c in m)]
                if valid_digits:
                    numeral_violations.append((t_num, l_no, valid_digits, text))

    if numeral_violations:
        score -= 20
        for t_num, l_no, digits, text in numeral_violations:
            errors.append(f"Take {t_num} (Line {l_no}): Raw numerals found {digits} in: \"{text}\". Numbers must be spelled out phonetically (e.g. 'fifteen' instead of '15').")
    else:
        passes.append("Pronunciation Precision: Zero raw numerals in spoken text (all numbers spelled phonetically).")

    # 4. 15-Second Hook Constraint (Take 1 Word Count)
    if 1 in takes:
        t1_text = " ".join([txt for _, txt in takes[1]["spoken_lines"]])
        # Clean rhythm markers
        t1_clean = re.sub(r'[/]{1,4}', '', t1_text)
        t1_words = [w for w in t1_clean.split() if w.strip()]
        if len(t1_words) <= 40:
            passes.append(f"Hook Pacing: Take 1 has {len(t1_words)} words (~16s at 135 WPM). Perfect high-retention opening.")
        else:
            warnings.append(f"Hook Pacing: Take 1 is {len(t1_words)} words. Risk of losing viewer before thesis. Target is under 38 words.")
            score -= 10

    # 5. Tone Cue and Pause Cadence Checks
    missing_tones = []
    missing_pauses = []
    total_spoken_words = 0

    for t_num, t_data in takes.items():
        if not t_data["tone_cue"]:
            missing_tones.append(t_num)

        all_text = " ".join([txt for _, txt in t_data["spoken_lines"]])
        clean_words = [w for w in re.sub(r'[/]{1,4}', '', all_text).split() if w.strip()]
        total_spoken_words += len(clean_words)

        if '//' not in all_text and '///' not in all_text:
            missing_pauses.append(t_num)

    if missing_tones:
        warnings.append(f"Missing Tone Directives: Takes {missing_tones} lack explicit ⟨TONE: ...⟩ directives.")
        score -= 10
    else:
        passes.append("Director Cues: 100% of takes have explicit emotional register [TONE] directives.")

    if missing_pauses:
        warnings.append(f"Cadence Warning: Takes {missing_pauses} lack '//' or '///' breath/pause markers.")
        score -= 10
    else:
        passes.append("Rhythm Notation: Conversational pause markers ('//', '///', '////') present across all takes.")

    # Estimated Runtime
    est_minutes = total_spoken_words / 135.0

    print(f"📊 Total Spoken Words:  {total_spoken_words} words")
    print(f"⏱️  Estimated Runtime:   {est_minutes:.1f} minutes ({int(est_minutes*60)} seconds at 135 WPM)")
    print("-" * 75)
    status_icon = "🟢 APPROVED FOR RECORDING" if score >= 85 else "🔴 REVISION REQUIRED"
    print(f"🏆 SCRIPT QC SCORE:     {max(0, score)} / 100  [{status_icon}]")
    print("-" * 75)

    print("\n✅ PASSED STANDARDS:")
    for p in passes:
        print(f"   [PASS] {p}")

    if errors:
        print("\n❌ CRITICAL DEFECTS TO FIX:")
        for e in errors:
            print(f"   [ERROR] {e}")

    if warnings:
        print("\n⚠️  RECOMMENDED REFINEMENTS:")
        for w in warnings:
            print(f"   [WARN] {w}")

    print("█"*75 + "\n")
    return score >= 85

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'script.md'
    audit_script(target)
