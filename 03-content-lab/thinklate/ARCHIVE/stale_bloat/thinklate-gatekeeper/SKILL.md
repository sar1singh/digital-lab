---
name: thinklate-gatekeeper
description: Master pre-publish release gatekeeper skill for ThinkLate documentaries. Executes final Go/No-Go release verification across all 8 quality pillars, reviews YouTube description bibliography, chapter markers, thumbnail variants, and ensures monetization policy compliance.
---

# ThinkLate Master Pre-Publish Gatekeeper Skill

## Purpose
The final quality gate before any ThinkLate documentary video is published on YouTube. Guarantees that no unverified fact, clipped audio, or uncredited claim reaches the public.

## Master Go / No-Go Checklist

### 1. Audio Verification
- [ ] 100% human voice recorded (zero AI TTS).
- [ ] All takes analyzed via `audit_audio.py` with Score ≥ 85.
- [ ] High-pass filter (80Hz) and DaVinci Voice Isolation (40–50%) applied.
- [ ] Ambient background music ducked to -22 dBFS under narration.

### 2. Video & Visual Verification
- [ ] Rendered at Full HD 1080p (1920x1080) at 25fps progressive.
- [ ] 3-Second Stagnation Rule honored across all scenes (Ken Burns push-in applied).
- [ ] ThinkLate Owl Avatar integrated at key anchor moments (Scene 1, 4, 8, 13).
- [ ] Lower-third citations slide in at 1.0s and hold for 4–6 seconds.

### 3. YouTube Metadata Package
- [ ] **Title:** High-CTR approved title: `Is AI a Bubble? Ask the Railways`
- [ ] **Thumbnail:** Photorealistic high-contrast documentary thumbnail (`thumbnail_v1_cinematic.jpg`) verified at 120px mobile size.
- [ ] **Description:** Complete **Sources & Bibliography Block** included with academic links to Prof. Odlyzko, Goldman Sachs, and Sequoia.
- [ ] **Chapters:** Clean timestamps included (00:00 Cold Open, 00:19 Core Thesis, 00:46 Personal Stake, etc.).
- [ ] **Policy:** "Altered or Synthetic Content" checkbox in YouTube Studio configured properly.

## Release Sign-Off
Once all 5 sections are checked, the video is approved for public broadcast.
