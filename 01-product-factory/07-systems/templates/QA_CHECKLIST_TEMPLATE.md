# QA Checklist Template

> Copy into product workspace as `QA_CHECKLIST.md`. Replace `[Product Name]` with actual product name.

---

**Product:** [Product Name]
**Current Status:** [Build / QA / Packaging / Ready to Publish]

## Layer 1: Automated Workbook Validation

Reference: `build/validate_workbook.py`

- [ ] Workbook opens without corruption (7 tabs, correct order)
- [ ] All column headers present (Clients, Register, etc.)
- [ ] All required formulas exist (pattern check)
- [ ] Data validations present on dropdown columns
- [ ] Freeze panes on data tabs
- [ ] Formula cells styled (gray) vs input cells (green/white)
- [ ] Tab colors match brand
- [ ] No hidden sheets
- [ ] No macros/VBA/external links
- [ ] No debug/internal text in buyer-facing tabs

## Layer 2: Formula / Business Logic Tests

Reference: `build/test_workbook_formulas.py`, `qa/TEST_CASES_FORMULAS.md`

- [ ] Core calculation formulas correct (tax, total, outstanding, status)
- [ ] Cross-sheet references resolve correctly
- [ ] Dashboard KPIs match source data
- [ ] Summary tables (revenue by month, status breakdown, top items) match data
- [ ] Generator/calculator sections compute correctly
- [ ] IFERROR wrappers present where needed
- [ ] No hardcoded values where formulas should exist

## Layer 3: Google Sheets Compatibility Lint

Reference: `build/lint_google_sheets_compatibility.py`

- [ ] No Excel-only functions used
- [ ] No risky GS functions used
- [ ] No external workbook references
- [ ] No structured table references
- [ ] No local path references
- [ ] All multi-word sheet names are single-quoted
- [ ] All formulas use only allowed GS-compatible functions

## Layer 4: UI / Layout / Static Checks

Reference: `build/test_workbook_layout.py`

- [ ] Brand name appears on Start Here and Dashboard
- [ ] All required sections present (From, Bill To, Summary, etc.)
- [ ] KPI card labels present on Dashboard
- [ ] Settings tab has all configuration sections
- [ ] Freeze panes on data tabs
- [ ] Date formatting on date columns
- [ ] Currency formatting on money columns
- [ ] Header rows are styled (bold/dark)
- [ ] No debug/internal text in buyer-facing sheets

## Layer 5: Manual Smoke QA

Reference: `docs/GOOGLE_SHEETS_MANUAL_QA_RUNBOOK.md`, `qa/GOOGLE_SHEETS_MANUAL_QA_RESULTS.md`

- [ ] GS-01: Upload XLSX to Google Drive
- [ ] GS-02: Open with Google Sheets without errors
- [ ] GS-03: All tabs open correctly
- [ ] GS-04: Spot-check 3–5 formulas (no errors)
- [ ] GS-05: Dropdowns work in UI
- [ ] GS-06: Dashboard displays correctly
- [ ] GS-07: Invoice Generator print/export layout acceptable
- [ ] GS-08: Copy link created and tested from incognito
- [ ] GS-09: Link pasted into buyer-facing file

## Layer 6: Delivery Package QA

Reference: `qa/TEST_CASES_DELIVERY_PACKAGE.md`

- [ ] All delivery filenames use correct brand prefix
- [ ] No version numbers in buyer-facing filenames
- [ ] ZIP contains exactly 3 files (xlsx, pdf, txt)
- [ ] ZIP contains no internal docs, QA files, or listing assets
- [ ] Copy link file exists with brand and instructions
- [ ] Copy link URL works (tested)
- [ ] Workbook and PDF titles include brand name
- [ ] No old brand names in delivery files
- [ ] Support email present in PDF and copy link file

## Layer 7: Marketplace Asset QA

Reference: `SCREENSHOT_PLAN.md`

- [ ] Cover image communicates value at thumbnail size
- [ ] All 6 screenshots present and meet spec
- [ ] No UI chrome or personal info visible
- [ ] Consistent dimensions across all images

## Layer 8: Listing Copy QA

Reference: `LISTING_COPY_GUMROAD.md`, `LISTING_COPY_PAYHIP.md`

- [ ] Title clear and searchable
- [ ] Subtitle explains value proposition
- [ ] What's Included lists specific deliverables
- [ ] Who It's For targets right buyer
- [ ] Benefits address buyer pain points
- [ ] FAQ answers common hesitations
- [ ] Support contact included
- [ ] Price set

## Layer 9: Link / Copy-Link QA

- [ ] Google Sheets copy link works (opens copy dialog)
- [ ] Link uses `/copy` suffix
- [ ] Link pasted into `google-sheets-copy-link.txt`
- [ ] Link file contains brand and usage instructions

## Layer 10: Final Pre-Publish Gate

Reference: `PRE_PUBLISH_REVIEW_CHECKLIST.md`

- [ ] All 10 QA layers complete and passing
- [ ] Automated scripts all pass
- [ ] Manual smoke tests documented as PASS
- [ ] Delivery ZIP verified programmatically
- [ ] Marketplace listing preview complete
- [ ] **Status set to: Ready to Publish**

---

## Coverage Map

| Layer | Coverage | Automated? | Status |
|-------|----------|-----------|--------|
| 1 | Workbook structural validation | Fully automated | [ ] |
| 2 | Formula/business logic | Fully automated | [ ] |
| 3 | GS compatibility | Fully automated | [ ] |
| 4 | UI/layout | Fully automated | [ ] |
| 5 | Manual smoke | Manual | [ ] |
| 6 | Delivery package | Manual + scripted | [ ] |
| 7 | Marketplace assets | Manual review | [ ] |
| 8 | Listing copy | Manual review | [ ] |
| 9 | Copy link | Manual | [ ] |
| 10 | Pre-publish gate | Manual gate check | [ ] |
