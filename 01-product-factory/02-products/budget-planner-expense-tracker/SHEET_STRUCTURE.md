# Sheet Structure — Budget Planner & Expense Tracker

## Tab 1: Start Here

| Row | Content |
|-----|---------|
| Title | Budget Planner & Expense Tracker — Quick Start |
| Section 1 | How to set up your budget |
| Section 2 | How to enter income |
| Section 3 | How to enter expenses |
| Section 4 | How to use the Dashboard |
| Section 5 | Important: Do not edit cells with blue background (formula cells) |

## Tab 2: Monthly Budget

| Column | Header | Type | Notes |
|--------|--------|------|-------|
| A | Category | Text | Income and expense categories |
| B | Type | Dropdown | Income / Expense / Savings |
| C | Planned Amount | Number | User enters planned budget |
| D | Actual Amount | Formula | Auto-summed from Expense Tracker |
| E | Difference | Formula | Planned - Actual |
| F | Notes | Text | Optional |

Category rows:
- Income: Salary, Freelance, Side Hustle, Other Income, Total Income
- Expenses: Housing, Utilities, Groceries, Transport, Insurance, Healthcare, Entertainment, Dining Out, Subscriptions, Shopping, Education, Personal Care, Miscellaneous, Total Expenses
- Savings: Savings Goal, Total Savings

## Tab 3: Expense Tracker

| Column | Header | Type | Notes |
|--------|--------|------|-------|
| A | Date | Date | Format: MM/DD/YYYY |
| B | Category | Dropdown | Same categories as Monthly Budget |
| C | Description | Text | Short description |
| D | Payment Method | Dropdown | Cash, Credit Card, Debit Card, Bank Transfer, PayPal, Other |
| E | Planned/Unplanned | Dropdown | Planned, Unplanned |
| F | Amount | Number | Positive values only |
| G | Month | Formula | Auto-derived from Date |
| H | Notes | Text | Optional |

## Tab 4: Bills Tracker

| Column | Header | Type | Notes |
|--------|--------|------|-------|
| A | Bill Name | Text | e.g. Rent, Electricity, Internet |
| B | Due Date | Date | Day of month |
| C | Amount | Number | Bill amount |
| D | Frequency | Dropdown | Monthly, Quarterly, Yearly, One-Time |
| E | Paid Status | Dropdown | Paid, Unpaid, Upcoming |
| F | Payment Method | Text | How it's paid |
| G | Paid Date | Date | When paid |
| H | Notes | Text | Optional |

## Tab 5: Debt Tracker

| Column | Header | Type | Notes |
|--------|--------|------|-------|
| A | Debt Name | Text | e.g. Credit Card A, Student Loan |
| B | Starting Balance | Number | Original balance |
| C | Current Balance | Number | Current remaining |
| D | Minimum Payment | Number | Required monthly payment |
| E | Extra Payment | Number | Additional payment beyond minimum |
| F | Interest Rate | Percentage | APR |
| G | Payoff Progress | Formula | (Starting - Current) / Starting |

## Tab 6: Savings Tracker

| Column | Header | Type | Notes |
|--------|--------|------|-------|
| A | Goal Name | Text | e.g. Emergency Fund, Vacation |
| B | Target Amount | Number | Goal amount |
| C | Current Amount | Number | Amount saved so far |
| D | Monthly Contribution | Number | Amount saved per month |
| E | Progress % | Formula | Current / Target |
| F | Target Date | Date | Goal completion date |

## Tab 7: Dashboard

| Cell | Metric | Formula/Source |
|------|--------|----------------|
| B2 | Total Income | =SUMIF(Monthly Budget!B:B, "Income", Monthly Budget!D:D) |
| B3 | Total Expenses | =SUMIF(Monthly Budget!B:B, "Expense", Monthly Budget!D:D) |
| B4 | Net Savings | =B2-B3 |
| B5 | Savings Rate % | =(B4/B2)*100 |
| B7 | Bills Due This Month | =COUNTIF(Bills Tracker!E:E, "Unpaid") |
| B8 | Debt Remaining | =SUM(Debt Tracker!C:C) |
| B9 | Savings Goal Progress | =AVERAGE(Savings Tracker!E:E) |
| B11 | Top Spending Category | =INDEX + SORT formula |
| Chart 1 | Monthly Income vs Expenses | Bar chart |
| Chart 2 | Expense by Category | Pie/donut chart |
| Chart 3 | Savings Goal Progress | Progress bar or gauge |
