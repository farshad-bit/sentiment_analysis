# src/models/sentiment_analyzer.py
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from langdetect import detect
from googletrans import Translator
from src.services.database_service import DatabaseService

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        self.db_service = DatabaseService()

    def analyze_sentiment(self, text):
        try:
            # تشخیص زبان
            language = detect(text)
            print(f"Detected language: {language}")
            if language != 'en':
                translator = Translator()
                translation = translator.translate(text, dest='en')
                if translation is None or translation.text is None:
                    raise ValueError("Translation failed")
                translated_text = translation.text
                print(f"Translated text: {translated_text}")
                text = translated_text

            # تحلیل احساسات
            sentiment = self.analyzer.polarity_scores(text)
            print(f"Sentiment scores: {sentiment}")
            compound = sentiment['compound']
            if compound > 0.05:
                sentiment_result = 'Positive'
            elif compound < -0.05:
                sentiment_result = 'Negative'
            else:
                sentiment_result = 'Neutral'

            # ذخیره در دیتابیس
            self.db_service.insert_sentiment(text, sentiment_result)

            return sentiment_result
        except Exception as e:
            print(f"Error: {e}")
            return str(e)
