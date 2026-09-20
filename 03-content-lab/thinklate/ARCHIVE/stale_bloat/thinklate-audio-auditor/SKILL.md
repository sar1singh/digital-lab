---
name: thinklate-audio-auditor
description: Voiceover acoustic analysis and sound design auditing skill for ThinkLate documentaries. Evaluates user-recorded voice takes via audit_audio.py for True Peak headroom, YouTube -14 LUFS compliance, Indian-Global English WPM cadence (130-150 WPM), phonetic pronunciation traps, dynamic vocal modulation (LRA), and atmospheric drone mix.
---

# ThinkLate Voiceover & Audio Auditor Skill

## Purpose
Ensures broadcast-grade vocal authority, conversational Indian-Global English cadence, clear phonetic enunciation, and immersive sound design.

## Automated Execution
Run the acoustic audit CLI tool against single takes or full take folders:
```bash
# Audit a single recorded take:
python digital-lab/03-content-lab/thinklate/videos/<video_slug>/audit_audio.py <audio_path> <take_num>

# Batch audit all takes for loudness continuity:
python digital-lab/03-content-lab/thinklate/videos/<video_slug>/audit_audio.py --all <directory_with_takes>
```

## Mandatory Acoustic Metrics
1. **Integrated Broadcast Loudness:**
   - Target: **-14.0 LUFS** (±1.0 LUFS) to align with YouTube's loudness normalizer.
2. **True Peak Headroom:**
   - Peak ceiling must stay between **-3.0 dBFS and -1.0 dBFS**. Zero digital clipping allowed.
3. **Pacing & WPM Cadence:**
   - Target: **130 to 150 Words Per Minute**.
   - Flag if < 115 WPM (dragging) or > 165 WPM (rushing Indian English trap).
4. **Conversational Breathing Ratio:**
   - **15% to 30%** of total scene duration must be natural pauses/breaths (`//`, `///`).
5. **Vocal Modulation (LRA):**
   - Loudness Range must stay between **3.0 and 7.5 LU**.
   - Below 2.5 LU = flat, robotic delivery. Above 9.5 LU = erratic shouting/whispering.
6. **Pronunciation & Accent Watchpoints:**
   - Phonetic enunciation guides checked per take (*Odlyzko*, *mania*, *prematurely*, *Brontë*, *depreciation*, *quantitative*).
7. **Soundscape Mix:**
   - Ambient synthesizer drone (`ambient_drone.wav`) ducked to **-22 dBFS** under narration.
   - Transition whoosh SFX (`transition_whoosh.wav`) aligned to scene cuts at **-18 dBFS**.
