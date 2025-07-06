# SafeText Scripts 🛠️

This directory contains convenience scripts for development setup and testing.

## 🚀 quick start

### unix/linux/macos
```bash
# initial setup (installs uv and dependencies)
./scripts/setup.sh

# run tests (various options available)
./scripts/run_tests.sh         # runs quick tests by default
./scripts/run_tests.sh help    # see all options
```

### windows
```batch
# initial setup (checks uv and installs dependencies)
scripts\setup.bat

# run tests (various options available)
scripts\run_tests.bat          # runs quick tests by default
scripts\run_tests.bat help     # see all options
```

## 📝 available scripts

### setup scripts
- **`setup.sh`** / **`setup.bat`**: One-time development environment setup
  - Installs/checks for uv package manager
  - Installs all development dependencies
  - Makes test scripts executable (Unix only)

### test runner scripts
- **`run_tests.sh`** / **`run_tests.bat`**: Flexible test execution with multiple modes

#### test modes

| mode | description | command |
|------|-------------|---------|
| **quick** | Fast parallel tests, excludes slow tests (default) | `./scripts/run_tests.sh quick` |
| **full** | All tests including performance tests | `./scripts/run_tests.sh full` |
| **coverage** | Generate coverage report in `htmlcov/` | `./scripts/run_tests.sh coverage` |
| **single** | Sequential execution (no parallelization) | `./scripts/run_tests.sh single` |
| **lint** | Run only linting checks (ruff) | `./scripts/run_tests.sh lint` |
| **all** | Complete suite: linting + all tests | `./scripts/run_tests.sh all` |

## 💡 tips

- **during development**: Use `quick` mode for rapid feedback
- **before committing**: Run `all` to ensure code quality
- **debugging failures**: Use `single` mode for clearer output
- **ci simulation**: Use `all` to replicate CI checks locally

## 🔧 troubleshooting

### "command not found" on unix/linux/macos
```bash
# make scripts executable
chmod +x scripts/*.sh
```

### uv not installed
- **unix/linux/macos**: The setup script will offer to install it
- **windows**: Install from https://github.com/astral-sh/uv or use `winget install --id=astral-sh.uv`

### virtual environment issues
```bash
# manually create/activate environment
uv sync --extra dev
source .venv/bin/activate  # unix/linux/macos
.venv\Scripts\activate     # windows
```

## 📚 see also

- [contributing guide](../CONTRIBUTING.md) - full development workflow
- [test documentation](../tests/README.md) - detailed testing information
- [ci configuration](../.github/workflows/ci.yml) - automated checks