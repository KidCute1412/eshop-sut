@echo off
echo ===================================================
echo [EShop SUT] KHOI CHAY CAC SERVERS...
echo ===================================================

:: 1. Backend
if exist backend\node_modules goto check_db
echo [Backend] Khong tim thay node_modules. Dang chay npm install...
cd backend
call npm install
cd ..

:check_db
if exist backend\database.sqlite goto check_web
echo [Backend] Khoi tao co so du lieu ban dau (database.js)...
cd backend
node database.js
cd ..

:check_web
:: 2. Frontend Web
if exist frontend-web\node_modules goto check_admin
echo [Frontend Web] Khong tim thay node_modules. Dang chay npm install...
cd frontend-web
call npm install
cd ..

:check_admin
:: 3. Frontend Admin
if exist frontend-admin\node_modules goto check_mobile
echo [Frontend Admin] Khong tim thay node_modules. Dang chay npm install...
cd frontend-admin
call npm install
cd ..

:check_mobile
:: 4. Frontend Mobile
if exist frontend-mobile\node_modules goto launch
echo [Frontend Mobile] Khong tim thay node_modules. Dang chay npm install...
cd frontend-mobile
call npm install
cd ..

:launch
echo Dang khoi chay 4 servers trong 1 cua so Windows Terminal (Split 2x2 grid)...

wt -d "%~dp0backend" cmd /k "title Backend && node server.js" ";" split-pane -H -d "%~dp0frontend-admin" cmd /k "title Frontend Admin && npm run dev" ";" split-pane -V -d "%~dp0frontend-mobile" cmd /k "title Frontend Mobile && npm run start" ";" move-focus up ";" split-pane -V -d "%~dp0frontend-web" cmd /k "title Frontend Web && npm run dev"

if %ERRORLEVEL% NEQ 0 (
    echo Khong the mo Windows Terminal. Dang chuyen sang mo 4 cua so cmd rieng...
    start cmd /k "cd /d %~dp0backend && title Backend && node server.js"
    start cmd /k "cd /d %~dp0frontend-web && title Frontend Web && npm run dev"
    start cmd /k "cd /d %~dp0frontend-admin && title Frontend Admin && npm run dev"
    start cmd /k "cd /d %~dp0frontend-mobile && title Frontend Mobile && npm run start"
)

echo ===================================================
echo Hoan tat khoi chay!
echo ===================================================


