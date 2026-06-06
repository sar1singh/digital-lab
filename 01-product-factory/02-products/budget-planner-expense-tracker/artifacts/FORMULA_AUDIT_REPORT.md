# Formula Audit Report — Budget Planner & Expense Tracker v1.1

**Audit date:** 2026-06-07
**Workbook:** `artifacts/budget-planner-expense-tracker-v1.1.xlsx`

## Summary

| Metric | Value |
|--------|-------|
| Total formula cells | 91 |
| Tabs | 7 |
| Data rows with formulas | 100% |
| Navigation links (Start Here) | 6 |
| Back links (to Start Here) | 6 |
| Conditional formatting rules | 2 (Bills Tracker + Monthly Budget) |
| P0 issues | 0 |
| P1 issues | 0 |

## Issues Found & Fixed

### Fixed in v1.1

| # | Severity | Tab | Issue | Fix |
|---|----------|-----|-------|-----|
| 1 | P0 | Monthly Budget | 17 SUMIF formulas referenced `'Expense Tracker'!B:B` (Month column) instead of `'Expense Tracker'!C:C` (Category column), causing all Actual values to return $0 | Changed all `!B:B` → `!C:C` |
| 2 | P1 | All tabs | No navigable links between Start Here and data tabs | Added 6 HYPERLINK navigation links on Start Here + "Back to Start Here" link on each data tab |
| 3 | P1 | Dashboard | B3 (Total Income) pulled from Actual column D — income is planned, not tracked in Expense Tracker, so always returned $0 | Changed to pull from Planned column C: `=SUMIF('Monthly Budget'!B:B,"Income",'Monthly Budget'!C:C)` |
| 4 | P1 | Bills Tracker | Conditional formatting used static fill instead of FormulaRule | Replaced with `=FormulaRule($E2="Unpaid", red) + FormulaRule($E2="Paid", green)` |
| 5 | P1 | Dashboard | B7 Net Savings used `=B3-B4` (skipped row due to separator) | Corrected to `=B3-B5` |
| 6 | P1 | Dashboard | B9 Savings Rate used `=IFERROR(B5/B3,0)` (wrong numerator) | Corrected to `=IFERROR(B7/B3,0)` |
| 7 | P2 | All tabs | Formula cells not visually distinguished | Marked with gray background (`D6DCE4`) |
| 8 | P2 | Monthly Budget | No conditional formatting on variance | Added green for ≥0, red for <0 in Difference column |

## False Positives (Audit Clean)

These were flagged by the automated scanner but are NOT bugs:

- **Monthly Budget D1, E1** — Row 1 is the header row ("Category", "Planned Amount", "Actual Amount", "Difference"). Formulas are intentionally absent.
- **Monthly Budget D2** ("INCOME"), **D8** ("EXPENSES"), **D24** ("SAVINGS") — Section header/label rows. No formulas needed.
- **Dashboard B37** ("Monthly Income vs Expenses"), **B38** ("Metric") — Section label rows in the income/expense comparison area. No formulas needed.

## Formula Coverage by Tab

| Tab | Rows with Data | Have Formulas | % |
|-----|---------------|--------------|---|
| Start Here | 1 section | 6 nav links | — |
| Monthly Budget | 20 data rows | 20 | 100% |
| Expense Tracker | 18 data rows | 18 (month auto-fill) | 100% |
| Bills Tracker | 6 data rows | 0 (manual entry) | — |
| Debt Tracker | 3 data rows | 3 | 100% |
| Savings Tracker | 3 data rows | 3 | 100% |
| Dashboard | 14 summary + category rows | 14 | 100% |

## Known Design Decisions

1. **Income Actual = $0 with sample data** — Income is planned in Monthly Budget but not tracked in Expense Tracker (which tracks expenses). Dashboard now shows Planned Income to give useful summary. Users who want to track actual income against plan can add income entries in Expense Tracker using a custom category.
2. **Bills Tracker has no SUMIF** — Bill amounts are manually entered. Status column drives Dashboard B11 (Bills Due) via COUNTIF.
3. **Separator rows** — Even rows in Dashboard summary area (B4, B6, B8, B10, B12, B14) are intentionally blank for visual grouping.

## Recommendation

**Workbook is ready for publishing gate.** Run the 71-case manual QA suite in Excel and Google Sheets, then proceed to packaging and listing.
