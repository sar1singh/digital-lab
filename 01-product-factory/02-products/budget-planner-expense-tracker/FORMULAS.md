# Formulas — Budget Planner & Expense Tracker

All formulas use Google Sheet syntax. Equivalent Excel formulas are noted where they differ.

## Monthly Budget Tab

### Category Totals (Expense Side)
Cell D3 (Housing Actual): `=SUMIF('Expense Tracker'!B:B, "Housing", 'Expense Tracker'!F:F)`
Cell E3 (Housing Difference): `=C3-D3` (Planned - Actual)

Repeat for each category matching the Expense Tracker category list.

### Income Total
Cell under Income section, Actual column: `=SUMIF('Expense Tracker'!B:B, "Salary", 'Expense Tracker'!F:F)` + SUMIF for each income category.

Simpler: Use a range sum for income-type rows:
`=SUMPRODUCT((B2:B20="Income")*D2:D20)` — but manual SUM of income category formulas is clearer.

### Total Expenses
`=SUM(D[expense_start]:D[expense_end])` — sum Actual column for all expense rows.

### Total Income
`=SUM(D[income_start]:D[income_end])` — sum Actual column for all income rows.

### Difference (Total)
`=SUM(C[total_income]:C[total_expenses]) - SUM(D[total_income]:D[total_expenses])` or use Net row.

**Excel equivalent:** Same formulas. Use `'Expense Tracker'!B:B` reference syntax — Excel may require structured references or named ranges for cross-sheet SUMIF.

## Expense Tracker Tab

### Month Auto-Fill
Column G: `=TEXT(A2, "MMMM")` or `=MONTH(A2)`

**Excel equivalent:** `=TEXT(A2, "MMMM")`

Drag down the column.

## Debt Tracker Tab

### Payoff Progress
Cell G2: `=(B2-C2)/B2`
Format as percentage.

If Starting Balance is 0, add IFERROR: `=IFERROR((B2-C2)/B2, 0)`

**Excel equivalent:** Same formula.

## Savings Tracker Tab

### Progress %
Cell E2: `=D2/C2`
Format as percentage.

If Target Amount is 0: `=IFERROR(D2/C2, 0)`

**Excel equivalent:** Same formula.

## Dashboard Tab

### Total Income
`=SUMIF('Monthly Budget'!B:B, "Income", 'Monthly Budget'!D:D)`

### Total Expenses
`=SUMIF('Monthly Budget'!B:B, "Expense", 'Monthly Budget'!D:D)`

### Net Savings
`=B2-B3` (Total Income - Total Expenses)

### Savings Rate %
`=IFERROR(B4/B2*100, 0)` or `=(B4/B2)*100` formatted as percentage.

### Bills Due Count
`=COUNTIF('Bills Tracker'!E:E, "Unpaid")`

### Debt Remaining
`=SUM('Debt Tracker'!C:C)`

### Savings Goal Progress (Average)
`=AVERAGE('Savings Tracker'!E:E)`

### Top Spending Category
`=INDEX('Monthly Budget'!A:A, MATCH(LARGE('Monthly Budget'!D:D, 1), 'Monthly Budget'!D:D, 0))`
Returns the category name with the highest actual spending.

**Excel equivalent:** Same formulas. Ensure sheet names with spaces are wrapped in single quotes.
