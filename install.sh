#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
PYTHON="${PYTHON:-python3}"
"$PYTHON" -m pip install --upgrade pip
"$PYTHON" -m pip install -r requirements.txt
echo "Installed. Run: ./run.sh"
