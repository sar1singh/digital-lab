# Test Cases — Formulas — Budget Planner & Expense Tracker

## Monthly Budget

### TC-F-01: Total Income Updates When Income Changes

| Field | Value |
|-------|-------|
| Test ID | TC-F-01 |
| Priority | P0 |
| Area | Monthly Budget |
| Steps | 1. Note current Total Income value (cell below income section). 2. Change Salary Planned Amount from 4500 to 5000. 3. Observe Total Income. |
| Expected result | Total Income increases by 500. Revert to 4500 after test. |
| Status | |

### TC-F-02: Planned Expense Total Updates

| Field | Value |
|-------|-------|
| Test ID | TC-F-02 |
| Priority | P0 |
| Area | Monthly Budget |
| Steps | 1. Note current Total Expenses planned value. 2. Change Housing Planned from 1200 to 1300. 3. Observe Total Expenses. |
| Expected result | Total Expenses increases by 100. Revert to 1200 after test. |
| Status | |

### TC-F-03: Actual Expense Total Pulls from Expense Tracker

| Field | Value |
|-------|-------|
| Test ID | TC-F-03 |
| Priority | P0 |
| Area | Monthly Budget |
| Steps | 1. Note Total Expenses Actual value. 2. Add a new row in Expense Tracker: Housing, $200. 3. Return to Monthly Budget. 4. Observe Total Expenses Actual. |
| Expected result | Total Expenses Actual increases by approximately $200 (combined with existing Housing entries). Remove the test row after confirming. |
| Status | |

### TC-F-04: Difference Formula Works (Planned - Actual)

| Field | Value |
|-------|-------|
| Test ID | TC-F-04 |
| Priority | P0 |
| Area | Monthly Budget |
| Steps | 1. Observe the Difference column for any expense category. 2. Verify the value equals Planned minus Actual. |
| Expected result | Difference = Planned − Actual. Positive values indicate underspend (green). Negative values indicate overspend (red). |
| Status | |

### TC-F-05: Category Totals Match Expected

| Field | Value |
|-------|-------|
| Test ID | TC-F-05 |
| Priority | P1 |
| Area | Monthly Budget |
| Steps | 1. Pick a category (e.g., Groceries). 2. Manually sum all Groceries entries from Expense Tracker. 3. Compare to the Actual cell for Groceries in Monthly Budget. |
| Expected result | Manual sum matches the Monthly Budget Actual cell for that category. |
| Status | |

---

## Expense Tracker

### TC-F-06: Month Auto-Fills from Date

| Field | Value |
|-------|-------|
| Test ID | TC-F-06 |
| Priority | P1 |
| Area | Expense Tracker |
| Steps | 1. Enter a new row with Date = 07/04/2026. 2. Observe the Month column. |
| Expected result | Month column displays "July" (or "7") based on the date entered. |
| Status | |

### TC-F-07: Amount Change Affects Monthly Budget

| Field | Value |
|-------|-------|
| Test ID | TC-F-07 |
| Priority | P0 |
| Area | Expense Tracker → Monthly Budget |
| Steps | 1. Note the Groceries Actual in Monthly Budget. 2. In Expense Tracker, change a Groceries entry amount (e.g., from $95 to $150). 3. Return to Monthly Budget. 4. Observe Groceries Actual. |
| Expected result | Groceries Actual updates to reflect the changed amount. Revert after test. |
| Status | |

### TC-F-08: Blank Rows Do Not Break Formulas

| Field | Value |
|-------|-------|
| Test ID | TC-F-08 |
| Priority | P1 |
| Area | Expense Tracker |
| Steps | 1. Leave row 20 blank (no data). 2. Verify no #REF!, #VALUE!, or #DIV/0! errors appear anywhere in the workbook. |
| Expected result | Blank rows produce empty cells. No spreadsheet-wide formula errors. |
| Status | |

---

## Debt Tracker

### TC-F-09: Payoff Progress % Calculates Correctly

| Field | Value |
|-------|-------|
| Test ID | TC-F-09 |
| Priority | P0 |
| Area | Debt Tracker |
| Steps | 1. Note Credit Card A: Starting=$3200, Current=$2100. 2. Calculate: (3200-2100)/3200 = 34.4%. 3. Compare to Payoff Progress % cell. |
| Expected result | Payoff Progress % = 34.4% (or 34%). |
| Status | |

### TC-F-10: Current Balance = 0 Shows 100%

| Field | Value |
|-------|-------|
| Test ID | TC-F-10 |
| Priority | P0 |
| Area | Debt Tracker |
| Steps | 1. Set Credit Card A Current Balance to 0 temporarily. 2. Observe Payoff Progress %. 3. Revert to 2100 after test. |
| Expected result | Payoff Progress % = 100%. |
| Status | |

### TC-F-11: Blank Debt Rows Do Not Error

| Field | Value |
|-------|-------|
| Test ID | TC-F-11 |
| Priority | P1 |
| Area | Debt Tracker |
| Steps | 1. Add a blank row below existing debts. 2. Check the formula cell in the Payoff Progress column. |
| Expected result | Blank row shows 0% or empty. No #DIV/0! error visible (IFERROR handles it). |
| Status | |

### TC-F-12: Zero Starting Balance Does Not Break

