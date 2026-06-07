# Delivery Standard

> Standard delivery package format for all Product Factory products.

---

## File Naming Convention

All delivery filenames use the brand prefix:

```
{nivora}-{product-name}.{ext}
```

| File | Pattern | Example |
|------|---------|---------|
| Workbook | `{brand}-{product-slug}.xlsx` | `nivora-budget-planner-expense-tracker.xlsx` |
| PDF Guide | `{brand}-{product-slug}-quick-start-guide.pdf` | `nivora-budget-planner-expense-tracker-quick-start-guide.pdf` |
| Copy Link | `google-sheets-copy-link.txt` | `google-sheets-copy-link.txt` |
| Delivery ZIP | `{brand}-{product-slug}-delivery.zip` | `nivora-budget-planner-expense-tracker-delivery.zip` |

**Rules:**
- Product slug = lowercase, hyphens between words
- Brand prefix = lowercase `nivora-`
- No version numbers in buyer-facing filenames
- No spaces in filenames

---

## Delivery Folder Structure

The `delivery/` folder contains only customer-facing assets:

```
delivery/
├── {brand}-{product-slug}.xlsx              # Buyer workbook
├── {brand}-{product-slug}-quick-start-guide.pdf  # Buyer PDF guide
├── google-sheets-copy-link.txt              # Google Sheets copy instructions
├── {brand}-{product-slug}-delivery.zip      # Buyer ZIP (contains above 3 files)
├── listing-assets/                          # Marketplace gallery images
└── screenshots/                             # Raw screenshot sources
```

**Rule: Delivery folder contains only buyer-facing assets and final ZIP.** Internal planning, QA, and reference documents belong in `docs/` or product workspace root.

---

## ZIP Contents

```
{brand}-{product-slug}-delivery.zip
├── {brand}-{product-slug}.xlsx
├── {brand}-{product-slug}-quick-start-guide.pdf
└── google-sheets-copy-link.txt
```

Exactly 3 files. No subdirectories. No extra files.

---

## What Must Be Excluded

| Type | Examples |
|------|----------|
| Internal docs | BUILD_CHECKLIST.md, QA reports, FINAL_ZIP_QA.md |
| Source files | .md, .html, .py, planning docs |
| Listing assets | Cover images, feature screenshots, listing copy |
| Screenshots | Any image files used for marketplace gallery |
| Release notes | release-notes.txt (internal unless buyer-facing) |
| QA checklists | BRAND_QA_CHECKLIST.md, any QA artifacts |
| Versioned artifacts | `*-v1.2.xlsx`, `*-v1.1.xlsx` |

---

## PDF Guide Requirements

- Title must include brand name: "Nivora {Product Name}"
- Must include support email
- Must include basic usage instructions
- 1 page (expand to 2 if needed, never more than 4)
- Generated from markdown or HTML source using fpdf2 or equivalent
- Regenerated whenever content changes

---

## Google Sheets Copy Link File

- Filename: `google-sheets-copy-link.txt`
- Must include: brand, copy link URL, usage instructions, support email
- Link must be tested before delivery

---

## Delivery Verification

Before finalizing:
1. Programmatically verify ZIP contents match expected list
2. Verify no old filenames exist in delivery folder
3. Verify no version numbers in filenames
4. Verify PDF title contains brand
5. Verify copy link file contains correct URL
6. Run brand consistency scan

## QA Gate

Delivery cannot be finalized unless all 10 QA layers from `QA_COVERAGE_STANDARD.md`
are complete. The delivery package is Layer 6; it must pass before ZIP is built.
Layer 10 (Pre-Publish Gate) is the final sign-off.

**No product can become "Delivery Ready" unless all 10 QA layers are complete.**
