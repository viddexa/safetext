# contributing to safetext 🚀

we're thrilled to have you contribute to **safetext**! your efforts help enhance a powerful tool for content moderation.

## how can I contribute? 🤝

### adding new languages 🌐

1. **create a folder**: make a new folder in the `languages` directory with the [ISO 639-1 code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes#) of the language (e.g., `fr` for French).
1. **add `words.txt`**: in this folder, add a `words.txt` file containing a list of profanity words/phrases, one per line.

### enhancing existing lists 🔍

- improve a language's `words.txt` by adding new words or refining the list by removing false positives.

### bug reports & suggestions 🐛

- use the [discussions](https://github.com/viddexa/safetext/discussions) section for bug reports, feature requests and any questions.
- share your feedback or suggestions to help us improve.

## development setup 🛠️

### using uv (recommended - fast!)

```bash
# quick setup
git clone https://github.com/safevideo/safetext.git
cd safetext

# Unix/Linux/macOS
./scripts/setup.sh            # installs uv and dependencies
./scripts/run_tests.sh        # run tests

# Windows
scripts\setup.bat             # checks uv and installs dependencies  
scripts\run_tests.bat         # run tests

# or manual setup (all platforms)
# install uv from https://github.com/astral-sh/uv
uv sync --extra dev

# run tests (after setup, the venv is activated automatically)
./scripts/run_tests.sh        # Unix/Linux/macOS  
scripts\run_tests.bat         # Windows

# or manually
source .venv/bin/activate     # Unix/Linux/macOS
# or
.venv\Scripts\activate        # Windows
pytest -n auto

# before committing - fix code style issues
ruff check --fix .
ruff format .

# if ruff fails, it will show you what needs to be fixed!

### important notes

- **always use `uv sync`**, never `uv pip install` for dependencies
- **always activate venv** before running python commands:
  ```bash
  source .venv/bin/activate  # Unix/Linux/macOS
  .venv\Scripts\activate     # Windows
  ```
- **never use `uv run pytest`**, use `pytest` after activating venv
```

### using pip (traditional)

```bash
# clone and setup
git clone https://github.com/safevideo/safetext.git
cd safetext

# create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# install
pip install -e ".[dev]"

# run tests with parallel execution
pytest -n auto

# before committing
ruff check --fix . && ruff format .
```

### troubleshooting

- **ruff errors**: If `ruff check` fails, read the error messages carefully. They tell you exactly what needs to be fixed. Run `ruff check --fix .` to automatically fix most issues.
- **formatting issues**: Run `ruff format .` to automatically format your code according to project standards.
- **test failures**: Run `pytest -v` for verbose output to see which tests are failing and why.

### test scripts

We provide convenient test scripts with different options:

```bash
# Unix/Linux/macOS
./scripts/run_tests.sh quick     # fast tests only (default)
./scripts/run_tests.sh full      # all tests including slow ones
./scripts/run_tests.sh coverage  # generate coverage report
./scripts/run_tests.sh lint      # run only linting checks
./scripts/run_tests.sh all       # linting + all tests

# Windows
scripts\run_tests.bat quick      # same options as above
scripts\run_tests.bat full
scripts\run_tests.bat coverage
scripts\run_tests.bat lint
scripts\run_tests.bat all
```

💡 **tip**: use `quick` during development for fast feedback, and `all` before committing!

## pull request process 📝

1. **fork the repo**: click 'Fork' on GitHub to copy the repository.
1. **create a branch**: make a branch in your fork, e.g., `add-spanish`.
1. **make changes**: update or add files.
1. **test your changes**: run `./scripts/run_tests.sh all` (or `scripts\run_tests.bat all` on Windows)
1. **commit**: commit your changes with a clear message.
1. **push**: upload your changes to your Github fork.
1. **open a PR**: go to the original `safetext` repository, click 'New Pull Request', pick your branch, then submit it with a clear description of your changes.

## license

Contributions are under the [MIT License](LICENSE).