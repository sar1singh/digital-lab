# Delivery Structure Standard

> Product factory standard for how delivery folders are organized.

---

## Product Workspace Structure

```
product-name/
├── artifacts/        # Final approved source workbook (versioned)
├── build/            # Build scripts, notes
├── docs/             # Internal documents, QA, planning
├── qa/               # QA reports, test cases
├── listing-assets/   # Marketplace gallery images
├── screenshots/      # Raw screenshot sources
└── delivery/         # Buyer-facing assets only
```

---

## Delivery Folder Rule

The `delivery/` folder contains **only customer-facing assets**:

```
delivery/
├── {brand}-{product-slug}.xlsx
├── {brand}-{product-slug}-quick-start-guide.pdf
├── google-sheets-copy-link.txt
├── {brand}-{product-slug}-delivery.zip
├── listing-assets/
└── screenshots/
```

**Strictly excluded from delivery/:**
- QA checklists
- Build scripts
- Internal notes
- Drafts
- Planning documents
- Versioned artifact files (*-v1.x.xlsx)

Plan to `docs/` for internal documents.

---

## Brand-First Workflow

Complete these steps **before** any asset generation or workbook export:

1. Brand name finalized (Nivora — locked for all products)
2. Support email finalized (workbysar1@gmail.com)
3. File naming conventions locked (`{brand}-{product-slug}.{ext}`)
4. Product marketplace title format decided

Do not generate listing assets, screenshots, or PDF guides until branding is locked.
