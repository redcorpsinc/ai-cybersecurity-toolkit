# ✅ Dockerfile for Red Corps AI Sentinel Backend
# Build Context: ./backend

FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies (WeasyPrint + recon tools)
RUN apt-get update && apt-get install -y \
    curl build-essential libffi-dev libssl-dev \
    libxml2-dev libxslt1-dev libjpeg-dev zlib1g-dev \
    libpangocairo-1.0-0 libpangoft2-1.0-0 \
    libgdk-pixbuf2.0-0 libcairo2 \
    && rm -rf /var/lib/apt/lists/*

# Copy backend source code and requirements file
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose API port
EXPOSE 8000

# Start FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
