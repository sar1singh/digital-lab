# Next Actions

## Product 1: Budget Planner & Expense Tracker

### Phase A: Product Workspace (Done)

- [x] PRODUCT_SPEC.md — product overview, tabs, format, target buyer
- [x] BUILD_CHECKLIST.md — task checklist for build phase
- [x] SHEET_STRUCTURE.md — column layout for all 7 tabs
- [x] FORMULAS.md — all formulas documented
- [x] SAMPLE_DATA.md — realistic sample rows per tab
- [x] QUICK_START_GUIDE.md — 1-page PDF-ready guide
- [x] LISTING_COPY_GUMROAD.md — full listing copy for Gumroad
- [x] LISTING_COPY_PAYHIP.md — full listing copy for Payhip
- [x] SCREENSHOT_PLAN.md — 5 screenshot descriptions
- [x] QA_CHECKLIST.md — quality assurance checklist

### Phase B: Build Spreadsheet (Done)

- [x] XLSX generated with all 7 tabs via Python/openpyxl script
- [x] All formulas from FORMULAS.md implemented (SUMIF, SUM, IFERROR, TEXT, COUNTIF, AVERAGE)
- [x] Sample data populated in all tabs
- [x] Formatting: headers, currency, percentage, date formats
- [x] Data validation dropdowns on Expense Tracker and Bills Tracker
- [x] Conditional formatting on Monthly Budget difference and unpaid bills
- [x] Dashboard: summary cards, category spending lookup, pie chart, bar chart
- [x] Freeze panes on data tabs

### Phase C: Final Publishing Polish (Done)

- [x] Workbook QA complete (91 formulas, 7 tabs)
- [x] PDF quick-start guide ready
- [x] ZIP package ready (3 buyer files only)
- [x] Google Sheets copy link ready (Nivora branded)
- [x] Listing copy ready (Gumroad + Payhip)
- [x] Listing images ready (5 assets)
- [x] Brand verified: Nivora, no "Work by Sar1" in buyer files

### Phase D: Publish Product #1 (Manual — Blocked)

1. Upload final ZIP to Gumroad
2. Upload 6 gallery images to Gumroad
3. Set price to $7
4. Test checkout preview
5. Publish Gumroad listing
6. Create Payhip listing
7. Publish Payhip listing
8. Record listing URLs in PRODUCT_CATALOG.csv
9. Update PRODUCT_CATALOG.csv status to Published

---

## Product 2: Invoice Generator & Payment Tracker

### Phase A: Planning (Done)

- [x] PRODUCT_SPEC.md — product overview, tabs, format, target buyer
- [x] SHEET_STRUCTURE.md — column layout for all 7 tabs
- [x] FORMULAS.md — all formulas with expected values
- [x] SAMPLE_DATA.md — realistic sample rows
- [x] QUICK_START_GUIDE.md — guide content
- [x] LISTING_COPY_GUMROAD.md — full Gumroad listing copy
- [x] LISTING_COPY_PAYHIP.md — full Payhip listing copy
- [x] SCREENSHOT_PLAN.md — 6 screenshot descriptions
- [x] QA_CHECKLIST.md — 10-layer QA coverage

### Phase B: Build Spreadsheet (Done)

- [x] XLSX generated via `build/build_workbook.py` (Python/openpyxl)
- [x] All formulas, formatting, data validation, freeze panes implemented
- [x] Sample data populated

### Phase C: QA (Done — All 10 layers PASS)

- [x] Layer 1: Formula Integrity (automated) — PASS
- [x] Layer 2: Structural Integrity (automated) — PASS
- [x] Layer 3: Cross-Reference Integrity (automated) — PASS
- [x] Layer 4: GS Compatibility (automated + manual) — PASS
- [x] Layer 5: Manual Functional QA — PASS (3 bugs found/fixed)
- [x] Layer 6: Sample Data Verification — PASS
- [x] Layer 7: Asset Specs — PASS
- [x] Layer 8: Asset Files (6 PNG screenshots) — PASS
- [x] Layer 9: PDF Guide — PASS
- [x] Layer 10: Delivery Package — PASS (Sections A-G all PASS)

