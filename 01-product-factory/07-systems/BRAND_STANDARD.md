# Brand Standard

> All Product Factory products use a single brand identity. This document defines how the brand is applied.

---

## Brand Identity

| Property | Value |
|----------|-------|
| Brand name | Nivora |
| Support email | workbysar1@gmail.com |
| Platform accounts | Gumroad, Payhip (under workbysar1@gmail.com) |

---

## Brand Usage Rules

### Allowed
- Brand on product covers, listing copy, delivery files, PDF guides
- Brand in marketplace title as publisher line ("by Nivora")
- Brand in file naming prefix (`nivora-*.xlsx`)

### Not Allowed
- "Work by Sar1" in any customer-facing content — this is the internal operator label only
- `workbysar1@gmail.com` used as a brand name — it is support contact only
- Personal name used in place of brand

### Email Usage
- `workbysar1@gmail.com` = support, platform signup, billing contact
- Appears in: PDF guide support section, listing copy support line, copy link file
- Never used as: brand name, publisher name, product title

---

## File Naming Convention

All buyer-facing files use the pattern:

```
nivora-{product-slug}.{ext}
```

| File | Pattern |
|------|---------|
| Workbook | `nivora-{product-slug}.xlsx` |
| PDF Guide | `nivora-{product-slug}-quick-start-guide.pdf` |
| Delivery ZIP | `nivora-{product-slug}-delivery.zip` |
| Copy Link | `google-sheets-copy-link.txt` (no brand prefix needed — this is a generic instructions file) |

---

## Product Naming on Marketplace

Two formats used:

**Full branded title** (in guides, copy link, PDF):
```
Nivora {Product Name}
```

**Marketplace listing title** (SEO-friendly, discoverable):
```
{Product Name} — Google Sheets + Excel
```

Publisher line:
```
by Nivora
```

---

## Screenshot Naming

Marketplace gallery images use numeric sequence:

```
01-cover.png
02-dashboard.png
03-primary-feature.png
04-secondary-feature.png
05-advanced-features.png
06-whats-included.png
```

Brand should appear on the cover image and optionally on other assets.

---

## Internal vs External

| Context | Brand |
|---------|-------|
| Buyer-facing delivery | Nivora |
| Marketplace listing | Nivora |
| PDF guide | Nivora |
| Listing images | Nivora |
| GitHub repo | N/A (internal, no brand required) |
| Internal filenames | No brand prefix needed |
| QA/planning docs | No brand prefix needed |

---

## Brand Consistency Check

Before every product publish:
1. Grep for "Work by Sar1" in all delivery files — must return 0 matches
2. Verify all buyer-facing filenames start with `nivora-`
3. Verify support email appears only as contact, not as brand
4. Verify PDF title includes "Nivora"
5. Verify listing copy publisher line is "by Nivora"
