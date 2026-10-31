# Master Index of Pre-Built Video Production Playbooks & Skills
> **Source:** Extracted and adapted from open-source agent skills (`Bomx/super-video-maker-skill`, `sb-dev/video-production-skills`, `ZeroLu/Ultimate-AI-Media-Generator-Skill`).
> **Goal:** Zero "hit and trial". Every agent operates from battle-tested, pre-built frameworks for prompts, scripts, planning, and asset generation.

---

## 📚 The Pre-Built Playbook Matrix

| Production Phase | Pre-Built Playbook | Key Capability & Framework | Assigned Agents |
| :--- | :--- | :--- | :--- |
| **1. Prompt Engineering & Photorealism** | [`HYPERREALISTIC_IMAGE_SOP.md`](HYPERREALISTIC_IMAGE_SOP.md) | • 12-part framework for non-AI photorealism<br>• Skin texture, lens realism (35mm/85mm), anti-slop negative tokens<br>• Real lighting (chiaroscuro, rim light) over flat digital renders | `thinklate-designer`<br>`packaging-director` |
| **2. Scripting & Narrative Architecture** | [`VIDEO_COPY_PLAYBOOK.md`](VIDEO_COPY_PLAYBOOK.md) | • The Four-Line Spine (Viewer, Promise, Mechanism, Action)<br>• The Two-Track Rule (Voice carries argument; screen carries evidence)<br>• The Pointing Test: viewer must be able to point at the spoken noun | `thinklate-story-architect`<br>`script-editor` |
| **3. Conversational Voice & Anti-AI Tells** | [`SPOKEN_VO_HUMANIZER.md`](SPOKEN_VO_HUMANIZER.md) | • 12 rules of spoken-human scripts ("talk to a friend over drinks")<br>• Rhythm variation: hard contrast between >15w and <6w sentences<br>• Banned AI tells: no "in a world where", "let's dive in", or bullet-talk | `storytelling-script-qc`<br>`thinklate-ceo` |
| **4. Viral 0–5s Hook Engineering** | [`HOOK_PLAYBOOK_ARTICLE_SPRINT.md`](HOOK_PLAYBOOK_ARTICLE_SPRINT.md) | • Hook families (The Absurd Contrast, The Secret Robbery, The Paradox)<br>• Loop accounting & angle-before-copy rule<br>• The Unbreakable 0–5s visual/audio payoff contract | `packaging-director`<br>`thinklate-story-architect` |
| **5. Commercial Shot Direction & Reference** | [`sb_production/video_production_skill.md`](sb_production/video_production_skill.md) | • 5-level tiered production (6s hero $\rightarrow$ 15s commercial $\rightarrow$ 8m deep dive)<br>• Brief $\rightarrow$ Reference Frame $\rightarrow$ 2 Candidate Shots $\rightarrow$ Selection<br>• Continuity tracking and material fidelity | `commercial-ad-director`<br>`video-editor` |
| **6. Automated Visual QC & Motion Artifacts** | [`sb_production/video_evaluate_skill.md`](sb_production/video_evaluate_skill.md) | • Automated inspection for video jitter, limb distortion, face morphing<br>• Temporal consistency checks across cuts<br>• Stop-loss spend bounding before rendering | `video-editor-qc` |
| **7. Living Canvas & Dynamic Motion** | [`LIVING_CANVAS_PLAYBOOK.md`](LIVING_CANVAS_PLAYBOOK.md) | • Single continuous canvas pacing (zero static frames)<br>• VO-word-locked camera choreography (Whisper sync)<br>• Spring dynamics and layout reflow | `video-editor`<br>`thinklate-designer` |
| **8. Broadcast Finishing & Captions** | [`FFMPEG_PLAYBOOK.md`](FFMPEG_PLAYBOOK.md) | • Karaoke captioning with active word yellow highlight (`Alignment=2`)<br>• Rounded borderless PiP mask compositing<br>• True-peak loudness compliance (-16 LUFS / -1.5 dBFS) | `video-editor` |
