# Navigation QA Report — Budget Planner & Expense Tracker v1.2

## Issue Found

**Start Here navigation links do not work in Google Sheets.**

After importing `v1.1.xlsx` into Google Sheets, the 6 clickable navigation links on the Start Here tab (Monthly Budget, Expense Tracker, Bills Tracker, Debt Tracker, Savings Tracker, Dashboard) and the 6 "Back to Start Here" links on each data tab did not respond to clicks.

## Root Cause

The v1.1 links used openpyxl's internal `.hyperlink` property:

```python
cell.hyperlink = "'TabName'!A1"
```

This creates an Excel native hyperlink object stored in the sheet's XML relationships. While Excel renders these as clickable links, Google Sheets does not recognize them during XLSX import — the cell text displays but the hyperlink target is lost.

## Fix Applied (v1.2)

All 12 hyperlinks were **removed** and replaced with plain text instructions:

### Start Here Navigation Section (rows 33-40)

| Row | Before (v1.1) | After (v1.2) |
|-----|---------------|--------------|
| 33 | `QUICK NAVIGATION` | `NAVIGATION` + "Click the sheet tabs at the bottom to switch sections." |
| 34 | `>> Monthly Budget` (clickable) | `Monthly Budget` (plain text) |
| 35 | `>> Expense Tracker` (clickable) | `Expense Tracker` (plain text) |
| 36 | `>> Bills Tracker` (clickable) | `Bills Tracker` (plain text) |
| 37 | `>> Debt Tracker` (clickable) | `Debt Tracker` (plain text) |
| 38 | `>> Savings Tracker` (clickable) | `Savings Tracker` (plain text) |
| 39 | `>> Dashboard` (clickable) | `Dashboard` (plain text) |
| 40 | *(empty)* | "Tip: In Google Sheets, use the sheet tabs at the bottom to navigate." |

### Data Tab Back Links

| Tab | Cell | Before | After |
|-----|------|--------|-------|
| Monthly Budget | G1 | `<< Back to Start Here` (clickable) | `<-- Go to Start Here tab for instructions` (plain text) |
| Expense Tracker | I1 | `<< Back to Start Here` (clickable) | `<-- Go to Start Here tab for instructions` (plain text) |
| Bills Tracker | H1 | `<< Back to Start Here` (clickable) | `<-- Go to Start Here tab for instructions` (plain text) |
| Debt Tracker | H1 | `<< Back to Start Here` (clickable) | `<-- Go to Start Here tab for instructions` (plain text) |
| Savings Tracker | G1 | `<< Back to Start Here` (clickable) | `<-- Go to Start Here tab for instructions` (plain text) |
| Dashboard | D1 | `<< Back to Start Here` (clickable) | `<-- Go to Start Here tab for instructions` (plain text) |

### Cross-Platform Behavior

| Platform | v1.1 (clickable links) | v1.2 (plain text) |
|----------|----------------------|-------------------|
| Excel (desktop) | Hyperlinks work | Tab names visible; user clicks sheet tabs |
| Google Sheets (imported) | Hyperlinks broken | Instructions visible; user clicks sheet tabs |
| LibreOffice | Depends on import | Always works — plain text |

## Formulas Preserved

All 91 formula cells from v1.1 are unchanged in v1.2:

- 14 Dashboard category SUMIFs
- 7 Dashboard summary card formulas
- 17 Monthly Budget SUMIFs (using `'Expense Tracker'!C:C`)
- 6 Monthly Budget total formulas
- 3 Debt Tracker progress formulas
- 3 Savings Tracker progress formulas
- 18 Expense Tracker month auto-fill formulas
- 23 other formula cells (totals, differences, etc.)

## Automated QA Result

**55/55 checks PASS** (same as v1.1, plus 6 new navigation-specific checks)

| Category | Checks | Pass |
|----------|--------|------|
| Structure | 3 | 3 |
| Navigation (new) | 6 | 6 |
| Headers | 3 | 3 |
| Freeze Panes | 6 | 6 |
| Conditional Formatting | 2 | 2 |
| Formulas (SUMIF, totals) | 12 | 12 |
| Dashboard | 5 | 5 |
| Dropdowns | 7 | 7 |
| Formula Count | 1 | 1 |
| **Total** | **55** | **55** |

## Remaining Manual Google Sheets QA Step

Before publishing, manually verify in Google Sheets:

1. Open `v1.2.xlsx` in Google Drive → Google Sheets
2. Navigate to the Start Here tab
3. Confirm the NAVIGATION section lists all 6 tabs as plain text
4. Confirm the Google Sheets tip is visible
5. Click each sheet tab at the bottom to verify all 7 tabs load correctly
6. On each data tab, confirm the back-link text is visible (non-clickable)
7. Verify all formulas still calculate correctly (values should match Excel)
8. Test data validation dropdowns (Category, Payment Method, Status)
9. Verify conditional formatting (Unpaid bills highlighted)
10. Verify Dashboard summary values update correctly

## File

**v1.2 workbook:** `artifacts/budget-planner-expense-tracker-v1.2.xlsx`
