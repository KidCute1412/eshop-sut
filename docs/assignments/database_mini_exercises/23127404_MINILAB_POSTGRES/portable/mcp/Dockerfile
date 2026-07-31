FROM node:22-alpine

RUN npm install --global --ignore-scripts --no-audit --no-fund \
    @modelcontextprotocol/server-postgres@0.6.2

ENTRYPOINT ["mcp-server-postgres"]
