# sentiment_analysis/src/api/sentiment_api.py

import sys
import os
from flask import Flask, request
from flask_restful import Resource, Api

# افزودن مسیر src به sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.models.sentiment_analyzer import SentimentAnalyzer

app = Flask(__name__)
api = Api(app)

analyzer = SentimentAnalyzer()

class SentimentAnalysisAPI(Resource):
    def post(self):
        data = request.get_json()
        text = data.get('text')
        
        if not text:
            return {'error': 'Text is required for sentiment analysis.'}, 400
        
        sentiment = analyzer.analyze_sentiment(text)
        return {'text': text, 'sentiment': sentiment}, 200

api.add_resource(SentimentAnalysisAPI, '/api/sentiment')

@app.route('/', methods=['GET'])
def home():
    return "Sentiment Analysis API is running."

if __name__ == '__main__':
    app.run(debug=True)
