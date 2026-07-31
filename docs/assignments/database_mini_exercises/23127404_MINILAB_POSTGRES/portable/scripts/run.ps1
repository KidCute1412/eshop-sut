$ErrorActionPreference = "Stop"
$labRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $labRoot

Write-Host "Checking Docker Engine..."
docker info *> $null
if ($LASTEXITCODE -ne 0) {
    throw "Docker Engine is not running. Open Docker Desktop, wait until it is ready, then run run.bat again."
}

New-Item -ItemType Directory -Force -Path "evidence" | Out-Null

Write-Host "Resetting the isolated mini-lab database..."
docker compose down --volumes --remove-orphans
if ($LASTEXITCODE -ne 0) { throw "Could not reset the mini-lab containers." }

Write-Host "Building the test and MCP images..."
docker compose build test mcp
if ($LASTEXITCODE -ne 0) { throw "Docker image build failed." }

Write-Host "Starting PostgreSQL and waiting for its healthcheck..."
docker compose up --detach --wait postgres
if ($LASTEXITCODE -ne 0) { throw "PostgreSQL did not become healthy." }

Write-Host "Running Jest and classifying expected defects..."
cmd.exe /d /c "docker compose run --rm -T test > evidence\test-run.log 2>&1"
$testExit = $LASTEXITCODE
Get-Content -LiteralPath "evidence\test-run.log"

Write-Host "Capturing EXPLAIN ANALYZE before and after the index..."
cmd.exe /d /c "docker compose exec -T postgres psql -X -U lab_admin -d eshop_minilab -f /submission/performance.sql > evidence\performance.log 2>&1"
$performanceExit = $LASTEXITCODE
Get-Content -LiteralPath "evidence\performance.log"

if ($testExit -ne 0) {
    throw "Test classification failed. Review evidence\test-run.log and evidence\test-results.json."
}
if ($performanceExit -ne 0) {
    throw "Performance analysis failed. Review evidence\performance.log."
}

Write-Host ""
Write-Host "Mini lab completed successfully."
Write-Host "PostgreSQL remains running so Codex can connect through the project MCP config."
Write-Host "Evidence: $labRoot\evidence"
