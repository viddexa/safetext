#!/bin/bash
# SafeText test runner with different options

set -e

echo "🧪 SafeText Test Runner"
echo "======================"

# Function to display help
show_help() {
    echo "Usage: ./scripts/run_tests.sh [option]"
    echo ""
    echo "Options:"
    echo "  quick     Run only fast tests in parallel"
    echo "  full      Run all tests including slow ones"
    echo "  coverage  Run with coverage report"
    echo "  single    Run tests sequentially (no parallel)"
    echo "  lint      Run linting checks only"
    echo "  all       Run linting and all tests"
    echo "  help      Show this help message"
    echo ""
    echo "If no option provided, runs quick tests by default."
}

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ Error: uv is not installed. Please install it first:"
    echo "   curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# Ensure dependencies are installed
if [ ! -d ".venv" ]; then
    echo "📦 Virtual environment not found. Running uv sync..."
    uv sync --extra dev
fi

# Activate virtual environment
source .venv/bin/activate

# Default to quick if no argument
MODE="${1:-quick}"

case $MODE in
    quick)
        echo "🚀 Running quick tests (parallel, excluding slow tests)..."
        pytest -n auto -m "not slow" -v
        ;;
    
    full)
        echo "🔍 Running all tests (including slow tests)..."
        pytest -n auto -v
        ;;
    
    coverage)
        echo "📊 Running tests with coverage..."
        pytest -n auto --cov=safetext --cov-report=html --cov-report=term-missing
        echo "📁 Coverage report generated in htmlcov/"
        ;;
    
    single)
        echo "🔧 Running tests sequentially (no parallel execution)..."
        pytest -v
        ;;
    
    lint)
        echo "🎨 Running linting checks..."
        echo "Checking with ruff..."
        if ! ruff check .; then
            echo "❌ Ruff check failed! Run 'ruff check --fix .' to fix issues."
            echo "📖 See contributing guidelines: https://github.com/viddexa/safetext/blob/main/CONTRIBUTING.md"
            exit 1
        fi
        
        echo "Checking formatting..."
        if ! ruff format --check .; then
            echo "❌ Format check failed! Run 'ruff format .' to fix formatting."
            echo "📖 See contributing guidelines: https://github.com/viddexa/safetext/blob/main/CONTRIBUTING.md"
            exit 1
        fi
        
        echo "✅ All linting checks passed!"
        ;;
    
    all)
        echo "🏁 Running complete test suite..."
        $0 lint
        echo ""
        $0 full
        ;;
    
    help|--help|-h)
        show_help
        ;;
    
    *)
        echo "❌ Unknown option: $MODE"
        echo ""
        show_help
        exit 1
        ;;
esac

echo ""
echo "✨ Done!"