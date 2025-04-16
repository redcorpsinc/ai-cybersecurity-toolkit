# 🔧 Build Stage
FROM python:3.11-slim AS base

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl build-essential libffi-dev libssl-dev \
    libxml2-dev libxslt1-dev libjpeg-dev zlib1g-dev \
    libpangocairo-1.0-0 libpangoft2-1.0-0 libgdk-pixbuf2.0-0 libcairo2 \
    && rm -rf /var/lib/apt/lists/*

COPY backend/ ./backend/
COPY reports/ ./reports/
COPY config.py ./backend/config.py
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# ✅ Production CMD
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
