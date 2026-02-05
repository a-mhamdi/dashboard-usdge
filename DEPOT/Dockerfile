FROM node:22.9.0
LABEL authors="A. Mhamdi"

ENV TZ="Africa/Tunis"

WORKDIR /app
COPY package*.json /app
RUN npm ci

COPY . .

RUN npm run build:prod

RUN chmod +x ./dev-to-prod.sh && ./dev-to-prod.sh

CMD ["node", "./src/server.mjs"]
