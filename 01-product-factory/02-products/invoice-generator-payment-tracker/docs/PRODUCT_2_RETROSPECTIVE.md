# Product #2 Retrospective — Nivora Invoice Generator & Payment Tracker

**Build date:** 2026-06-07
**Status:** Ready to Publish
**Total effort:** ~10 hours (1.25 working days)
**Effort vs Product #1:** ~30% faster (QA framework, asset specs, delivery standard pre-built)

---

## Product Overview

| Attribute | Value |
|-----------|-------|
| Format | Google Sheet / Excel (7 tabs) |
| Target buyer | Freelancers and small business owners needing clean invoices + payment tracking |
| Price | $7 |
| Build approach | Python/openpyxl generator (`build_workbook.py`) |
| QA layers | 10/10 PASS |
| Bugs found | 3 (all fixed before delivery) |
| Delivery | ZIP with 3 files (workbook, PDF, copy link) |

---

## What Worked Well

- **Upfront spec docs** (PRODUCT_SPEC.md, SHEET_STRUCTURE.md, FORMULAS.md, SAMPLE_DATA.md) served as single source of truth — no logic drift during build
- **Python workbook generator** allowed full regeneration in seconds after bug fixes (edit Python, rebuild, re-run QA)
- **4 automated QA suites** (85 structural checks + 19 formula groups + 11 GS lint rules + 10 layout sections) caught every bug before manual testing
- **9-step manual GS smoke QA runbook** caught 3 bugs that automation couldn't (formula text rendering, GS-specific DV behavior, dropdown UI)
- **6 listing-asset spec files** with exact crop areas, expected values, annotations, color palettes, acceptance criteria — made screenshot generation a mechanical execution
- **79 screenshot QA test cases** created a clear pass/fail framework for visual assets
- **fpdf2 PDF generator** with embedded screenshots produced professional 10-page buyer guide
- **Delivery standard rules** made packaging a checklist execution — no internal files leaked
- **10-layer QA gate rule** forced systematic verification before packaging

---

## Bugs Found

### Bug 1: Invoice Total Formula

**Root cause:** `build_workbook.py:802` used `=D24+D25` instead of `=D23+D25`. D24 = Tax Rate field (0.10), D25 = Tax Amount (500.00). Formula computed Tax Rate + Tax Amount instead of Subtotal + Tax Amount. Row reference was off by one.

**Fix:** Changed to `=D23+D25` (Subtotal + Tax Amount = 5,500.00).

**Prevention rule:** Every formula spec in FORMULAS.md must include explicit cell references AND expected values for at least one test row. Build script must use structured row lookups instead of hardcoded row numbers where possible.

---

### Bug 2: Average Invoice Value

**Root cause:** `build_workbook.py:503` used `COUNTIFS(M:M,"<>Draft")` — whole-column range M:M. In Google Sheets, empty cells in column M contain formula output `""` from IFERROR, so COUNTIFS counted them as matching `"<>Draft"`. This inflated the denominator, producing `$1,364.00` instead of `$2,182.40`.

**Fix:** Changed `M:M` to `M2:M999` and added `"<>"` non-empty criterion: `COUNTIFS(M2:M999,"<>Draft",M2:M999,"<>")`.

**Prevention rule (Rule 23):** Never use whole-column ranges (`A:A`, `M:M`) in COUNTIFS/SUMIFS with negative-match criteria (`"<>Draft"`). Always use finite ranges and add a non-empty criterion. QA rule F-013 to flag whole-column ranges with negative-match criteria.

---

### Bug 3: Data Validation Dropdowns

**Root cause:** `build_workbook.py:197,405` referenced cells `Settings!$C$6` and `Settings!$C$7` as dropdown sources. These cells were empty because the Settings tab had not been populated. During Google Sheets conversion, broken range references caused dropdowns to show nothing or error.

**Fix:** Changed data validations to inline comma-separated lists: `"Active,Inactive,Archived"` and `"Bank Transfer,PayPal,Cash,Credit Card,Check"`.

**Prevention rule (Rule 24):** Data validations referencing other sheet cells break during GS conversion if source cells are empty. Use inline comma-separated lists for GS-compatible data validations. Add lint rule L-011 to detect range-based data validations.

---

## QA Learnings

