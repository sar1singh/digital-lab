# Google Sheets Manual QA Runbook — Nivora Invoice Generator & Payment Tracker

**QA Layer:** 5 (Manual Smoke QA)
**Coverage standard:** `01-product-factory/07-systems/QA_COVERAGE_STANDARD.md`

**Product:** Nivora Invoice Generator & Payment Tracker
**Status:** Automated workbook QA passed — GS smoke QA pending
**Workbook:** `build/nivora-invoice-generator-payment-tracker.xlsx`
**Estimated time:** 10–15 minutes

**Note:** Full formula, layout, and GS compatibility verification is automated
(Layers 1–4 via `build/run_all_qa.py`). This manual smoke test (Layer 5) covers
what cannot be automated: Google Drive import, UI interaction, and print layout.

---

## Smoke Test Steps

### Step 1: Upload XLSX to Google Drive

1. Go to `https://drive.google.com`
2. Click **+ New** → **File upload**
3. Select: `build/nivora-invoice-generator-payment-tracker.xlsx`
4. Wait for upload confirmation

### Step 2: Open with Google Sheets

1. Locate the uploaded file in Drive
2. Double-click to open preview
3. Click **Open with Google Sheets**
4. Look for any conversion error messages

### Step 3: Verify All 7 Tabs

Confirm these tabs exist in order:
1. Start Here
2. Dashboard
3. Clients
4. Invoice Register
5. Payment Tracker
6. Invoice Generator
7. Settings

### Step 4: Spot-Check Key Formulas

Check 3–5 formula cells for errors:
- **Invoice Register** column I (Tax Amount), J (Total), L (Outstanding), M (Status)
- **Payment Tracker** column C (Client Name — VLOOKUP)
- Look for `#REF!`, `#VALUE!`, `#DIV/0!`

### Step 5: Verify Dropdowns

- **Clients** tab, column G (Status): should show Active, Inactive, Archived
- **Payment Tracker** tab, column E (Payment Method): should show Bank Transfer, PayPal, etc.

### Step 6: Verify Dashboard

Check that KPI cards show visible values (not errors or blank).

**Reference values (for today = 2026-06-07):**
- Total Revenue: 54,560.00
- Paid Revenue: 18,700.00
- Total Invoices: 25
- Paid Invoices: 10
- Overdue Invoices: 7
- Active Clients: 8

### Step 7: Verify Invoice Generator Print/Export

1. Go to **Invoice Generator** tab
2. **File** → **Print** (or Ctrl+P)
3. Check: all content fits, professional appearance, no cut-off columns
4. Try **File** → **Share** → **Export as PDF** for PDF preview

### Step 8: Create Copy Link

1. Click **Share** (top-right)
2. Set **Anyone with the link** → **Viewer**
3. Click **Copy link**
4. Test in incognito browser window

### Step 9: Paste Link

1. Open `build/google-sheets-copy-link-template.txt`
2. Replace the placeholder with the actual link
3. Save the file

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `#REF!` in VLOOKUP | Sheet name changed by GS | Edit formula to match actual sheet name |
| Dropdown shows range text | GS needs named ranges | Create named range in Settings |
| Formula shows `#NAME?` | Unsupported function | Check for Excel-only functions |

## After Smoke QA

**If all 9 steps pass:**
- Update `qa/GOOGLE_SHEETS_MANUAL_QA_RESULTS.md` — mark all tests PASS
- Update `QA_CHECKLIST.md` — GS section all checked
- Update status to **Product #2 — Google Sheets QA passed**

**If any step fails:**
- Record specific failures in `qa/GOOGLE_SHEETS_MANUAL_QA_RESULTS.md`
- Fix in `build/build_workbook.py`, regenerate, re-upload, re-test
