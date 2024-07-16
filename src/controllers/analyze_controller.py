# src/controllers/analyze_controller.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from src.models.sentiment_analyzer import SentimentAnalyzer

analyze_blueprint = Blueprint('analyze', __name__)

@analyze_blueprint.route('/api/sentiment', methods=['POST'])
@jwt_required()
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text', '')
    analyzer = SentimentAnalyzer()
    sentiment = analyzer.analyze_sentiment(text)
    return jsonify({'text': text, 'sentiment': sentiment})
