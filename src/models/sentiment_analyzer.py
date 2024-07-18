# src/models/sentiment_analyzer.py
# این فایل برای تحلیل احساسات استفاده می‌شود

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from langdetect import detect
from deep_translator import GoogleTranslator
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
                translation = GoogleTranslator(source='auto', target='en').translate(text)
                if not translation:
                    raise ValueError("Translation failed")
                print(f"Translated text: {translation}")
                text = translation

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
