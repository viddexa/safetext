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
# install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# clone and setup
git clone https://github.com/viddexa/safetext.git
cd safetext
uv venv --python 3.10  # or use your preferred Python version

# activate environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

uv sync --extra dev 

# before committing
ruff check --fix . && ruff format .
pytest
```

### using pip (traditional)

```bash
# clone and install
git clone https://github.com/viddexa/safetext.git
cd safetext
pip install -e ".[dev]"

# before committing
ruff check --fix . && ruff format .
pytest
```

## pull request process 📝

1. **fork the repo**: click 'Fork' on GitHub to copy the repository.
1. **create a branch**: make a branch in your fork, e.g., `add-spanish`.
1. **make changes**: update or add files.
1. **format code**: run `ruff check --fix . && ruff format .`
1. **commit**: commit your changes with a clear message.
1. **push**: upload your changes to your Github fork.
1. **open a PR**: go to the original `safetext` repository, click 'New Pull Request', pick your branch, then submit it with a clear description of your changes.

## license

Contributions are under the [MIT License](LICENSE).