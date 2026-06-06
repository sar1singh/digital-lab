# Google Sheets Upload Guide — Budget Planner & Expense Tracker

## Step 1: Upload XLSX to Google Drive

1. Go to drive.google.com
2. Click **+ New** → **File upload**
3. Select `budget-planner-expense-tracker-v1.xlsx`
4. Wait for upload to complete

## Step 2: Open with Google Sheets

1. Locate the file in Google Drive
2. Right-click → **Open with** → **Google Sheets**
3. The file opens as a Google Sheet in a new tab

## Step 3: Convert to Google Sheets Format

1. In the Google Sheet, click **File** → **Save as Google Sheets**
2. A new Google Sheets-native version is created
3. The original XLSX remains in Drive as a backup

## Step 4: Review Converted Workbook

Check each tab for conversion issues:

| Tab | What to Check |
|-----|---------------|
| Start Here | Text formatting preserved |
| Monthly Budget | SUMIF formulas converted correctly |
| Expense Tracker | Dropdown data validation preserved |
| Bills Tracker | Dropdown data validation preserved |
| Debt Tracker | Payoff progress formulas work |
| Savings Tracker | Progress % formulas work |
| Dashboard | Summary formulas work, charts recreated |

### Common Conversion Issues

- **Column widths** may need manual adjustment after conversion
- **Charts** may not survive XLSX → Google Sheets conversion. If so, recreate them:
  - Select the source data
  - Click **Insert** → **Chart**
  - Choose the same chart type (Pie or Bar)
- **Conditional formatting** rules should convert but verify the ranges

## Step 5: Set Sharing Permissions

1. Click **Share** in the top-right corner
2. Under **General access**, select **Anyone with the link**
3. Role: **Viewer** (not Editor — you want buyers to make copies, not edit your original)
4. Click **Done**

## Step 6: Create Buyer Copy Link

The standard Google Sheets sharing link looks like:
```
https://docs.google.com/spreadsheets/d/ABC123/edit?usp=sharing
```

For buyers, use the **/copy** link so they are prompted to make their own copy:
```
https://docs.google.com/spreadsheets/d/ABC123/copy
```

To create this:
1. Copy the sheet URL
2. Replace `/edit?usp=sharing` with `/copy`
3. Test the link in an incognito/private browser window

## Step 7: Test Copy Link

1. Open an incognito/private browser window
2. Paste the /copy link
3. You should see: "Copy this spreadsheet to your Google Drive"
4. Click **Make a copy**
5. Confirm the copied workbook opens with all tabs, formulas, and data intact

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Charts not showing | Delete and recreate via Insert → Chart |
| Dropdowns not working | Re-add data validation on the affected range |
| Formulas showing #REF! | Check if sheet names changed during conversion |
| Sharing link not working | Verify permissions are set to "Anyone with the link" |
