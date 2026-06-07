# Product Factory Delivery Standard

> Standard delivery package format for all Product Factory products. Hardened from Product #1 cleanup learnings.

---

## Delivery ZIP Contents

Every product delivers exactly **3 files** in the ZIP:

```
{brand}-{product-slug}-delivery.zip
├── {brand}-{product-slug}.xlsx
├── {brand}-{product-slug}-quick-start-guide.pdf
└── google-sheets-copy-link.txt
```

### Rules

- Exactly 3 files. No more, no less.
- No subdirectories inside the ZIP.
- No duplicate files.
- No version numbers in filenames.
- All filenames use brand prefix (`nivora-`).
- ZIP is the **last step** in the packaging process.

---

## File Naming Convention

| File | Pattern | Example |
|------|---------|---------|
| Workbook | `{brand}-{product-slug}.xlsx` | `nivora-budget-planner-expense-tracker.xlsx` |
| PDF Guide | `{brand}-{product-slug}-quick-start-guide.pdf` | `nivora-budget-planner-expense-tracker-quick-start-guide.pdf` |
| Copy Link | `google-sheets-copy-link.txt` | `google-sheets-copy-link.txt` |
| Delivery ZIP | `{brand}-{product-slug}-delivery.zip` | `nivora-budget-planner-expense-tracker-delivery.zip` |

### Naming Rules

- Brand prefix = lowercase `nivora-`
- Product slug = lowercase, hyphens between words
- No version numbers in buyer-facing filenames (e.g., `-v1.2` is forbidden)
- No spaces in filenames
- Copy link file is the only exception to brand prefix (it's a generic instructions file)

---

## What Must Be Excluded

| Category | Examples | Destination |
|----------|----------|-------------|
| Internal docs | BUILD_CHECKLIST.md, QA reports, planning notes | `docs/` |
| Source files | .md, .html, .py source for PDF, build scripts | `docs/` or product root |
| Listing assets | Cover images, feature screenshots | `listing-assets/` |
| Raw screenshots | Any image files used to create gallery images | `screenshots/` |
| Release notes | Any release or changelog file | `docs/` |
| QA checklists | Brand QA, ZIP QA, formula validation reports | `qa/` or `docs/` |
| Versioned artifacts | `product-v1.2.xlsx`, `product-v1.1.xlsx` | `artifacts/` |
| Temporary screenshots | Test captures, partial screenshots | `screenshots/` or delete |

**If it's not a final buyer deliverable, it does not go in delivery/ or the ZIP.**

---

## Delivery Folder Structure

```
delivery/
├── {brand}-{product-slug}.xlsx                     # Buyer workbook (final, branded)
├── {brand}-{product-slug}-quick-start-guide.pdf    # Quick start guide (final, branded)
├── google-sheets-copy-link.txt                     # Google Sheets copy instructions
├── {brand}-{product-slug}-delivery.zip             # Buyer ZIP (contains above 3 files)
├── listing-assets/                                 # 6 gallery images for marketplace
│   ├── 01-cover.png
│   ├── 02-dashboard.png
│   ├── 03-primary-feature.png
│   ├── 04-secondary-feature.png
│   ├── 05-supporting-feature.png
│   └── 06-whats-included.png
└── screenshots/                                    # Raw screenshot sources (optional)
```

**Delivery folder contains only:**
- Final buyer deliverables (xlsx, PDF, copy link)
- Delivery ZIP (contains the above 3 files)
- Marketplace images (listing-assets/)
- Screenshot sources (screenshots/)

**No internal files in delivery/.** Put them in `docs/` or `qa/`.

---

## PDF Guide Requirements

| Requirement | Specification |
|-------------|---------------|
| Title | Must include brand: "Nivora {Product Name}" |
| Support email | workbysar1@gmail.com |
| Usage instructions | Basic steps to start using the product |
| Length | 1 page (2 max if needed, never more than 4) |
| Content | How to use, features overview, support contact |
| Generation | Generate 2nd-to-last (before ZIP, after all other files are final) |
| Regeneration | Regenerate whenever workbook content changes |
| Source | Generated from markdown or HTML using fpdf2 or equivalent |

---

## Google Sheets Copy Link File

| Requirement | Specification |
|-------------|---------------|
| Filename | `google-sheets-copy-link.txt` (no brand prefix) |
| Content | Brand name, copy link URL, usage instructions, support email |
| Link validation | Test the link before finalizing delivery |
| Timing | Create after Google Sheets copy is created and validated |
| Fragility | Copy link is fragile — lock it early, change only if necessary |

---

## Packaging Sequence (Order Matters)

1. **Brand lock** — Nivora, support email, naming conventions (before anything else)
2. **Final workbook** — QA'd, branded, ready for delivery
3. **Google Sheets copy** — upload, validate copy link
4. **Copy link file** — `google-sheets-copy-link.txt`
5. **PDF guide** — 2nd-to-last step
6. **Delivery ZIP** — final step, after all files are verified
7. **Listing assets** — 6 gallery images (can be done in parallel with steps 2–4)

---

## Delivery Verification Checklist

Before marking delivery as final:

- [ ] ZIP contains exactly 3 files (workbook, PDF, copy link)
- [ ] All filenames use brand prefix (except copy link)
- [ ] No version numbers in filenames
- [ ] No internal files in ZIP
- [ ] No duplicate files in ZIP
- [ ] No subdirectories in ZIP
- [ ] ZIP opens without errors
- [ ] Excel file opens without errors
- [ ] PDF guide opens and has correct brand/title
- [ ] Google Sheets copy link works (test manually)
- [ ] Brand consistency scan passed (grep for old names = 0)
- [ ] Delivery folder has no stray internal files
