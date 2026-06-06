# QA Checklist — Budget Planner & Expense Tracker

## Formulas

- [ ] All SUMIF formulas in Monthly Budget reference correct Expense Tracker categories
- [ ] Total Income formula sums correctly
- [ ] Total Expenses formula sums correctly
- [ ] Difference formulas (Planned - Actual) are correct
- [ ] Month auto-fill formula works in Expense Tracker
- [ ] Payoff Progress formulas in Debt Tracker calculate correctly
- [ ] Savings Progress formulas in Savings Tracker calculate correctly
- [ ] Dashboard Total Income matches Monthly Budget total
- [ ] Dashboard Total Expenses matches Monthly Budget total
- [ ] Dashboard Net Savings formula correct
- [ ] Dashboard Savings Rate % correct
- [ ] Dashboard Bills Due COUNTIF correct
- [ ] Dashboard Debt Remaining SUM correct
- [ ] Dashboard Savings Goal Progress AVERAGE correct
- [ ] IFERROR wrappers on all division formulas

## Sample Data

- [ ] Sample data populates all tabs
- [ ] Sample data produces correct totals on Dashboard
- [ ] Sample data marked as example (clear callout)
- [ ] Sample data category names match dropdown lists

## Formatting

- [ ] Formula cells have distinct background color (e.g., light blue)
- [ ] Input cells have clear borders
- [ ] Currency format applied to all amount columns
- [ ] Percentage format applied to progress columns
- [ ] Date columns formatted as dates
- [ ] Dashboard gridlines removed
- [ ] Consistent font across all tabs
- [ ] Column headers bold and frozen

## Data Validation

- [ ] Category column in Expense Tracker has dropdown
- [ ] Payment Method column in Expense Tracker has dropdown
- [ ] Planned/Unplanned column in Expense Tracker has dropdown
- [ ] Frequency column in Bills Tracker has dropdown
- [ ] Paid Status column in Bills Tracker has dropdown

## Conditional Formatting

- [ ] Overdue bills (past due date + Unpaid) highlighted
- [ ] Debt progress color scale (low → high)
- [ ] Savings progress color scale (low → high)
- [ ] Negative difference in budget highlighted

## Edge Cases

- [ ] Empty state: all tabs work with no data entered
- [ ] Zero values display correctly
- [ ] New row added to Expense Tracker appears in Dashboard
- [ ] Category name change works across all formulas

## Export

- [ ] Google Sheet copy link works
- [ ] Download as XLSX works
- [ ] No formulas broken in XLSX
- [ ] All 7 tabs present in XLSX
- [ ] Formatting preserved in XLSX

## Quick-Start Guide

- [ ] Guide covers all 7 steps
- [ ] Common mistakes section included
- [ ] Support note included
- [ ] Clear and readable at 1 page

## Listing Copy

- [ ] Title matches product name
- [ ] Price set to $7
- [ ] What's included matches actual deliverables
- [ ] Refund policy included
- [ ] FAQ answers common questions
- [ ] No typos or broken markdown
