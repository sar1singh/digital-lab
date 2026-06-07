# Formulas — Nivora Invoice Generator & Payment Tracker

All formulas are Excel and Google Sheets compatible. No macros, VBA, or Apps Script.

---

## Invoice Register (Tab 4)

### Tax Amount (Column I)
```
=G2*H2
```
Where G2 = Subtotal, H2 = Tax Rate.

### Total (Column J)
```
=G2+I2
```
Where G2 = Subtotal, I2 = Tax Amount.

### Outstanding (Column L)
```
=J2-K2
```
Where J2 = Total, K2 = Amount Paid.

### Status (Column M)
```
=IF(L2=0,"Paid",IF(TODAY()>C2,"Overdue",IF(K2>0,"Partial","Sent")))
```
Where L2 = Outstanding, C2 = Due Date, K2 = Amount Paid.

Logic:
- Outstanding = 0 → Paid
- Today > Due Date → Overdue
- Amount Paid > 0 but Outstanding > 0 → Partial
- Otherwise → Sent

---

## Dashboard (Tab 2)

### Total Revenue
```
=SUMIFS(Register!J:J,Register!M:M,"<>Draft")
```
Sum of Total column excluding Draft invoices.

### Paid Revenue
```
=SUMIFS(Register!J:J,Register!M:M,"Paid")
```
Sum of Total where status = Paid.

### Outstanding Revenue
```
=SUMIFS(Register!L:L,Register!M:M,"Sent",Register!L:L,">0")+SUMIFS(Register!L:L,Register!M:M,"Overdue",Register!L:L,">0")+SUMIFS(Register!L:L,Register!M:M,"Partial",Register!L:L,">0")
```
Sum of Outstanding where invoice is not fully paid.

### Total Invoices
```
=COUNTIF(Register!M:M,"<>")-1
```
Count all invoice entries (minus header).

### Paid Invoices
```
=COUNTIFS(Register!M:M,"Paid")
```

### Unpaid Invoices
```
=COUNTIFS(Register!M:M,"Sent")+COUNTIFS(Register!M:M,"Overdue")+COUNTIFS(Register!M:M,"Partial")+COUNTIFS(Register!M:M,"Draft")
```

### Overdue Invoices
```
=COUNTIFS(Register!M:M,"Overdue")
```

### Active Clients
```
=COUNTIFS(Clients!G:G,"Active")
```

### Average Invoice Value
```
=IFERROR(SUMIFS(Register!J:J,Register!M:M,"<>Draft")/COUNTIFS(Register!M:M,"<>Draft"),0)
```

### Revenue by Month (summary table)
```
=SUMIFS(Register!J:J,Register!M:M,"<>Draft",Register!B:B,">="&DATE(year,month,1),Register!B:B,"<"&DATE(year,month+1,1))
```
Where year and month reference helper cells.

### Invoice Status Breakdown (summary table)
Count per status using COUNTIFS for each: Paid, Sent, Overdue, Partial, Draft.

### Top Clients by Revenue (summary table)
```
=SUMIFS(Register!J:J,Register!E:E,client_name,Register!M:M,"<>Draft")
```
Where client_name references each top client row.

---

## Payment Tracker (Tab 5)

### Client Name (Column C)
```
=VLOOKUP(B2,Register!A:E,5,FALSE)
```
Where B2 = Invoice ID, lookup in Invoice Register for Client Name.

Alternative (simpler, no cross-sheet VLOOKUP):
Manual entry or IFERROR(VLOOKUP(...),"") with IFERROR wrapper.

---

## Invoice Generator (Tab 6)

### Line Item Amount
```
=Quantity*Rate
```

### Subtotal
```
=SUM(Amount_column)
```

### Tax Amount
```
=Subtotal*TaxRate
```
Tax Rate referenced from Settings tab.

### Total
```
=Subtotal+TaxAmount
```

---

## Settings (Tab 7)

Settings tab contains reference values used by data validation and formulas across other tabs. No complex formulas needed — simple cell references.

---

## Formula Rules

1. All formulas must work identically in Excel and Google Sheets
2. Use IFERROR wrappers where division or zero-value lookups are possible
3. No INDIRECT, OFFSET, or volatile functions unless absolutely necessary
4. No array formulas (CSE) — use SUMIFS/COUNTIFS instead
5. Cross-sheet references use standard SheetName!Cell notation
6. Data validation dropdowns reference Settings tab value ranges
7. All formula cells marked with gray background at build stage
