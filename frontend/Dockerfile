FROM node:16-alpine 

WORKDIR /frontend

COPY . .

RUN npm ci

RUN npm run build

ENV NODE_ENV development

EXPOSE 3000

CMD ["npm", "start"]