- **Automated QA before manual QA is essential.** Layers 1-4 (automated) caught formula errors, structural issues, and GS incompatibilities before any human looked at the workbook. Manual QA (Layer 5) was then focused solely on platform behavior — formula rendering, dropdown UI, conditional formatting appearance.
- **4 QA suites is the right number:** workbook validation, formula tests, GS compatibility lint, layout/UI tests. Single `run_all_qa.py` entry point makes execution trivial.
- **79 screenshot QA test cases** was thorough but high-maintenance. For Product #3, reduce to 30-40 critical tests covering dimensions, branding, annotations, and file presence. Skip per-pixel checks.
- **22 delivery QA tests** was appropriate. It verified ZIP contents, file sizes, branding, copy link validity, and exclusion of internal files. Keep this pattern.
- **Expected values in formula specs prevent row-off-by-one bugs.** Bug 1 would have been caught at spec time if `=D23+D25` with expected 5,500.00 had been documented in FORMULAS.md before the generator was written.
- **GS import test is non-negotiable.** The XLSX-to-GS conversion changes behavior in subtle ways (formula text rendering, DV sources, conditional format ranges). Always import and run the 9-step smoke QA.

## Asset Learnings

- **Write spec files before capturing screenshots.** The 6 listing-asset spec files with exact crop areas, annotation positions, color palettes, and acceptance criteria made screenshot generation a mechanical task. No creative decisions during capture.
- **Screenshot QA checklist prevents reshoots.** With 79 test cases, every screenshot issue was caught before delivery. The time investment in writing tests paid for itself in zero reshoots.
- **1536x1024 is a good cover/detail image size.** It fits Gumroad's recommended aspect ratio (3:2). For dashboard and feature screenshots, use sizes that match the actual content area to avoid excessive whitespace.
- **Document the GS zoom level and viewport size** used for capture. Product #2 screenshots were taken at varying zoom levels, causing slight size inconsistency. Standardize to 100% zoom for Product #3.
- **Screenshot before building the PDF.** The PDF embeds screenshots, so screenshots must be final before PDF generation. This is captured in the `ASSETS_BEFORE_PDF` ordering rule.

## PDF Learnings

