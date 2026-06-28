@echo off
echo ===================================================
echo [EShop SUT] KHOI CHAY CAC SERVERS...
echo ===================================================

:: Khoi chay Backend
echo Dang kiem tra va khoi chay Backend server...
if not exist backend\node_modules goto install_backend
goto check_db

:install_backend
echo [Backend] Khong tim thay node_modules. Dang chay npm install...
cd backend
call npm install
cd ..

:check_db
if not exist backend\database.sqlite goto init_db
goto start_backend

:init_db
echo [Backend] Khoi tao co so du lieu ban dau (database.js)...
cd backend
node database.js
cd ..

:start_backend
start cmd /k "cd backend && node server.js"


:: Khoi chay Frontend Web
echo Dang kiem tra va khoi chay Frontend Web (http://localhost:5173)...
if not exist frontend-web\node_modules goto install_web
goto start_web

:install_web
echo [Frontend Web] Khong tim thay node_modules. Dang chay npm install...
cd frontend-web
call npm install
cd ..

:start_web
start cmd /k "cd frontend-web && npm run dev"


:: Khoi chay Frontend Admin
echo Dang kiem tra va khoi chay Frontend Admin (http://localhost:5174)...
if not exist frontend-admin\node_modules goto install_admin
goto start_admin

:install_admin
echo [Frontend Admin] Khong tim thay node_modules. Dang chay npm install...
cd frontend-admin
call npm install
cd ..

:start_admin
start cmd /k "cd frontend-admin && npm run dev"

:: Khoi chay Frontend Mobile
echo Dang kiem tra va khoi chay Frontend Mobile...
if not exist frontend-mobile\node_modules goto install_mobile
goto start_mobile

:install_mobile
echo [Frontend Mobile] Khong tim thay node_modules. Dang chay npm install...
cd frontend-mobile
call npm install
cd ..

:start_mobile
start cmd /k "cd frontend-mobile && npm run start"


echo ===================================================
echo Tat ca servers da duoc mo trong cua so moi!
echo Bam ctrl+c hoac tat cua so cmd tuong ung de dung.
echo ===================================================
pause
