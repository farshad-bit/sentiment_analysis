# src/models/advanced_sentiment_analyzer.py
from transformers import pipeline
from googletrans import Translator

class AdvancedSentimentAnalyzer:
    def __init__(self):
        self.analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
        self.translator = Translator()

    def analyze_sentiment(self, text):
        # Translate the text to English
        translation = self.translator.translate(text, dest='en').text

        # Analyze the sentiment of the translated text
        sentiment = self.analyzer(translation)

        # Get the sentiment label and score
        label = sentiment[0]['label']
        score = sentiment[0]['score']

        # Determine sentiment result based on the label
        if label == "1 star":
            sentiment_result = "Very Bad"
        elif label == "2 stars":
            sentiment_result = "Bad"
        elif label == "3 stars":
            sentiment_result = "Neutral"
        elif label == "4 stars":
            sentiment_result = "Good"
        elif label == "5 stars":
            sentiment_result = "Very Good"

        return {
            'original_text': text,
            'translated_text': translation,
            'sentiment': sentiment_result,
            'score': score
        }
