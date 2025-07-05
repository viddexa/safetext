# SafeText Tests

This directory contains the test suite for SafeText, organized for efficiency and clarity.

## Running Tests

### Quick Start (using uv)

```bash
# First time setup
uv sync --extra dev

# Activate virtual environment
source .venv/bin/activate  # Unix/Linux/macOS
# or
.venv\Scripts\activate      # Windows

# Run all tests in parallel
pytest -n auto

# Run only fast tests (skip slow/performance tests)
pytest -m "not slow"

# Run specific test file
pytest tests/test_basic.py

# Run with coverage
pytest --cov=safetext --cov-report=html
```

### Test Organization

- **`test_basic.py`**: Core functionality tests (initialization, detection, censoring)
- **`test_advanced.py`**: Advanced features (whitelist files, edge cases, phrases)
- **`test_performance.py`**: Performance and scaling tests (marked as `@pytest.mark.slow`)
- **`conftest.py`**: Shared fixtures and test configuration

### Test Features

1. **Parallel Execution**: Tests run in parallel using `pytest-xdist` for faster execution
2. **DRY Principle**: Common test data and fixtures are shared via `conftest.py`
3. **Parametrized Tests**: Extensive use of `@pytest.mark.parametrize` to test multiple scenarios efficiently
4. **Performance Tests**: Separate slow tests that can be skipped during quick test runs

### Tips

- Use `-n auto` to run tests in parallel (automatically detects CPU cores)
- Use `-m "not slow"` to skip performance tests during development
- Use `-v` for verbose output when debugging test failures
- Use `--lf` to run only the last failed tests
- Use `-k "test_name"` to run specific tests by name pattern