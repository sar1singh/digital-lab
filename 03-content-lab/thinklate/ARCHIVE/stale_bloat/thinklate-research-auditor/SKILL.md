---
name: thinklate-research-auditor
description: Research and primary source fact-checking skill for ThinkLate documentaries. Verifies 1:1 primary document traceability, checks verbatim quotes against opened PDFs, coordinates NotebookLM source ingestion, and enforces honest inference labeling.
---

# ThinkLate Research & Citation Auditor Skill

## Purpose
Guarantees 100% intellectual honesty, rigorous academic grounding, and zero ungrounded hype across all ThinkLate video essays.

## Key Checkpoints
1. **1:1 Primary Source Traceability:**
   - Every factual claim, date, or statistic must cite an opened primary source ID (`<src: ID>`) defined in `sources.md`.
2. **Verbatim Quote Verification:**
   - Quotes attributed to researchers (e.g. Prof. Andrew Odlyzko) or financial institutions (Goldman Sachs, Sequoia) must match the primary PDF verbatim.
   - Preserves author framing (e.g., distinguishing between actual cash capital invested vs stock market paper valuation).
3. **Inference vs Fact Transparency:**
   - Modern market extrapolations or estimates without verified balance sheet filings must be spoken and labeled on-screen as an **"inference / hypothesis"**.
4. **NotebookLM Integration (`NOTEBOOKLM-SOURCES.md`):**
   - Provide direct PDF download links and citation notes for seamless NotebookLM ingestion, allowing real-time AI fact cross-examination.
