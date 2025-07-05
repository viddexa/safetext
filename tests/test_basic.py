"""Basic tests for SafeText."""

import pytest

from safetext import SafeText


def test_saftext_initialization():
    """Test SafeText can be initialized with different languages."""
    # Test English
    st = SafeText("en")
    assert st.language == "en"
    assert st.checker is not None


def test_profanity_detection():
    """Test basic profanity detection."""
    st = SafeText("en")

    # Test with known profanity
    result = st.check_profanity("This is shit")
    assert len(result) > 0
    assert result[0]["word"] == "shit"

    # Test clean text
    result = st.check_profanity("This is a nice day")
    assert len(result) == 0


def test_profanity_censoring():
    """Test profanity censoring."""
    st = SafeText("en")

    # Test censoring
    censored = st.censor_profanity("This is shit")
    assert censored == "This is ****"

    # Test clean text remains unchanged
    clean = st.censor_profanity("This is nice")
    assert clean == "This is nice"


def test_whitelist():
    """Test whitelist functionality."""
    # Test with whitelist
    st = SafeText("en", whitelist=["shit"])

    # Should not detect whitelisted word
    result = st.check_profanity("This is shit")
    assert len(result) == 0

    # Should still detect other profanity
    result = st.check_profanity("This is damn shit")
    assert any(r["word"] == "damn" for r in result)


def test_multiple_languages():
    """Test that multiple languages can be loaded."""
    languages = ["ar", "az", "de", "en", "es", "fa", "fr", "hi", "ja", "pt", "ru", "tr", "zh"]

    for lang in languages:
        st = SafeText(lang)
        assert st.language == lang
        assert st.checker is not None


def test_invalid_language():
    """Test handling of invalid language code."""
    with pytest.raises(ValueError, match="No profanity word list found"):
        SafeText("xx")  # Invalid language code


def test_auto_language_detection():
    """Test automatic language detection from text."""
    st = SafeText(language=None)

    # Test English detection
    st.set_language_from_text("This is an English sentence with multiple words to ensure proper detection")
    assert st.language == "en"

    # Test that language can be changed
    st.set_language("es")
    assert st.language == "es"
