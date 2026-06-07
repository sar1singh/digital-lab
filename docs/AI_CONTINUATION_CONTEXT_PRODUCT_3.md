# AI Continuation Context — Product #3: Project Budget Tracker

> Copy this file into a new AI session to resume Product #3 work with full context of the factory state.
> This is the **primary handoff file** for any session that will work on Product #3 (Project Budget Tracker).

---

## Factory State

**Digital-Lab** is a personal digital products experiment. The active execution track is **Product Factory** (building and selling small spreadsheet/template products on Gumroad and Payhip). Three other labs are **parked**: SaaS Lab, Content Lab, Agency Lab.

**Current goal:** First $50-$100 revenue from spreadsheet products.

**Products shipped:**
- Product #1: **Budget Planner & Expense Tracker** — Ready to Publish (blocked by manual marketplace upload)
- Product #2: **Invoice Generator & Payment Tracker** — Ready to Publish (all 10 QA layers complete, delivery ZIP ready)
- Product #3: **Project Budget Tracker** — Specification Phase (do not build workbook yet)
- Products #4-5: Backlog (Net Worth Tracker, POD Profit Calculator)

---

## Critical Anti-Drift Rules

Before any task, ask: **"Will this increase probability of first $50-$100 revenue?"** If no, park it.

**What you MUST NOT do:**
- Build Product Factory SaaS, marketplace, or automation platform
- Build a website before products exist
- Spend weeks on branding/logo/newsletter
- Do endless market research
- Optimize before first sale
- Start Product #4 before Product #3 is Ready to Publish
- Modify Product #1 or Product #2 workbooks or delivery files (they are frozen)
- Revisit Product #1 or Product #2 planning decisions

