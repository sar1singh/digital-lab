# Product #2 Build Plan — Nivora Invoice Generator & Payment Tracker

## Overview

Build the second Product Factory product using the standards hardened from Product #1.

**Current Status:** Workbook draft built — in `build/nivora-invoice-generator-payment-tracker.xlsx`. Next: Internal QA.

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

### Phase 3: Internal QA (Current)
- [ ] Run formula test cases (qa/TEST_CASES_FORMULAS.md)
- [ ] Run Google Sheets import test (qa/TEST_CASES_GOOGLE_SHEETS_IMPORT.md)
- [ ] Fix all P0/P1 issues
- [ ] Run automated QA checks

### Phase 4: Asset Generation (After QA)
- [ ] Capture 6 screenshots per SCREENSHOT_PLAN.md
- [ ] Create cover image with Nivora brand
- [ ] Save to listing-assets/ with correct naming

### Phase 5: Packaging (After Assets)
- [ ] Export final branded workbook
- [ ] Create Google Sheets copy and validate copy link
- [ ] Create copy link file (google-sheets-copy-link.txt)
- [ ] Generate PDF quick-start guide (2nd-to-last step)
- [ ] Build delivery ZIP (last step — exactly 3 files)

### Phase 6: Pre-Publish QA
- [ ] Run 5-review process: Content, Branding, Packaging, Marketplace, Delivery
- [ ] All reviews must pass before listing

### Phase 7: Publish
- [ ] Create Gumroad listing
- [ ] Create Payhip listing
- [ ] Publish
- [ ] Record URLs

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
