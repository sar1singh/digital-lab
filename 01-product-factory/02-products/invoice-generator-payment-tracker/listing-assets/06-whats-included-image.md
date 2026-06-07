# Asset 6: What's Included Image (`06-whats-included.png`)

**Purpose:** Answer "what do I get?" — show deliverables checklist.
**Output file:** `listing-assets/06-whats-included.png`
**Dimensions:** 1200 × 800 px (3:2 aspect ratio)
**Reference screen:** Composed graphic (no direct tab screenshot)

---

## Layout Specification

Two-column grid layout with icons and descriptive text.

### Background
- White (#FFFFFF) or very light gray (#F5F5F5)
- Subtle bottom border or shadow on each item card

### Header
```
What's Included
Nivora Invoice Generator & Payment Tracker
```

**Font:** Calibri Bold, 36pt, dark navy (#0D1B2A)
**Subtitle:** Calibri Regular, 16pt, gray (#666666)

---

## Deliverable Grid

### Left Column

| # | Icon | Feature | Description |
|---|------|---------|-------------|
| 1 | 📄 | **Invoice Generator** | Professional, printable invoice template with auto-calculated subtotal, tax, and total |
| 2 | 📊 | **Revenue Dashboard** | Real-time KPI cards, monthly revenue breakdown, invoice status tracking, and top client insights |
| 3 | 💳 | **Payment Tracker** | Track payments linked to invoices with VLOOKUP-auto-populated client names and customizable payment methods |
| 4 | 👥 | **Client Manager** | Directory with 10 sample clients, contact details, and Active/Inactive/Archived status tracking |

### Right Column

| # | Icon | Feature | Description |
|---|------|---------|-------------|
| 5 | 📋 | **Invoice Register** | Complete invoice log with auto-calculating status (Paid, Sent, Overdue, Partial) and outstanding balances |
| 6 | ⚙️ | **Settings Panel** | Customizable currency symbol, default tax rate, invoice status values, payment methods, and client statuses |
| 7 | 📘 | **Quick-Start PDF Guide** | Step-by-step instructions: setup, invoice creation, payment tracking, Google Sheets import |
| 8 | 🔄 | **Excel + Google Sheets** | Works in Microsoft Excel AND Google Sheets — no special software required |

---

## Item Card Style

Each deliverable item rendered as a card/badge:

- **Background:** White card with 1px light gray (#E0E0E0) border
- **Border radius:** 6px
- **Padding:** 12px inside card
- **Gap between cards:** 12px
- **Icon:** 24 × 24 px, left-aligned within card
- **Title:** Calibri Bold, 14pt, dark (#333333)
- **Description:** Calibri Regular, 11pt, gray (#666666), 1 line max

---

## Layout Wireframe

```
┌──────────────────────────────────────────────────┐
│           What's Included                        │
│    Nivora Invoice Generator & Payment Tracker    │
│                                                  │
│  ┌────────────┐    ┌────────────┐               │
│  │ 📄 Invoice │    │ 📋 Invoice │               │
│  │   Generator│    │   Register │               │
│  └────────────┘    └────────────┘               │
│  ┌────────────┐    ┌────────────┐               │
│  │ 📊 Revenue │    │ ⚙️ Settings │               │
│  │   Dashboard│    │   Panel    │               │
│  └────────────┘    └────────────┘               │
│  ┌────────────┐    ┌────────────┐               │
│  │ 💳 Payment │    │ 📘 Quick-  │               │
│  │   Tracker  │    │   Start PDF│               │
│  └────────────┘    └────────────┘               │
│  ┌────────────┐    ┌────────────┐               │
│  │ 👥 Client  │    │ 🔄 Excel + │               │
│  │   Manager  │    │   GS       │               │
│  └────────────┘    └────────────┘               │
│                                                  │
│  [Bottom bar: "Instant Download · Nivora"]       │
└──────────────────────────────────────────────────┘
```

---

## Bottom Bar

- **Background:** Dark navy (#0D1B2A)
- **Text:** "Instant Download · Nivora" in white, 14pt
- **Height:** 40px
- **Position:** Bottom of image

---

## Acceptance Criteria

- [ ] "What's Included" header with brand subtitle
- [ ] 8 deliverable items in 2×4 grid
- [ ] Each item has icon, title, and description
- [ ] Invoice Generator listed first (primary feature)
- [ ] Excel + Google Sheets listed last (cross-platform message)
- [ ] Quick-Start PDF Guide included in grid
- [ ] Bottom bar with "Instant Download · Nivora"
- [ ] Clean, uncluttered layout — no overlapping elements
- [ ] All text readable at full resolution

---

## QA Checklist

- [ ] 8 unique deliverables listed (not duplicated)
- [ ] Invoice Generator appears (primary feature)
- [ ] Revenue Dashboard appears
- [ ] Payment Tracker appears
- [ ] Client Manager appears
- [ ] Invoice Register appears
- [ ] Settings Panel appears
- [ ] Quick-Start PDF Guide appears
- [ ] Excel + Google Sheets appears
- [ ] No missing features from the workbook
- [ ] No features listed that aren't in the workbook
- [ ] Brand name "Nivora" appears at least twice
- [ ] Spelling checked on all text
- [ ] Consistent card sizes across both columns
