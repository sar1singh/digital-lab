# Product Factory Asset Specifications

> Standard specifications for all marketplace images and visual assets. Hardened from Product #1 learnings.

---

## Image Types

### Thumbnail

| Property | Specification |
|----------|---------------|
| Shape | Square |
| Minimum size | 600×600px |
| Recommended size | 1000×1000px |
| Format | PNG |
| Content | Product cover or branded preview |
| Platform | Used as listing thumbnail on Gumroad, Payhip |

### Cover Image

| Property | Specification |
|----------|---------------|
| Aspect ratio | 16:9 |
| Recommended size | 1600×900px |
| Format | PNG |
| Content | Product cover with brand, workbook preview, key benefits |
| Priority | Most important image — drives click-through rate |
| Legibility | Text must be readable at 280px width (Gumroad thumbnail display) |

### Screenshot Images

| Property | Specification |
|----------|---------------|
| Aspect ratio | Consistent across all 6 images |
| Width | 1000–1920px |
| Format | PNG |
| Content | Real product screenshots with sample data |
| Branding | Brand (Nivora) must appear on cover and where appropriate |
| Data | Real sample data — never empty sheets or placeholder text |
| UI | No browser chrome, bookmarks, tabs, or personal data unless intentional |
| Cropping | No cropped UI elements — show full feature context |

---

## Required Gallery Set (6 Images)

| # | File | Content | Purpose |
|---|------|---------|---------|
| 1 | `01-cover.png` | Product cover — brand, preview, benefits, Google Sheets + Excel badge | Primary thumbnail — drives click-through |
| 2 | `02-dashboard.png` | Dashboard or summary view with real sample data and charts | First value impression after cover |
| 3 | `03-primary-feature.png` | Main input sheet — shows data entry workflow with real data | Core utility demonstration |
| 4 | `04-secondary-feature.png` | Secondary workflow — filtering, categorization, or analysis | Shows product depth |
| 5 | `05-supporting-feature.png` | Less obvious features — additional tabs that add value | Captures undecided buyers |
| 6 | `06-whats-included.png` | Deliverables checklist, feature grid, or contents overview | Answers "what do I get?" |

---

## File Naming Convention

```
NN-description.png
```

- Zero-padded sequence number (01, 02, 03...)
- Lowercase
- Hyphen-separated words
- No spaces, no special characters

Examples:
- `01-cover.png`
- `02-dashboard.png`
- `03-primary-feature.png`
- `04-secondary-feature.png`
- `05-supporting-feature.png`
- `06-whats-included.png`

---

## Gallery Upload Order

| Position | Asset | Rationale |
|----------|-------|-----------|
| 1st | Cover | First thing buyer sees — drives click-through |
| 2nd | Dashboard | Show product value immediately |
| 3rd | Primary Feature | Confirm core utility |
| 4th | Secondary Feature | Support purchase decision |
| 5th | Supporting Feature | Convert hesitant buyers |
| 6th | What's Included | Final confirmation before checkout |

This order is critical. Do not reorder.

---

## Quality Requirements

| Check | Standard |
|-------|----------|
| Text legibility | Readable at 280px thumbnail width (Gumroad) and full size |
| Brand visibility | Nivora on cover, optionally on other assets |
| Data realism | Realistic sample data — no empty cells, no "Sample Data" placeholder text |
| UI cleanliness | No browser chrome, bookmarks, personal info |
| Consistency | Same aspect ratio and styling across all 6 images |
| Version matching | Screenshots must match the final workbook version |
| Color accuracy | Screenshots should match actual product colors |
| File size | Keep reasonable — optimize PNGs, avoid >5MB per image |

---

## Generation Workflow

```
1. Finalize workbook (Build + QA complete)
2. Lock brand (Nivora) on all buyer-facing content
3. Capture screenshots from the final workbook
4. Create cover image with brand, preview, benefits
5. Create remaining 5 feature/images in order
6. Name files according to convention (01- through 06-)
7. Save to listing-assets/ folder
8. QA: verify against all quality requirements
9. Upload to marketplace in correct order
```

**Critical rule:** Generate assets only after the workbook is complete and QA'd. Generating early causes rework (brand changes, workbook fixes, screenshot retakes).

---

## Platform-Specific Notes

| Platform | Thumbnail | Cover | Gallery |
|----------|-----------|-------|---------|
| Gumroad | Square crop of cover | 16:9 recommended | Up to 10 images — upload all 6 |
| Payhip | Auto-generated from first image | Required | Supported |
| Etsy | First image is primary thumbnail | Required | 5+ required, up to 10 |
| Creative Market | Lifestyle + flatlay expected | Required | Multiple angles expected |

For all platforms: the same 6-image set is the baseline. Add platform-specific images (lifestyle, mockups) only after baseline is established.

---

## Anti-Patterns (From Product #1)

| Anti-Pattern | Why It Fails | Fix |
|--------------|-------------|-----|
| Generating screenshots before workbook is final | Rework — retake all images when workbook changes | Generate last, after QA |
| Empty sheets in screenshots | Looks unprofessional, no perceived value | Always populate with realistic sample data |
| No brand on cover | Buyer doesn't know who made it | Add Nivora brand to cover |
| Browser chrome visible | Distracting, looks unprofessional | Full-screen app mode, crop chrome |
| Inconsistent aspect ratios | Looks sloppy in gallery | Lock one ratio and use for all 6 |
| Placeholder text ("Sample Data") | Looks unfinished | Use real category names, real numbers |
