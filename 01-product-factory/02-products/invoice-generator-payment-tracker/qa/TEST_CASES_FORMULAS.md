# Test Cases: Formulas — Invoice Generator & Payment Tracker

## Invoice Register

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| F-001 | Tax Amount = Subtotal * Tax Rate | Correct for all 25 invoices | P0 |
| F-002 | Total = Subtotal + Tax Amount | Correct for all 25 invoices | P0 |
| F-003 | Outstanding = Total - Amount Paid | Correct for all 25 invoices | P0 |
| F-004 | Status = "Paid" when Outstanding = 0 | INV-001 through INV-005, INV-007-009 | P0 |
| F-005 | Status = "Overdue" when Outstanding > 0 and Due Date < TODAY | INV-010, INV-014, INV-019 | P0 |
| F-006 | Status = "Partial" when Amount Paid > 0 and Outstanding > 0 | INV-006 | P0 |
| F-007 | Status = "Sent" when Amount Paid = 0 and Due Date > TODAY | INV-011-013, INV-015-017, INV-020, INV-022-025 | P0 |
| F-008 | Status = "Draft" | INV-018, INV-021 | P1 |

## Dashboard

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| F-009 | Total Revenue = SUM of all non-Draft invoice totals | Matches manual calculation | P0 |
| F-010 | Paid Revenue = SUM of Paid invoice totals | Matches manual calculation | P0 |
| F-011 | Outstanding Revenue = SUM of Outstanding where not fully paid | Matches manual calculation | P0 |
| F-012 | Total Invoices count | 25 | P0 |
| F-013 | Paid Invoices count | 9 | P1 |
| F-014 | Unpaid Invoices count | 14 | P1 |
| F-015 | Overdue Invoices count | 3 | P1 |
| F-016 | Active Clients count | 9 (1 inactive, 1 archived) | P1 |
| F-017 | Average Invoice Value = Total Revenue / Non-Draft count | IFERROR — not #DIV/0! | P1 |

## Payment Tracker

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| F-018 | Client Name resolves from Invoice ID via VLOOKUP | Correct for all 15 payments | P1 |
| F-019 | Payment amounts are positive numbers | All > 0 | P1 |

## Invoice Generator

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| F-020 | Line Amount = Quantity * Rate | Correct | P0 |
| F-021 | Subtotal = SUM of line amounts | Correct | P0 |
| F-022 | Tax Amount = Subtotal * Tax Rate | Correct | P0 |
| F-023 | Total = Subtotal + Tax Amount | Correct | P0 |
| F-024 | IFERROR wrappers prevent #DIV/0! on empty invoice | Shows 0 or blank | P1 |

## Edge Cases

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| F-025 | Zero-subtotal invoice doesn't break formulas | Displays correctly | P1 |
| F-026 | Tax Rate = 0% produces correct Total = Subtotal | Correct | P1 |
| F-027 | Overdue status triggers when TODAY > Due Date | Correct | P0 |
| F-028 | Partial payment followed by full payment updates status to Paid | Correct | P1 |
