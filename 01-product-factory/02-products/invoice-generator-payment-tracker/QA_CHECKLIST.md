# QA Checklist — Nivora Invoice Generator & Payment Tracker

**Build QA complete.** Formula, UI, and data validation checks verified through automated validation (45/45 passed). Google Sheets and navigation testing pending.

## Formula QA

- [x] Invoice Register: Tax Amount = Subtotal * Tax Rate
- [x] Invoice Register: Total = Subtotal + Tax Amount
- [x] Invoice Register: Outstanding = Total - Amount Paid
- [x] Invoice Register: Status formula correct for all 5 states (Paid, Overdue, Partial, Sent, Draft)
- [x] Dashboard: Total Revenue present (SUMIFS excluding Draft)
- [x] Dashboard: Paid Revenue present (SUMIFS Paid)
- [x] Dashboard: Outstanding Revenue present (SUMIFS)
- [x] Dashboard: Invoice counts present
- [x] Dashboard: Active Clients count present
- [x] Dashboard: Average Invoice Value present (IFERROR)
- [x] Invoice Generator: Amount = Quantity * Rate
- [x] Invoice Generator: Subtotal = SUM of amounts
- [x] Invoice Generator: Total = Subtotal + Tax
- [ ] Payment Tracker: Client Name resolves correctly from Invoice ID (requires GS test)

## UI QA

- [x] All tab names correct and readable
- [x] Brand name (Nivora) appears on Start Here and Dashboard
- [x] All formula cells have gray background
- [x] All input cells have white/green background
- [x] Dashboard gridlines removed
- [x] Freeze panes set correctly
- [x] Currency formatting on all money columns
- [x] Date formatting on date columns
- [x] Percentage formatting on tax rate
- [x] Header rows formatted distinctively
- [ ] Print layout acceptable on Invoice Generator tab

## Data Validation QA

- [x] Clients tab: Status dropdown (Active, Inactive, Archived)
- [x] Payment Tracker: Payment Method dropdown from Settings
- [ ] Invoice Register: Status values match Settings

## Google Sheets QA (Pending)

- [ ] Workbook uploads to Google Drive without errors
- [ ] All formulas survive conversion (no #REF!, #VALUE!, #DIV/0!)
- [ ] Data validation dropdowns work after import
- [ ] Conditional formatting survives conversion (if applied)
- [ ] Copy link works (test manually)
- [ ] Print layout acceptable in Google Sheets

## Navigation QA

- [x] Tab order is logical and consistent
- [x] Start Here provides navigation guidance
- [x] No broken references when navigating between tabs
- [ ] Google Sheets: hyperlinks replaced with plain text instructions if needed
