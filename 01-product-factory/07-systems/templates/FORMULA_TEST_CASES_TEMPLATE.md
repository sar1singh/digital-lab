# Formula Test Cases Template

> Copy into product workspace as `qa/TEST_CASES_FORMULAS.md`.
> Define all formula-driven calculations the workbook performs.

---

## Product: [Product Name]

**Automated test script:** `build/test_workbook_formulas.py`
**Run via:** `py build/run_all_qa.py`

---

## [Tab Name 1] Formulas

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| F-001 | [Formula description] | [Expected result] | P0 |

## [Tab Name 2] Formulas

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| F-002 | [Formula description] | [Expected result] | P0 |

## Dashboard KPIs

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| F-003 | [KPI description] | [Expected value] | P0 |

## Edge Cases

| ID | Test | Expected | P0/P1 |
|----|------|----------|-------|
| F-004 | [Edge case description] | [Expected behavior] | P1 |

---

## Test Categories

- **P0 (Critical):** Must pass before any QA can proceed. Formula bugs that produce wrong numbers.
- **P1 (Important):** Should pass before delivery. Edge cases, formatting edge conditions.
- **P2 (Nice to have):** May pass after delivery if time-constrained. Very unlikely edge cases.

---

## Automated Test Coverage

The following formula groups must be covered by `build/test_workbook_formulas.py`:

- [ ] Core calculation formulas (tax, total, outstanding, status)
- [ ] Cross-sheet references (VLOOKUP, SUMIFS, COUNTIFS)
- [ ] Dashboard KPI values (revenue, counts, averages)
- [ ] Summary tables (revenue by month, status breakdown, top items)
- [ ] Calculator/generator formulas (line items, subtotal, tax, total)
- [ ] IFERROR wrappers and edge cases
