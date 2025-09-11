FROM node:22.9.0
LABEL authors="A. Mhamdi"

EXPOSE ${MONGO_PORT} ${APP_PORT}

WORKDIR /app
COPY package*.json /app
RUN npm ci --only=production

CMD ["npm", "start"]