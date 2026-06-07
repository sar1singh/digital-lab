"""
QA Runner -- Nivora Invoice Generator & Payment Tracker
Runs all 4 QA suites and reports aggregated results.
"""

import subprocess
import sys
import os
import re

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = [
    ("validate_workbook.py",       "Structural Validation"),
    ("test_workbook_formulas.py",  "Formula Unit Tests"),
    ("lint_google_sheets_compatibility.py", "GS Compatibility Lint"),
    ("test_workbook_layout.py",    "Layout / UI QA"),
]

python = sys.executable or "python"
exit_code = 0

print("=" * 60)
print("  NIVORA INVOICE GENERATOR & PAYMENT TRACKER")
print("  COMPREHENSIVE QA SUITE")
print("=" * 60)

for script, label in SCRIPTS:
    script_path = os.path.join(SCRIPTS_DIR, script)
    if not os.path.exists(script_path):
        print(f"\n  SKIP: {script} not found")
        continue

    print(f"\n--- [{label}] ---")

    result = subprocess.run(
        [python, script_path],
        capture_output=True,
        text=True,
        cwd=SCRIPTS_DIR,
    )

    output = result.stdout
    print(output)

    # Check if ALL ... PASSED is in output
    if "ALL" in output and "PASSED" in output:
        print(f"  >>> [{label}] PASSED <<<")
    else:
        print(f"  >>> [{label}] FAILED (check output above) <<<")
        exit_code = 1

print()
print("=" * 60)
if exit_code == 0:
    print("  ALL QA SUITES PASSED")
else:
    print("  SOME QA SUITES FAILED")
print("=" * 60)

sys.exit(exit_code)
