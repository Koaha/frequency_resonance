@echo off
REM ── run_processing.bat ─────────────────────────────────────────────────────
REM Windows Task Scheduler wrapper for the signal processing pipeline.
REM
REM Usage:
REM   scripts\run_processing.bat                     (uses default config.yaml)
REM   scripts\run_processing.bat C:\path\to\cfg.yaml
REM
REM Task Scheduler setup:
REM   Program : C:\Python313\python.exe   (or path to your python)
REM   Arguments: D:\Workspace\frequency_resonance\src\main_processing.py
REM   Start in : D:\Workspace\frequency_resonance\src
REM
REM   Or just point "Program" at this .bat file.
REM ────────────────────────────────────────────────────────────────────────────

setlocal

set SCRIPT_DIR=%~dp0
set PROJECT_DIR=%SCRIPT_DIR%..
set SRC_DIR=%PROJECT_DIR%\src

if "%~1"=="" (
    set CONFIG=%PROJECT_DIR%\config.yaml
) else (
    set CONFIG=%~1
)

if not exist "%PROJECT_DIR%\output" mkdir "%PROJECT_DIR%\output"

echo ========================================
echo [%date% %time%] Starting processing
echo   Project : %PROJECT_DIR%
echo   Config  : %CONFIG%
echo ========================================

REM Activate venv if present
if exist "%PROJECT_DIR%\venv\Scripts\activate.bat" (
    call "%PROJECT_DIR%\venv\Scripts\activate.bat"
) else if exist "%PROJECT_DIR%\.venv\Scripts\activate.bat" (
    call "%PROJECT_DIR%\.venv\Scripts\activate.bat"
)

cd /d "%SRC_DIR%"
python main_processing.py --config "%CONFIG%"

set EXIT_CODE=%ERRORLEVEL%
echo [%date% %time%] Finished with exit code %EXIT_CODE%
exit /b %EXIT_CODE%
