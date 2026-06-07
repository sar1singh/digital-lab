# Build Checklist — Nivora Invoice Generator & Payment Tracker

## Sheet Setup

- [ ] 7 tabs created and named: Start Here, Dashboard, Clients, Invoice Register, Payment Tracker, Invoice Generator, Settings
- [ ] Formula cells marked with gray background
- [ ] Input cells clearly marked (white/green background)
- [ ] Dashboard gridlines removed
- [ ] Consistent formatting across all tabs
- [ ] Freeze panes on data tabs (Clients, Invoice Register, Payment Tracker)

## Start Here Tab

- [ ] Setup instructions complete
- [ ] Invoice creation instructions clear
- [ ] Payment tracking instructions clear
- [ ] Dashboard usage explained
- [ ] "Do not edit formula cells" warning present

## Dashboard Tab

- [ ] Total Revenue formula (SUMIFS excluding Draft)
- [ ] Paid Revenue formula (SUMIFS Paid)
- [ ] Outstanding Revenue formula (SUMIFS Sent + Overdue + Partial)
- [ ] Total Invoices count (COUNTA)
- [ ] Paid Invoices count (COUNTIFS)
- [ ] Unpaid Invoices count (COUNTIFS)
- [ ] Overdue Invoices count (COUNTIFS)
- [ ] Active Clients count (COUNTIFS)
- [ ] Average Invoice Value (IFERROR SUMIFS/COUNTIFS)
- [ ] Revenue by Month table
- [ ] Invoice Status Breakdown table
- [ ] Top Clients by Revenue table

## Clients Tab

- [ ] All columns created per spec
- [ ] Client ID column
- [ ] Client Name column
- [ ] Company column
- [ ] Email column
- [ ] Phone column
- [ ] Address column
- [ ] Status column with dropdown (Active, Inactive, Archived)
- [ ] Notes column

## Invoice Register Tab

- [ ] All columns created per spec
- [ ] Invoice ID
- [ ] Invoice Date
- [ ] Due Date
- [ ] Client ID
- [ ] Client Name (VLOOKUP from Clients)
- [ ] Description
- [ ] Subtotal
- [ ] Tax Rate
- [ ] Tax Amount (formula: Subtotal * Tax Rate)
- [ ] Total (formula: Subtotal + Tax)
- [ ] Amount Paid
- [ ] Outstanding (formula: Total - Amount Paid)
- [ ] Status (formula: Paid/Overdue/Partial/Sent/Draft)

## Payment Tracker Tab

- [ ] All columns created per spec
- [ ] Payment ID
- [ ] Invoice ID
- [ ] Client Name (VLOOKUP from Invoice Register)
- [ ] Payment Date
- [ ] Payment Method dropdown (from Settings)
- [ ] Amount
- [ ] Notes

## Invoice Generator Tab

- [ ] Header section (invoice title, number, date, due date)
- [ ] From section (your name/company, address)
- [ ] Bill To section (client name, company, address)
- [ ] Line items table (#, Description, Quantity, Rate, Amount)
- [ ] Amount formula (=Quantity*Rate) for each line
- [ ] Subtotal formula (=SUM of Amounts)
- [ ] Tax Rate reference (from Settings)
- [ ] Tax Amount formula (=Subtotal*TaxRate)
- [ ] Total formula (=Subtotal+TaxAmount)
- [ ] Payment instructions section

## Settings Tab

- [ ] Currency Symbol setting
- [ ] Default Tax Rate setting
- [ ] Invoice Status Values list
- [ ] Payment Method Values list
- [ ] Client Status Values list
- [ ] Named ranges or cell references for dropdown sources

## Sample Data

- [ ] 10 clients populated
- [ ] 25 invoices with mixed statuses
- [ ] 15 payments distributed
- [ ] Sample data works with all formulas
- [ ] Sample data clearly marked as example (Start Here note)
- [ ] Dashboard metrics match expected values

## Formatting

- [ ] Currency formatting on all monetary values
- [ ] Percentage formatting on tax rate
- [ ] Date formatting on date columns
- [ ] Header row styling on all data tabs
- [ ] Column widths appropriate for content

## QA

- [ ] Run automated formula checks (qa/TEST_CASES_FORMULAS.md)
- [ ] Run Google Sheets import test (qa/TEST_CASES_GOOGLE_SHEETS_IMPORT.md)
- [ ] Run delivery package test (qa/TEST_CASES_DELIVERY_PACKAGE.md)
- [ ] All P0/P1 issues fixed before packaging
