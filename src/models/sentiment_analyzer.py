from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from langdetect import detect
from googletrans import Translator

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        try:
            # تشخیص زبان
            language = detect(text)
            print(f"Detected language: {language}")
            if language != 'en':
                translator = Translator()
                translation = translator.translate(text, dest='en')
                if not translation or not translation.text:
                    raise ValueError("Translation failed")
                translated_text = translation.text
                print(f"Translated text: {translated_text}")
                text = translated_text

            # تحلیل احساسات
            sentiment = self.analyzer.polarity_scores(text)
            print(f"Sentiment scores: {sentiment}")
            compound = sentiment['compound']
            if compound > 0.05:
                return 'Positive'
            elif compound < -0.05:
                return 'Negative'
            else:
                return 'Neutral'
        except Exception as e:
            print(f"Error: {e}")
            return str(e)
