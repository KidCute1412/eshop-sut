@echo off
setlocal
cd /d "%~dp0"
docker compose down --volumes --remove-orphans
exit /b %ERRORLEVEL%
