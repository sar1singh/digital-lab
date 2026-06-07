# QA Checklist — Nivora Invoice Generator & Payment Tracker

**Status:** ALL 10 QA LAYERS PASSED — Ready to Publish.

**Reference:** This checklist maps to the Product Factory 10-layer QA standard
(`01-product-factory/07-systems/QA_COVERAGE_STANDARD.md`).

---

## Coverage Map

| Layer | Area | Coverage | Status |
|-------|------|----------|--------|
| 1 | Automated workbook validation | `build/validate_workbook.py` (85 checks) | PASS |
| 2 | Formula/business logic tests | `build/test_workbook_formulas.py` (19 groups) | PASS |
| 3 | GS compatibility lint | `build/lint_google_sheets_compatibility.py` (10 checks) | PASS |
| 4 | UI/layout tests | `build/test_workbook_layout.py` (10 sections) | PASS |
| 5 | Manual smoke QA | `docs/GOOGLE_SHEETS_MANUAL_QA_RUNBOOK.md` (9 steps) | PASS |
| 6 | Delivery package QA | `qa/TEST_CASES_DELIVERY_PACKAGE.md` | PASS |
| 7 | Marketplace asset QA | `qa/TEST_CASES_SCREENSHOTS.md` (79 tests) | PASS |
| 8 | Listing copy QA | `LISTING_COPY_GUMROAD.md`, `LISTING_COPY_PAYHIP.md` | PASS |
| 9 | Link/copy-link QA | `build/google-sheets-copy-link-template.txt` | PASS |
| 10 | Pre-publish gate | `PRE_PUBLISH_REVIEW_CHECKLIST.md` | PASS |

## Formula QA

- [x] Invoice Register: Tax Amount = Subtotal * Tax Rate
- [x] Invoice Register: Total = Subtotal + Tax Amount
- [x] Invoice Register: Outstanding = Total - Amount Paid
- [x] Invoice Register: Status formula correct (Paid/Overdue/Partial/Sent auto; Draft manual-only)
- [x] Invoice Register: Status formula does NOT auto-produce "Draft" (verified)
- [x] Dashboard: Total Revenue present (SUMIFS excluding Draft)
- [x] Dashboard: Paid Revenue present (SUMIFS Paid)
- [x] Dashboard: Outstanding Revenue present (SUMIFS)
- [x] Dashboard: Invoice counts present
- [x] Dashboard: Active Clients count present
- [x] Dashboard: Average Invoice Value present (IFERROR)
- [x] Invoice Generator: Amount = Quantity * Rate
- [x] Invoice Generator: Subtotal = SUM of amounts
- [x] Invoice Generator: Total = Subtotal + Tax
- [x] Payment Tracker: Client Name is VLOOKUP formula (IFERROR-wrapped) referencing Invoice Register

## UI QA

- [x] All tab names correct and readable
- [x] Brand name (Nivora) appears on Start Here and Dashboard
- [x] All formula cells have gray background
- [x] All input cells have white/green background
- [x] Dashboard gridlines removed
- [x] Freeze panes set correctly
- [x] Currency formatting on all money columns
- [x] Date formatting on date columns
- [x] Percentage formatting on tax rate
- [x] Header rows formatted distinctively
- [ ] Print layout acceptable on Invoice Generator tab

## Data Validation QA

- [x] Clients tab: Status dropdown (Active, Inactive, Archived)
- [x] Payment Tracker: Payment Method dropdown from Settings
- [x] Invoice Register: Status is formula-only (no dropdown; values produced by formula)
- [x] Draft is available as manual override in Settings list

## Google Sheets Smoke QA (Passed — 9/9 tests)

Results: `qa/GOOGLE_SHEETS_MANUAL_QA_RESULTS.md`

- [x] GS-01: Upload XLSX to Google Drive
- [x] GS-02: Open with Google Sheets without errors
- [x] GS-03: All 7 tabs open correctly
- [x] GS-04: Spot-check formulas (no #REF!, #VALUE!, #DIV/0!) — 3 bugs fixed during testing
- [x] GS-05: Dropdowns work in UI (Status, Payment Method)
- [x] GS-06: Dashboard values display correctly
- [x] GS-07: Invoice Generator print/export layout acceptable
- [x] GS-08: Copy link created and tested from incognito
- [x] GS-09: Link pasted into `build/google-sheets-copy-link-template.txt`

## Navigation QA

- [x] Tab order is logical and consistent
- [x] Start Here provides navigation guidance
- [x] No broken references when navigating between tabs
- [x] Google Sheets: hyperlinks replaced with plain text instructions

## Delivery Package QA (Layer 6 — Passed)

Reference: `qa/TEST_CASES_DELIVERY_PACKAGE.md`

Delivery folder verified:
- [x] `delivery/nivora-invoice-generator-payment-tracker.xlsx` — exists, opens correctly
- [x] `delivery/nivora-invoice-generator-payment-tracker-quick-start-guide.pdf` — exists, 10 pages
- [x] `delivery/google-sheets-copy-link.txt` — exists, brand + link verified
- [x] `delivery/nivora-invoice-generator-payment-tracker-delivery.zip` — exists, 3 files inside
- [x] ZIP contains exactly: workbook + PDF + copy-link (no extras)
- [x] No internal files in delivery /
- [x] All filenames use brand prefix convention
- [x] No version numbers in filenames

## Buyer Link File QA (Layer 9 — Passed)

- [x] Google Sheets copy link works (opens copy dialog from incognito)
- [x] Link uses `/copy` suffix
- [x] Link pasted into `build/google-sheets-copy-link-template.txt`
- [x] Link file contains brand name and usage instructions
