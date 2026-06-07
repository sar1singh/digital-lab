# Sheet Structure — Nivora Project Budget Tracker

## Tab 1: Start Here

**Purpose:** Setup instructions, navigation guide, formula warnings.

**Content:**
- Product name and brand
- Quick-start checklist
- Tab navigation guide
- Formula cell warning ("Do not edit gray cells")
- Input cell guide ("White/green cells are for your input")
- Sample data note
- Google Sheets vs Excel notes
- Support email

---

## Tab 2: Dashboard

**Purpose:** High-level budget KPIs and visual breakdowns.

**Layout:**

### KPI Cards (Row 1–3)
| KPI | Formula Source |
|-----|---------------|
| Total Budget | SUM of Project budgets |
| Total Spent | SUMIFS from Expenses |
| Total Remaining | Total Budget - Total Spent |
| % Budget Used | Total Spent / Total Budget (formatted as %) |
| Total Income | SUMIFS from Income tab |
| Net Profit | Total Income - Total Spent |
| Projects on Budget | COUNTIFS from Projects (Status = On Budget) |
| Projects Over Budget | COUNTIFS from Projects (Status = Over Budget) |

### Budget by Project (Rows 5–12)
Table showing each project with Budget, Spent, Remaining, % Used.

### Spending by Category (Rows 14–20)
Table showing total spent per expense category.

### Monthly Spending Trend (Rows 22–28)
Table showing total spending by month.

### Project Status Breakdown (Rows 30–34)
Count of projects by status: On Budget, Over Budget, Completed, On Hold.

---

## Tab 3: Projects

**Purpose:** Master list of all projects with budget tracking.

**Columns:**
| Col | Header | Type | Description |
|-----|--------|------|-------------|
| A | Project ID | Data (auto) | PROJ-001, PROJ-002, etc. |
| B | Project Name | Input | Name of the project |
| C | Client | Input | Client or department name |
| D | Budget | Input | Total budget for the project |
| E | Total Spent | Formula | SUMIFS from Expenses tab |
| F | Remaining | Formula | Budget - Total Spent |
| G | % Used | Formula | Total Spent / Budget |
| H | Status | Formula | On Budget / Over Budget / Completed / On Hold |
| I | Notes | Input | Optional notes |

**Status formula logic:**
- If Status = Completed → "Completed"
- Else if % Used > 100% → "Over Budget"
- Else if % Used > 80% → "At Risk" (or "On Budget" with caution)
- Else → "On Budget"

---

## Tab 4: Expenses

**Purpose:** Log individual expenses linked to projects.

**Columns:**
| Col | Header | Type | Description |
|-----|--------|------|-------------|
| A | Date | Input | Date of expense |
| B | Project | Input (dropdown) | Select project from Projects list |
| C | Category | Input (dropdown) | Select category from Categories list |
| D | Description | Input | Description of expense |
| E | Amount | Input | Expense amount |
| F | Notes | Input | Optional notes |

**Data validation:**
- Column B: Dropdown sourced from Projects!Project Name (inline list)
- Column C: Dropdown sourced from Categories!Category Name (inline list)

---

## Tab 5: Income

**Purpose:** Log revenue/income entries linked to projects.

**Columns:**
| Col | Header | Type | Description |
|-----|--------|------|-------------|
| A | Date | Input | Date of income |
| B | Project | Input (dropdown) | Select project from Projects list |
| C | Description | Input | Description of income |
| D | Amount | Input | Income amount |
| E | Payment Status | Input (dropdown) | Paid, Pending, Expected |
| F | Notes | Input | Optional notes |

**Data validation:**
- Column B: Dropdown sourced from Projects!Project Name (inline list)
- Column E: Dropdown inline list "Paid,Pending,Expected"

---

## Tab 6: Categories

**Purpose:** Define expense categories for consistent tracking.

**Columns:**
| Col | Header | Type | Description |
|-----|--------|------|-------------|
| A | Category Name | Input | Name of category |
| B | Description | Input | Optional description |

**Sample categories:**
- Software & Tools
- Contractor Payments
- Marketing & Ads
- Travel & Meetings
- Office Expenses
- Equipment & Hardware
- Subscriptions
- Other

---

## Tab 7: Settings

**Purpose:** Customize currency and dropdown values.

**Layout:**
| Setting | Value |
|---------|-------|
| Currency Symbol | $ |
| Project Status Values | On Budget, Over Budget, Completed, On Hold |
| Payment Status Values | Paid, Pending, Expected |

---

## Tab Colors

| Tab | Color | Hex |
|-----|-------|-----|
| Start Here | Dark Blue | #2F5496 |
| Dashboard | Blue | #2E75B6 |
| Projects | Green | #548235 |
| Expenses | Gold | #BF8F00 |
| Income | Red | #C00000 |
| Categories | Purple | #7030A0 |
| Settings | Gray | #404040 |

---

## Freeze Panes

| Tab | Freeze Panes |
|-----|-------------|
| Projects | A2 |
| Expenses | A2 |
| Income | A2 |
| Categories | A2 |
