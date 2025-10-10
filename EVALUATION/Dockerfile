FROM node:22.9.0
LABEL authors="A. Mhamdi"

ENV TZ="Africa/Tunis"

WORKDIR /app
COPY package*.json /app
RUN npm ci --only=production

CMD ["node", "./src/server.mjs"]