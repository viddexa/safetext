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

# Default to quick if no argument
MODE="${1:-quick}"

case $MODE in
    quick)
        echo "🚀 Running quick tests (parallel, excluding slow tests)..."
        uv run pytest -n auto -m "not slow" -v
        ;;
    
    full)
        echo "🔍 Running all tests (including slow tests)..."
        uv run pytest -n auto -v
        ;;
    
    coverage)
        echo "📊 Running tests with coverage..."
        uv run pytest -n auto --cov=safetext --cov-report=html --cov-report=term-missing
        echo "📁 Coverage report generated in htmlcov/"
        ;;
    
    single)
        echo "🔧 Running tests sequentially (no parallel execution)..."
        uv run pytest -v
        ;;
    
    lint)
        echo "🎨 Running linting checks..."
        echo "Checking with ruff..."
        if ! uv run ruff check .; then
            echo "❌ Ruff check failed! Run 'uv run ruff check --fix .' to fix issues."
            echo "📖 See contributing guidelines: https://github.com/safevideo/safetext/blob/main/CONTRIBUTING.md"
            exit 1
        fi
        
        echo "Checking formatting..."
        if ! uv run ruff format --check .; then
            echo "❌ Format check failed! Run 'uv run ruff format .' to fix formatting."
            echo "📖 See contributing guidelines: https://github.com/safevideo/safetext/blob/main/CONTRIBUTING.md"
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