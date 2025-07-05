#!/bin/bash
# Initial setup script for SafeText development

echo "🚀 Setting up SafeText development environment..."

# Make test scripts executable
chmod +x scripts/run_tests.sh

# Install uv if not already installed
if ! command -v uv &> /dev/null; then
    echo "📦 Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
else
    echo "✅ uv is already installed"
fi

# Install development dependencies
echo "📚 Installing dependencies..."
uv sync --extra dev

echo ""
echo "✨ Setup complete! You can now run tests with:"
echo "   ./scripts/run_tests.sh"
echo ""
echo "💡 Tip: Run './scripts/run_tests.sh help' to see all available options"