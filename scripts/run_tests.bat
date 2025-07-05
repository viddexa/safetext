@echo off
REM SafeText test runner for Windows

echo 🧪 SafeText Test Runner
echo ======================

REM Check if .venv exists
if not exist ".venv" (
    echo 📦 Virtual environment not found. Running uv sync...
    uv sync --extra dev
)

REM Activate virtual environment
call .venv\Scripts\activate

if "%1"=="" goto quick
if "%1"=="quick" goto quick
if "%1"=="full" goto full
if "%1"=="coverage" goto coverage
if "%1"=="single" goto single
if "%1"=="lint" goto lint
if "%1"=="all" goto all
if "%1"=="help" goto help
goto unknown

:quick
echo 🚀 Running quick tests (parallel, excluding slow tests)...
pytest -n auto -m "not slow" -v
goto end

:full
echo 🔍 Running all tests (including slow tests)...
pytest -n auto -v
goto end

:coverage
echo 📊 Running tests with coverage...
pytest -n auto --cov=safetext --cov-report=html --cov-report=term-missing
echo 📁 Coverage report generated in htmlcov/
goto end

:single
echo 🔧 Running tests sequentially (no parallel execution)...
pytest -v
goto end

:lint
echo 🎨 Running linting checks...
echo Checking with ruff...
ruff check .
if errorlevel 1 (
    echo ❌ Ruff check failed! Run 'ruff check --fix .' to fix issues.
    echo 📖 See contributing guidelines: https://github.com/safevideo/safetext/blob/main/CONTRIBUTING.md
    exit /b 1
)

echo Checking formatting...
ruff format --check .
if errorlevel 1 (
    echo ❌ Format check failed! Run 'ruff format .' to fix formatting.
    echo 📖 See contributing guidelines: https://github.com/safevideo/safetext/blob/main/CONTRIBUTING.md
    exit /b 1
)

echo ✅ All linting checks passed!
goto end

:all
echo 🏁 Running complete test suite...
call %0 lint
echo.
call %0 full
goto end

:help
echo Usage: scripts\run_tests.bat [option]
echo.
echo Options:
echo   quick     Run only fast tests in parallel
echo   full      Run all tests including slow ones
echo   coverage  Run with coverage report
echo   single    Run tests sequentially (no parallel)
echo   lint      Run linting checks only
echo   all       Run linting and all tests
echo   help      Show this help message
echo.
echo If no option provided, runs quick tests by default.
goto end

:unknown
echo ❌ Unknown option: %1
echo.
goto help

:end
echo.
echo ✨ Done!