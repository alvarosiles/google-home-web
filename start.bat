@echo off
cd /d "%~dp0"

echo Verificando dependencias...
python -c "import flask, pychromecast, yt_dlp" 2>nul
if errorlevel 1 (
    echo Instalando dependencias faltantes...
    pip install flask pychromecast yt-dlp
)

echo.
echo Iniciando servidor en http://localhost:5000
echo Presiona CTRL+C para detener
echo.

python web_app.py
