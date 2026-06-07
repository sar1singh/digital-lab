# Pre-Publish Checklist

> Gate: all sections must pass before a product listing goes live.

---

## 1. Workbook QA

- [ ] All tabs created and named correctly
- [ ] No formula errors (#REF!, #VALUE!, #DIV/0!)
- [ ] Formula cells marked (gray background)
- [ ] Input cells clearly marked (white/green background)
- [ ] Data validation dropdowns working
- [ ] Conditional formatting applied
- [ ] Freeze panes set on data tabs
- [ ] Sample data populated and realistic
- [ ] Charts render correctly (if applicable)
- [ ] Cross-sheet SUMIF/COUNTIF references verified

## 2. Google Sheets QA

- [ ] Workbook uploads to Google Drive without errors
- [ ] All formulas survive conversion
- [ ] Conditional formatting survives conversion
- [ ] Data validation dropdowns work
- [ ] Charts render in Google Sheets
- [ ] Copy link works (test manually)

## 3. Brand QA

- [ ] Brand name (Nivora) appears consistently on all buyer-facing content
- [ ] No personal email used as brand
- [ ] Support email is contact-only, not brand
- [ ] No old brand names in buyer files
- [ ] Brand consistency scan passed (grep for old names = 0 results)

## 4. Screenshot QA

- [ ] Cover communicates value in 3 seconds at thumbnail size
- [ ] All 6 screenshots show real product data
- [ ] Text legible at marketplace sizes
- [ ] No browser chrome or personal info
- [ ] Brand appears where appropriate
- [ ] Screenshots match final workbook (not an earlier version)

## 5. ZIP QA

- [ ] ZIP contains exactly 3 files: workbook, PDF guide, copy link
- [ ] No subdirectories inside ZIP
- [ ] All filenames use brand prefix (`nivora-*`)
- [ ] No version numbers in filenames
- [ ] No internal files (QA docs, source files, screenshots)
- [ ] ZIP contents verified programmatically

## 6. Listing QA

- [ ] Title is clear and searchable
- [ ] Publisher line says "by Nivora"
- [ ] What's Included section lists specific deliverables
- [ ] Who It's For section targets the right buyer
- [ ] Benefits address buyer pain points
- [ ] FAQ answers common hesitations
- [ ] Support contact included
- [ ] Price set
- [ ] All 6 images uploaded in correct order
- [ ] ZIP uploaded as product file
- [ ] Cover set as thumbnail
- [ ] Test purchase completed (preview/checkout works)

---

## Exit Criteria

✅ All items checked = ready to publish  
❌ Any item unchecked = do not publish, fix first
