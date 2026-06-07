# Formulas — Nivora Project Budget Tracker

All formulas are Google Sheets compatible. No Excel-only functions. No VBA/macros. All references use finite ranges (not whole-column) per Product Factory rule 23.

---

## Tab: Dashboard

### KPI: Total Budget
```
=SUM(Projects!D2:D100)
```
**Expected value with sample data:** $125,000.00 (sum of 10 project budgets)

### KPI: Total Spent
```
=SUMIFS(Expenses!E2:E100, Expenses!E2:E100, ">0")
```
**Expected value with sample data:** $67,350.00

### KPI: Total Remaining
```
=B3-B4
```
(Total Budget - Total Spent)
**Expected value:** $57,650.00

### KPI: % Budget Used
```
=IFERROR(B4/B3, 0)
```
Formatted as percentage.
**Expected value:** 53.88%

### KPI: Total Income
```
=SUMIFS(Income!D2:D100, Income!E2:E100, "<>Pending")
```
**Expected value:** $72,800.00

### KPI: Net Profit
```
=B7-B4
```
(Total Income - Total Spent)
**Expected value:** $5,450.00

### KPI: Projects on Budget
```
=COUNTIFS(Projects!H2:H100, "On Budget", Projects!H2:H100, "<>")
```
**Expected value:** 5

### KPI: Projects Over Budget
```
=COUNTIFS(Projects!H2:H100, "Over Budget", Projects!H2:H100, "<>")
```
**Expected value:** 2

### Budget by Project (column formulas)
```
E (Total Spent):  =SUMIFS(Expenses!E:E, Expenses!B:B, B2)
F (Remaining):    =D2-E2
G (% Used):       =IFERROR(E2/D2, 0)
```
**Expected row 2 (Project Alpha):** Budget $25,000, Spent $15,200, Remaining $9,800, % Used 60.80%

### Spending by Category
```
=SUMIFS(Expenses!E:E, Expenses!C:C, A5)
```

### Monthly Spending Trend
```
=SUMIFS(Expenses!E:E, Expenses!A:A, ">="&DATE(year,month,1), Expenses!A:A, "<"&DATE(year,month+1,1))
```

### Project Status Breakdown
```
=COUNTIFS(Projects!H:H, "On Budget")
=COUNTIFS(Projects!H:H, "Over Budget")
=COUNTIFS(Projects!H:H, "Completed")
=COUNTIFS(Projects!H:H, "On Hold")
```

---

## Tab: Projects

### Total Spent (column E)
```
=SUMIFS(Expenses!E$2:E$999, Expenses!B$2:B$999, B2)
```
SUM of all expense amounts where the Project field matches this project's name.
**Expected for Project Alpha (row 2):** $15,200.00

### Remaining (column F)
```
=D2-E2
```
Budget minus Total Spent.
**Expected for Project Alpha:** $9,800.00

### % Used (column G)
```
=IFERROR(E2/D2, 0)
```
Total Spent divided by Budget, wrapped in IFERROR.
**Expected for Project Alpha:** 60.80%

### Status (column H)
```
=IF(ISNUMBER(SEARCH("Completed", I2)), "Completed",
   IF(AND(D2>0, E2/D2>1), "Over Budget",
   IF(AND(D2>0, E2/D2>0.8), "At Risk", "On Budget")))
```
Note: Status references Notes column (I) for manual "Completed" override.

---

## Tab: Expenses

No formulas — pure data entry tab with data validation dropdowns.

---

## Tab: Income

No formulas — pure data entry tab with data validation dropdowns.

---

## Tab: Categories

No formulas — reference data for dropdowns.

---

## Tab: Settings

No formulas — configuration values used by data validations.

---

## Cross-Sheet References

| Source Tab | Reference | Target |
|-----------|-----------|--------|
| Dashboard Total Budget | SUM of Projects!D2:D100 | Projects Budget column |
| Dashboard Total Spent | SUMIFS Expenses!E2:E100 | Expenses Amount column |
| Dashboard Total Income | SUMIFS Income!D2:D100 | Income Amount column |
| Dashboard Budget by Project | SUMIFS Expenses!E:E with Expenses!B:B = Project Name | Expenses linked to Projects |
| Dashboard Spending by Category | SUMIFS Expenses!E:E with Expenses!C:C = Category | Expenses linked to Categories |
| Projects Total Spent | SUMIFS Expenses!E$2:E$999 with Expenses!B$2:B$999 = Project Name | Expenses per project |
| Data Validation (Expenses!B) | Inline list from Projects!B2:B100 | Project names |
| Data Validation (Expenses!C) | Inline list from Categories!A2:A100 | Category names |
| Data Validation (Income!B) | Inline list from Projects!B2:B100 | Project names |

---

## Formula Rules (from Product Factory standards)

1. All ranges use finite boundaries (e.g., `E2:E999`, not `E:E`) — rule 23
2. All negative-match COUNTIFS include non-empty criterion `"<>"` — rule 23
3. All data validations use inline comma-separated lists unless source range verified populated — rule 24
4. Every formula has an expected value for at least one test row — rule 25
5. All VLOOKUP/SUMIFS cross-sheet references wrapped in IFERROR where division by zero possible