- **fpdf2 with embedded PNG screenshots produces a professional result.** 10 pages, all sections, consistent branding. The markdown-to-PDF pipeline via Python is fast to regenerate.
- **Generate PDF as the 2nd-last delivery artifact** (before ZIP). This prevents the PDF from being rebuilt multiple times as screenshots change.
- **Include the same branding in the PDF** (Nivora logo/name, consistent colors, fonts). The PDF is a buyer-facing document and must pass brand review.
- **PDF generation script should be in `build/` alongside the workbook generator**, not in its own directory. Keep all build scripts together.
- **Document page count expectations.** The current 10-page guide is appropriate. For simpler products (Product #3), aim for 6-8 pages.

## Delivery Learnings

- **The 3-file ZIP standard (workbook + PDF + copy link) works.** No buyer needs more than these. No internal files leaked.
- **Copy link must be tested from an incognito window.** A link that works for the creator may not work for a buyer who hasn't authenticated.
- **ZIP building must be the absolute last step.** Every time a delivery file changes, the ZIP must be rebuilt. The automated ZIP verification test ensures the ZIP matches the expected content list.
- **Delivery folder should only contain buyer-facing files.** Internal QA files, build scripts, screenshots, and spec docs must never be copied into delivery/.
- **Verification checklist:** Verify workbook opens without errors, PDF renders correctly, copy link works, ZIP contains exactly 3 files, no version numbers in filenames, branding consistent.

## Listing Learnings

- **Gumroad and Payhip listing copy are 95% identical.** Write one source file and generate the second. This prevents drift between listings and saves 10 minutes.
- **6-image gallery order matters:** Cover → Dashboard → Primary Feature → Secondary Feature → Supporting Feature → What's Included. This order tells a story. Document it in the asset spec.
- **Cover image must work at both full size (1536x1024) and thumbnail (small card).** Test the cover at thumbnail resolution before uploading.
- **Listing copy should highlight the specific buyer problem** (invoicing hassle, late payments) before describing features. Product #2 copy does this well.
- **Price ($7) matches Product #1.** Consistent pricing builds buyer trust. Don't change price until there's data to justify it.

---

## Factory Improvements

The following rules were added to factory standards based on Product #2 lessons:

1. **Rule 23 — COUNTIFS negative-match finite range:** Any COUNTIFS/SUMIFS using `"<>X"` must use finite range (not whole-column) and include non-empty criterion `"<>"`.
2. **Rule 24 — Data validation inline lists for GS compatibility:** All data validations must use inline comma-separated lists instead of sheet cell references.
3. **Rule 25 — Formula expected values in spec:** Every formula in FORMULAS.md must have an expected numeric value for at least one test row.

Additional proposed improvements for Product #3:
4. **Screenshot dimension standard:** Capture at consistent zoom level (100%) and document viewport size.
5. **Single listing copy source file:** Write one source, generate platform-specific versions programmatically.

---

## Reusable Components

### Direct Reuse (copy + rename)
| Component | Path | Notes |
|-----------|------|-------|
| QA runner | `build/run_all_qa.py` | Universal — imports from build/ scripts |
| Validation script | `build/validate_workbook.py` | Replace tab/column/row checks per product |
| Formula tests | `build/test_workbook_formulas.py` | Replace expected values per product |
| GS compatibility lint | `build/lint_google_sheets_compatibility.py` | Generic — works on any workbook |
| Layout/UI tests | `build/test_workbook_layout.py` | Replace tab/section checks per product |
| PDF generator | `build/generate_pdf.py` | Replace content, keep fpdf2 wrapper |
| Screenshot QA template | `qa/TEST_CASES_SCREENSHOTS.md` | Update image names for product |
| Delivery QA template | `qa/TEST_CASES_DELIVERY_PACKAGE.md` | Generic — update filenames only |
| Pre-publish review | `qa/PRE_PUBLISH_REVIEW_RESULTS.md` | Template format, auto-populate layers |
| Listing copy template | `LISTING_COPY_GUMROAD.md` | Structural template for any product |
| Quick-start guide template | `QUICK_START_GUIDE.md` | Section structure reusable |

### Pattern Reuse (adapt per product)
| Pattern | Description |
|---------|-------------|
| Workbook generator | Python/openpyxl script building all tabs, formulas, formatting, data validation, freeze panes |
| QA checklist pattern | `QA_CHECKLIST.md` with 10-layer coverage map |
| Asset spec pattern | 6-file listing-assets/ with capture instructions, annotations, acceptance criteria |
| Delivery folder pattern | workbook + PDF + copy-link.txt, no extras |
| ZIP verification | Programmatic check of contents vs expected list |
| Pre-publish gate | 10-layer sign-off with Section A-G checklist |

---

## Time Estimates

| Phase | Actual Effort | Notes |
|-------|--------------|-------|
| Planning | 2 hours | Spec documents, formula design, sample data |
| Workbook generation | 3 hours | Python generator, debugging 3 formula bugs |
| Automated QA (Layers 1-4) | 1 hour | Writing 4 QA scripts, adjusting for pattern |
| Manual QA (Layer 5) | 1 hour | GS upload, 9 smoke tests, 3 bugs found/fixed |
| Asset specs (Layer 7) | 1 hour | 6 spec files, 79 test cases |
| Screenshot generation | 0.5 hour | User-generated via guided instructions |
| PDF generation | 0.5 hour | Markdown + fpdf2 script |
| Delivery packaging + QA | 0.5 hour | Copy files, build ZIP, verify |
| Pre-publish review | 0.5 hour | Execute checklist, produce results |
| **Total** | **~10 hours** | ~1.25 working days |

**Expected effort for Product #3: ~6-7 hours** — QA scripts, asset specs, and delivery are template work. Workbook generation is the variable.

---

## Final Verdict

**Would I change anything if rebuilt from scratch?** Three changes:

1. **Write formula tests before the generator.** For Bug 1 (Invoice Total), a formula unit test written during spec phase would have caught the wrong cell reference the first time the generator ran, not during manual QA.

2. **Add GS data validation check to automated lint earlier.** Bug 3 (broken dropdowns) was caught during manual QA. An L-011 rule added at Layer 3 would have flagged it during `lint_google_sheets_compatibility.py` in the first pass.

3. **Don't write both listing copy files separately.** The Gumroad and Payhip copy are 95% identical. Write one source file, generate the second.

Overall: **Clean build.** All 3 bugs found and fixed before delivery. Factory process worked — specs first, automated QA, manual verification, then packaging. No buyer-facing issues. The 10-layer QA gate rule was the most important structural decision.
