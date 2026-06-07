# Asset 5: Client Management Screenshot (`05-advanced-features.png`)

**Purpose:** Show client directory with contact details and status management.
**Output file:** `listing-assets/05-client-management.png`
**Dimensions:** 1200 × 800 px (3:2 aspect ratio)
**Reference screen:** Clients tab in Google Sheets + Settings tab Status Values inset

---

## Capture Instructions

**Source:** Google Sheets → Clients tab

**Crop area (primary):**
- **Top:** Row 1 (column headers)
- **Bottom:** Row 11 (last client entry)
- **Left:** Column A
- **Right:** Column H (or F if H is empty for most rows)

**Zoom level:** 100%

**Pre-capture steps:**
1. Open Clients tab in Google Sheets
2. Hide formula bar and gridlines
3. Deselect all cells
4. Ensure Status column shows dropdown arrows

---

## Elements Must Be Visible

### Client Table (all 10 clients)

**Column headers:**
| Col | Header | Sample Data |
|-----|--------|-------------|
| A | Client ID | CL-001 through CL-010 |
| B | Client Name | Sarah Chen, James Wilson, etc. |
| C | Company | TechVision Inc., etc. |
| D | Email | sarah@techvision.com, etc. |
| E | Phone | (555) 123-4567, etc. |
| F | Address | San Francisco, CA, etc. |
| G | Status | Active (8), Inactive (1), Archived (1) |
| H | Notes | (various) |

### Status Values (optional callout inset)
If adding a callout to show the available statuses:
- **Inset text:** "Client Status Options → Active, Inactive, Archived"
- **Position:** Right side of Status column

---

## Annotations / Callouts

| Callout | Position | Text |
|---------|----------|------|
| 1 | Right of Status column | "Track client status — Active, Inactive, or Archived" |
| 2 | Below client list | "10 sample clients included — add unlimited clients" |
| 3 | Right of Contact columns | "Full contact details — name, company, email, phone, address" |

---

## Title Overlay

```
Client Management Directory
Organize clients with contact details and status tracking
```

---

## Acceptance Criteria

- [ ] All 10 client entries visible (CL-001 to CL-010)
- [ ] All 8 column headers visible
- [ ] Status column shows Active, Inactive, and Archived values
- [ ] Gridlines hidden
- [ ] Formula bar hidden
- [ ] No cell selected
- [ ] Client names and companies visible and readable
- [ ] At least one Inactive and one Archived client visible (to show all statuses)

---

## QA Checklist

- [ ] 10 client rows visible (CL-001 to CL-010)
- [ ] 8 Active clients, 1 Inactive, 1 Archived
- [ ] Column headers: Client ID, Client Name, Company, Email, Phone, Address, Status, Notes
- [ ] Status dropdown arrows visible (column G)
- [ ] Sarah Chen (CL-001) shown as first client
- [ ] Most clients have company names filled in
- [ ] Email addresses use realistic domains
- [ ] Phone numbers formatted consistently: (555) XXX-XXXX
