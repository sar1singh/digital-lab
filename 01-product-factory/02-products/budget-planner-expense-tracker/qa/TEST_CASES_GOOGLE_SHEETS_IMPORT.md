# Test Cases — Google Sheets Import — Budget Planner & Expense Tracker

## TC-GS-01: Upload XLSX to Google Drive

| Field | Value |
|-------|-------|
| Test ID | TC-GS-01 |
| Priority | P0 |
| Area | Import |
| Steps | 1. Go to drive.google.com. 2. Click + New → File upload. 3. Select the XLSX file. 4. Wait for upload. |
| Expected result | File appears in Google Drive with correct file name. |

## TC-GS-02: Open with Google Sheets

| Field | Value |
|-------|-------|
| Test ID | TC-GS-02 |
| Priority | P0 |
| Area | Import |
| Steps | 1. Right-click the uploaded file. 2. Select Open with → Google Sheets. |
| Expected result | File opens in Google Sheets in a new browser tab. No conversion errors. |

## TC-GS-03: All 7 Tabs Preserved

| Field | Value |
|-------|-------|
| Test ID | TC-GS-03 |
| Priority | P0 |
| Area | Import |
| Steps | 1. Look at sheet tabs at the bottom of the Google Sheets window. 2. Count and note the names. |
| Expected result | All 7 tabs present: Start Here, Monthly Budget, Expense Tracker, Bills Tracker, Debt Tracker, Savings Tracker, Dashboard. |

## TC-GS-04: Formulas Preserved

| Field | Value |
|-------|-------|
| Test ID | TC-GS-04 |
| Priority | P0 |
| Area | Import |
| Steps | 1. Click a cell that had a formula in Excel (e.g., Monthly Budget Actual column). 2. Look at the formula bar. 3. Check Dashboard Total Income cell. |
| Expected result | Formulas are present and calculating. SUMIF, IFERROR, TEXT, SUM, COUNTIF, AVERAGE all converted correctly. No #REF! errors from sheet name changes. |

## TC-GS-05: Dropdowns Preserved

| Field | Value |
|-------|-------|
| Test ID | TC-GS-05 |
| Priority | P0 |
| Area | Import |
| Steps | 1. Click an empty cell in Expense Tracker Category column. 2. Look for the dropdown arrow. 3. Try selecting a value. 4. Repeat for Payment Method and Planned/Unplanned. |
| Expected result | All three dropdowns present and functional. |

## TC-GS-06: Conditional Formatting Preserved

| Field | Value |
|-------|-------|
| Test ID | TC-GS-06 |
| Priority | P1 |
| Area | Import |
| Steps | 1. Go to Monthly Budget. 2. Check if Difference column has red/green conditional formatting. 3. Check Bills Tracker for unpaid row highlighting. |
| Expected result | Conditional formatting is present and functional. Negative values in Difference column show red fill. Unpaid bills show red fill. |

## TC-GS-07: Charts Survive Conversion (or Document Recreation Need)

| Field | Value |
|-------|-------|
| Test ID | TC-GS-07 |
| Priority | P1 |
| Area | Import |
| Steps | 1. Go to Dashboard tab. 2. Check if charts are visible. 3. If not, note that they need to be recreated. |
| Expected result | Charts either display correctly, or it is documented that they need recreation in Google Sheets. |

## TC-GS-08: Column Widths Acceptable

| Field | Value |
|-------|-------|
| Test ID | TC-GS-08 |
| Priority | P2 |
| Area | Import |
| Steps | 1. Inspect each tab. 2. Verify text is not clipped. 3. Adjust any columns that are too narrow. |
| Expected result | Column widths are acceptable. No critical data is truncated. |

## TC-GS-09: Create /copy Link

| Field | Value |
|-------|-------|
| Test ID | TC-GS-09 |
| Priority | P0 |
| Area | Publishing |
| Steps | 1. Click Share in Google Sheets. 2. Set Anyone with the link → Viewer. 3. Copy the sharing URL. 4. Replace /edit with /copy. |
| Expected result | A working /copy link is created. |

## TC-GS-10: Test /copy Link in Incognito

| Field | Value |
|-------|-------|
| Test ID | TC-GS-10 |
| Priority | P1 |
| Area | Publishing |
| Steps | 1. Open an incognito/private browser window. 2. Paste the /copy link. 3. Observe the page. |
| Expected result | Page shows "Copy this spreadsheet to your Google Drive" with Make a copy button. |

## TC-GS-11: Copied Sheet Is Independent

| Field | Value |
|-------|-------|
| Test ID | TC-GS-11 |
| Priority | P0 |
| Area | Publishing |
| Steps | 1. Click Make a copy in incognito. 2. Sign in to a test Google account if prompted. 3. Wait for copy to open. |
| Expected result | A new, independent copy opens. All tabs, formulas, and sample data are intact. The copy is not linked to the original. |

## TC-GS-12: Buyer Can Edit Their Copy

| Field | Value |
|-------|-------|
| Test ID | TC-GS-12 |
| Priority | P0 |
| Area | Publishing |
| Steps | 1. In the copied sheet, change a Planned Amount in Monthly Budget. 2. Enter a test expense in Expense Tracker. |
| Expected result | User can edit input cells. Formulas recalculate. Dashboard updates. The buyer has full edit access to their own copy. |
