<div align="center">
  <p>
    <a align="center" href="" target="_blank">
      <img
        width="1280"
        src="https://github.com/viddexa/safetext/assets/44926076/9af66dde-3a93-4c5b-b802-cb31dffcb2e5"
      >
    </a>
  </p>

[![version](https://badge.fury.io/py/safetext.svg)](https://badge.fury.io/py/safetext)
[![downloads](https://pepy.tech/badge/safetext)](https://pepy.tech/project/safetext)
[![license](https://img.shields.io/pypi/l/safetext)](LICENSE)

</div>

## 🤔 why safetext?

**Detect. Filter. Protect.**

- **Effortless Profanity Management**: Instantly identify and censor profanity with just one line of code.
- **Multilingual Capability**: Fluent in five languages, designed for easy expansion.
- **Optimized for Content Moderation**: Perfect for efficiently moderating and cleaning up text in various applications.
- **Automated**: Smart language detection for quick setup.

## 📦 installation

easily install **safetext** with pip:

```bash
pip install safetext
```

## 🎯 quickstart

### check and censor profanity

```python
>>> from safetext import SafeText

>>> st = SafeText(language='en')

>>> results = st.check_profanity(text='Some text with <profanity-word>.')
>>> results
{'word': '<profanity-word>', 'index': 4, 'start': 15, 'end': 31}

>>> text = st.censor_profanity(text='Some text with <profanity-word>.')
>>> text
"Some text with ***."
```

### using whitelist

exclude specific words from profanity detection:

```python
# Using a list of words
>>> st = SafeText(language='en', whitelist=['word1', 'word2'])

# Using a file (one word per line)
>>> st = SafeText(language='en', whitelist='path/to/whitelist.txt')
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

see our [contributing guidelines](CONTRIBUTING.md) for more.

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
