# QA Checklist — Nivora Project Budget Tracker

**Status:** Planning phase — not yet built.

**Reference:** Product Factory 10-layer QA standard (`01-product-factory/07-systems/QA_COVERAGE_STANDARD.md`).

---

## Coverage Map

| Layer | Area | Coverage | Status |
|-------|------|----------|--------|
| 1 | Automated workbook validation | `build/validate_workbook.py` | NOT STARTED |
| 2 | Formula/business logic tests | `build/test_workbook_formulas.py` | NOT STARTED |
| 3 | GS compatibility lint | `build/lint_google_sheets_compatibility.py` | NOT STARTED |
| 4 | UI/layout tests | `build/test_workbook_layout.py` | NOT STARTED |
| 5 | Manual smoke QA | 9-step GS runbook | NOT STARTED |
| 6 | Delivery package QA | `qa/TEST_CASES_DELIVERY_PACKAGE.md` | NOT STARTED |
| 7 | Marketplace asset QA | `qa/TEST_CASES_SCREENSHOTS.md` (79 tests) | NOT STARTED |
| 8 | Listing copy QA | `LISTING_COPY_GUMROAD.md`, `LISTING_COPY_PAYHIP.md` | NOT STARTED |
| 9 | Link/copy-link QA | `build/google-sheets-copy-link-template.txt` | NOT STARTED |
| 10 | Pre-publish gate | `PRE_PUBLISH_REVIEW_CHECKLIST.md` | NOT STARTED |

---

## Formula QA

- [ ] Total Budget = SUM of project budgets
- [ ] Total Spent = SUMIFS from Expenses (finite range)
- [ ] Total Remaining = Total Budget - Total Spent
- [ ] % Budget Used = Total Spent / Total Budget (IFERROR-wrapped)
- [ ] Total Income = SUMIFS from Income (finite range, excluding Pending)
- [ ] Net Profit = Total Income - Total Spent
- [ ] Projects on/over budget = COUNTIFS with non-empty criterion (rule 23)
- [ ] Projects Total Spent = SUMIFS from Expenses (finite range)
- [ ] Projects Remaining = Budget - Spent
- [ ] Projects % Used = Total Spent / Budget (IFERROR)
- [ ] Projects Status formula covers all conditions

## Data Validation QA

- [ ] Expenses: Project dropdown (inline list)
- [ ] Expenses: Category dropdown (inline list)
- [ ] Income: Project dropdown (inline list)
- [ ] Income: Payment Status dropdown ("Paid,Pending,Expected")
- [ ] All validations use inline comma-separated lists (rule 24)
- [ ] No range-based validations without GS source verification

## UI QA

- [ ] All tab names correct and readable
- [ ] Brand name (Nivora) appears on Start Here and Dashboard
- [ ] All formula cells have gray background
- [ ] All input cells have white/green background
- [ ] Dashboard gridlines removed
- [ ] Freeze panes set correctly
- [ ] Currency formatting on all money columns
- [ ] Date formatting on date columns
- [ ] Percentage formatting on % Used
- [ ] Header rows formatted distinctively
