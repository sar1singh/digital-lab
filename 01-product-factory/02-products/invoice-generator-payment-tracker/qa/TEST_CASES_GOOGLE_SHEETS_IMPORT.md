# Test Cases: Google Sheets Import — Invoice Generator & Payment Tracker

## Import

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| GS-001 | XLSX uploads to Google Drive without errors | No conversion errors | P0 |
| GS-002 | All 7 tabs present and named correctly | Start Here, Dashboard, Clients, Invoice Register, Payment Tracker, Invoice Generator, Settings | P0 |
| GS-003 | All formulas survive conversion | No #REF!, #VALUE!, #DIV/0! errors anywhere | P0 |

## Formulas in Google Sheets

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| GS-004 | Tax Amount formula works in GS | Correct for all invoices | P0 |
| GS-005 | Total formula works in GS | Correct for all invoices | P0 |
| GS-006 | Outstanding formula works in GS | Correct for all invoices | P0 |
| GS-007 | Status formula works in GS | All 5 states display correctly | P0 |
| GS-008 | Dashboard SUMIFS formulas work in GS | All dashboard metrics correct | P0 |
| GS-009 | COUNTIFS formulas work in GS | All counts correct | P0 |
| GS-010 | VLOOKUP for Client Name works in GS | Correct resolution | P1 |
| GS-011 | Invoice Generator Amount formula works in GS | Correct | P0 |

## Data Validation

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| GS-012 | Client Status dropdown works in GS | Active, Inactive, Archived options | P1 |
| GS-013 | Payment Method dropdown works in GS | All methods from Settings | P1 |
| GS-014 | Named ranges for dropdown sources survive GS import | Dropdowns reference correct ranges | P1 |

## Conditional Formatting

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| GS-015 | Formula cell gray background survives GS import | All formula cells gray | P1 |
| GS-016 | Input cell styling survives GS import | Input cells distinguishable | P1 |

## Navigation

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| GS-017 | Start Here navigation guide works as plain text | Users can navigate without hyperlinks | P1 |
| GS-018 | Dashboard sheet navigation is intuitive | All tabs accessible from bottom bar | P1 |

## Print / Output

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| GS-019 | Invoice Generator tab prints correctly from GS | No cutoff content, readable | P1 |
| GS-020 | Copy link works from incognito browser | Opens copy dialog | P0 |
