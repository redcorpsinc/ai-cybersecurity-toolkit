# 📦 Build Stage
FROM node:18-alpine AS builder

WORKDIR /app

COPY frontend/package*.json ./
RUN npm install

COPY frontend/ ./
RUN npm run build

# 🧾 Serve with lightweight web server
FROM node:18-alpine

WORKDIR /app
COPY --from=builder /app/.next .next
COPY --from=builder /app/public ./public
COPY --from=builder /app/package*.json ./

RUN npm install --omit=dev
ENV NODE_ENV=production

EXPOSE 3000
CMD ["npm", "start"]
