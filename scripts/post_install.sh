#!/bin/bash

echo "🚀 Starting AI Cybersecurity Toolkit Environment Setup..."

# Update + core tools
sudo apt update && sudo apt upgrade -y
sudo apt install -y git curl unzip build-essential python3-pip python3-venv nmap nodejs npm docker.io docker-compose mongodb-org

# Python backend setup
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
cd ..

# Frontend setup
cd frontend
npm install
cd ..

# Create environment file
cp .env.template .env

# Docker permissions
sudo usermod -aG docker $USER

# MongoDB init
sudo systemctl start mongodb

echo "✅ Setup complete. Run with: docker-compose up --build"
