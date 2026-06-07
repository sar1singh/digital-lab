# QA Coverage Standard

> Mandatory QA framework for every Product Factory product.
> No product may become "Delivery Ready" unless all 10 QA layers are complete.

---

## Core Principle

**Automate everything deterministic. Manual QA only for real platform behavior and visual smoke checks.**

| Can be automated | Must be manual |
|-----------------|----------------|
| Formula correctness | Google Sheets import behavior |
| Data validation existence | Dropdown UI interaction |
| Column/header completeness | Print layout appearance |
| Sample data counts | Copy link test from incognito |
| Formula pattern verification | Visual review on target platform |
| Number format verification | PDF rendering |
| Brand text presence | Marketplace listing preview |
| No-debug-text scan | — |
| GS function compatibility lint | — |
| Delivery ZIP contents | — |

---

## The 10 QA Layers

Every product must implement these 10 layers before reaching "Delivery Ready" status.

### Layer 1: Automated Workbook Validation

**Script:** `build/validate_workbook.py`

Minimum checks:
- Workbook opens without corruption
- Tab count matches spec
- Tab order matches spec
- All column headers present and correctly named
- All required formulas exist (bare pattern check)
- Data validations (dropdowns) present on required columns
- Freeze panes on data tabs
- Tab colors match brand spec
- Formula cells styled (gray fill vs input fill)
- No hidden sheets
- No macros/VBA
- No external workbook links
- No debug/internal text (`TODO`, `FIXME`, `DEBUG`, `WIP`, `XXX`)
- File is in `build/` directory (not delivered prematurely)

### Layer 2: Formula / Business Logic Tests

**Script:** `build/test_workbook_formulas.py`

Must independently calculate expected values from source data and verify:
- All cross-sheet references resolve correctly
- Tax, totals, outstanding, and status formulas produce correct values
- Dashboard KPIs (revenue, counts, averages) match data
- Summary tables (revenue by month, status breakdown, top clients) match data
- Invoice generator calculations (line items, subtotal, tax, total)
- IFERROR wrappers present where division is possible
- No hardcoded values where formulas should exist

**Rule:** Every formula must be tested. If openpyxl cannot calculate it, compute the expected value in Python from the raw data.

### Layer 3: Google Sheets Compatibility Lint

**Script:** `build/lint_google_sheets_compatibility.py`

Scans every formula and flags:
- Excel-only functions (XLOOKUP, FILTER, LAMBDA, etc.)
- Risky GS functions (INDIRECT, OFFSET, HYPERLINK)
- External workbook references
- Structured table references (`[@column]`)
- Dynamic array spill operators
- Local file path references
- VBA / macro references
- Unquoted sheet names containing spaces
- Unknown/unrecognized functions

**Allowed functions:** SUM, SUMIF, SUMIFS, COUNTIF, COUNTIFS, IF, IFERROR, TODAY, VLOOKUP, TEXT, AVERAGE, DATE, YEAR, MONTH, DAY, MIN, MAX, ROUND, LEFT, RIGHT, MID, LEN, TRIM, UPPER, LOWER, `&` (concatenation), and standard arithmetic operators.

### Layer 4: UI / Layout / Static Checks

**Script:** `build/test_workbook_layout.py`

Automated checks for:
- Product name (brand) present on Start Here and Dashboard
- All tabs contain expected headings and labels
- Dashboard has all KPI card labels
- Invoice Generator has all required sections (From, Bill To, Line Items, Summary, Payment)
- Settings tab has all configuration sections
- Required freeze panes set correctly
- Key tables have styled headers (bold)
- Date formatting on date columns
- Currency formatting on money columns
- No debug/internal text in buyer-facing sheets

### Layer 5: Manual Smoke QA

**Document:** `docs/GOOGLE_SHEETS_MANUAL_QA_RUNBOOK.md`

