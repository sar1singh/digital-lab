# Automated QA Plan Template

> Copy into product workspace as `docs/AUTOMATED_QA_PLAN.md` (or integrate into build plan).
> Replace `[Product Name]` with actual product name.

---

## Product: [Product Name]

### QA Scripts

| # | Script | Purpose | Status |
|---|--------|---------|--------|
| 1 | `build/validate_workbook.py` | Structural validation: tabs, columns, formulas, dropdowns, freeze panes, styling, no debug text | [ ] Planned / [ ] Built / [ ] Passing |
| 2 | `build/test_workbook_formulas.py` | Independent formula unit tests: calculate expected values from raw data | [ ] Planned / [ ] Built / [ ] Passing |
| 3 | `build/lint_google_sheets_compatibility.py` | GS function compatibility: scan all formulas, flag disallowed/risky functions | [ ] Planned / [ ] Built / [ ] Passing |
| 4 | `build/test_workbook_layout.py` | UI/layout checks: brand text, section headings, freeze panes, formats, debug text | [ ] Planned / [ ] Built / [ ] Passing |
| 5 | `build/run_all_qa.py` | Unified runner: executes all scripts, aggregates pass/fail | [ ] Planned / [ ] Built / [ ] Passing |

### Implementation Order

1. `validate_workbook.py` — always first (catches structural issues early)
2. `test_workbook_formulas.py` — second (catches formula bugs)
3. `lint_google_sheets_compatibility.py` — third (compatibility issues)
4. `test_workbook_layout.py` — fourth (UI issues)
5. `run_all_qa.py` — last (integrates all above)

### Data Requirements

- Sample data must be populated before formula tests will pass
- Workbook must be buildable from `build/build_workbook.py`
- All scripts load the workbook from `build/{brand}-{product-slug}.xlsx`

### Script Patterns

Each script follows this pattern:
- Load workbook with `openpyxl.load_workbook(path, data_only=False)`
- Use a global `all_pass` boolean and a `check(ok, msg)` function
- Print clear PASS/FAIL for each check
- Final output: "ALL CHECKS PASSED" or "SOME CHECKS FAILED"

### File Location

All scripts in `build/` directory alongside `build_workbook.py`.

### Runner Command

```
py build/run_all_qa.py
```
