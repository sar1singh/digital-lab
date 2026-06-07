# Google Sheets Manual QA Results — Nivora Invoice Generator & Payment Tracker

**QA Layer:** 5 (Manual Smoke QA)
**Coverage standard:** `01-product-factory/07-systems/QA_COVERAGE_STANDARD.md`

**Workbook:** `build/nivora-invoice-generator-payment-tracker.xlsx`
**Test Date:** 2026-06-07
**Tested By:** sar1s
**Status:** PASSED — All 9 smoke tests passed

**Note:** Full automated QA (Layers 1–4: formula, layout, GS compatibility lint) passed via
`build/run_all_qa.py`. This smoke test (Layer 5) covers manual-only verification steps.

---

## Results Summary

| Total Tests | Passed | Failed | Skipped | Blocked |
|------------|--------|--------|---------|---------|
| 9 | 9 | 0 | 0 | 0 |

---

## Smoke Test Results

| ID | Step | Test | Expected | Status | Notes |
|----|------|------|----------|--------|-------|
| GS-01 | 1 | Upload XLSX to Google Drive | Upload completes without error | PASS | — |
| GS-02 | 2 | Open with Google Sheets | Opens without conversion errors | PASS | — |
| GS-03 | 3 | All 7 tabs present and named correctly | All tabs open | PASS | — |
| GS-04 | 4 | Spot-check formulas | No #REF!, #VALUE!, #DIV/0! | PASS | 3 bugs fixed during test (Invoice Total, Avg Invoice Value, dropdowns) |
| GS-05 | 5 | Dropdowns work in UI | Status + Method dropdowns functional | PASS | Fixed: inline lists instead of broken range refs |
| GS-06 | 6 | Dashboard displays correctly | KPI values visible | PASS | All 9 KPI values match expected |
| GS-07 | 7 | Invoice Generator print/export layout | Fits page, professional | PASS | — |
| GS-08 | 8 | Copy link created and tested | Opens copy dialog from incognito | PASS | Link: `https://docs.google.com/spreadsheets/d/1bGzHBf0SMqZZ-nzX26_EG_CwiDmhkrZJ/copy` |
| GS-09 | 9 | Link pasted into buyer-facing file | `google-sheets-copy-link-template.txt` updated | PASS | Updated |

---

## Notes

- **3 bugs discovered and fixed during QA:**
  1. Invoice Generator Total formula was `=D24+D25` (Tax Rate + Tax Amount) — fixed to `=D23+D25` (Subtotal + Tax Amount)
  2. Average Invoice Value used whole-column `M:M` in COUNTIFS counting empty cells — fixed to finite range `M2:M999` with non-empty criterion
  3. Both data validations referenced empty cells (`Settings!$C$6` and `Settings!$C$7`) instead of inline lists — fixed to inline comma-separated values
- Automated QA was also enhanced: F-013 now validates the formula uses finite range; L-011 now catches broken range references in data validations
- Copy link verified working from incognito browser

---

## Decision

- [x] All smoke tests pass — Ready for Asset Generation phase
- [ ] Issues found — See notes above; fixes required before proceeding

---

## Change Log

| Date | Change | Author |
|------|--------|--------|
| — | Reduced to 9 smoke tests (full automated QA covers formula/layout) | — |
| 2026-06-07 | All 9 GS smoke tests passed. 3 bugs fixed during QA. Product #2 — Google Sheets QA passed | sar1s |
