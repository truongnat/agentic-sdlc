#!/bin/bash
# Unix shell wrapper for agent scripts

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$SCRIPT_DIR/run.py" "$@"
