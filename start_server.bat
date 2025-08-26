@echo off
echo.
echo ========================================
echo       🚀 INICIANDO SERVIDOR WEB
echo ========================================
echo.

cd /d "%~dp0"

echo 📁 Directorio actual: %cd%
echo 🐍 Iniciando servidor Python...
echo.

python server.py

pause
