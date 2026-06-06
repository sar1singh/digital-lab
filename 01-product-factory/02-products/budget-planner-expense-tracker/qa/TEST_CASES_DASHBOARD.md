# Test Cases — Dashboard — Budget Planner & Expense Tracker

## TC-DB-01: Summary Cards Show Non-Empty Values

| Field | Value |
|-------|-------|
| Test ID | TC-DB-01 |
| Priority | P0 |
| Area | Dashboard |
| Steps | 1. Go to Dashboard tab. 2. Observe cells B3 through B11 (the summary cards). |
| Expected result | All summary cards display calculated values (not empty, not error). With sample data: Total Income ≈ $5,500, Total Expenses ≈ $1,265 (approximate). |

## TC-DB-02: Total Income Changes When Income Changes

| Field | Value |
|-------|-------|
| Test ID | TC-DB-02 |
| Priority | P0 |
| Area | Dashboard |
| Steps | 1. Note Dashboard Total Income. 2. Go to Monthly Budget and change Salary Planned from 4500 to 5000. 3. Return to Dashboard. |
| Expected result | Dashboard Total Income reflects the change. Note: This test checks if the formula references Monthly Budget correctly. Revert Salary to 4500 after test. |

## TC-DB-03: Expense Chart Updates When Expense Data Changes

| Field | Value |
|-------|-------|
| Test ID | TC-DB-03 |
| Priority | P1 |
| Area | Dashboard |
| Steps | 1. Note the pie chart layout. 2. Add a new expense of $500 in a category that was small (e.g., Health). 3. Observe the chart. |
| Expected result | The pie chart slice for Health increases visibly. Remove the test expense after confirming. |

## TC-DB-04: Category Summary Updates

| Field | Value |
|-------|-------|
| Test ID | TC-DB-04 |
| Priority | P1 |
| Area | Dashboard |
| Steps | 1. Note a category total in the Dashboard category breakdown (rows 15+). 2. Add a $100 expense to that category in Expense Tracker. 3. Return to Dashboard. |
| Expected result | The category total in Dashboard increases by $100. Remove the test expense after test. |

## TC-DB-05: Bills Due Count Changes When Paid Status Changes

| Field | Value |
|-------|-------|
| Test ID | TC-DB-05 |
| Priority | P0 |
| Area | Dashboard |
| Steps | 1. Note Bills Due value (B8). 2. Go to Bills Tracker. 3. Change a bill from "Unpaid" to "Paid". 4. Return to Dashboard. |
| Expected result | Bills Due count decreases by 1. Revert to "Unpaid" after test. |

## TC-DB-06: Debt Remaining Changes When Current Balance Changes

| Field | Value |
|-------|-------|
| Test ID | TC-DB-06 |
| Priority | P0 |
| Area | Dashboard |
| Steps | 1. Note Debt Remaining value (B9). 2. Go to Debt Tracker. 3. Reduce Credit Card A Current Balance by $100 (from 2100 to 2000). 4. Return to Dashboard. |
| Expected result | Debt Remaining decreases by $100. Revert to 2100 after test. |

## TC-DB-07: Savings Goal Progress Changes When Current Amount Changes

| Field | Value |
|-------|-------|
| Test ID | TC-DB-07 |
| Priority | P0 |
| Area | Dashboard |
| Steps | 1. Note Avg Savings Progress (B10). 2. Go to Savings Tracker. 3. Increase Emergency Fund Current Amount by $500 (from 4500 to 5000). 4. Return to Dashboard. |
| Expected result | Avg Savings Progress increases. Revert to 4500 after test. |

## TC-DB-08: Dashboard Remains Readable With Sample Data Removed

| Field | Value |
|-------|-------|
| Test ID | TC-DB-08 |
| Priority | P1 |
| Area | Dashboard |
| Steps | 1. Temporarily delete all sample data from Expense Tracker. 2. Go to Dashboard. 3. Observe values. 4. Undo the deletion. |
| Expected result | Dashboard does not show errors. Values may show 0 or empty, but no #DIV/0!, #REF!, #VALUE!, or #N/A errors. |

## TC-DB-09: No Formula Error Values

| Field | Value |
|-------|-------|
| Test ID | TC-DB-09 |
| Priority | P0 |
| Area | Dashboard |
| Steps | 1. Scan every cell in the Dashboard tab. 2. Look for #DIV/0!, #REF!, #VALUE!, #N/A, #NAME?, #NUM!, or #NULL!. |
| Expected result | No error values visible anywhere on Dashboard. |

## TC-DB-10: Charts Render Correctly

| Field | Value |
|-------|-------|
| Test ID | TC-DB-10 |
| Priority | P1 |
| Area | Dashboard |
| Steps | 1. Observe all chart objects on the Dashboard. 2. Verify they display data and labels. |
| Expected result | Charts render with visible data slices/bars and category labels. Charts reflect current data in the spreadsheet. |
