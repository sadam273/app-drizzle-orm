FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

RUN apk add --no-cache netcat-openbsd   # ← tambahin ini

EXPOSE 3000

CMD ["sh", "-c", "until nc -z db 5432; do echo 'waiting db...'; sleep 2; done; npm run db:migrate && node dist/index.js"]