@echo off
REM ── run_processing.bat ─────────────────────────────────────────────────────
REM Windows Task Scheduler wrapper for the signal processing pipeline.
REM
REM Usage:
REM   scripts\run_processing.bat                                 (all patients)
REM   scripts\run_processing.bat --max-patients 10               (first 10)
REM   scripts\run_processing.bat --config C:\cfg.yaml --max-patients 5
REM
REM Task Scheduler setup:
REM   Program : C:\Python313\python.exe   (or path to your python)
REM   Arguments: D:\Workspace\frequency_resonance\src\main_processing.py
REM   Start in : D:\Workspace\frequency_resonance\src
REM
REM   Or just point "Program" at this .bat file.
REM ────────────────────────────────────────────────────────────────────────────

setlocal enabledelayedexpansion

set SCRIPT_DIR=%~dp0
set PROJECT_DIR=%SCRIPT_DIR%..
set SRC_DIR=%PROJECT_DIR%\src
set CONFIG=%PROJECT_DIR%\config.yaml
set MAX_PATIENTS=0
set EXTRA_ARGS=

REM ── parse named arguments ──────────────────────────────────────────────────
:parse_args
if "%~1"=="" goto done_args
if /i "%~1"=="--config" (
    set CONFIG=%~2
    shift & shift
    goto parse_args
)
if /i "%~1"=="--max-patients" (
    set MAX_PATIENTS=%~2
    shift & shift
    goto parse_args
)
set EXTRA_ARGS=!EXTRA_ARGS! %1
shift
goto parse_args
:done_args

if not exist "%PROJECT_DIR%\output" mkdir "%PROJECT_DIR%\output"

echo ========================================
echo [%date% %time%] Starting processing
echo   Project      : %PROJECT_DIR%
echo   Config       : %CONFIG%
echo   Max patients : %MAX_PATIENTS%
echo ========================================

REM Activate venv if present
if exist "%PROJECT_DIR%\venv\Scripts\activate.bat" (
    call "%PROJECT_DIR%\venv\Scripts\activate.bat"
) else if exist "%PROJECT_DIR%\.venv\Scripts\activate.bat" (
    call "%PROJECT_DIR%\.venv\Scripts\activate.bat"
)

cd /d "%SRC_DIR%"

set CMD=python main_processing.py --config "%CONFIG%"
if %MAX_PATIENTS% GTR 0 set CMD=%CMD% --max-patients %MAX_PATIENTS%
if defined EXTRA_ARGS set CMD=%CMD% %EXTRA_ARGS%

%CMD%

set EXIT_CODE=%ERRORLEVEL%
echo [%date% %time%] Finished with exit code %EXIT_CODE%
exit /b %EXIT_CODE%
