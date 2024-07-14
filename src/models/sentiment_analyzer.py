from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from langdetect import detect
from googletrans import Translator
from src.services.database_service import DatabaseService
import bleach

class SentimentAnalyzer:
    def __init__(self):
        self.results = {'Positive': 0, 'Negative': 0, 'Neutral': 0}
        self.analyzer = SentimentIntensityAnalyzer()
        self.db_service = DatabaseService()

    def analyze_sentiment(self, text):
        try:
            # پاکسازی ورودی کاربر برای جلوگیری از حملات XSS
            text = bleach.clean(text)
            
            # تشخیص زبان
            language = detect(text)
            if language != 'en':
                translator = Translator()
                translated_text = translator.translate(text, dest='en').text
                text = translated_text
            
            # تحلیل احساسات
            sentiment = self.analyzer.polarity_scores(text)
            compound = sentiment['compound']
            
            if compound > 0.05:
                sentiment_label = 'Positive'
                self.results['Positive'] += 1
            elif compound < -0.05:
                sentiment_label = 'Negative'
                self.results['Negative'] += 1
            else:
                sentiment_label = 'Neutral'
                self.results['Neutral'] += 1
            
            # ذخیره در پایگاه داده
            self.db_service.save_sentiment(text, sentiment_label)

            return sentiment_label
        except Exception as e:
            return str(e)

    def get_results(self):
        return self.results
