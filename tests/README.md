# SafeText Tests 🧪

This directory contains the test suite for SafeText, organized for efficiency and clarity.

## 🚀 running tests

### quick start (using uv)

```bash
# first time setup
uv sync --extra dev

# activate virtual environment
source .venv/bin/activate  # unix/linux/macos
# or
.venv\Scripts\activate      # windows

# run all tests in parallel
pytest -n auto

# run only fast tests (skip slow/performance tests)
pytest -m "not slow"

# run specific test file
pytest tests/test_basic.py

# run with coverage
pytest --cov=safetext --cov-report=html
```

💡 **tip**: Use the [convenient test scripts](../scripts/README.md) for easier test execution!

## 📁 test organization

| file | description |
|------|-------------|
| **`test_basic.py`** | Core functionality tests (initialization, detection, censoring) |
| **`test_advanced.py`** | Advanced features (whitelist files, edge cases, phrases) |
| **`test_performance.py`** | Performance and scaling tests (marked as `@pytest.mark.slow`) |
| **`conftest.py`** | Shared fixtures and test configuration |

## ✨ test features

1. **parallel execution**: Tests run in parallel using `pytest-xdist` for faster execution
2. **dry principle**: Common test data and fixtures are shared via `conftest.py`
3. **parametrized tests**: Extensive use of `@pytest.mark.parametrize` to test multiple scenarios efficiently
4. **performance tests**: Separate slow tests that can be skipped during quick test runs

## 💡 tips

| command | description |
|---------|-------------|
| `-n auto` | Run tests in parallel (automatically detects CPU cores) |
| `-m "not slow"` | Skip performance tests during development |
| `-v` | Verbose output when debugging test failures |
| `--lf` | Run only the last failed tests |
| `-k "test_name"` | Run specific tests by name pattern |

## 📚 see also

- [development scripts](../scripts/README.md) - convenient test runners
- [contributing guide](../CONTRIBUTING.md) - complete development workflow