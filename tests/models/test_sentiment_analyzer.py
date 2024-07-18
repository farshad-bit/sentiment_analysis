# tests/models/test_sentiment_analyzer.py
import pytest
from unittest.mock import patch, MagicMock
from src.models.sentiment_analyzer import SentimentAnalyzer

@pytest.fixture
def analyzer():
    return SentimentAnalyzer()

def test_analyze_sentiment_positive(analyzer):
    text = "I love programming."
    expected_result = "Positive"

    with patch('src.models.sentiment_analyzer.GoogleTranslator.translate', return_value="I love programming."), \
         patch.object(analyzer.db_service, 'insert_sentiment') as mock_insert_sentiment:
        result = analyzer.analyze_sentiment(text)
        assert result == expected_result
        mock_insert_sentiment.assert_called_once_with("I love programming.", "Positive")

def test_analyze_sentiment_negative(analyzer):
    text = "I hate bugs."
    expected_result = "Negative"

    with patch('src.models.sentiment_analyzer.GoogleTranslator.translate', return_value="I hate bugs."), \
         patch.object(analyzer.db_service, 'insert_sentiment') as mock_insert_sentiment:
        result = analyzer.analyze_sentiment(text)
        assert result == expected_result
        mock_insert_sentiment.assert_called_once_with("I hate bugs.", "Negative")

def test_analyze_sentiment_neutral(analyzer):
    text = "This is a pen."
    expected_result = "Neutral"

    with patch('src.models.sentiment_analyzer.GoogleTranslator.translate', return_value="This is a pen."), \
         patch.object(analyzer.db_service, 'insert_sentiment') as mock_insert_sentiment:
        result = analyzer.analyze_sentiment(text)
        assert result == expected_result
        mock_insert_sentiment.assert_called_once_with("This is a pen.", "Neutral")
