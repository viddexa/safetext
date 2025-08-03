<div align="center">
  <p>
    <a align="center" href="" target="_blank">
      <img
        width="1280"
        src="https://github.com/viddexa/safetext/assets/44926076/9af66dde-3a93-4c5b-b802-cb31dffcb2e5"
      >
    </a>
  </p>

[![Context7 MCP](https://img.shields.io/badge/Context7%20MCP-Indexed-blue)](https://context7.com/viddexa/safetext)
[![llms.txt](https://img.shields.io/badge/llms.txt-✓-brightgreen)](https://context7.com/viddexa/safetext/llms.txt)
[![version](https://badge.fury.io/py/safetext.svg)](https://badge.fury.io/py/safetext)
[![downloads](https://pepy.tech/badge/safetext)](https://pepy.tech/project/safetext)
[![license](https://img.shields.io/pypi/l/safetext)](LICENSE)

</div>

## 🤔 why safetext?

**Fast profanity detection and filtering for 13 languages.**

- **Multi-format Detection**: Single words, phrases, and contextual profanity
- **Custom Word Lists**: Extend built-in lists with your own profanity words
- **Whitelisting**: Exclude specific words from detection
- **Auto Language Detection**: From text or subtitle files
- **Precise Filtering**: Exact position tracking and custom censoring
- **Simple Integration**: One-line setup with clean API

## 📦 installation

easily install **safetext** with pip:

```bash
pip install safetext
```

for development setup, see our [scripts documentation](scripts/README.md).

## 🎯 quickstart

### check and censor profanity

```python
>>> from safetext import SafeText

>>> st = SafeText(language='en')

>>> results = st.check_profanity(text='Some text with <profanity-word>.')
>>> results
[{'word': '<profanity-word>', 'index': 4, 'start': 15, 'end': 31}]

>>> text = st.censor_profanity(text='Some text with <profanity-word>.')
>>> text
"Some text with ***."
```

### extending profanity lists with custom words

Add your own profanity words by providing a custom words directory:

```python
# Directory structure:
# custom_profanity_words/
# ├── en.txt              # English custom words
# ├── tr.txt              # Turkish custom words
# └── es.txt              # Spanish custom words

>>> st = SafeText(language='en', custom_words_dir='custom_profanity_words')

>>> # Custom words from en.txt are now included
>>> results = st.check_profanity('This mycustomword is inappropriate')
>>> results
[{'word': 'mycustomword', 'index': 2, 'start': 5, 'end': 17}]
```

Custom word files should contain one word/phrase per line:

```
# custom_profanity_words/en.txt
mycustomword
inappropriate phrase
company specific term
```

### using whitelist

exclude specific words from profanity detection:

```python
# Using a list of words
>>> st = SafeText(language='en', whitelist=['word1', 'word2'])

# Using a file (one word per line)
>>> st = SafeText(language='en', whitelist='path/to/whitelist.txt')

# Combining custom words with whitelist
>>> st = SafeText(
...     language='en', 
...     custom_words_dir='custom_profanity_words',
...     whitelist=['allowedcustomword']
... )
```

### automated language detection

- from text:

```python
>>> from safetext import SafeText

>>> eng_text = "This story is about to take a dark turn."

>>> st = SafeText(language=None)
>>> st.set_language_from_text(eng_text)

>>> st.language
'en'
```

- from .srt (subtitle) file:

```python
>>> from safetext import SafeText

>>> turkish_srt_file_path = "turkish.srt"

>>> st = SafeText(language=None)
>>> st.set_language_from_srt(turkish_srt_file_path)

>>> st.language
'tr'
```

## 🌍 supported languages

**safetext** currently supports profanity detection in 13 languages:

| Language | ISO 639-1 Code | Language Name |
|----------|----------------|---------------|
| 🇸🇦 | `ar` | Arabic |
| 🇦🇿 | `az` | Azerbaijani |
| 🇩🇪 | `de` | German |
| 🇬🇧 | `en` | English |
| 🇪🇸 | `es` | Spanish |
| 🇮🇷 | `fa` | Persian (Farsi) |
| 🇫🇷 | `fr` | French |
| 🇮🇳 | `hi` | Hindi |
| 🇯🇵 | `ja` | Japanese |
| 🇵🇹 | `pt` | Portuguese |
| 🇷🇺 | `ru` | Russian |
| 🇹🇷 | `tr` | Turkish |
| 🇨🇳 | `zh` | Chinese |

## 🤝 contribute to safetext

join our mission in refining content moderation!

contribute by:

- **adding new languages**: create a folder with the ISO 639-1 code and include a `words.txt`.
- **enhancing word lists**: improve detection accuracy.
- **sharing feedback**: your ideas can shape `safetext`.

see our [contributing guidelines](CONTRIBUTING.md) for development workflow, [test documentation](tests/README.md) for running tests, and [scripts guide](scripts/README.md) for automation tools.

______________________________________________________________________

## 🏆 contributors

meet our awesome contributors who make **safetext** better every day!

<p align="center">
    <a href="https://github.com/viddexa/safetext/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=viddexa/safetext" />
    </a>
</p>

______________________________________________________________________

<div align="center">
  <b>follow us for more!</b>
  <br><br>
  <a href="https://www.linkedin.com/company/viddexa/">LinkedIn</a> • 
  <a href="https://huggingface.co/viddexa">Hugging Face</a> • 
  <a href="https://x.com/viddexa">X</a>
</div>
