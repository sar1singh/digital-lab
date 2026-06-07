# Product Factory Product Structure

> Standard workspace structure for every Product Factory product.

---

## Directory Layout

```
products/
└── {product-slug}/
    ├── artifacts/          # Final approved source workbooks (versioned originals)
    ├── build/              # Build scripts, generation code, notes
    ├── qa/                 # QA reports, test outputs, validation scripts
    ├── listing-assets/     # Marketplace gallery images (6 final PNGs)
    ├── screenshots/        # Raw screenshot sources (before processing)
    ├── docs/               # Internal documents (no buyer-facing content)
    └── delivery/           # Buyer-facing deliverables only
```

---

## Directory Purpose

### `artifacts/`

Versioned source workbooks. These are the approved originals.

Contains:
- `{product-slug}-v{major}.{minor}.xlsx` — versioned artifact files
- Source docs if applicable

**Rules:**
- No buyer-facing filenames here (those go in `delivery/`)
- Each version is preserved — do not overwrite
- Final approved version is the one used for delivery

### `build/`

Build-time files that are not part of the final product.

Contains:
- Python scripts (openpyxl generators)
- Build configuration
- Generation notes
- Draft workbooks (if any)

**Rules:**
- Temporary and working files only
- Not included in `delivery/` or ZIP

### `qa/`

Quality assurance artifacts and outputs.

Contains:
- QA reports
- Formula audit logs
- Validation scripts
- Test outputs
- Automated check results

**Rules:**
- Created during QA phase
- Archived per product
- Not included in `delivery/` or ZIP

### `listing-assets/`

The final 6 marketplace gallery images.

Contains:
```
01-cover.png
02-dashboard.png
03-primary-feature.png
04-secondary-feature.png
05-supporting-feature.png
06-whats-included.png
```

**Rules:**
- Only final PNGs — no source files (.psd, .xcf, .svg)
- Named per asset naming convention
- Generated during Asset Generation phase (after workbook is final)
- Also present in `delivery/` for marketplace upload
- Never include in buyer ZIP

### `screenshots/`

Raw screenshot captures before processing.

Contains:
- Full-resolution captures
- Multiple attempts (before selection)
- Source files for gallery images

**Rules:**
- Working directory — not buyer-facing
- Not included in `delivery/` or ZIP
- Can be cleaned up after listing is live

### `docs/`

Internal documents that inform the build process.

Contains:
- BUILD_CHECKLIST.md
- Release notes
- Planning documents
- Research notes
- Listing copy drafts
- Screenshot guides
- Publishing readiness reports
- Brand QA checklists
- Final ZIP QA reports
- Any internal/planning file that is not a buyer deliverable

**Rules:**
- Internal only — never customer-facing
- This is the default destination for any document that isn't a buyer deliverable
- Not included in `delivery/` or ZIP

### `delivery/`

The only buyer-facing directory.

Contains exactly:
```
{brand}-{product-slug}.xlsx
{brand}-{product-slug}-quick-start-guide.pdf
google-sheets-copy-link.txt
{brand}-{product-slug}-delivery.zip
listing-assets/       # 6 gallery images (for marketplace upload)
screenshots/          # (optional — raw sources if needed for reference)
```

**Rules:**
- Buyer-facing assets only
- No internal docs, QA reports, source files, or planning documents
- ZIP is the final buyer download — contains exactly 3 files
- These 3 files also exist loose in delivery/ for individual access

---

## Workspace Initialization

When starting a new product:

```powershell
# From products/ directory
mkdir "{product-slug}"
cd "{product-slug}"
mkdir artifacts, build, qa, listing-assets, screenshots, docs, delivery
```

Then create:
- `BUILD_CHECKLIST.md` in product root
- Link back to product entry in PRODUCT_CATALOG.csv

---

## Product Workspace Lifecycle

| Phase | Active Directories | Notes |
|-------|-------------------|-------|
| Idea | (product root) | Create workspace, link to catalog |
| Build | `build/`, `artifacts/` | Draft workbooks, generate |
| QA | `qa/`, `artifacts/` | Validate, fix issues |
| Asset Generation | `listing-assets/`, `screenshots/` | Capture and create images |
| Packaging | `delivery/`, `docs/` | Move internal files to docs/ |
| Marketplace Listing | `delivery/` | Upload from delivery/ |
| Publish | `delivery/` | Live — no more changes |
| Post-Publish | `docs/` | Retrospective, lessons |

---

## File Migration Rules (for cleanup)

When reorganizing a workspace:

| If you find it in... | Move it to... |
|---------------------|---------------|
| delivery/ but it's internal (QA, notes, source) | docs/ |
| delivery/ but it's a listing image | listing-assets/ (keep in delivery/ too — it belongs there for upload) |
| delivery/ but it's a versioned artifact | artifacts/ |
| delivery/ but it's a temporary screenshot | screenshots/ or delete |
| product root/ but it's an internal doc | docs/ |
| product root/ but it's a buyer file | delivery/ |

---

## Structure Rules Summary

| # | Rule |
|---|------|
| 1 | `delivery/` = buyer-facing only. No internal files. |
| 2 | `docs/` = internal documents. Default for non-deliverable files. |
| 3 | `listing-assets/` = exactly 6 PNGs. Named per convention. |
| 4 | `artifacts/` = versioned source workbooks. Preserve all versions. |
| 5 | ZIP = exactly 3 files from `delivery/`. No subdirectories. |
| 6 | No file appears in more than one functional directory (except listing-assets which is also in delivery/) |
