FROM node:22-alpine

WORKDIR /lab

COPY portable/package*.json ./
RUN npm ci --ignore-scripts --no-audit --no-fund

COPY portable/src ./portable/src
COPY portable/scripts ./portable/scripts
COPY db-tests.test.js ./

CMD ["node", "portable/scripts/run-tests.mjs"]
