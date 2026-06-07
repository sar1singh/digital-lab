# Product #2 Automated QA Upgrade Plan

## Overview

This document defines the automated QA scripts implemented for Product #2
(Nivora Invoice Generator & Payment Tracker). All scripts are in `build/`.

---

## QA Scripts

| # | Script | Purpose | Status | Checks |
|---|--------|---------|--------|--------|
| 1 | `build/validate_workbook.py` | Structural validation: tabs, columns, formulas, dropdowns, freeze panes, styling, hidden sheets, debug text | Implemented — PASS | 85 |
| 2 | `build/test_workbook_formulas.py` | Independent formula unit tests: compute expected values from raw data, verify correctness | Implemented — PASS | 19 formula groups |
| 3 | `build/lint_google_sheets_compatibility.py` | GS function compatibility lint: scan all 148 formulas, flag disallowed/risky functions | Implemented — PASS | 10 checks |
| 4 | `build/test_workbook_layout.py` | UI/layout checks: brand text, section headings, freeze panes, date/currency formats, debug text scan | Implemented — PASS | 10 sections |
| 5 | `build/run_all_qa.py` | Unified runner: executes all 4 scripts, aggregates pass/fail | Implemented — PASS | 4 suites |

---

## Implementation Order

1. **validate_workbook.py** — created first during initial build phase
2. **test_workbook_formulas.py** — created during QA upgrade phase
3. **lint_google_sheets_compatibility.py** — created during QA upgrade phase
4. **test_workbook_layout.py** — created during QA upgrade phase
5. **run_all_qa.py** — created last to integrate all suites

---

## Script Patterns

All scripts follow the same conventions:
- Load workbook via `openpyxl.load_workbook(path, data_only=False)`
- Use `all_pass` boolean + `check(ok, msg)` function
- Print clear PASS/FAIL per check
- Final output: "ALL CHECKS PASSED" or "SOME CHECKS FAILED"

---

## Automation Coverage by QA Layer

### Layer 1: Automated Workbook Validation (validate_workbook.py)

| Check | Coverage |
|-------|----------|
| Tab count and order | 7 tabs, exact order verified |
| Column headers | Clients (8), Register (13), Payments (7) verified |
| Formula existence | Tax Amount (=G*H), Total (=G+I), Outstanding (=J-K), Status (IF+TODAY) |
| Payment Tracker VLOOKUP | IFERROR+VLOOKUP pattern, correct sheet reference |
| Dashboard Draft exclusion | `<>Draft` present in Total Revenue formula |
| Settings Draft presence | "Draft" in Settings Status Values list |
| No Draft in auto-formula | Status formula does not contain "Draft" |
| Data validations | 2 dropdowns present (Client Status, Payment Method) |
| Freeze panes | 3 data tabs frozen at A2 |
| Tab colors | 7 tabs, exact hex colors verified |
| Formula cell styling | Gray fill (not input green) on key cells |
| File location | In build/, not delivery/ |
| No macros/VBA/external links | Scanned and verified |
| No hidden sheets | All sheets visible |
| No debug text | Scanned all buyer-facing tabs for TODO/FIXME/DEBUG |

### Layer 2: Formula / Business Logic Tests (test_workbook_formulas.py)

| Group | Coverage |
|-------|----------|
| Clients | 10 clients loaded, status counts (8 Active, 1 Inactive, 1 Archived) |
| Invoice Count | 25 invoices |
| Tax Amount | =G*H formula pattern for all 25 rows |
| Total | =G+I formula pattern for all 25 rows |
| Outstanding | =J-K formula pattern for all 25 rows |
| Status Formula | IF+TODAY pattern, correct values: 10 Paid / 7 Overdue / 2 Partial / 6 Sent / 0 Draft |
| Payment Tracker | 15 payments, VLOOKUP formulas, positive amounts, valid Invoice IDs |
| Total Revenue | 54,560.00 (sum of all non-Draft totals) |
| Paid Revenue | 18,700.00 (sum of Paid totals) |
| Outstanding Revenue | 28,520.00 (sum of Outstanding where not fully paid) |
| Invoice Counts | Total=25, Paid=10, Unpaid=15, Overdue=7 |
| Active Clients | 8 |
| Average Invoice Value | 2,182.40 |
| Revenue by Month | Jan=16,610 / Feb=14,190 / Mar=18,040 / Apr=5,720 — sum = Total Revenue |
| Status Breakdown | Paid=10, Sent=6, Partial=2, Overdue=7, Draft=0 |
| Top Clients | James Wilson and Sarah Chen in top 6 |
| Payment Totals | Payment Tracker amounts match Invoice Register |
| Invoice Generator | 3 line items, Subtotal=5,000, Tax Rate=0.10, Tax Amount=500, Total=5,500 |
| Edge Cases | Outstanding=0 → Paid, Overdue triggers, no auto-Draft |

### Layer 3: GS Compatibility Lint (lint_google_sheets_compatibility.py)

| Check | Coverage |
|-------|----------|
| Formula count | 148 formulas across all sheets |
| Disallowed functions | 0 Excel-only functions, 0 risky GS functions |
| External references | 0 external workbook links |
| Structured table refs | 0 `[@column]` references |
| Dynamic array operators | 0 spill/reference errors |
| Local file paths | 0 path references |
| VBA/macro refs | 0 VBA or macro references |
| Allowed functions | COUNTIF, COUNTIFS, DATE, IF, IFERROR, SUM, SUMIFS, TODAY, VLOOKUP — all allowed |
| Sheet name quoting | All multi-word names quoted correctly |
| Formula distribution | 0 in Start Here/Clients/Settings, 24 in Dashboard, 100 in Register, 15 in Payments, 9 in Generator |

### Layer 4: UI/Layout Tests (test_workbook_layout.py)

| Check | Coverage |
|-------|----------|
| Start Here | Brand name, all tab names, Quick Start, formula warning, backup note, GS mention, Draft mention, no debug text |
| Dashboard | All 9 KPI labels, 3 section headings (Revenue by Month, Status Breakdown, Top Clients) |
| Clients | 8 column headers, freeze panes |
| Register | 13 column headers, freeze panes |
| Payments | 7 column headers, freeze panes |
| Invoice Generator | INVOICE title, From, Bill To, Line Items, Summary, Payment sections, all field labels |
| Settings | All 5 configuration sections, Draft listed |
| Freeze panes | 3 frozen, 4 unfrozen (correct) |
| Number formats | DD-MMM-YYYY on dates, #,##0.00 on money |
| Header styling | Bold headers on 3 data tabs |

---

## Future Automation Ideas

These are not implemented but could be added for higher coverage:

- **PDF generation QA** — verify PDF guide renders correctly (fpdf2 validation)
- **ZIP integrity test** — programmatically verify delivery ZIP contents
- **Brand consistency scan** — automatically grep for old brand names in all delivery files
- **Marketplace preview test** — screenshot comparison against spec (non-trivial)

---

## Runner Command

```
py build/run_all_qa.py
```

Expected output: "ALL QA SUITES PASSED" (all 4 scripts pass).
