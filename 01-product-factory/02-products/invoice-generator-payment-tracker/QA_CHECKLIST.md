# QA Checklist — Nivora Invoice Generator & Payment Tracker

## Formula QA

- [ ] Invoice Register: Tax Amount = Subtotal * Tax Rate
- [ ] Invoice Register: Total = Subtotal + Tax Amount
- [ ] Invoice Register: Outstanding = Total - Amount Paid
- [ ] Invoice Register: Status formula correct for all 5 states (Paid, Overdue, Partial, Sent, Draft)
- [ ] Dashboard: Total Revenue matches SUM of non-Draft invoices
- [ ] Dashboard: Paid Revenue matches SUM of Paid invoices
- [ ] Dashboard: Outstanding Revenue matches SUM of outstanding amounts
- [ ] Dashboard: Invoice counts match actual data
- [ ] Dashboard: Overdue detection works (TODAY past Due Date)
- [ ] Dashboard: Active Clients count matches Clients tab
- [ ] Dashboard: Average Invoice Value matches calculated value
- [ ] Invoice Generator: Amount = Quantity * Rate
- [ ] Invoice Generator: Subtotal = SUM of amounts
- [ ] Invoice Generator: Total = Subtotal + Tax
- [ ] Payment Tracker: Client Name resolves correctly from Invoice ID

## UI QA

- [ ] All tab names correct and readable
- [ ] Brand name (Nivora) appears on Start Here and Dashboard
- [ ] All formula cells have gray background
- [ ] All input cells have white/green background
- [ ] Dashboard gridlines removed
- [ ] Freeze panes set correctly
- [ ] Column widths reasonable for content
- [ ] Currency formatting on all money columns
- [ ] Date formatting on date columns
- [ ] Percentage formatting on tax rate
- [ ] Header rows formatted distinctively
- [ ] Print layout acceptable on Invoice Generator tab

## Data Validation QA

- [ ] Clients tab: Status dropdown (Active, Inactive, Archived)
- [ ] Payment Tracker: Payment Method dropdown from Settings
- [ ] Invoice Register: Status values match Settings

## Google Sheets QA

- [ ] Workbook uploads to Google Drive without errors
- [ ] All formulas survive conversion (no #REF!, #VALUE!, #DIV/0!)
- [ ] Data validation dropdowns work after import
- [ ] Conditional formatting survives conversion (if applied)
- [ ] Copy link works (test manually)
- [ ] Print layout acceptable in Google Sheets
- [ ] Charts render correctly (if applicable)

## Navigation QA

- [ ] Tab order is logical and consistent
- [ ] Start Here provides navigation guidance
- [ ] No broken references when navigating between tabs
- [ ] Google Sheets: hyperlinks replaced with plain text instructions if needed