| Field | Value |
|-------|-------|
| Test ID | TC-F-12 |
| Priority | P1 |
| Area | Debt Tracker |
| Steps | 1. Enter a test row with Starting Balance = 0, Current Balance = 0. 2. Observe Payoff Progress %. 3. Delete the test row. |
| Expected result | Payoff Progress % shows 0% or empty. No #DIV/0! error (IFERROR returns 0). |
| Status | |

---

## Savings Tracker

### TC-F-13: Progress % Calculates Correctly

| Field | Value |
|-------|-------|
| Test ID | TC-F-13 |
| Priority | P0 |
| Area | Savings Tracker |
| Steps | 1. Note Emergency Fund: Target=$10000, Current=$4500. 2. Calculate: 4500/10000 = 45%. 3. Compare to Progress % cell. |
| Expected result | Progress % = 45%. |
| Status | |

### TC-F-14: Current = Target Shows 100%

| Field | Value |
|-------|-------|
| Test ID | TC-F-14 |
| Priority | P0 |
| Area | Savings Tracker |
| Steps | 1. Set Vacation Fund Current Amount = 2500 (same as Target). 2. Observe Progress %. 3. Revert to 800 after test. |
| Expected result | Progress % = 100%. |
| Status | |

### TC-F-15: Blank Savings Rows Do Not Error

| Field | Value |
|-------|-------|
| Test ID | TC-F-15 |
| Priority | P1 |
| Area | Savings Tracker |
| Steps | 1. Add a blank row below existing goals. 2. Check the Progress % formula cell. |
| Expected result | Blank row shows 0% or empty. No #DIV/0! error. |
| Status | |

### TC-F-16: Zero Target Amount Does Not Break

| Field | Value |
|-------|-------|
| Test ID | TC-F-16 |
| Priority | P1 |
| Area | Savings Tracker |
| Steps | 1. Enter a test row with Target = 0, Current = 0. 2. Observe Progress %. 3. Delete the test row. |
| Expected result | Progress % shows 0% or empty. No #DIV/0! error (IFERROR wraps division). |
| Status | |

---

## Dashboard Cross-Sheet

### TC-F-17: Total Income Matches Monthly Budget

| Field | Value |
|-------|-------|
| Test ID | TC-F-17 |
| Priority | P0 |
| Area | Dashboard |
| Steps | 1. Note Total Income in Dashboard (cell B3). 2. Go to Monthly Budget and verify Total Income Actual. 3. Compare. |
| Expected result | Dashboard Total Income = Monthly Budget Total Income Actual. |
| Status | |

### TC-F-18: Total Expenses Match

| Field | Value |
|-------|-------|
| Test ID | TC-F-18 |
| Priority | P0 |
| Area | Dashboard |
| Steps | 1. Note Total Expenses in Dashboard (cell B4). 2. Go to Monthly Budget and verify Total Expenses Actual. 3. Compare. |
| Expected result | Dashboard Total Expenses = Monthly Budget Total Expenses Actual. |
| Status | |

### TC-F-19: Net Savings = Income − Expenses

| Field | Value |
|-------|-------|
| Test ID | TC-F-19 |
| Priority | P0 |
| Area | Dashboard |
| Steps | 1. Note Total Income (B3) and Total Expenses (B4). 2. Subtract manually. 3. Compare to Net Savings (B5). |
| Expected result | Net Savings = Total Income − Total Expenses. |
| Status | |

### TC-F-20: Savings Rate % = Net Savings / Income

| Field | Value |
|-------|-------|
| Test ID | TC-F-20 |
| Priority | P0 |
| Area | Dashboard |
| Steps | 1. Note Net Savings (B5) and Total Income (B3). 2. Calculate Net Savings / Income. 3. Compare to Savings Rate % (B6). |
| Expected result | Savings Rate % = Net Savings / Total Income (formatted as %). |
| Status | |

### TC-F-21: Debt Remaining Matches Debt Tracker

| Field | Value |
|-------|-------|
| Test ID | TC-F-21 |
| Priority | P0 |
| Area | Dashboard |
| Steps | 1. Note Debt Remaining in Dashboard (B9). 2. Go to Debt Tracker and sum all Current Balances. 3. Compare. |
| Expected result | Dashboard Debt Remaining = SUM of all Current Balances in Debt Tracker. |
| Status | |

### TC-F-22: Savings Goal Progress Matches Savings Tracker

| Field | Value |
|-------|-------|
| Test ID | TC-F-22 |
| Priority | P0 |
| Area | Dashboard |
| Steps | 1. Note Avg Savings Progress in Dashboard (B10). 2. Go to Savings Tracker and average all Progress % values. 3. Compare. |
| Expected result | Dashboard Avg Savings Progress = AVERAGE of Progress % in Savings Tracker. |
| Status | |

### TC-F-23: No Formula Error Values Visible

| Field | Value |
|-------|-------|
| Test ID | TC-F-23 |
| Priority | P0 |
| Area | All tabs |
| Steps | 1. Scan every cell in every tab. 2. Look for #DIV/0!, #REF!, #VALUE!, #N/A, #NAME?, #NUM!, or #NULL!. |
| Expected result | No error values visible anywhere in the workbook (with sample data loaded). |
| Status | |
