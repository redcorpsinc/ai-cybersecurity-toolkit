# ✅ Dockerfile for Red Corps AI Sentinel Frontend
# Build Context: ./frontend (optimized for build cache)

# --- Build Stage ---
FROM node:23.11.0-slim AS builder

WORKDIR /app

# Install only dependencies first to enable caching
COPY package.json package-lock.json ./
RUN npm install --legacy-peer-deps

# Copy rest of the code
COPY . .
RUN npm run build

# --- Production Stage ---
FROM node:18-slim

WORKDIR /app

# Copy built app and install prod deps only
COPY --from=builder /app/.next .next
COPY --from=builder /app/public ./public
COPY --from=builder /app/package*.json ./

RUN npm install --omit=dev --legacy-peer-deps

ENV NODE_ENV=production
EXPOSE 3000

CMD ["npm", "start"]
