# Product Factory Continuation Context

> Copy-paste this file into a new AI session to resume Product Factory execution with full context.

---

## Repository Overview

**Digital-Lab** is a personal digital products experiment. The active execution track is **Product Factory** (building and selling small spreadsheet/template products on Gumroad and Payhip). Three other labs are **parked**: SaaS Lab, Content Lab, Agency Lab.

---

## Current Strategy

- Build small proven-format digital products (spreadsheets, templates, calculators)
- Sell on Gumroad and Payhip (Phase 1)
- Compete in existing proven markets; copy successful formats legally
- Max 1-2 days per product before publishing
- Build → Publish → Learn → Repeat
- First revenue ($50-$100) is more important than innovation

---

## Locked Decisions

- Product Factory is active; SaaS Lab, Content Lab, Agency Lab are parked
- First revenue is primary goal — do not optimize for portfolio, resume, or innovation
- No SaaS, website, logo, newsletter, audience-building, automation platform, or Product Factory app
- No Etsy setup before first sale or 5 products published
- No broad research loops — move directly to execution
- Do not start Product N+1 until Product N is published or explicitly parked
- Products 1-2 are frozen — no further development unless customer reports issue
- Max 1-2 days per product before publishing
- All P0 and P1 tests must pass before listing goes live
- No buyer-facing filenames may include version numbers
- Internal QA files must not be included in buyer delivery

---

## Branding

**Customer-facing publisher brand:** Nivora
**Founder/operator email:** workbysar1@gmail.com
**Support email:** workbysar1@gmail.com
**Platform signup email:** workbysar1@gmail.com

**Critical rule:** Never use "Work by Sar1" as customer-facing branding again.

---

## Current Product Status

### Product 1: Budget Planner & Expense Tracker
**Status:** Ready to Publish

**Completed:**
- Product strategy finalized
- Product workspace created
- Workbook architecture completed (7 tabs, 91 formulas)
- Formula audit completed (17 cross-sheet fixes)
- Navigation links fixed for Google Sheets
- Automated QA: 55/55 PASS
- Manual QA: PASS (Excel + Google Sheets)
- Delivery package completed (workbook, guides, release notes)
- PDF quick-start guide generated
- 5 listing/demo images generated
- Branding updated to Nivora
- BRAND_QA_CHECKLIST.md created
- Google Sheets copy link finalized and pasted into delivery file
- Dashboard bottom summary fixed: B40(=B4->=B5), B41(=B5->=B7)
- Final clean ZIP rebuilt with only 3 buyer files (xlsx, pdf, copy-link.txt)
- FINAL_ZIP_QA.md created
- PRODUCT_CATALOG.csv status set to Ready to Publish

**Publishing candidate:** `delivery/nivora-budget-planner-expense-tracker.xlsx`

**Outstanding:**
- Create Gumroad listing
- Create Payhip listing
- Publish
- Record URLs

### Product 2: Invoice Generator & Payment Tracker
**Status:** READY TO PUBLISH — All 10 QA layers complete.
**Delivery:** `delivery/nivora-invoice-generator-payment-tracker-delivery.zip` (3 files)
**QA summary:**
- All 10 QA layers PASSED
- 3 bugs found and fixed during QA (Invoice Total formula, Average Invoice Value, Data Validation dropdowns)
- 4 automated suites + 9-step manual GS smoke QA + 79 screenshot test cases + 22 delivery tests
- Pre-publish review: Sections A–G all PASS
- Full retrospective: `docs/PRODUCT_2_RETROSPECTIVE.md`
- **Outstanding:** Create Gumroad listing, Create Payhip listing, Publish, Record URLs

### Product 3: Project Budget Tracker
**Status:** Planning phase — workspace created, all spec documents complete

### Product 4: Net Worth Tracker
**Status:** Backlog

### Product 5: POD Profit Calculator
**Status:** Backlog

---

## Product Roadmap

| # | Product | Format | Status | Price |
|---|---------|--------|--------|-------|
| 1 | Budget Planner & Expense Tracker | Spreadsheet (7 tabs) | Ready to Publish | $7 |
| 2 | Invoice Generator & Payment Tracker | Spreadsheet (7 tabs) | READY TO PUBLISH | $7 |
| 3 | Project Budget Tracker | Spreadsheet (7 tabs) | Planning — specs in progress | $7 |
| 4 | Net Worth Tracker | Spreadsheet | Backlog | $5-$12 |
| 5 | POD Profit Calculator | Spreadsheet | Backlog | $5-$12 |

---

## Product Selection Rules

