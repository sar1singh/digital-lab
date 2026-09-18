# Working This Folder Outside Cowork

**Created 2026-09-13.** For running ThinkLate on free-tier chat UIs (ChatGPT, Gemini, Claude, Grok) or a local CLI agent.

---

## 1. The actual constraint

**It is context, not tools.** This folder is ~11 MB and 198 files. No free-tier chat will ingest that, and no VPS or agent framework changes it — they all feed the same context window.

**So the rule is: never upload the zip to a chat. Upload 2–4 files for the task at hand.**

## 2. Grounding any new chat

**Paste `CONTEXT-PACK.md`.** One screen, self-sufficient: niche, language, audience, method, exclusions, the 9 hard rules, locked brand, voice, and how to work with me. That alone makes a cold chat usable.

Then attach only the task files below.

## 3. Per-task file bundles

| Task | Attach |
|---|---|
| **Branding close-out** | `brand/BRANDING-SESSION.md` · `brand/ART-DIRECTION.md` · `brand/EXPRESSIONS.md` · `brand/QC.md` |
| **Pick a topic / title** | `04_TITLES-AND-THUMBNAILS.md` · `05_ASSETS-AND-PROMPTS.md` · `11_TECH-AS-SUBSTRATE.md` |
| **Build the causal chain** | `10_MACRO-TO-MICRO.md` · `00_CONTEXT.md` |
| **Research a video** | `13_RUNBOOK.md` · `05_ASSETS-AND-PROMPTS.md` |
| **Write the script** | `15_SCRIPT-FORMAT.md` · `03_CONTENT-AND-VOICE.md` · `12_CRAFT-EVIDENCE.md` |
| **Per-scene visuals** | `14_SCENE-SHEET.md` · `06_MOTION-AND-SURFACE.md` |
| **Thumbnails** | `04_TITLES-AND-THUMBNAILS.md` · `12_CRAFT-EVIDENCE.md` |
| **Charts** | `templates/charts.py` · `templates/brand.py` |
| **Business / money / legal** | `17_BUSINESS-AND-SCALE.md` · `23_REVENUE-ROADMAP.md` |
| **Direction feels unclear** | `21_VISION.md` · `20_PORTFOLIO-ARCHITECTURE.md` |

**Never more than four files.** If a task seems to need more, the task is too big.

## 4. What replaces file access — local CLI, not a VPS

The thing lost by leaving Cowork is **an agent that can read and write these files directly.** That is solved locally, on your own Mac, for ₹0. A server is not required.

| Option | Free tier | Notes |
|---|---|---|
| **Codex CLI** | **Free for ChatGPT Free and Go users** as of March 2026 | Local file access, runs commands. Strongest free option |
| **Antigravity CLI** | Google's replacement path for consumer users | **Gemini CLI stopped serving personal Google accounts on 18 June 2026** — the old free login is gone |
| **Gemini API key** | 250 requests/day unpaid, Flash models only | Usable with OpenCode or a small agent, but Flash-only |
| **OpenCode** | Client is free; you supply keys | 75+ providers, local models. Best if you want model freedom |
| **PicoClaw / OpenClaw** | Open source | Small CLI agent; commonly run against a free Gemini key |

**Verify current terms before committing — this tier churns constantly.**

## 5. Why not the VPS + agent stack, yet

- **It does not solve the context problem.** Same window, same limits
- **It contradicts "free tier."** A VPS is roughly ₹400–800/month and agents burn far more tokens than chat does, metered per API call. Leaving paid tools to save money and then adding a metered server increases cost
- **Your bottleneck is published videos, not automation.** 31 strategy docs, 1 off-niche video. An agent stack automates a pipeline you have not run manually even once
- **`25_AI-ARCHITECTURE.md` §5 still binds:** automate assembly, never judgement. The confidence labels are the product; a pipeline that writes videos end-to-end produces exactly what you positioned against
- **Revisit when** you have a repeatable task you have done manually five times and are tired of

## 6. What to actually set up — one evening, ₹0

1. **`git init` in `ThinkLate/`**, commit after every session. **Highest-value action available** — it turns a snapshot into a history
2. **Push to a private GitHub repo.** You already have an account. This is the portable memory; any machine or agent clones it
3. **Install one local CLI agent** from the table above and point it at the folder
4. **Open the folder as an Obsidian vault** for search and backlinks. Free, local, no migration
5. **Nothing else.** No VPS, no orchestration, no vector DB, no fine-tuning

## 7. Unverified

**I could not find "agentOS" or "Odysseus" as identifiable agent projects.** Confirm the exact names and links before evaluating them — and treat any tool under two years old as replaceable. Keep the knowledge in markdown, never in a tool's config.

## Sources

[Gemini CLI announcement](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-cli-open-source-ai-agent/) · [Gemini CLI features and pricing](https://www.therundown.ai/tools/gemini-cli) · [Gemini free tier limits 2026](https://pecollective.com/tools/gemini-free-tier-guide/) · [free AI CLI tools ranked](https://www.termdock.com/en/blog/free-ai-cli-tools-ranked) · [OpenCode vs Gemini CLI](https://www.morphllm.com/comparisons/opencode-vs-gemini-cli)
