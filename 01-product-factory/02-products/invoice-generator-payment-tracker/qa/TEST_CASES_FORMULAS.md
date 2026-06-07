# Test Cases: Formulas — Invoice Generator & Payment Tracker

**QA Layer:** 2 (Formula / Business Logic Tests)
**Coverage standard:** `01-product-factory/07-systems/QA_COVERAGE_STANDARD.md`

**All 19 formula groups now verified by automated tests in `build/test_workbook_formulas.py`.**
**Run via:** `py build/run_all_qa.py` (includes this + 3 other QA suites)

Status: All formula tests pass automatically. This file documents the test cases
for reference; no manual formula testing needed.

### Coverage Map

| Group | Test IDs | Automated | Status |
|-------|----------|-----------|--------|
| Invoice Register formulas | F-001 to F-008 | `test_workbook_formulas.py` | PASS |
| Dashboard KPIs | F-009 to F-017 | `test_workbook_formulas.py` | PASS |
| Payment Tracker | F-018 to F-019 | `test_workbook_formulas.py` | PASS |
| Invoice Generator | F-020 to F-024 | `test_workbook_formulas.py` | PASS |
| Edge Cases | F-025 to F-028 | `test_workbook_formulas.py` | PASS |

## Invoice Register

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| F-001 | Tax Amount = Subtotal * Tax Rate | Correct for all 25 invoices | P0 |
| F-002 | Total = Subtotal + Tax Amount | Correct for all 25 invoices | P0 |
| F-003 | Outstanding = Total - Amount Paid | Correct for all 25 invoices | P0 |
| F-004 | Status = "Paid" when Outstanding = 0 | INV-001-005, INV-007-009, INV-015-016 (10 invoices) | P0 |
| F-005 | Status = "Overdue" when Outstanding > 0 and Due Date < TODAY | INV-006, INV-010-014, INV-019 (7) | P0 |
| F-006 | Status = "Partial" when Amount Paid > 0, Outstanding > 0, Due Date >= TODAY | INV-020, INV-023 (2) | P0 |
| F-007 | Status = "Sent" when Amount Paid = 0 and Due Date >= TODAY | INV-017-018, INV-021-022, INV-024-025 (6) | P0 |
| F-008 | Status = "Draft" is manual-only (auto-formula never produces it) | No auto-Draft invoices (verified) | P1 |

## Dashboard

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| F-009 | Total Revenue = SUM of all non-Draft invoice totals | Matches manual calculation | P0 |
| F-010 | Paid Revenue = SUM of Paid invoice totals | Matches manual calculation | P0 |
| F-011 | Outstanding Revenue = SUM of Outstanding where not fully paid | Matches manual calculation | P0 |
| F-012 | Total Invoices count | 25 | P0 |
| F-013 | Paid Invoices count | 10 | P1 |
| F-014 | Unpaid Invoices count | 15 | P1 |
| F-015 | Overdue Invoices count | 7 | P1 |
| F-016 | Active Clients count | 9 (1 inactive, 1 archived) | P1 |
| F-017 | Average Invoice Value = Total Revenue / Non-Draft count | IFERROR — not #DIV/0! | P1 |

## Payment Tracker

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| F-018 | Client Name resolves from Invoice ID via VLOOKUP (IFERROR wrapped) | Correct for all 15 payments | P0 |
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
