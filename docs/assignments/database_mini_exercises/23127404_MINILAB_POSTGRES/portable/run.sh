#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")"

docker info >/dev/null
mkdir -p evidence
docker compose down --volumes --remove-orphans
docker compose build test mcp
docker compose up --detach --wait postgres

set +e
docker compose run --rm -T test >evidence/test-run.log 2>&1
test_exit=$?
set -e
cat evidence/test-run.log

docker compose exec -T postgres \
  psql -X -U lab_admin -d eshop_minilab -f /submission/performance.sql \
  >evidence/performance.log 2>&1
cat evidence/performance.log

if [ "$test_exit" -ne 0 ]; then
  echo "Test classification failed; inspect evidence/." >&2
  exit "$test_exit"
fi

echo "Mini lab completed. PostgreSQL remains running for MCP inspection."
