@echo off
echo ===================================================
echo   AI CRM HCP Interaction Logging Module
echo   Starting the Application...
echo ===================================================

echo.
echo [1/2] Starting the Python Backend Server...
start "Backend API Server" cmd /k "cd backend && python -m uvicorn main:app --reload"

echo.
echo [2/2] Starting the React Frontend Server...
start "Frontend UI Server" cmd /k "cd frontend && npm start"

echo.
echo Both servers have been launched in separate windows!
echo Please wait a moment for the frontend to compile and open in your browser.
echo.
echo If the browser does not open automatically, go to: http://localhost:3000
echo.
pause
