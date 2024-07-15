from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.models.sentiment_analyzer import SentimentAnalyzer

analyze_blueprint = Blueprint('analyze', __name__)
analyzer = SentimentAnalyzer()

@analyze_blueprint.route('/api/sentiment', methods=['POST'])
@jwt_required()
def analyze_sentiment():
    text = request.json.get('text')
    sentiment = analyzer.analyze_sentiment(text)
    return jsonify(text=text, sentiment=sentiment), 200
