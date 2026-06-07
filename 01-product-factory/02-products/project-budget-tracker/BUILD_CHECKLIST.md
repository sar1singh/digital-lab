# Build Checklist — Nivora Project Budget Tracker

**Status:** Planning phase — not yet built.

## Sheet Setup
- [ ] 7 tabs created and named: Start Here, Dashboard, Projects, Expenses, Income, Categories, Settings
- [ ] Formula cells marked with gray background
- [ ] Input cells clearly marked (white/green background)
- [ ] Dashboard gridlines removed
- [ ] Consistent formatting across all tabs
- [ ] Freeze panes on data tabs (Projects, Expenses, Income, Categories)

## Start Here Tab
- [ ] Setup instructions complete
- [ ] Tab navigation guide
- [ ] Formula cell warning present
- [ ] Input cell guide present
- [ ] Sample data note present

## Dashboard Tab
- [ ] Total Budget formula (SUM)
- [ ] Total Spent formula (SUMIFS)
- [ ] Total Remaining formula
- [ ] % Budget Used formula (IFERROR)
- [ ] Total Income formula (SUMIFS)
- [ ] Net Profit formula
- [ ] Projects on/over budget (COUNTIFS with non-empty criterion)
- [ ] Budget by Project table
- [ ] Spending by Category table
- [ ] Monthly Spending Trend table
- [ ] Project Status Breakdown table

## Projects Tab
- [ ] All columns per spec
- [ ] Project ID column (auto)
- [ ] Project Name column
- [ ] Client column
- [ ] Budget column
- [ ] Total Spent formula (SUMIFS from Expenses — finite range)
- [ ] Remaining formula
- [ ] % Used formula (IFERROR)
- [ ] Status formula (On Budget / Over Budget / Completed / On Hold)

## Expenses Tab
- [ ] All columns per spec
- [ ] Date column
- [ ] Project column with dropdown (inline list from Projects)
- [ ] Category column with dropdown (inline list from Categories)
- [ ] Description column
- [ ] Amount column
- [ ] Notes column

## Income Tab
- [ ] All columns per spec
- [ ] Date column
- [ ] Project column with dropdown (inline list from Projects)
- [ ] Description column
- [ ] Amount column
- [ ] Payment Status column with dropdown (inline list "Paid,Pending,Expected")
- [ ] Notes column

## Categories Tab
- [ ] Category Name column
- [ ] Description column
- [ ] 8 sample categories populated

## Settings Tab
- [ ] Currency Symbol setting
- [ ] Project Status Values list
- [ ] Payment Status Values list

## Sample Data
- [ ] 10 projects populated
- [ ] 25 expenses distributed across projects
- [ ] 12 income entries
- [ ] Sample data works with all formulas
- [ ] Dashboard metrics match expected values

## Formatting
- [ ] Currency formatting on all monetary values
- [ ] Percentage formatting on % Used
- [ ] Date formatting on date columns
- [ ] Header row styling on all data tabs
- [ ] Column widths appropriate for content

## QA
- [ ] Automated formula checks pass
- [ ] Google Sheets import test passes
- [ ] Delivery package test passes