**Reject if:**
- No demand evidence
- No competitors
- Requires education
- Requires SaaS
- Requires >2 days effort

**Accept if:**
- Existing demand
- Existing competitors
- Existing buyers
- Deliverable as XLSX, Google Sheet, PDF, template, or toolkit

---

## Anti-Drift Rules

Before any task, ask: **"Will this increase probability of first $50-$100 revenue?"**

If no, park it.

**Do not:**
- Build Product Factory SaaS
- Build a marketplace
- Build an automation platform
- Build a website before products exist
- Spend weeks on branding
- Do endless market research
- Optimize before first sale

---

## Success Metrics

| Stage | Milestone | Status |
|-------|-----------|--------|
| 1 | Product 1 live | Blocked — manual listing needed |
| 2 | Product 2 live | Blocked — manual listing needed |
| 3 | First sale | Not yet |
| 4 | First $50 revenue | Not yet |
| 5 | First $100 revenue | Not yet |
| 6 | Five products live | Not yet |

---

## What Must Not Be Changed

1. **Products 1-2 are frozen** — no further development unless customer reports issue. Do not modify workbooks, delivery files, screenshots, or PDFs.
2. **Do not start Product 4** until Product 3 is published or explicitly parked.
3. **Do not change Product 1 workbook formulas** — 91 formulas are verified and tested.
4. **Do not change product strategy** — Product Factory active, other labs parked.
5. **Do not do market research** — move directly to execution.
6. **Do not set up Etsy, website, logo, newsletter, or branding** before first sale or 5 products published.
7. **No buyer-facing filenames may include version numbers** (v1.2, v1.1, etc.).
8. **Internal QA files must not be included in buyer delivery.**
9. **Nivora is the sole customer-facing brand.** Never use "Work by Sar1" for buyer-facing content.
10. **workbysar1@gmail.com is support/operations only** — not a brand name.
11. **Brand-first workflow:** Brand, support email, naming conventions locked before any asset or build work.
12. **Standard product structure:** artifacts/, build/, qa/, listing-assets/, screenshots/, docs/, delivery/
13. **Delivery folder rule:** buyer-facing assets only — no QA, drafts, or internal files.
14. **6-screenshot standard:** Cover, Dashboard, Primary Feature, Secondary Feature, Supporting Feature, What's Included.
15. **5-review exit criteria:** Must pass all reviews — Content, Branding, Packaging, Marketplace, Delivery.
16. **Retrospective required:** RETROSPECTIVE.md for every shipped product; lessons become factory standards.
17. **Assets after QA:** Generate marketplace images only after workbook is final and QA'd.
18. **ZIP as final step:** Build ZIP last, exactly 3 files (workbook, PDF, copy link), no subdirectories.
19. **Gumroad first:** List on Gumroad first, then Payhip. Add platforms only after consistent sales.
20. **10-stage pipeline:** Idea → Build → QA → Assets → Packaging → List → Publish → Distribute → Learn → Update.
21. **QA coverage gate:** All 10 QA layers from `QA_COVERAGE_STANDARD.md` must pass before "Delivery Ready" status.
22. **Automated QA before manual:** Implement Layers 1–4 (automated) before Layers 5–9 (manual). Manual QA only for platform/visual behavior.
23. **COUNTIFS negative-match requires finite range + non-empty criterion:** Any `COUNTIFS(...,"<>X")` must use finite range (not `A:A`) and include `"<>"` as secondary criterion to avoid counting empty formula cells.
24. **Data validations use inline lists for GS compatibility:** Set data validation with comma-separated values `"A,B,C"` instead of referencing sheet cells like `Settings!$C$6`. Range refs break during Google Sheets conversion.
25. **Formula spec must include expected values:** Every formula in FORMULAS.md needs at least one test-row expected value, not just a structural description. This enables automated QA to catch wrong cell references.

---

## Immediate Next Actions

### Product 1 & 2: Publish Both Listings
1. Create Gumroad listing for Product 1 from `LISTING_COPY_GUMROAD.md`
2. Create Payhip listing for Product 1 from `LISTING_COPY_PAYHIP.md`
3. Create Gumroad listing for Product 2 from `.../invoice-generator-payment-tracker/LISTING_COPY_GUMROAD.md`
4. Create Payhip listing for Product 2 from `.../invoice-generator-payment-tracker/LISTING_COPY_PAYHIP.md`
5. Upload delivery ZIPs + screenshots to both listings
6. Set price to $7 on both platforms for both products
7. Test checkout preview
8. Publish both listings
9. Record listing URLs in `PRODUCT_CATALOG.csv`
10. Update `PRODUCT_CATALOG.csv` status to Published
11. Build Product 3 (Project Budget Tracker) — workbook generation is next phase

