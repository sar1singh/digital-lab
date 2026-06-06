# Build Checklist — Budget Planner & Expense Tracker

## Sheet Setup  (Done — generated programmatically)

- [x] 7 tabs created and named correctly
- [x] Formula cells marked with gray background
- [x] Dashboard gridlines removed
- [x] Consistent formatting applied across all tabs

## Start Here Tab  (Done)

- [x] Setup instructions complete
- [x] Income entry instructions clear
- [x] Expense entry instructions clear
- [x] Dashboard usage explained
- [x] "Do not edit formula cells" warning present

## Monthly Budget Tab  (Done)

- [x] Income section with categories and planned amount
- [x] Expense section with categories, planned, actual, difference
- [x] Category total formulas working (SUMIF from Expense Tracker)
- [x] Monthly total formulas working
- [x] Difference column (planned - actual) working

## Expense Tracker Tab  (Done)

- [x] All columns created per spec
- [x] Month auto-fill via TEXT formula
- [x] Data validation on Category column
- [x] Data validation on Payment Method column
- [x] Data validation on Planned/Unplanned column

## Bills Tracker Tab  (Done)

- [x] All columns created per spec
- [x] Data validation on Frequency column
- [x] Data validation on Paid Status column
- [x] Unpaid bills highlighted with red fill

## Debt Tracker Tab  (Done)

- [x] All columns created per spec
- [x] Payoff Progress formula (%) with IFERROR
- [x] Interest rate formatted as percentage

## Savings Tracker Tab  (Done)

- [x] All columns created per spec
- [x] Progress % formula with IFERROR
- [x] Target Date formatted as date

## Dashboard Tab  (Done)

- [x] Total Income from Monthly Budget (SUMIF)
- [x] Total Expenses from Monthly Budget (SUMIF)
- [x] Net Savings formula
- [x] Savings Rate % formula (IFERROR)
- [x] Bills Due count (COUNTIF)
- [x] Debt Remaining total (SUM)
- [x] Savings Goal Progress average (AVERAGE)
- [x] Category spending breakdown (SUMIF per category)
- [x] Pie chart (expenses by category)
- [x] Bar chart (income vs expenses vs savings)

## Sample Data  (Done)

- [x] 18 realistic expense entries
- [x] 6 bills entries
- [x] 3 debt entries
- [x] 3 savings goals
- [x] Sample data works with all formulas
- [x] Sample data clearly marked as example (Start Here note)

## QA Test Suite

- [x] QA test suite created (qa/ directory — 8 files)
- [x] Automated QA checks passed (55 checks, 0 P0/P1 blockers)
- [x] v1.1 created with fixes (Dashboard formulas, Bills Tracker CF)
- [x] v1.2 created with navigation fix (broken hyperlinks removed, plain text instructions added for Google Sheets compatibility)
- [x] Navigation QA report created (qa/NAVIGATION_QA_REPORT.md)
- [x] Manual Google Sheets QA passed (v1.2 verified working in Google Sheets)

## Packaging Tasks

- [x] Final buyer-facing workbook copied (delivery/budget-planner-expense-tracker.xlsx)
- [x] Delivery folder created with all buyer-facing files
- [x] Google Sheets copy link file created (delivery/google-sheets-copy-link.txt)
- [x] Release notes created (delivery/release-notes.txt)
- [x] Quick-start guide Markdown created (delivery/quick-start-guide.md)
- [x] Quick-start guide HTML created (delivery/quick-start-guide.html)
- [x] Quick-start guide PDF generated (delivery/budget-planner-expense-tracker-quick-start-guide.pdf)
- [x] Listing/demo assets generated (5 images in delivery/listing-assets/)
- [x] Screenshots placeholder guide created (delivery/screenshots/README.md)
- [x] Delivery zip created (delivery/budget-planner-expense-tracker-delivery.zip)
- [x] Customer-facing brand updated to Nivora (all delivery files, images, PDF, listing copy)
- [x] Delivery PDF regenerated with Nivora brand
- [x] Listing assets regenerated with Nivora brand
- [x] Final zip regenerated with updated files
- [x] BRAND_QA_CHECKLIST.md created
- [x] Google Sheets copy link pasted into delivery/google-sheets-copy-link.txt
- [x] Final ZIP regenerated with clean buyer-only contents (3 files)
- [x] Final ZIP QA completed (FINAL_ZIP_QA.md)
- [x] Dashboard B40/B41 formulas fixed: "Expenses" (=B4->=B5), "Net Savings" (=B5->=B7)
- [ ] Capture real screenshots per delivery/screenshots/README.md
- [ ] Create Gumroad listing from LISTING_COPY_GUMROAD.md
- [ ] Create Payhip listing from LISTING_COPY_PAYHIP.md
- [ ] Publish and record URLs in PRODUCT_CATALOG.csv
