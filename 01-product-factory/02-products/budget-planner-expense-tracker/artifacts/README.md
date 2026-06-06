# Budget Planner & Expense Tracker — Artifact

## Generated Files

| File | Status |
|------|--------|
| `budget-planner-expense-tracker-v1.xlsx` | Initial build (retained for reference) |
| `budget-planner-expense-tracker-v1.1.xlsx` | Previous version (retained for reference) |
| `budget-planner-expense-tracker-v1.2.xlsx` | **Current recommended version** (navigation fixed for Google Sheets) |

### v1.2 Changes

- **Fixed** Navigation links: replaced broken openpyxl hyperlinks (incompatible with Google Sheets) with plain tab-name listings and text instructions.
- **Added** Google Sheets navigation tip: "In Google Sheets, use the sheet tabs at the bottom to navigate."
- **Added** "Go to Start Here" plain text instruction on all 6 data tabs (replaces broken clickable back-links).
- **Preserved** all 91 formulas, dropdowns, conditional formatting, charts, and sample data from v1.1.
- **Automated QA**: 55/55 checks pass.
- **Formula count**: 91 (unchanged).

### v1.1 Changes (included in v1.2)

- **Fixed** Dashboard Net Savings formula: was `=B3-B4` (blank row), now `=B3-B5` (Income − Expenses)
- **Fixed** Dashboard Savings Rate % formula: was `=IFERROR(B5/B3,0)` (Expenses/Income), now `=IFERROR(B7/B3,0)` (Net Savings/Income)
- **Fixed** Bills Tracker unpaid highlighting: replaced static cell fill with real conditional formatting (highlight follows status changes)

## Spreadsheet Tabs

| # | Tab | Purpose |
|---|-----|---------|
| 1 | Start Here | Setup instructions, currency note, warnings, checklist |
| 2 | Monthly Budget | Planned vs actual income/expenses/savings by category |
| 3 | Expense Tracker | Log every expense with date, category, payment method |
| 4 | Bills Tracker | Track recurring bills and payment status |
| 5 | Debt Tracker | Monitor debt payoff progress across multiple debts |
| 6 | Savings Tracker | Track savings goals with progress % |
| 7 | Dashboard | Summary cards, category breakdown, charts |

## Formula Areas

- **Monthly Budget**: SUMIF formulas pull actual amounts from Expense Tracker by category. Difference column shows planned vs actual variance.
- **Expense Tracker**: Month auto-fills from Date column via TEXT formula.
- **Debt Tracker**: Payoff Progress % = (Starting - Current) / Starting, with IFERROR.
- **Savings Tracker**: Progress % = Current / Target, with IFERROR.
- **Dashboard**: Summary cards use SUMIF, COUNTIF, SUM, AVERAGE across tabs. Category spending table uses SUMIF per category. Two charts: expense pie chart and income/expenses/savings bar chart.

## How to Use in Google Sheets

1. Upload the XLSX to Google Drive.
2. Open with Google Sheets.
3. File → Save as Google Sheets.
4. All formulas and formatting are preserved.
5. Navigation is plain-text based: use the sheet tabs at the bottom to switch between sections.

## How to Create a Copy Link

After opening in Google Sheets:
1. File → Share → Publish to web.
2. Or set sharing to "Anyone with the link can view" and copy the URL.

## How to Export to XLSX

From Google Sheets: File → Download → Microsoft Excel (.xlsx)

## What Still Needs Manual Verification

- [ ] Open file in Excel and verify no formula breakage (SUMIF cross-sheet references)
- [ ] Open file in Google Sheets and test all tabs
- [ ] Verify navigation works: sheet tabs at the bottom (not clickable links)
- [ ] Verify charts render correctly
- [ ] Test data validation dropdowns on Expense Tracker, Bills Tracker
- [ ] Test conditional formatting on Monthly Budget difference column
- [ ] Verify Dashboard summary values match source tabs
- [ ] Clear sample data before creating buyer copy (optional — sample data helps first-time users)

## Known Limitations

- SUMIF references use full-column ranges (e.g., `'Expense Tracker'!C:C`). This works in both Excel and Google Sheets but may cause slower performance in Excel with very large datasets.
- Navigation is plain-text based (not clickable hyperlinks) for Google Sheets compatibility. Use sheet tabs at the bottom to switch sections.
- No VBA macros or advanced automation.
- Charts are Excel native charts — may need regeneration in Google Sheets after upload.
- Interest calculations in Debt Tracker are for tracking progress only; they do not model compound interest.
- The file was generated programmatically. Manual formatting polish (row heights, print areas, exact color matching) may be desired before listing.
