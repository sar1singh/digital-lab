# Test Cases: Google Sheets Smoke QA — Invoice Generator & Payment Tracker

**QA Layer:** 5 (Manual Smoke QA)
**Coverage standard:** `01-product-factory/07-systems/QA_COVERAGE_STANDARD.md`

**Reduced to 9 manual smoke tests.** Full automated formula, layout, and GS compatibility
lint coverage is provided by `build/run_all_qa.py` (4 suites).

See `docs/GOOGLE_SHEETS_MANUAL_QA_RUNBOOK.md` for detailed instructions.
See `qa/GOOGLE_SHEETS_MANUAL_QA_RESULTS.md` for results tracker.

| ID | Step | Test | Expected | P0/P1 |
|----|------|------|----------|-------|
| GS-01 | 1 | Upload XLSX to Google Drive | Upload completes without error | P0 |
| GS-02 | 2 | Open with Google Sheets | Opens without conversion errors | P0 |
| GS-03 | 3 | All 7 tabs present | All tabs open and named correctly | P0 |
| GS-04 | 4 | Spot-check 3–5 key formulas | No #REF!, #VALUE!, #DIV/0! errors | P0 |
| GS-05 | 5 | Dropdowns work in UI | Status + Payment Method dropdowns functional | P1 |
| GS-06 | 6 | Dashboard displays correctly | KPI values visible, formulas resolved | P0 |
| GS-07 | 7 | Invoice Generator print/export layout | Fits page, professional appearance | P1 |
| GS-08 | 8 | Copy link created and tested | Opens copy dialog from incognito | P0 |
| GS-09 | 9 | Link pasted into buyer-facing file | `build/google-sheets-copy-link-template.txt` updated | P0 |
