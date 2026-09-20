---
name: thinklate-orchestrator
description: Master production orchestrator for ThinkLate YouTube explainer documentaries (@wethinklate). Coordinates the 4 production phases and dispatches to specialized skills for scriptwriting, research, thumbnail design, visual QC, audio audit, retention check, and final release gatekeeping.
---

# ThinkLate Master Video Production Orchestrator

## Overview
This skill orchestrates the end-to-end production of ThinkLate documentary visual essays (`digital-lab/03-content-lab/thinklate/`). It ensures every video adheres to ThinkLate's 8-Pillar Quality Framework, coordinates sub-skills, tracks stage completion, and guards against premature publishing.

## Production Phases & Skill Dispatch Matrix

```
[Phase 1: Pre-Production]
  ├── thinklate-script-auditor       (Script writing, zero numerals, hook timing, cadence)
  └── thinklate-research-auditor     (Primary PDFs, NotebookLM ingestion, 1:1 citations)

[Phase 2: Packaging & Design]
  ├── thinklate-thumbnail-auditor    (3-second glance rule, 120px mobile test, curiosity gap)
  └── thinklate-design-auditor       (Brand palette #1B2A4A, 10-ft TV legibility, UI hierarchy)

[Phase 3: Asset Assembly & Production]
  ├── thinklate-visual-qc            (Ken Burns motion, Google Vids prompts, Avatar placement)
  └── thinklate-audio-auditor        (Voiceover QC, WPM cadence, pronunciation, -14 LUFS)

[Phase 4: Post-Production & Release]
  ├── thinklate-retention-auditor    (Retention curve milestones, zero algorithmic begging)
  └── thinklate-gatekeeper           (Master Go/No-Go release checklist, YouTube metadata)
```

## Orchestration Workflow

When a user asks to create, audit, or progress a ThinkLate video:
1. **Initialize or Identify the Video Folder:**
   - For a new video (Video 2+): Execute `python scaffold_video.py <number> <slug> "<title>"` to generate all turnkey templates, teleprompter, and audio tools instantly.
   - Confirm target directory under `digital-lab/03-content-lab/thinklate/videos/<video_slug>/`.
2. **Read Current State:** Inspect `script.md`, `AI-VIDEO-GENERATION-BIBLE.md`, `SCREENSHOT-GUIDE.md`, `sources.md`, and any recorded takes.
3. **Determine Active Stage:**
   - If script is being drafted/revised ➔ Invoke `thinklate-script-auditor`.
   - If sources/facts are being verified ➔ Invoke `thinklate-research-auditor`.
   - If thumbnail/packaging is needed ➔ Invoke `thinklate-thumbnail-auditor`.
   - If visuals/prompts are needed ➔ Invoke `thinklate-visual-qc` (MANDATORY: Generate `AI-VIDEO-GENERATION-BIBLE.md` with scene-wise AI video prompts matched to dialogue).
   - If user is recording voiceover ➔ Invoke `thinklate-audio-auditor` (Read via `recording_studio.html`, 1-click Audacity macro, run `audit_audio.py`).
   - If narrative retention needs review ➔ Invoke `thinklate-retention-auditor`.
   - If video is ready for export and release ➔ Invoke `thinklate-gatekeeper`.
4. **Enforce Brand Invariants:**
   - **Zero PPT Slides:** 100% dynamic living 1080p AI B-roll video with Style Lock suffix and floating evidence overlay cards.
   - **Scene-Wise AI Prompt Bible:** Every scene and dialogue line must have an explicit AI video generation prompt and manual screenshot guide with exact web/PDF links.
   - **Spoken Language:** Natural conversational Indian-Global English (informal office meeting register, no forced radio announcer voice).
   - **Voiceover:** 100% human voice recording with Audacity `ThinkLate Voice Chain` macro.
   - **Avatar Integration:** Full-body or waist-up ThinkLate Owl mascot (`00_MASTER_avatar.png`) featured at key anchor moments.
   - **Editorial Dignity:** Zero spoken "like, share, and subscribe" requests.
