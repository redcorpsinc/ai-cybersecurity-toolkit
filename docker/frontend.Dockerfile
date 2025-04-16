# ✅ Dockerfile for Red Corps AI Sentinel Frontend
# Build Context: ./frontend (optimized for build cache)

# --- Build Stage ---
FROM node:23.11.0-slim AS builder

# Optional: manually install specific NPM version
RUN npm install -g npm@11.3.0

WORKDIR /app

# Copy and install dependencies
COPY package.json package-lock.json ./
RUN npm install --legacy-peer-deps

# Copy the rest of the app
COPY . .

# Build the frontend
RUN npm run build

# --- Serve Stage ---
FROM node:23.11.0-slim

# Optional: use same NPM version here as well
RUN npm install -g npm@11.3.0

WORKDIR /app

COPY --from=builder /app ./
RUN npm install --omit=dev

EXPOSE 3000
CMD ["npm", "start"]