### Phase D: Assets (Done)

- [x] 6 listing-asset spec files created
- [x] 6 PNG screenshots generated
- [x] Screenshot QA (79 test cases) — PASS

### Phase E: Delivery (Done)

- [x] PDF quick-start guide generated (10 pages, fpdf2)
- [x] Delivery folder: workbook + PDF + copy-link.txt
- [x] Delivery ZIP built: `nivora-invoice-generator-payment-tracker-delivery.zip`
- [x] Delivery QA (22 test cases) — PASS
- [x] Pre-publish review — Sections A-G all PASS
- [x] Retrospective completed — `docs/PRODUCT_2_RETROSPECTIVE.md`
- [x] 3 new factory rules added (Rules 23-25)

### Phase F: Publish Product #2 (Manual — Blocked)

1. Create Gumroad listing from `LISTING_COPY_GUMROAD.md`
2. Create Payhip listing from `LISTING_COPY_PAYHIP.md`
3. Upload delivery ZIP + 6 screenshots to both listings
4. Set price to $7
5. Test checkout preview
6. Publish both listings
7. Record listing URLs in PRODUCT_CATALOG.csv
8. Update PRODUCT_CATALOG.csv status to Published

---

## Product 3: Project Budget Tracker

### Phase A: Planning (Done)

- [x] PRODUCT_SPEC.md — product overview, tabs, format, target buyer
- [x] SHEET_STRUCTURE.md — column layout for all tabs
- [x] FORMULAS.md — all formulas with expected values per Rule 25
- [x] SAMPLE_DATA.md — realistic sample rows
- [x] SCREENSHOT_PLAN.md — 6 screenshot descriptions
- [x] BUILD_CHECKLIST.md — build phase task checklist
- [x] QA_CHECKLIST.md — 10-layer QA coverage
- [x] QUICK_START_GUIDE.md — guide content
- [x] LISTING_COPY_GUMROAD.md — full Gumroad listing copy
- [x] LISTING_COPY_PAYHIP.md — full Payhip listing copy

### Phase B: Build Spreadsheet (Next — wait until Products 1-2 are listed or parked)

1. Create `build/` directory structure
2. Create `build/build_workbook.py` — Python/openpyxl generator with all tabs
3. Create `build/validate_workbook.py` — structural checks
4. Create `build/test_workbook_formulas.py` — formula assertions
5. Create `build/lint_google_sheets_compatibility.py` — GS compatibility
6. Create `build/test_workbook_layout.py` — layout/UI tests
7. Create `build/run_all_qa.py` — unified QA runner
8. Create `build/generate_pdf.py` — PDF generator

### Phase C: QA (After build)

9. Run Layers 1-4 (automated QA)
10. Upload to GS and run Layer 5 (manual smoke QA)
11. Fix bugs found

### Phase D: Assets (After QA)

12. Create 6 listing-asset spec files
13. Generate 6 PNG screenshots at 100% zoom
14. Run screenshot QA

### Phase E: Delivery (After assets)

15. Generate PDF quick-start guide
16. Build delivery folder and ZIP
17. Run delivery QA

### Phase F: Publish (After delivery — blocked until Products 1-2 are on marketplace)

18. Create Gumroad listing
19. Create Payhip listing
20. Record URLs in PRODUCT_CATALOG.csv
21. Complete retrospective
22. Update factory standards

---

## Anti-Drift

- No SaaS.
- No website.
- No logo.
- No branding system.
- No newsletter.
- No audience-building plan.
- No broad research loop.
- No automation system.
- No product factory app.
- No starting Product 4 before Product 3 is published.
- No modifying Products 1-2 (frozen).
