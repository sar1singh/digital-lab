#!/usr/bin/env python3
"""
ThinkLate Motion Graphics CLI Bridge (Forwarding Shim)
======================================================
Forwarding shim ensuring 100% backward compatibility for Video 05 and existing scripts.
Directs all render requests to the centralized shared engine at:
digital-lab/03-content-lab/shared/tools/render_motion.py
"""

import os
import sys
import subprocess

SHARED_TOOL = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "shared", "tools", "render_motion.py"
))

if __name__ == "__main__":
    if os.path.exists(SHARED_TOOL):
        cmd = [sys.executable, SHARED_TOOL] + sys.argv[1:]
        res = subprocess.run(cmd)
        sys.exit(res.returncode)
    else:
        print(f"Error: Shared motion tool not found at {SHARED_TOOL}")
        sys.exit(1)
