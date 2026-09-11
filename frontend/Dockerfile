FROM node:18
WORKDIR /app

COPY . .

RUN npm install

RUN npm run build

CMD ["npx", "-y", "http-server", "-p", "8000", "/app/build"]
