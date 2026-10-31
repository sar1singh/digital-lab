#!/usr/bin/env python3
"""
ThinkLate / Off Script / Sarwanology Universal Story Script QC Gate
Enforces the 5 Universal Storytelling Laws & Adversarial Council Rules:
  1. Zero rigid 'Act/Chapter' syllabus markers
  2. Zero teacher/lecturer clichés ('Do the math', 'Three moves', etc.)
  3. Zero hypothetical detached openings ('Imagine you buy...', 'Picture this...')
  4. Zero self-help checklist endings ('One... Two... Three...')
  5. Mandatory 12-word breath marker caps (// and ///)
  6. Mandatory diegetic Foley sound cues and dead-air drops
"""

import sys
import os
import re

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BANNED_SYLLABUS = [
    r'\bact\s+\d+\b', r'\bchapter\s+\d+\b', r'\bpart\s+\d+\b',
    r'\bsection\s+\d+\b', r'\bact\s+one\b', r'\bact\s+two\b',
    r'\bact\s+three\b', r'\bact\s+four\b'
]

BANNED_TEACHER_PHRASES = [
    'do the math', 'let me give you a picture first', 'here is your escape plan',
    'three moves', 'now let us examine', 'now let me explain', 'now you might think this is new',
    'so what does this look like for real people', 'here is the strange part',
    'so why is every ceo doing this', 'three tips', 'first move', 'second move', 'third move',
    'in conclusion', 'as we all know', 'to summarize', 'quote unquote', 'quote-unquote'
]

BANNED_DETACHED_HOOKS = [
    'imagine you buy', 'imagine you are', 'picture this', 'think about a time',
    'have you ever wondered', 'in today\'s video', 'today we are going to look at'
]

def audit_story_script(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        return 1

    with open(filepath, 'r', encoding='utf-8') as f:
        raw_lines = f.readlines()
    raw_text = "".join(raw_lines)

    # Clean text for speech analysis
    clean_text = re.sub(r'\[.*?\]', '', raw_text)      # remove stage directions [VISUAL: ...]
    clean_text = re.sub(r'#.*', '', clean_text)          # remove markdown headers
    clean_text = re.sub(r'\*[^*]*\*', '', clean_text)    # remove italics notes
    
    spoken_words = [w for w in clean_text.replace('//', ' ').replace('///', ' ').split() if re.search(r'[a-zA-Z0-9]', w)]
    total_spoken_words = len(spoken_words)
    runtime_mins_135 = total_spoken_words / 135.0

    print("=" * 70)
    print("🎬 UNIVERSAL STORY SCRIPT QC AUDIT")
    print(f"File: {filepath}")
    print(f"Spoken Words: {total_spoken_words} | Runtime: ~{runtime_mins_135:.2f} min ({int(runtime_mins_135)}m {int((runtime_mins_135%1)*60)}s @ 135 WPM)")
    print("=" * 70)

    violations = []

    # 1. Syllabus Marker Check
    for pattern in BANNED_SYLLABUS:
        matches = re.findall(pattern, raw_text, re.IGNORECASE)
        if matches:
            violations.append(f"CRITICAL: Found rigid syllabus marker: {set(matches)} (Banned).")

    # 2. Teacher Clichés Check
    for idx, line in enumerate(raw_lines, 1):
        if line.strip().startswith('#') or line.strip().startswith('['):
            continue
        line_lower = line.lower()
        for phrase in BANNED_TEACHER_PHRASES:
            if phrase in line_lower:
                violations.append(f"Line {idx}: Teacher cliché found: '{phrase}' -> \"{line.strip()}\"")

    # 3. Detached Hook Check (first 25 lines)
    opening_snippet = " ".join([l.lower() for l in raw_lines[:25] if not l.startswith('[') and not l.startswith('#')])
    for hook_phrase in BANNED_DETACHED_HOOKS:
        if hook_phrase in opening_snippet:
            violations.append(f"Opening Hook Violation: Detached hypothetical phrasing '{hook_phrase}' found. Must ground in real conflict/character.")

    # 4. Self-Help Checklist Ending Check (last 40 lines)
    ending_snippet = " ".join([l.lower() for l in raw_lines[-40:] if not l.startswith('[')])
    if re.search(r'\b(three moves|three steps|step 1|move 1|one\.\s+choose|two\.\s+back)\b', ending_snippet):
        violations.append("Ending Violation: Script ends like a self-help checklist. Must end in a narrative resolution & shattered worldview.")

    # 5. Sentence Length Check (Max 12 words between breath markers)
    chunks = re.split(r'///|//|\n\n+', clean_text)
    length_violations = []
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk:
            continue
        words = [w for w in chunk.split() if re.search(r'[a-zA-Z0-9]', w)]
        if len(words) > 12:
            length_violations.append((len(words), chunk))

    if length_violations:
        for w_count, snippet in length_violations[:5]:
            disp = snippet[:75] + '...' if len(snippet) > 75 else snippet
            violations.append(f"Pacing Violation: Breath chunk exceeded 12 words ({w_count} words): \"{disp}\"")

    # 6. Audio Foley Presence Check
    foley_count = len(re.findall(r'(?i)\[sfx:.*?\]', raw_text))
    if foley_count < 3:
        violations.append(f"Sound Design Violation: Only {foley_count} [SFX: ...] cues found. Must have at least 3 diegetic Foley cues.")

    # Print Results
    print(f"\nAUDIT FINDINGS: {len(violations)} violation(s)")
    if violations:
        for v in violations:
            print(f"  ❌ {v}")
        print("\n" + "=" * 70)
        print(" [RESULT] FAILED! Script violates Universal Storytelling Laws.")
        print("=" * 70)
        return 1
    else:
        print("  ✅ [PASS] Zero syllabus markers (No Act 1/2/3).")
        print("  ✅ [PASS] Zero teacher clichés.")
        print("  ✅ [PASS] Grounded character C-Hook.")
        print("  ✅ [PASS] Narrative resolution (No self-help checklist).")
        print("  ✅ [PASS] All breath chunks <= 12 words.")
        print(f"  ✅ [PASS] Adequate diegetic Foley cues ({foley_count} found).")
        print("\n" + "=" * 70)
        print(" [RESULT] PASSED! Script approved for production recording.")
        print("=" * 70)
        return 0

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "videos/04_the-subscription-trap/script_final.md"
    sys.exit(audit_story_script(target))
