# Manual QA Runbook Template

> Copy into product workspace as `docs/GOOGLE_SHEETS_MANUAL_QA_RUNBOOK.md`.
> Replace `[Product Name]` and `[Workbook Path]` with actual values.

---

## Product: [Product Name]

**Workbook:** `[Workbook Path]`
**Estimated time:** 10–15 minutes

**Note:** Full formula, layout, and GS compatibility verification is automated.
This manual smoke test covers what cannot be automated: Google Drive import,
UI interaction, and print layout.

---

## Smoke Test Steps

### Step 1: Upload XLSX to Google Drive
1. Go to `https://drive.google.com`
2. Click **+ New** → **File upload**
3. Select the workbook file from `build/`
4. Wait for upload confirmation

### Step 2: Open with Google Sheets
1. Locate the uploaded file in Drive
2. Double-click → **Open with Google Sheets**
3. Look for any conversion error messages

### Step 3: Verify All Tabs
Confirm all tabs exist in the correct order (list them here):
1. [Tab 1]
2. [Tab 2]
3. [Tab 3]
...

### Step 4: Spot-Check Key Formulas
Check 3–5 formula cells across different tabs for `#REF!`, `#VALUE!`, `#DIV/0!`.

### Step 5: Verify Dropdowns
- [Dropdown 1 location]: should show [options]
- [Dropdown 2 location]: should show [options]

### Step 6: Verify Dashboard
Check that KPI cards show visible values (not errors or blank).
Reference values (list here).

### Step 7: Verify Print/Export Layout
1. Go to the printable/export tab
2. **File** → **Print** (or Ctrl+P)
3. Check: all content fits, professional appearance, no cut-off columns

### Step 8: Create Copy Link
1. Click **Share** → **Anyone with the link** → **Viewer**
2. Click **Copy link**
3. Test in incognito browser window

### Step 9: Paste Link
1. Open `google-sheets-copy-link-template.txt`
2. Replace placeholder with actual link
3. Save file

---

## Results

Document results in `qa/GOOGLE_SHEETS_MANUAL_QA_RESULTS.md`.
