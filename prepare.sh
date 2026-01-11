#!/bin/bash

# Sales Brain - Activate Virtual Environment
# Usage: source prepare.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ ! -d "$SCRIPT_DIR/venv" ]; then
    echo "❌ Virtual environment not found. Run ./setup.sh first."
    return 1 2>/dev/null || exit 1
fi

source "$SCRIPT_DIR/venv/bin/activate"
echo "✅ Virtual environment activated"
