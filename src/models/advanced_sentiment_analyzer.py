# src/models/advanced_sentiment_analyzer.py
# این فایل برای تحلیل پیشرفته احساسات استفاده می‌شود

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from langdetect import detect
from deep_translator import GoogleTranslator
from src.services.database_service import DatabaseService

class AdvancedSentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        self.db_service = DatabaseService()

    def translate_text(self, text, target_language='en'):
        try:
            translated_text = GoogleTranslator(source='auto', target=target_language).translate(text)
            return translated_text
        except Exception as e:
            print(f"Translation error: {e}")
            return None

    def analyze_sentiment(self, text):
        try:
            # تشخیص زبان
            language = detect(text)
            print(f"Detected language: {language}")  # Debugging log
            translated_text = text
            if language != 'en':
                translated_text = self.translate_text(text)
                if not translated_text:
                    raise ValueError("Translation failed")
                print(f"Translated text: {translated_text}")  # Debugging log

            # تحلیل احساسات
            sentiment = self.analyzer.polarity_scores(translated_text)
            print(f"Sentiment scores: {sentiment}")  # Debugging log
            compound = sentiment['compound']
            if compound >= 0.5:
                sentiment_result = 'Very Positive'
            elif 0.2 < compound < 0.5:
                sentiment_result = 'Positive'
            elif -0.2 <= compound <= 0.2:
                sentiment_result = 'Neutral'
            elif -0.5 < compound < -0.2:
                sentiment_result = 'Negative'
            else:
                sentiment_result = 'Very Negative'

            # ذخیره در دیتابیس
            self.db_service.insert_sentiment(translated_text, sentiment_result)

            return {'sentiment': sentiment_result, 'translated_text': translated_text}
        except Exception as e:
            print(f"Error: {e}")
            return {'error': str(e)}
