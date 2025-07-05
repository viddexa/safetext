"""Basic tests for SafeText with DRY optimizations."""

import pytest

from safetext import SafeText

# Test data fixtures
SUPPORTED_LANGUAGES = ["ar", "az", "de", "en", "es", "fa", "fr", "hi", "ja", "pt", "ru", "tr", "zh"]

TEST_CASES = {
    "profanity": [
        ("This is shit", "shit", "This is ****"),
        ("damn shit", "damn", None),  # Multiple profanities
    ],
    "clean": [
        ("This is a nice day", None, "This is a nice day"),
        ("This is nice", None, "This is nice"),
    ],
}

LANGUAGE_TEST_TEXTS = {
    "en": "This is an English sentence with multiple words to ensure proper detection",
    "es": "Esta es una oración en español con múltiples palabras para asegurar la detección adecuada",
}


class TestSafeTextInitialization:
    """Test SafeText initialization scenarios."""

    @pytest.mark.parametrize("language", SUPPORTED_LANGUAGES)
    def test_language_initialization(self, language):
        """Test SafeText can be initialized with different languages."""
        st = SafeText(language)
        assert st.language == language
        assert st.checker is not None

    def test_invalid_language(self):
        """Test handling of invalid language code."""
        with pytest.raises(ValueError, match="No profanity word list found"):
            SafeText("xx")  # Invalid language code


class TestProfanityDetection:
    """Test profanity detection functionality."""

    @pytest.fixture
    def english_safetext(self):
        """Fixture for English SafeText instance."""
        return SafeText("en")

    @pytest.mark.parametrize("text,expected_word,_", TEST_CASES["profanity"])
    def test_profanity_detection(self, english_safetext, text, expected_word, _):
        """Test basic profanity detection."""
        result = english_safetext.check_profanity(text)
        assert len(result) > 0
        assert any(r["word"] == expected_word for r in result)

    @pytest.mark.parametrize("text,_,__", TEST_CASES["clean"])
    def test_clean_text_detection(self, english_safetext, text, _, __):
        """Test clean text returns empty results."""
        result = english_safetext.check_profanity(text)
        assert len(result) == 0


class TestProfanityCensoring:
    """Test profanity censoring functionality."""

    @pytest.fixture
    def english_safetext(self):
        """Fixture for English SafeText instance."""
        return SafeText("en")

    @pytest.mark.parametrize("text,_,expected_censored", TEST_CASES["profanity"])
    def test_profanity_censoring(self, english_safetext, text, _, expected_censored):
        """Test profanity censoring."""
        if expected_censored:  # Skip if no expected censored text
            censored = english_safetext.censor_profanity(text)
            assert censored == expected_censored

    @pytest.mark.parametrize("text,_,expected", TEST_CASES["clean"])
    def test_clean_text_unchanged(self, english_safetext, text, _, expected):
        """Test clean text remains unchanged."""
        censored = english_safetext.censor_profanity(text)
        assert censored == expected


class TestWhitelist:
    """Test whitelist functionality."""

    def test_whitelist_from_list(self):
        """Test whitelist functionality with list."""
        st = SafeText("en", whitelist=["shit"])

        # Should not detect whitelisted word
        result = st.check_profanity("This is shit")
        assert len(result) == 0

        # Should still detect other profanity
        result = st.check_profanity("This is damn shit")
        assert any(r["word"] == "damn" for r in result)
        assert not any(r["word"] == "shit" for r in result)

    def test_whitelist_case_insensitive(self):
        """Test whitelist is case insensitive."""
        st = SafeText("en", whitelist=["SHIT"])
        result = st.check_profanity("This is shit")
        assert len(result) == 0


class TestLanguageDetection:
    """Test automatic language detection."""

    @pytest.mark.parametrize("lang_code,text", LANGUAGE_TEST_TEXTS.items())
    def test_auto_language_detection_from_text(self, lang_code, text):
        """Test automatic language detection from text."""
        st = SafeText(language=None)
        st.set_language_from_text(text)
        assert st.language == lang_code

    def test_language_change(self):
        """Test that language can be changed after initialization."""
        st = SafeText("en")
        assert st.language == "en"

        st.set_language("es")
        assert st.language == "es"
