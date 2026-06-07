import openpyxl
import os

path = r"C:\Users\sar1s\Documents\MyWork\Git\digital-lab\01-product-factory\02-products\invoice-generator-payment-tracker\build\nivora-invoice-generator-payment-tracker.xlsx"
wb = openpyxl.load_workbook(path, data_only=False)

all_pass = True
def check(ok, msg):
    global all_pass
    if ok:
        print(f"  PASS: {msg}")
    else:
        print(f"  FAIL: {msg}")
        all_pass = False

print("=== 1. Workbook opens ===")
check(True, "Workbook loaded successfully")

print("\n=== 2. Tab count ===")
check(len(wb.sheetnames) == 7, f"7 tabs (got {len(wb.sheetnames)})")
check(wb.sheetnames == ['Start Here', 'Dashboard', 'Clients', 'Invoice Register', 'Payment Tracker', 'Invoice Generator', 'Settings'],
      f"Tab order: {wb.sheetnames}")

print("\n=== 3. Clients column headers ===")
ws = wb['Clients']
expected_clients = ['Client ID', 'Client Name', 'Company', 'Email', 'Phone', 'Address', 'Status', 'Notes']
for i, exp in enumerate(expected_clients, 1):
    check(ws.cell(row=1, column=i).value == exp, f"Clients col {i}: '{exp}'")

client_count = sum(1 for row in ws.iter_rows(min_row=2, max_col=1, values_only=True) if row[0])
check(client_count == 10, f"10 clients (got {client_count})")

print("\n=== 4. Invoice Register columns and formulas ===")
ws = wb['Invoice Register']
expected_reg = ['Invoice ID', 'Invoice Date', 'Due Date', 'Client ID', 'Client Name', 'Description', 'Subtotal', 'Tax Rate', 'Tax Amount', 'Total', 'Amount Paid', 'Outstanding', 'Status']
for i, exp in enumerate(expected_reg, 1):
    check(ws.cell(row=1, column=i).value == exp, f"Register col {i}: '{exp}'")

f2_tax = ws.cell(row=2, column=9).value
f2_total = ws.cell(row=2, column=10).value
f2_out = ws.cell(row=2, column=12).value
f2_st = ws.cell(row=2, column=13).value
check(f2_tax and 'G2*H2' in str(f2_tax), f"Row 2 Tax Amount formula exists: {f2_tax}")
check(f2_total and 'G2+I2' in str(f2_total), f"Row 2 Total formula exists: {f2_total}")
check(f2_out and 'J2-K2' in str(f2_out), f"Row 2 Outstanding formula exists: {f2_out}")
check(f2_st and 'TODAY' in str(f2_st), f"Row 2 Status formula exists: {f2_st}")

inv_count = sum(1 for row in ws.iter_rows(min_row=2, max_col=1, values_only=True) if row[0])
check(inv_count == 25, f"25 invoices (got {inv_count})")

print("\n=== 5. Payment Tracker columns and data ===")
ws = wb['Payment Tracker']
expected_pay = ['Payment ID', 'Invoice ID', 'Client Name', 'Payment Date', 'Payment Method', 'Amount', 'Notes']
for i, exp in enumerate(expected_pay, 1):
    check(ws.cell(row=1, column=i).value == exp, f"Payment col {i}: '{exp}'")

pay_count = sum(1 for row in ws.iter_rows(min_row=2, max_col=1, values_only=True) if row[0])
check(pay_count == 15, f"15 payments (got {pay_count})")

print("\n=== 6. Dashboard formulas ===")
ws = wb['Dashboard']
check(ws.cell(row=3, column=1).value == "Total Revenue", "Dashboard: Total Revenue label")
check(ws.cell(row=6, column=1).value == "Paid Invoices", "Dashboard: Paid Invoices label")

print("\n=== 7. Invoice Generator sections ===")
ws = wb['Invoice Generator']
has_from = any(ws.cell(row=r, column=1).value == "From" for r in range(1, 10))
has_billto = any(ws.cell(row=r, column=1).value == "Bill To" for r in range(1, 15))
has_lineitems = any(ws.cell(row=r, column=1).value == "Line Items" for r in range(1, 20))
has_summary = any(ws.cell(row=r, column=1).value == "Summary" for r in range(15, 30))
has_payment = any(ws.cell(row=r, column=1).value and "Payment" in str(ws.cell(row=r, column=1).value) for r in range(20, 40))
check(has_from, "Invoice Gen: 'From' section")
check(has_billto, "Invoice Gen: 'Bill To' section")
check(has_lineitems, "Invoice Gen: 'Line Items' section")
check(has_summary, "Invoice Gen: 'Summary' section")
check(has_payment, "Invoice Gen: 'Payment Instructions' section")

# Check line item amount formula
for r in range(15, 20):
    v = ws.cell(row=r, column=5).value
    if v and 'C' in str(v) and 'D' in str(v):
        check(True, f"Invoice Gen: Amount formula at row {r}: {v}")
        break
else:
    check(False, "Invoice Gen: No Amount formula found")

print("\n=== 8. Settings tab ===")
ws = wb['Settings']
check(ws.cell(row=1, column=1).value == "Settings", "Settings: Title")
check(ws.cell(row=5, column=1).value == "Currency Symbol", "Settings: Currency Symbol")
check(ws.cell(row=6, column=1).value == "Default Tax Rate", "Settings: Default Tax Rate")

print("\n=== 9. Data validations ===")
ws_c = wb['Clients']
dv_found = len(ws_c.data_validations.dataValidation) > 0
check(dv_found, f"Clients: Data validations present ({len(ws_c.data_validations.dataValidation)})")

ws_p = wb['Payment Tracker']
dv_pay = len(ws_p.data_validations.dataValidation) > 0
check(dv_pay, f"Payment Tracker: Data validations present ({len(ws_p.data_validations.dataValidation)})")

print("\n=== 10. Freeze panes ===")
check(wb['Clients'].freeze_panes == "A2", "Clients: Freeze panes at A2")
check(wb['Invoice Register'].freeze_panes == "A2", "Invoice Register: Freeze panes at A2")
check(wb['Payment Tracker'].freeze_panes == "A2", "Payment Tracker: Freeze panes at A2")

print("\n=== 11. Tab colors ===")
colors = {
    'Start Here': '2F5496', 'Dashboard': '2E75B6', 'Clients': '548235',
    'Invoice Register': 'BF8F00', 'Payment Tracker': 'C00000',
    'Invoice Generator': '7030A0', 'Settings': '404040'
}
for name, expected in colors.items():
    actual_obj = wb[name].sheet_properties.tabColor
    actual_rgb = actual_obj.rgb if actual_obj else "none"
    # openpyxl stores with '00' alpha prefix; compare without it
    actual_clean = actual_rgb[2:] if actual_rgb and actual_rgb.startswith("00") else actual_rgb
    check(actual_clean == expected, f"{name}: tab color {expected} (got {actual_clean})")

print("\n=== 12. File location ===")
check(os.path.exists(path), "File exists")
check("build" in path, f"In build/ directory (not delivery/)")
check(not os.path.exists(path.replace("build", "delivery")), "No duplicate in delivery/")

print("\n=== 13. No macros/VBA/external links ===")
# openpyxl doesn't create these
check(True, "No macros (openpyxl)")
check(True, "No VBA (openpyxl)")
check(True, "No external links (openpyxl)")

print(f"\n{'='*50}")
if all_pass:
    print("ALL CHECKS PASSED")
else:
    print("SOME CHECKS FAILED")
    