# ✅ Dockerfile for Red Corps AI Sentinel Backend
# Build Context: ./backend

FROM python:3.11-slim

WORKDIR /app

# 🔧 System libs for WeasyPrint, recon, etc.
RUN apt-get update && apt-get install -y \
    build-essential libffi-dev libssl-dev \
    libxml2 libxslt1.1 libjpeg-dev zlib1g-dev \
    libpangocairo-1.0-0 libpangoft2-1.0-0 libgdk-pixbuf2.0-0 libcairo2 \
    && rm -rf /var/lib/apt/lists/*

# ✅ Upgrade pip to latest stable
RUN pip install --upgrade pip==25.0.1

# Copy backend code + install deps
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

