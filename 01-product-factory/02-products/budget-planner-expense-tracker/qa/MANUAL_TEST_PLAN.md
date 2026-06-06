# Manual Test Plan — Budget Planner & Expense Tracker

## QA Objective

Verify that the Budget Planner & Expense Tracker spreadsheet is functionally correct, visually clean, and ready for publishing on Gumroad and Payhip. All critical paths (formulas, dropdowns, cross-sheet references, Dashboard, and Google Sheets import) must pass before listing goes live.

## Test Environment

| Environment | Version / Config |
|-------------|------------------|
| Excel Desktop | Microsoft Excel 2019 / 365 or later |
| LibreOffice Calc | Latest stable (fallback) |
| Google Sheets | Via Google Drive (latest web version) |
| Browser | Chrome or Firefox (latest) for /copy link testing |

## Test Scope

- Spreadsheet UI and formatting
- All formulas across all 7 tabs
- Data validation dropdowns
- Cross-sheet formula references
- Google Sheets import fidelity
- Dashboard aggregation and charts
- Edge cases (empty state, zeros, blank rows)

## Out of Scope

- Performance testing with large datasets (10k+ rows)
- Mobile rendering in Google Sheets app
- Accessibility compliance
- Localization/internationalization
- Macro or VBA functionality
- Third-party tool integration

## Pass / Fail Rules

- **Pass:** Actual result matches expected result exactly.
- **Fail:** Actual result deviates from expected.
- **Blocked:** Cannot test due to environment or dependency issue.

## Severity Definitions

| Severity | Label | Description | Publishing Gate |
|----------|-------|-------------|-----------------|
| P0 | Critical | Blocks core functionality (broken formulas, missing tabs, wrong totals) | Must pass before publish |
| P1 | High | Significant usability issue (dropdowns broken, formatting unreadable, charts missing) | Must pass before publish |
| P2 | Medium | Minor issue that does not block purchase (cosmetic gridlines, minor alignment) | Can ship, document in release notes |
| P3 | Low | Cosmetic or nice-to-have (font choice, color preference) | Can defer to next version |

## Publishing Gate

**Product cannot be published until:**
- All P0 test cases pass
- All P1 test cases pass
- P2 items documented in release notes
- P3 items deferred or fixed at discretion

## Test Execution

1. Open `budget-planner-expense-tracker-v1.xlsx` in Excel or LibreOffice
2. Run all test cases in `TEST_CASES_SPREADSHEET_UI.md`
3. Run all test cases in `TEST_CASES_FORMULAS.md`
4. Run all test cases in `TEST_CASES_DROPDOWNS.md`
5. Run all test cases in `TEST_CASES_DASHBOARD.md`
6. Upload to Google Sheets and run `TEST_CASES_GOOGLE_SHEETS_IMPORT.md`
7. Log any bugs using `BUG_REPORT_TEMPLATE.md`
8. Sign off using `QA_SIGNOFF_CHECKLIST.md`

## Artifact Under Test

`artifacts/budget-planner-expense-tracker-v1.xlsx`
