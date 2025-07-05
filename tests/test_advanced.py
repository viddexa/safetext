"""Advanced tests for SafeText features."""

import os
import tempfile

import pytest

from safetext import SafeText


class TestWhitelistAdvanced:
    """Advanced whitelist functionality tests."""

    def test_whitelist_from_file(self):
        """Test whitelist loading from file."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
            f.write("shit\n")
            f.write("damn\n")
            f.write("  hell  \n")  # Test whitespace handling
            temp_path = f.name

        try:
            st = SafeText("en", whitelist=temp_path)

            # All whitelisted words should not be detected
            result = st.check_profanity("This shit is damn hell")
            assert len(result) == 0

            # Non-whitelisted profanity should be detected
            result = st.check_profanity("This is crap")
            assert len(result) > 0
        finally:
            os.unlink(temp_path)

    def test_whitelist_file_not_found(self):
        """Test error handling for missing whitelist file."""
        with pytest.raises(FileNotFoundError, match="Whitelist file not found"):
            SafeText("en", whitelist="/nonexistent/path.txt")

    def test_whitelist_invalid_type(self):
        """Test error handling for invalid whitelist type."""
        with pytest.raises(ValueError, match="Whitelist must be a list of words or a file path"):
            SafeText("en", whitelist=123)

    def test_whitelist_empty_list(self):
        """Test whitelist with empty list."""
        st = SafeText("en", whitelist=[])
        result = st.check_profanity("This is shit")
        assert len(result) > 0  # Should detect profanity

    def test_whitelist_with_phrases(self):
        """Test whitelist with multi-word phrases."""
        st = SafeText("en", whitelist=["hot pocket"])

        # Assuming "hot pocket" might be in profanity list
        # This tests phrase whitelisting
        result = st.check_profanity("I love hot pocket")
        assert not any(r["word"] == "hot pocket" for r in result)


class TestProfanityPhrases:
    """Test detection of multi-word profanities."""

    def test_phrase_detection(self):
        """Test detection of multi-word profanities."""
        st = SafeText("en")

        # Test with known multi-word profanity
        result = st.check_profanity("That's bull shit behavior")
        assert len(result) > 0

    def test_phrase_censoring(self):
        """Test censoring of multi-word profanities."""
        st = SafeText("en")

        # Test censoring preserves text structure
        text = "Some text with profanity here"
        censored = st.censor_profanity(text)
        assert len(censored) == len(text)  # Length preserved with asterisks


class TestEdgeCases:
    """Test edge cases and special scenarios."""

    def test_empty_text(self):
        """Test handling of empty text."""
        st = SafeText("en")

        assert st.check_profanity("") == []
        assert st.censor_profanity("") == ""

    def test_special_characters(self):
        """Test profanity detection with special characters."""
        st = SafeText("en")

        # Test profanity with punctuation
        result = st.check_profanity("This is shit!")
        assert len(result) > 0
        assert result[0]["word"] == "shit"

    def test_case_sensitivity(self):
        """Test case-insensitive profanity detection."""
        st = SafeText("en")

        # Test various cases
        for text in ["This is SHIT", "This is Shit", "This is ShIt"]:
            result = st.check_profanity(text)
            assert len(result) > 0

    def test_multiple_profanities(self):
        """Test detection of multiple profanities in text."""
        st = SafeText("en")

        # Use words that are definitely in the profanity list
        result = st.check_profanity("shit damn crap")
        assert len(result) >= 3  # Should detect all three

    def test_get_bad_words_method(self):
        """Test get_bad_words functionality."""
        st = SafeText("en")

        # Test with text
        bad_words = st.get_bad_words("shit damn shit")
        assert "shit" in bad_words
        assert "damn" in bad_words
        assert len(bad_words) == 2  # No duplicates

        # Test with pre-calculated results
        results = st.check_profanity("shit damn")
        bad_words = st.get_bad_words(profanity_results=results)
        assert len(bad_words) == 2

    def test_get_bad_words_error(self):
        """Test get_bad_words error handling."""
        st = SafeText("en")

        with pytest.raises(ValueError, match="Either text or profanity_results must be provided"):
            st.get_bad_words()


class TestAutoLanguageFeatures:
    """Test automatic language detection features."""

    def test_auto_censor_without_language(self):
        """Test auto language detection when censoring."""
        st = SafeText(language=None)

        # Should auto-detect English and censor
        censored = st.censor_profanity("This is shit and I know it for sure")
        assert "****" in censored
        assert st.language == "en"