Minimal manual steps (target: 10–15 minutes):
1. Upload XLSX to Google Drive
2. Open with Google Sheets (verify no conversion errors)
3. Verify all tabs present
4. Spot-check 3–5 formulas (no #REF!, #VALUE!, #DIV/0!)
5. Verify dropdowns work in UI
6. Verify Dashboard displays correctly
7. Verify Invoice Generator print/export layout
8. Create and test copy link from incognito
9. Paste link into buyer-facing file

**Results documented in:** `qa/GOOGLE_SHEETS_MANUAL_QA_RESULTS.md`

### Layer 6: Delivery Package QA

**Document:** `qa/TEST_CASES_DELIVERY_PACKAGE.md`

Tests:
- All 3 delivery filenames use correct brand prefix
- No version numbers in buyer-facing filenames
- ZIP contains exactly 3 files (flat structure, no subdirectories)
- ZIP contains no internal docs, QA files, listing assets, or screenshots
- Copy link file exists and contains brand + instructions
- Copy link URL works (tested manually)
- Workbook title includes brand name
- PDF guide title includes brand name
- No old brand names in any delivery file
- Support email present in PDF and copy link file

**Run as last step before delivery finalization.**

### Layer 7: Marketplace Asset QA

**Document:** `SCREENSHOT_PLAN.md` + asset specification

Tests:
- Cover image communicates value at thumbnail size
- Dashboard screenshot shows real data
- Primary/secondary/supporting feature screenshots capture distinct value
- All screenshots show actual product, no generic mockups
- Text legible at marketplace display sizes
- Brand appears where appropriate
- No UI chrome, bookmarks, or personal info visible
- Consistent dimensions across all images
- 6-image set per spec: Cover, Dashboard, Primary Feature, Secondary Feature, Supporting Feature, What's Included

### Layer 8: Listing Copy QA

**Document:** `LISTING_COPY_GUMROAD.md`, `LISTING_COPY_PAYHIP.md`

Tests:
- Product title clear and searchable
- Subtitle explains value proposition
- What's Included lists specific deliverables
- Who It's For targets right buyer
- Benefits address buyer pain points
- FAQ answers common hesitations
- Support contact included
- Price set (Product #1 baseline: $7)
- Gallery images uploaded in correct order
- ZIP uploaded as product file
- Cover image set as thumbnail
- Preview/test purchase works end-to-end

### Layer 9: Link / Copy-Link QA

Tests:
- Google Sheets copy link works (opens copy dialog from incognito)
- Link URL uses `/copy` suffix (forces buyer to make their own copy)
- Link pasted into `google-sheets-copy-link.txt`
- Link file contains brand name and usage instructions
- Support email present in link file
- Excel file opens without errors from the ZIP

### Layer 10: Final Pre-Publish QA Gate

**Document:** `PRE_PUBLISH_REVIEW_CHECKLIST.md` (sections A–G)

Gate check: All 10 QA layers must pass before "Delivery Ready" status is set.

The gate keeper (AI or human) must verify:
- All automated QA scripts pass with zero failures
- All manual smoke tests are documented as PASS
- Delivery ZIP verified programmatically
- Copy link tested from incognito
- Marketplace listing preview complete
- No old brand/staging content remains

---

## Pass Thresholds

| Layer | Required Pass Rate | Notes |
|-------|-------------------|-------|
| 1. Automated Validation | 100% | All checks must pass |
| 2. Formula Tests | 100% | All formula groups must pass |
| 3. GS Compatibility Lint | 100% | Zero blockers; warnings acceptable with justification |
| 4. UI/Layout Checks | 100% | All automated checks must pass |
| 5. Manual Smoke QA | 100% | All 9 steps must pass |
| 6. Delivery Package QA | 100% | All tests must pass |
| 7. Marketplace Asset QA | 100% | All 6 images meet spec |
| 8. Listing Copy QA | 100% | All sections complete |
| 9. Link/Copy-Link QA | 100% | Link tested and verified |
| 10. Pre-Publish Gate | 100% | All sections A–G checked |

---

## Automation Priority

When adding QA to a new product, implement layers in this order:

1. **Layer 1** (validate_workbook.py) — catches structural issues first
2. **Layer 2** (test_workbook_formulas.py) — catches formula bugs
3. **Layer 3** (lint_google_sheets_compatibility.py) — catches compatibility issues
4. **Layer 4** (test_workbook_layout.py) — catches UI issues
5. **Layer 5–10** — manual/documentation layers (created during build planning)

---

## Template Files

The following templates provide reusable starting points for each product:

| Layer | Template |
|-------|----------|
| 1–4 (Automated QA) | `templates/AUTOMATED_QA_PLAN_TEMPLATE.md` |
| 2 (Formula Tests) | `templates/FORMULA_TEST_CASES_TEMPLATE.md` |
| 5 (Manual Smoke QA) | `templates/MANUAL_QA_RUNBOOK_TEMPLATE.md` |
| 1–10 (Overall QA) | `templates/QA_CHECKLIST_TEMPLATE.md` |
| 6 (Delivery QA) | `templates/DELIVERY_QA_TEMPLATE.md` |

---

## Enforcement

1. **Product workspace setup** must include QA directory (`qa/`) and script directory (`build/`)
2. **Build phase** must create stub QA test case files referencing these templates
3. **QA phase** must implement all 10 layers before assets can be generated
4. **Pre-publish gate** rejects any product with incomplete QA coverage

**No product can become "Delivery Ready" unless all 10 QA layers are complete.**
