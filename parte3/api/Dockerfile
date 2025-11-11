# Etapa 1: dependencias
FROM node:18-alpine AS build
WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm ci --omit=dev || npm install --omit=dev
COPY server.js .

# Etapa 2: runtime
FROM node:18-alpine
WORKDIR /app
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/server.js ./server.js
EXPOSE 3000
CMD ["node", "server.js"]
