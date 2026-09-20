---
name: thinklate-script-auditor
description: Scriptwriting and editorial auditing skill for ThinkLate documentaries. Enforces zero numerals in spoken lines, conversational Indian-Global English register, 15-second hook constraint, pause cadence notation, explicit tone directives, and runs automated script validation via audit_script.py.
---

# ThinkLate Script Auditor & Writer Skill

## Purpose
Enforces ThinkLate's high-prestige, conversational script standards. Transforms stiff corporate writing into natural, engaging spoken English that educated knowledge workers speak over coffee.

## Automated Verification
Always run the script auditor script to lint the script:
```bash
python digital-lab/03-content-lab/thinklate/videos/<video_slug>/audit_script.py digital-lab/03-content-lab/thinklate/videos/<video_slug>/script.md
```

## Mandatory Standards
1. **Zero Numeral Rule:**
   - 0 bare digits (`\b\d+\b`) allowed in spoken narration.
   - Numbers must be spelled out phonetically (*"fifteen to twenty percent"*, *"three hundred to four hundred billion"*).
2. **15-Second Hook Rule:**
   - Take 1 must contain **under 38 words** (~16s at 135 WPM).
   - Must hook the viewer's everyday workplace/salary reality before introducing historical or technical subjects.
3. **Conversational Rhythm Markers:**
   - `//` = Short breath pause (0.3s–0.5s).
   - `///` = Clause pause (0.8s–1.0s).
   - `////` = Major section breath (1.5s–2.0s).
4. **Director Tone Directives:**
   - Every single take must have an explicit `⟨TONE: ...⟩` directive defining the emotional register.
5. **Zero Algorithmic Begging:**
   - Strictly no spoken "like and subscribe" or "hit the bell". Subscriptions are earned through intellectual respect.
6. **Word Count & Floor Tier Runtime:**
   - 650–850 spoken words total (landing at 5.5 to 6.5 minutes at 135 WPM).
