"""Tests for custom words directory functionality."""

import os
import tempfile

import pytest

from safetext import SafeText


class TestCustomWordsDirectory:
    """Test custom profanity words directory functionality."""

    def test_custom_words_extension(self):
        """Test extending profanity list with custom words directory."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create custom English profanity file
            custom_en_file = os.path.join(temp_dir, "en.txt")
            with open(custom_en_file, "w", encoding="utf-8") as f:
                f.write("mycustomword\n")
                f.write("anotherbadword\n")

            # Initialize SafeText with custom words directory
            st = SafeText("en", custom_words_dir=temp_dir)

            # Test that custom words are detected
            result = st.check_profanity("This mycustomword is bad")
            assert len(result) > 0
            assert any(r["word"] == "mycustomword" for r in result)

            # Test censoring of custom words
            censored = st.censor_profanity("This mycustomword is bad")
            assert "************" in censored

    def test_custom_words_with_builtin(self):
        """Test that custom words are combined with built-in words."""
        with tempfile.TemporaryDirectory() as temp_dir:
            custom_en_file = os.path.join(temp_dir, "en.txt")
            with open(custom_en_file, "w", encoding="utf-8") as f:
                f.write("customword\n")

            st = SafeText("en", custom_words_dir=temp_dir)

            # Should detect both built-in and custom words
            result = st.check_profanity("This shit and customword are bad")
            words = [r["word"] for r in result]
            assert "shit" in words  # Built-in word
            assert "customword" in words  # Custom word

    def test_custom_words_nonexistent_file(self):
        """Test behavior when custom words file doesn't exist for language."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # No custom file for English
            st = SafeText("en", custom_words_dir=temp_dir)

            # Should still work with built-in words only
            result = st.check_profanity("This is shit")
            assert len(result) > 0

    def test_custom_words_directory_none(self):
        """Test that None custom_words_dir works normally."""
        st = SafeText("en", custom_words_dir=None)
        result = st.check_profanity("This is shit")
        assert len(result) > 0

    def test_custom_words_with_whitelist(self):
        """Test custom words combined with whitelist functionality."""
        with tempfile.TemporaryDirectory() as temp_dir:
            custom_en_file = os.path.join(temp_dir, "en.txt")
            with open(custom_en_file, "w", encoding="utf-8") as f:
                f.write("customword\n")
                f.write("allowedword\n")

            # Whitelist one of the custom words
            st = SafeText("en", custom_words_dir=temp_dir, whitelist=["allowedword"])

            # Should detect customword but not allowedword
            result = st.check_profanity("Both customword and allowedword here")
            words = [r["word"] for r in result]
            assert "customword" in words
            assert "allowedword" not in words

    def test_custom_words_phrases(self):
        """Test custom multi-word phrases."""
        with tempfile.TemporaryDirectory() as temp_dir:
            custom_en_file = os.path.join(temp_dir, "en.txt")
            with open(custom_en_file, "w", encoding="utf-8") as f:
                f.write("bad phrase\n")
                f.write("terrible words\n")

            st = SafeText("en", custom_words_dir=temp_dir)

            # Test phrase detection
            result = st.check_profanity("This bad phrase is not allowed")
            assert len(result) > 0
            assert any(r["word"] == "bad phrase" for r in result)

    def test_multiple_languages_custom(self):
        """Test custom words for multiple languages."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create custom files for multiple languages
            with open(os.path.join(temp_dir, "en.txt"), "w", encoding="utf-8") as f:
                f.write("englishcustom\n")

            with open(os.path.join(temp_dir, "tr.txt"), "w", encoding="utf-8") as f:
                f.write("turkishcustom\n")

            # Test English
            st_en = SafeText("en", custom_words_dir=temp_dir)
            result = st_en.check_profanity("This englishcustom word")
            assert any(r["word"] == "englishcustom" for r in result)

            # Test Turkish
            st_tr = SafeText("tr", custom_words_dir=temp_dir)
            result = st_tr.check_profanity("Bu turkishcustom kelime")
            assert any(r["word"] == "turkishcustom" for r in result)