**What Product #3 is NOT:**
- Not a code product (no Python apps, no web apps)
- Not a SaaS product
- Not a content product (no courses, no ebooks)
- Not a multi-platform calculator (that's Product #5)

---

## Product #2 Ready-to-Publish State (for reference)

Product #2 is **frozen**. All work is complete. No further development unless customer reports issue.

**Completed:**
- 7-tab XLSX workbook built via Python/openpyxl generator
- All 10 QA layers PASSED (4 automated suites + 9-step manual GS smoke QA + 79 screenshot tests + 22 delivery tests)
- 3 bugs found and fixed during QA (Invoice Total formula, Average Invoice Value COUNTIFS, Data Validation dropdowns)
- Pre-publish review: Sections A-G all PASS
- 6 PNG screenshots generated (01-cover.png through 06-whats-included.png)
- 10-page PDF quick-start guide generated (fpdf2 with embedded screenshots)
- Delivery folder built: workbook + PDF + copy-link.txt
- Delivery ZIP built and verified: 3 files, no extras, branding consistent
- Full retrospective documented: `docs/PRODUCT_2_RETROSPECTIVE.md`
- 3 new factory rules added (Rules 23-25)

**Outstanding:** Create Gumroad listing, Create Payhip listing, Publish, Record URLs — blocked by payment verification / manual marketplace upload.

**Delivery paths:**
- Workbook: `delivery/nivora-invoice-generator-payment-tracker.xlsx`
- PDF: `delivery/nivora-invoice-generator-payment-tracker-quick-start-guide.pdf`
- Copy link: `delivery/google-sheets-copy-link.txt` (URL: `https://docs.google.com/spreadsheets/d/1bGzHBf0SMqZZ-nzX26_EG_CwiDmhkrZJ/copy`)
- ZIP: `delivery/nivora-invoice-generator-payment-tracker-delivery.zip`

---

## Product #3 Specification (Current Phase)

**Product name:** Project Budget Tracker
**Format:** Spreadsheet
**Target buyer:** Freelancers and small business owners managing multiple projects with budgets, tracking actuals vs planned, and monitoring profitability per project
**Price:** $7

**Phase:** Specification Phase ONLY. Do NOT build the workbook, generate screenshots, create PDF, or build delivery.

### Specification Documents (all complete in `01-product-factory/02-products/project-budget-tracker/`)

| Document | Description | File |
|----------|-------------|------|
| Product Spec | Overview, tab structure, target buyer, format, key features | `PRODUCT_SPEC.md` |
| Sheet Structure | Column layouts, row counts, field types for all tabs | `SHEET_STRUCTURE.md` |
| Formulas | All formulas with expected values (must include at least one test-row expected value per Rule 25) | `FORMULAS.md` |
| Sample Data | Realistic sample rows across all tabs for QA assertions | `SAMPLE_DATA.md` |
| Screenshot Plan | 6 screenshots with capture instructions, annotations, acceptance criteria | `SCREENSHOT_PLAN.md` |
| Build Checklist | Task checklist for build phase | `BUILD_CHECKLIST.md` |
| QA Checklist | 10-layer coverage map for QA phase | `QA_CHECKLIST.md` |
| Quick-Start Guide | Markdown source for PDF generation | `QUICK_START_GUIDE.md` |
| Listing Copy (Gumroad) | Full Gumroad listing copy | `LISTING_COPY_GUMROAD.md` |
| Listing Copy (Payhip) | Full Payhip listing copy | `LISTING_COPY_PAYHIP.md` |

### Key Spec Decisions to Follow

1. **7-tab structure:** Dashboard, Project List, Budget Detail, Expense Log, Invoice Tracker, Profit Analysis, Settings
2. **Data validation:** Use inline comma-separated lists only (Rule 24). No sheet-cell-range references.
3. **COUNTIFS/SUMIFS:** Use finite ranges (e.g., `B2:B500`, not `B:B`). Add non-empty criterion for negative matches (Rule 23).
4. **Formula spec:** Every formula must have at least one test-row expected value (Rule 25).
5. **Generator:** Use Python/openpyxl (`build_workbook.py`) following the Product #2 pattern. Build all tabs, formulas, formatting, data validation, and freeze panes in a single regeneratable script.
6. **Screenshots:** Capture at 100% zoom, consistent viewport. 6-image standard: Cover, Dashboard, Primary Feature, Secondary Feature, Supporting Feature, What's Included.
7. **PDF:** Generate after screenshots are final. Use fpdf2 with embedded PNGs. 6-8 pages target.
8. **Delivery:** 3-file ZIP (workbook + PDF + copy link). No subdirectories. No internal files.

---

## Reusable Components from Product #2

These can be copied and adapted for Product #3:

| Component | Source Path | Adaptation Needed |
|-----------|-------------|-------------------|
| QA runner | `invoice-generator-payment-tracker/build/run_all_qa.py` | Update imports for new product name |
| Workbook validation | `invoice-generator-payment-tracker/build/validate_workbook.py` | Replace tab/column/row checks |
| Formula tests | `invoice-generator-payment-tracker/build/test_workbook_formulas.py` | Replace expected values |
| GS compatibility lint | `invoice-generator-payment-tracker/build/lint_google_sheets_compatibility.py` | No changes needed (generic) |
| Layout/UI tests | `invoice-generator-payment-tracker/build/test_workbook_layout.py` | Replace tab/section checks |
| PDF generator | `invoice-generator-payment-tracker/build/generate_pdf.py` | Replace content, keep fpdf2 wrapper |
| Delivery QA template | `invoice-generator-payment-tracker/qa/TEST_CASES_DELIVERY_PACKAGE.md` | Update filenames only |
| Pre-publish review template | `invoice-generator-payment-tracker/qa/PRE_PUBLISH_REVIEW_RESULTS.md` | Auto-populate layers |

---

## QA Standards Reference

**All 10 QA layers must pass before "Delivery Ready" status:**

| Layer | Phase | What It Covers | Method |
|-------|-------|----------------|--------|
| 1 | Formula Integrity | All formulas compute correct values | Automated |
| 2 | Structural Integrity | Tab names, sheet count, named ranges, freeze panes | Automated |
| 3 | Cross-Reference Integrity | Sheet names, tab colors, navigation links, hyperlinks | Automated |
| 4 | GS Compatibility | Import/export to Google Sheets, formula conversion, data validation, conditional formats | Automated + Manual |
| 5 | Manual Functional | Dashboard KPIs, dropdown interactions, navigation, data entry, conditional formatting, print layout | Manual |
| 6 | Sample Data | Realistic data in every data tab, at least 5 rows, covers all formulas and groupings | Automated |
| 7 | Asset Specs | 6 spec files exist with capture instructions, annotations, acceptance criteria | Manual |
| 8 | Asset Files | 6 PNG screenshots exist at correct dimensions, branding, annotations, no placeholders | Automated + Manual |
| 9 | PDF Guide | All sections present, screenshots embedded, branding correct, no placeholder text | Manual |
| 10 | Delivery Package | ZIP contains exactly 3 files, branding consistent, copy link valid, no internal files | Automated + Manual |

**Gate:** Layer 10 (Pre-Publish Review) requires Sections A-G all PASS before "Delivery Ready" status.

---

## Factory Rules (All Products)

| # | Rule | Detail |
|---|------|--------|
| 1 | Brand-first | Brand (Nivora), support email, naming conventions locked before any asset or build work |
| 2 | Standard folder structure | artifacts/, build/, qa/, listing-assets/, screenshots/, docs/, delivery/ |
| 3 | Delivery folder rule | Buyer-facing assets only — no QA, drafts, or internal files |
| 4 | 6-screenshot standard | Cover, Dashboard, Primary Feature, Secondary Feature, Supporting Feature, What's Included |
| 5 | 5-review exit criteria | Pass all: Content, Branding, Packaging, Marketplace, Delivery reviews |
| 6 | Retrospective required | RETROSPECTIVE.md for every shipped product; lessons update factory standards |
| 7 | Assets after QA | Generate marketplace images only after workbook is final and QA'd |
| 8 | ZIP as final step | Build ZIP last, exactly 3 files (workbook, PDF, copy link), no subdirectories |
| 9 | Gumroad first | List on Gumroad first, then Payhip. Add platforms only after consistent sales |
| 10 | 10-stage pipeline | Idea → Build → QA → Assets → Packaging → List → Publish → Distribute → Learn → Update |
| 11 | QA coverage gate | All 10 QA layers must pass before "Delivery Ready" status |
| 12 | Automated QA before manual | Layers 1-4 (automated) before Layers 5-9 (manual) |
| 13 | No version numbers | No buyer-facing filenames may include version numbers |
| 14 | Internal files excluded | Internal QA files must not be included in buyer delivery |
| 15 | Single brand | Nivora is sole customer-facing brand. Never use "Work by Sar1" for buyer-facing content |
| 16 | Support email | workbysar1@gmail.com is support/operations only, not a brand name |
| 17 | No Etsy before 5 products | Do not set up Etsy before first sale or 5 products published |
| 18 | No market research loops | Move directly to execution |
| 19 | Max 1-2 days per product | Build and publish in 1-2 days per product |
| 20 | P0/P1 tests must pass | All P0 and P1 tests must pass before listing goes live |
| 21 | No SaaS or website | No SaaS, website, logo, newsletter, audience-building before first $50-$100 |
| 22 | No product factory app | Do not build an automation platform for the factory itself |
| 23 | COUNTIFS finite range | Negative-match COUNTIFS/SUMIFS must use finite range + non-empty criterion |
| 24 | DV inline lists | Data validations use inline comma-separated lists for GS compatibility |
| 25 | Formula expected values | Every formula in FORMULAS.md needs at least one test-row expected value |

---

## Key File Paths

```
Repository root:              digital-lab/

Product 1 (Budget Planner):   01-product-factory/02-products/budget-planner-expense-tracker/
  Delivery ZIP:               .../delivery/nivora-budget-planner-expense-tracker-delivery.zip

Product 2 (Invoice Gen):      01-product-factory/02-products/invoice-generator-payment-tracker/
  Delivery ZIP:               .../delivery/nivora-invoice-generator-payment-tracker-delivery.zip
  Retrospective:              .../docs/PRODUCT_2_RETROSPECTIVE.md
  QA results:                 .../qa/PRE_PUBLISH_REVIEW_RESULTS.md

Product 3 (Budget Tracker):   01-product-factory/02-products/project-budget-tracker/
  Product spec:               .../PRODUCT_SPEC.md
  Sheet structure:            .../SHEET_STRUCTURE.md
  Formulas:                   .../FORMULAS.md
  Sample data:                .../SAMPLE_DATA.md
  Screenshot plan:            .../SCREENSHOT_PLAN.md
  Build checklist:            .../BUILD_CHECKLIST.md
  QA checklist:               .../QA_CHECKLIST.md
  Quick-start guide:          .../QUICK_START_GUIDE.md
  Listing copy (Gumroad):     .../LISTING_COPY_GUMROAD.md
  Listing copy (Payhip):      .../LISTING_COPY_PAYHIP.md

Factory docs:                 01-product-factory/
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

Systems:
  QA standard:                07-systems/QA_COVERAGE_STANDARD.md
  Brand standard:             07-systems/BRAND_STANDARD.md
  Delivery standard:          07-systems/DELIVERY_STANDARD.md
  Pre-publish checklist:      07-systems/PRE_PUBLISH_REVIEW_CHECKLIST.md
  Asset standard:             07-systems/MARKETPLACE_ASSET_STANDARD.md

Context/control:
  Session continuation:       00-control/SESSION_CONTINUATION.md
  Factory continuation:       00-control/PRODUCT_FACTORY_CONTINUATION_CONTEXT.md
  Product catalog:            00-control/PRODUCT_CATALOG.csv
  Next actions:               NEXT_ACTIONS.md
  Progress dashboard:         docs/PRODUCT_FACTORY_PROGRESS_DASHBOARD.md
  This file:                  docs/AI_CONTINUATION_CONTEXT_PRODUCT_3.md
```

---

## Immediate Next Actions for Product #3

### Phase A: Workbook Build (do not start until spec is finalized)
1. Create `build/` directory structure
2. Create `build/build_workbook.py` — Python/openpyxl generator with all 7 tabs
3. Create `build/validate_workbook.py` — structural checks
4. Create `build/test_workbook_formulas.py` — formula assertions with expected values
5. Create `build/lint_google_sheets_compatibility.py` — GS compatibility checks
6. Create `build/test_workbook_layout.py` — layout/UI tests
7. Create `build/run_all_qa.py` — unified QA runner
8. Create `build/generate_pdf.py` — PDF generator

### Phase B: QA
9. Run Layers 1-4 (automated QA)
10. Upload to Google Sheets and run Layer 5 (manual smoke QA)
11. Fix any bugs found
12. Document bugs in retrospective

### Phase C: Assets
13. Create 6 listing-asset spec files
14. Generate 6 PNG screenshots at 100% zoom
15. Run screenshot QA (30-40 test cases)

### Phase D: Delivery
16. Generate PDF quick-start guide (6-8 pages)
17. Build delivery folder (workbook + PDF + copy link)
18. Run delivery QA (22 test cases)
19. Build and verify ZIP

### Phase E: Publish (blocked until Products 1-2 are on marketplace)
20. Create Gumroad listing
21. Create Payhip listing
22. Record URLs in PRODUCT_CATALOG.csv
23. Complete retrospective
24. Update factory standards with new lessons

---

## Do NOT Start Until Directed

- Do NOT build the Product #3 workbook until the next session explicitly says "start build phase"
- Do NOT create screenshots, PDF, or delivery until the workbook is built and QA'd
- Do NOT modify Product #1 or Product #2 files
- Do NOT start Product #4 planning
- Do NOT do market research
- Do NOT set up marketplace accounts (Gumroad/Payhip) — that's a manual action for the founder
