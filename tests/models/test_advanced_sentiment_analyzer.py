# tests/models/test_advanced_sentiment_analyzer.py
import pytest
from unittest.mock import patch
from src.models.advanced_sentiment_analyzer import AdvancedSentimentAnalyzer

@pytest.fixture
def analyzer():
    return AdvancedSentimentAnalyzer()

def test_translate_text(analyzer):
    text = "Bonjour tout le monde"
    expected_translation = "Hello everyone"

    with patch('src.models.advanced_sentiment_analyzer.GoogleTranslator.translate', return_value=expected_translation):
        translated_text = analyzer.translate_text(text)
        assert translated_text == expected_translation

def test_analyze_sentiment_very_positive(analyzer):
    text = "I absolutely love this!"
    expected_result = {'sentiment': 'Very Positive', 'translated_text': 'I absolutely love this!'}

    with patch('src.models.advanced_sentiment_analyzer.GoogleTranslator.translate', return_value="I absolutely love this!"), \
         patch.object(analyzer.db_service, 'insert_sentiment') as mock_insert_sentiment:
        result = analyzer.analyze_sentiment(text)
        print(f"Test result: {result}")  # Debugging log
        assert result == expected_result
        mock_insert_sentiment.assert_called_once_with("I absolutely love this!", "Very Positive")

def test_analyze_sentiment_positive(analyzer):
    text = "I had a pleasant day at the beach."
    expected_result = {'sentiment': 'Positive', 'translated_text': 'I had a pleasant day at the beach.'}

    with patch('src.models.advanced_sentiment_analyzer.GoogleTranslator.translate', return_value="I had a pleasant day at the beach."), \
         patch.object(analyzer.db_service, 'insert_sentiment') as mock_insert_sentiment:
        result = analyzer.analyze_sentiment(text)
        print(f"Test result: {result}")  # Debugging log
        assert result == expected_result
        mock_insert_sentiment.assert_called_once_with("I had a pleasant day at the beach.", "Positive")

def test_analyze_sentiment_neutral(analyzer):
    text = "I am going to the store to buy groceries."
    expected_result = {'sentiment': 'Neutral', 'translated_text': 'I am going to the store..'}

    with patch('src.models.advanced_sentiment_analyzer.GoogleTranslator.translate', return_value="I am going to the store.."), \
         patch.object(analyzer.db_service, 'insert_sentiment') as mock_insert_sentiment:
        result = analyzer.analyze_sentiment(text)
        print(f"Test result: {result}")  # Debugging log
        assert result == expected_result
        mock_insert_sentiment.assert_called_once_with("I am going to the store..", "Neutral")

def test_analyze_sentiment_negative(analyzer):
    text = "I don't like this."
    expected_result = {'sentiment': 'Negative', 'translated_text': "I don't like this."}

    with patch('src.models.advanced_sentiment_analyzer.GoogleTranslator.translate', return_value="I don't like this."), \
         patch.object(analyzer.db_service, 'insert_sentiment') as mock_insert_sentiment:
        result = analyzer.analyze_sentiment(text)
        print(f"Test result: {result}")  # Debugging log
        assert result == expected_result
        mock_insert_sentiment.assert_called_once_with("I don't like this.", "Negative")

def test_analyze_sentiment_very_negative(analyzer):
    text = "I absolutely hate this!"
    expected_result = {'sentiment': 'Very Negative', 'translated_text': "I absolutely hate this!"}

    with patch('src.models.advanced_sentiment_analyzer.GoogleTranslator.translate', return_value="I absolutely hate this!"), \
         patch.object(analyzer.db_service, 'insert_sentiment') as mock_insert_sentiment:
        result = analyzer.analyze_sentiment(text)
        print(f"Test result: {result}")  # Debugging log
        assert result == expected_result
        mock_insert_sentiment.assert_called_once_with("I absolutely hate this!", "Very Negative")
