#!/bin/bash

# Sales Brain - Setup Script
# Creates Python virtual environment and installs dependencies

set -e  # Exit on error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "🧠 Sales Brain Setup"
echo "===================="

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Creating Python virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip --quiet

# Install requirements
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Optional: Chrome TLS impersonation to bypass bot protections (script will auto-install on first run if missing)
if pip install curl_cffi --quiet; then
    echo "✅ Optional: curl_cffi installed (Chrome impersonation)"
else
    echo "⏭️  Optional curl_cffi skipped (script will install when needed)"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "To activate the environment, run:"
echo "  source venv/bin/activate   # or: source prepare.sh"
echo ""
echo "To run the scraper (use -d brains/<company>/ so logs and context stay in company dir):"
echo "  python .cursor/rules/sales-brain/scripts/scrape.py scrape <url> -d brains/<company>/"
echo ""
echo "Note: The scrape script auto-installs missing dependencies (requests, beautifulsoup4,"
echo "      and optionally curl_cffi) if you run it without activating the venv."
