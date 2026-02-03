#!/bin/bash

# Sales Brain - Activate Virtual Environment
# Usage: source prepare.sh   (or run ./prepare.sh)
#
# Optional: The scrape script auto-installs missing deps (requests, beautifulsoup4,
# curl_cffi) when run, so you can run it without activating the venv.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ ! -d "$SCRIPT_DIR/venv" ]; then
    echo "❌ Virtual environment not found. Run ./setup.sh first."
    return 1 2>/dev/null || exit 1
fi

source "$SCRIPT_DIR/venv/bin/activate"
echo "✅ Virtual environment activated"
