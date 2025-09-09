FROM node:22.9.0
LABEL authors="mhamdi"

EXPOSE 27017 3000

WORKDIR /app
COPY package*.json /app
RUN npm ci --only=production

CMD ["npm", "start"]