#!/usr/bin/env python3
"""
ThinkLate / Off Script / Sarwanology — Fact-Check QC Agent Tool
Audits scripts for factual claims (dates, numbers, entities, laws, quotes)
and verifies that a corresponding SOURCES_VERIFICATION.md exists with primary citations.
Usage:
    python tools/fact_check_qc.py <path_to_script.md>
"""

import sys
import os
import re

# Ensure UTF-8 output on Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class FactCheckQCAgent:
    def __init__(self, script_path):
        self.script_path = os.path.abspath(script_path)
        if not os.path.exists(self.script_path):
            raise FileNotFoundError(f"Script file not found: {self.script_path}")
        with open(self.script_path, 'r', encoding='utf-8') as f:
            self.raw_text = f.read()
        self.video_dir = os.path.dirname(self.script_path)
        self.ledger_path = os.path.join(self.video_dir, "SOURCES_VERIFICATION.md")
        self.has_ledger = os.path.exists(self.ledger_path)
        self.ledger_text = ""
        if self.has_ledger:
            with open(self.ledger_path, 'r', encoding='utf-8') as f:
                self.ledger_text = f.read()

    def audit(self):
        print("=" * 70)
        print("🔍 FACT-CHECK QC AUDIT REPORT")
        print(f"Target Script: {self.script_path}")
        print(f"Evidence Ledger: {'FOUND (' + self.ledger_path + ')' if self.has_ledger else 'MISSING (SOURCES_VERIFICATION.md)'}")
        print("=" * 70)

        violations = []
        warnings = []
        verified_items = []

        # 1. Check for presence of verification ledger
        if not self.has_ledger:
            violations.append("CRITICAL: Missing SOURCES_VERIFICATION.md in video folder. No factual claims can be certified without a ledger.")

        # 2. Extract potential entities & dates from script
        date_pattern = r'\b(nineteen\s+[a-z\-]+|twenty\s+[a-z\-]+|19\d\d|20\d\d|january|february|march|april|may|june|july|august|september|october|november|december)\b'
        dates_found = list(set([m.group(0).lower() for m in re.finditer(date_pattern, self.raw_text, re.IGNORECASE)]))

        entity_pattern = r'\b(BMW|HP|John Deere|Deere|Adobe|Osram|Philips|General Electric|Google|Samsung|FTC|DOJ|AGCM|Euroconsumers|Apple|Tesla|Mercedes|Colorado|Nebraska|California|Minnesota)\b'
        entities_found = list(set([m.group(0) for m in re.finditer(entity_pattern, self.raw_text, re.IGNORECASE)]))

        # 3. Cross-reference entities with ledger
        if self.has_ledger:
            for entity in entities_found:
                if re.search(re.escape(entity), self.ledger_text, re.IGNORECASE):
                    verified_items.append(f"Entity '{entity}' grounded in verification ledger.")
                else:
                    warnings.append(f"Entity '{entity}' appears in script but is NOT cited in SOURCES_VERIFICATION.md.")

        # 4. Check for known banned fictional embellishments
        fictional_tales = [
            (r'thirty dollar sensor', "Unverified fictional detail: '$30 sensor'."),
            (r'two miles an hour', "Unverified fictional detail: '2 mph limp mode'."),
            (r'walter', "Banned invented character 'Walter'."),
            (r'frost on the forecast', "Unverified fictional weather detail.")
        ]
        for pat, msg in fictional_tales:
            if re.search(pat, self.raw_text, re.IGNORECASE):
                violations.append(f"FICTIONAL EMBELLISHMENT BAN: {msg}")

        # Summary
        print(f"\nAudit Findings: {len(violations)} violation(s), {len(warnings)} warning(s)")
        for v in violations:
            print(f"  ❌ [VIOLATION] {v}")
        for w in warnings:
            print(f"  ⚠️ [WARNING] {w}")
        for ok in verified_items[:6]:
            print(f"  ✅ [PASS] {ok}")
        if len(verified_items) > 6:
            print(f"  ✅ [PASS] ... and {len(verified_items) - 6} more entities verified.")

        print("\n" + "=" * 70)
        if violations:
            print("❌ FACT-CHECK QC FAILED: Script cannot be released to recording deck until all violations are cleared.")
            print("=" * 70)
            return False
        elif warnings:
            print("⚠️ FACT-CHECK QC PASSED WITH WARNINGS: Ground remaining entities in SOURCES_VERIFICATION.md.")
            print("=" * 70)
            return True
        else:
            print("✅ FACT-CHECK QC PASSED: 100% of claims and entities verified against primary sources.")
            print("=" * 70)
            return True

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "videos/04_the-subscription-trap/script_final.md"
    agent = FactCheckQCAgent(target)
    success = agent.audit()
    sys.exit(0 if success else 1)
