# Product #2 Build Plan — Nivora Invoice Generator & Payment Tracker

## Overview

Build the second Product Factory product using the standards hardened from Product #1.

**Current Status:** READY TO PUBLISH — All 10 QA layers passed.

## Phases

### Phase 1: Planning (Done)
- [x] Create workspace with 7-directory structure
- [x] PRODUCT_SPEC.md
- [x] SHEET_STRUCTURE.md
- [x] FORMULAS.md
- [x] SAMPLE_DATA.md
- [x] SCREENSHOT_PLAN.md
- [x] All QA test case files created

### Phase 2: Build (Done)
- [x] Generate workbook with 7 tabs via Python/openpyxl
- [x] Implement all formulas from FORMULAS.md
- [x] Populate sample data from SAMPLE_DATA.md
- [x] Apply formatting, data validation, tab colors
- [x] Set freeze panes, formula/input cell styling
- [x] Validation: 45/45 checks passed

### Phase 3: Internal QA (Done)
- [x] Run formula test cases (qa/TEST_CASES_FORMULAS.md) — corrected expected values
- [x] Run automated QA checks — 4 QA suites via run_all_qa.py (validate + formulas + lint + layout)
- [x] Fix all P0/P1 issues — Payment Tracker VLOOKUP, Draft decision, formula corrections
- [x] Run Google Sheets smoke test (9 manual steps in docs/GOOGLE_SHEETS_MANUAL_QA_RUNBOOK.md) — 9/9 PASSED

### Phase 4: Asset Generation (Complete)
- [x] Create screenshot specs (listing-assets/01–06) — capture instructions, annotations, acceptance criteria
- [x] Create screenshot QA test cases (qa/TEST_CASES_SCREENSHOTS.md — 79 tests)
- [x] Capture 6 screenshots per specs in listing-assets/
- [x] Create cover image with Nivora brand
- [x] Save PNGs to screenshots/
- [x] Validate screenshots against qa/TEST_CASES_SCREENSHOTS.md

### Phase 5: Packaging (Complete)
- [x] Export final branded workbook
- [x] Create Google Sheets copy and validate copy link
- [x] Create copy link file (google-sheets-copy-link.txt)
- [x] Generate PDF quick-start guide (2nd-to-last step)
- [x] Build delivery ZIP (last step — exactly 3 files)

### Phase 6: Pre-Publish QA (Complete)
- [x] Run 10-layer QA gate (Layers 1–10)
- [x] Pre-publish review checklist (Sections A–G)
- [x] All reviews pass — Ready to Publish

### Phase 7: Publish (Manual)
- [ ] Create Gumroad listing — upload ZIP, set thumbnail, publish
- [ ] Create Payhip listing — upload ZIP, set thumbnail, publish
- [ ] Record URLs
- [ ] Run test purchase

### Phase 8: Post-Publish
- [ ] Complete Retrospective
- [ ] Update factory standards with any new lessons

## Standards Reference

- [Product Factory Workflow](../../PRODUCT_FACTORY_WORKFLOW.md)
- [Publishing Playbook](../../PRODUCT_FACTORY_PUBLISHING_PLAYBOOK.md)
- [Asset Specifications](../../PRODUCT_FACTORY_ASSET_SPECIFICATIONS.md)
- [Delivery Standard](../../PRODUCT_FACTORY_DELIVERY_STANDARD.md)
- [Pre-Publish QA](../../PRODUCT_FACTORY_PRE_PUBLISH_QA.md)
- [Marketplace Checklist](../../PRODUCT_FACTORY_MARKETPLACE_CHECKLIST.md)
