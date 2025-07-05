"""Shared test configuration and fixtures."""

import pytest


def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line("markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')")
    config.addinivalue_line("markers", "integration: marks tests as integration tests")


@pytest.fixture(scope="session")
def supported_languages():
    """Return list of supported languages."""
    return ["ar", "az", "de", "en", "es", "fa", "fr", "hi", "ja", "pt", "ru", "tr", "zh"]


@pytest.fixture
def test_texts():
    """Return common test texts for various scenarios."""
    return {
        "clean": [
            "This is a nice day",
            "Hello world",
            "Python programming is fun",
        ],
        "profane": [
            "This is shit",
            "What the hell",
            "damn it",
        ],
        "mixed": [
            "This shit is really nice",
            "What a damn beautiful day",
        ],
        "multilingual": {
            "en": "This is an English sentence",
            "es": "Esta es una oración en español",
            "fr": "Ceci est une phrase en français",
            "de": "Dies ist ein deutscher Satz",
        },
    }


@pytest.fixture
def sample_profanity_words():
    """Return sample profanity words for testing."""
    return ["shit", "damn", "hell", "crap", "ass"]
