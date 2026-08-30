#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
TARGET = ROOT / "Nova.py"

if not TARGET.exists():
    raise SystemExit(f"Không tìm thấy tệp: {TARGET}")

raise SystemExit(subprocess.call([sys.executable, str(TARGET)], cwd=ROOT))
