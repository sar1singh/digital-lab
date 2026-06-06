# Test Cases — Spreadsheet UI — Budget Planner & Expense Tracker

## TC-UI-01: Workbook Opens Without Errors

| Field | Value |
|-------|-------|
| Test ID | TC-UI-01 |
| Priority | P0 |
| Area | General |
| Steps | 1. Double-click the XLSX file. 2. If Excel Protected View appears, click Enable Editing. 3. Observe any warning dialogs. |
| Expected result | File opens without error messages. No "We found a problem with some content" dialog. |


## TC-UI-02: All 7 Tabs Exist

| Field | Value |
|-------|-------|
| Test ID | TC-UI-02 |
| Priority | P0 |
| Area | General |
| Steps | 1. Look at the sheet tabs at the bottom of the workbook. 2. Count the tabs. 3. Note the names. |
| Expected result | Exactly 7 tabs present: Start Here, Monthly Budget, Expense Tracker, Bills Tracker, Debt Tracker, Savings Tracker, Dashboard. |


## TC-UI-03: Tab Order Is Correct

| Field | Value |
|-------|-------|
| Test ID | TC-UI-03 |
| Priority | P1 |
| Area | General |
| Steps | 1. Observe the left-to-right order of sheet tabs. |
| Expected result | Tab order: Start Here → Monthly Budget → Expense Tracker → Bills Tracker → Debt Tracker → Savings Tracker → Dashboard. |


## TC-UI-04: Headers Readable

| Field | Value |
|-------|-------|
| Test ID | TC-UI-04 |
| Priority | P1 |
| Area | General |
| Steps | 1. Click each tab. 2. Verify column headers are bold and readable. 3. Check that header text is not truncated. |
| Expected result | All column headers are bold, fully visible, and use a clear dark font on a distinct background. |


## TC-UI-05: Column Widths Acceptable

| Field | Value |
|-------|-------|
| Test ID | TC-UI-05 |
| Priority | P2 |
| Area | General |
| Steps | 1. Inspect each tab. 2. Verify text is not clipped. 3. Verify no excessively wide or narrow columns. |
| Expected result | Column widths fit content. Long text (descriptions) is fully visible. No columns so wide that scrolling is excessive. |


## TC-UI-06: Sample Data Visible

| Field | Value |
|-------|-------|
| Test ID | TC-UI-06 |
| Priority | P1 |
| Area | General |
| Steps | 1. Check Expense Tracker for sample rows. 2. Check Bills Tracker for sample rows. 3. Check Debt Tracker for sample rows. 4. Check Savings Tracker for sample rows. |
| Expected result | Each tracker tab has at least 3-5 rows of realistic sample data. Monthly Budget has planned amounts filled in. |


## TC-UI-07: Input Cells vs Formula Cells Distinguishable

| Field | Value |
|-------|-------|
| Test ID | TC-UI-07 |
| Priority | P1 |
| Area | General |
| Steps | 1. Look at Monthly Budget. 2. Note which cells have green (input) vs gray (formula) background. 3. Check Expense Tracker Month column. 4. Check Dashboard summary cells. |
| Expected result | Input cells (user-editable) have green or white background. Formula cells (auto-calculated) have gray background. |


## TC-UI-08: Currency Formatting Visible

| Field | Value |
|-------|-------|
| Test ID | TC-UI-08 |
| Priority | P1 |
| Area | Formatting |
| Steps | 1. Go to Monthly Budget Planned Amount. 2. Go to Expense Tracker Amount column. 3. Check Dashboard Total Income. |
| Expected result | All monetary values display with currency symbol ($) and two decimal places or whole-number format. |


## TC-UI-09: Percentage Formatting Visible

| Field | Value |
|-------|-------|
| Test ID | TC-UI-09 |
| Priority | P1 |
| Area | Formatting |
| Steps | 1. Check Debt Tracker Payoff Progress %. 2. Check Savings Tracker Progress %. 3. Check Dashboard Savings Rate %. |
| Expected result | Percentage values display with % symbol (e.g., 45% or 45.0%). |


## TC-UI-10: Frozen Headers

| Field | Value |
|-------|-------|
| Test ID | TC-UI-10 |
| Priority | P2 |
| Area | Usability |
| Steps | 1. Go to Monthly Budget. 2. Scroll down. 3. Observe whether row 1 stays visible. 4. Repeat for Expense Tracker, Bills Tracker, Debt Tracker, Savings Tracker. |
| Expected result | Header row remains visible when scrolling down on Monthly Budget, Expense Tracker, Bills Tracker, Debt Tracker, and Savings Tracker. |


## TC-UI-11: No Hidden Broken Sheets

| Field | Value |
|-------|-------|
| Test ID | TC-UI-11 |
| Priority | P0 |
| Area | General |
| Steps | 1. Right-click any sheet tab. 2. Select Unhide. 3. Verify no hidden sheets exist. |
| Expected result | No hidden sheets. All 7 tabs are visible. |


## TC-UI-12: No Obvious Spelling Issues

| Field | Value |
|-------|-------|
| Test ID | TC-UI-12 |
| Priority | P2 |
| Area | General |
| Steps | 1. Read through Start Here instructions. 2. Scan headers and labels on each tab. 3. Note any typos. |
| Expected result | No typos, misspellings, or grammatical errors. |


## TC-UI-13: Start Here Instructions Are Clear

| Field | Value |
|-------|-------|
| Test ID | TC-UI-13 |
| Priority | P1 |
| Area | Start Here |
| Steps | 1. Read the entire Start Here tab. 2. Verify it covers: how to set up budget, how to enter income, how to enter expenses, how to use Dashboard, and the formula cell warning. |
| Expected result | All 5 instructional sections are present and understandable to a non-technical user. |


## TC-UI-14: Dashboard Has Charts

| Field | Value |
|-------|-------|
| Test ID | TC-UI-14 |
| Priority | P1 |
| Area | Dashboard |
| Steps | 1. Go to Dashboard tab. 2. Look for chart objects. |
| Expected result | At least one chart is visible (pie chart for expense categories or bar chart for income vs expenses). |
