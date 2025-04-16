#!/bin/bash

# =============================
# RedCorps Sentinel Post-Install Script
# =============================
# Prepares environment for offline, Docker-based deployment
# - Loads .env
# - Installs requirements (optional)
# - Builds containers
# - Generates license (dev mode)

set -e

# ✅ Step 1: Check if .env exists
if [ ! -f .env ]; then
  echo "❌ .env file not found. Creating from template..."
  cp .env.template .env
  echo "✅ .env created. Please edit it with your keys before running Docker."
  exit 1
fi

# ✅ Step 2: Optional local virtualenv setup (if running CLI or backend manually)
if [ ! -d ".venv" ]; then
  echo "🔧 Creating Python virtual environment..."
  python3 -m venv .venv
fi

source .venv/bin/activate
pip install -r requirements.txt

# ✅ Step 3: Build Docker containers
echo "🐳 Building Docker containers..."
docker-compose build

# ✅ Step 4: Generate Dev License (Optional)
if [ ! -f ~/.ai-sec-cli/license.lic ]; then
  echo "🔐 Generating developer license..."
  python3 scripts/license_generator.py --generate-key
  python3 scripts/license_generator.py --create dev-user > ~/.ai-sec-cli/license.lic
  echo "✅ License saved to ~/.ai-sec-cli/license.lic"
fi

# ✅ Step 5: Start containers
echo "🚀 Launching RedCorps Sentinel..."
docker-compose up -d

echo "🎉 Setup complete! Access UI at http://localhost:3000"
echo "🔎 API Docs available at http://localhost:8000/docs"
echo "📄 Reports saved to backend/reports/output/"
echo "💡 CLI tool: python cli/cli.py --scan example.com"

exit 0

