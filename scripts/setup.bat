@echo off
REM Initial setup script for SafeText development on Windows

echo 🚀 Setting up SafeText development environment...

REM Check if uv is installed
where uv >nul 2>nul
if %errorlevel% neq 0 (
    echo 📦 Installing uv...
    echo Please install uv from https://github.com/astral-sh/uv
    echo Or use: winget install --id=astral-sh.uv
    exit /b 1
) else (
    echo ✅ uv is already installed
)

REM Install development dependencies
echo 📚 Installing dependencies...
uv sync --extra dev

echo.
echo ✨ Setup complete! You can now run tests with:
echo    scripts\run_tests.bat
echo.
echo 💡 Tip: Run 'scripts\run_tests.bat help' to see all available options