---

## Key File Paths

```
Repository root:              digital-lab/
Active products:
  Product 1 (Budget Planner): 01-product-factory/02-products/budget-planner-expense-tracker/
    Source workbook:           .../artifacts/budget-planner-expense-tracker-v1.2.xlsx
    Delivery folder:           .../delivery/
    Buyer workbook:            .../delivery/nivora-budget-planner-expense-tracker.xlsx
    Retrospective:             .../RETROSPECTIVE.md
  Product 2 (Invoice Gen):    01-product-factory/02-products/invoice-generator-payment-tracker/
    Build script:              .../build/build_workbook.py
    QA runner:                 .../build/run_all_qa.py
    QA suites:                 .../build/validate_workbook.py, test_workbook_formulas.py, lint_google_sheets_compatibility.py, test_workbook_layout.py
    PDF generator:             .../build/generate_pdf.py
    Delivery folder:           .../delivery/
    Buyer workbook:            .../delivery/nivora-invoice-generator-payment-tracker.xlsx
    Buyer PDF:                 .../delivery/nivora-invoice-generator-payment-tracker-quick-start-guide.pdf
    Delivery ZIP:              .../delivery/nivora-invoice-generator-payment-tracker-delivery.zip
    QA test suite:             .../qa/ (TEST_CASES_SCREENSHOTS.md, TEST_CASES_DELIVERY_PACKAGE.md, GOOGLE_SHEETS_MANUAL_QA_RESULTS.md, PRE_PUBLISH_REVIEW_RESULTS.md)
    Listing assets (specs):    .../listing-assets/ (01-cover-image.md through 06-whats-included-image.md)
    Screenshots (PNG):         .../screenshots/ (01-cover.png through 06-whats-included.png)
    Listing copy:              .../LISTING_COPY_GUMROAD.md, LISTING_COPY_PAYHIP.md
    Quick-start guide (src):   .../QUICK_START_GUIDE.md
    Retrospective:             .../docs/PRODUCT_2_RETROSPECTIVE.md

Product factory docs:         01-product-factory/
  Workflow:                   PRODUCT_FACTORY_WORKFLOW.md
  Playbook:                   PRODUCT_FACTORY_PUBLISHING_PLAYBOOK.md
  Context:                    PRODUCT_FACTORY_CONTEXT.md
  Marketplace checklist:      PRODUCT_FACTORY_MARKETPLACE_CHECKLIST.md
  Asset specs:                PRODUCT_FACTORY_ASSET_SPECIFICATIONS.md
  Pre-publish QA:             PRODUCT_FACTORY_PRE_PUBLISH_QA.md
  Delivery standard:          PRODUCT_FACTORY_DELIVERY_STANDARD.md
  Product structure:          PRODUCT_FACTORY_PRODUCT_STRUCTURE.md
  Strategy:                   PRODUCT_FACTORY_STRATEGY.md
  Roadmap:                    FIRST_10_PRODUCTS_ROADMAP.md

  Product 3 (Budget Tracker): 01-product-factory/02-products/project-budget-tracker/
    Product spec:              .../PRODUCT_SPEC.md
    Sheet structure:           .../SHEET_STRUCTURE.md
    Formulas:                  .../FORMULAS.md
    Sample data:               .../SAMPLE_DATA.md
    Screenshot plan:           .../SCREENSHOT_PLAN.md
    Build checklist:           .../BUILD_CHECKLIST.md
    QA checklist:              .../QA_CHECKLIST.md
    Quick-start guide:         .../QUICK_START_GUIDE.md
    Listing copy (Gumroad):    .../LISTING_COPY_GUMROAD.md
    Listing copy (Payhip):     .../LISTING_COPY_PAYHIP.md

Product catalog:              01-product-factory/00-control/PRODUCT_CATALOG.csv
Context/continuation:         00-control/
  NOW.md                      Current active task
  DIGITAL_LAB_CONTEXT.md      Full decision log and strategic context
  SESSION_CONTINUATION.md     Copy-paste session resume
  PRODUCT_FACTORY_CONTINUATION_CONTEXT.md  This file
NEXT_ACTIONS.md               Detailed phased action list (repo root)
```

## Approval Flow

`DIGITAL_LAB_CONTEXT.md` → `NOW.md` → `NEXT_ACTIONS.md` → `BUILD_CHECKLIST.md`
