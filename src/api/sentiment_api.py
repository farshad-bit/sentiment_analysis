# src/api/sentiment_api.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from src.models.sentiment_analyzer import SentimentAnalyzer
from src.models.advanced_sentiment_analyzer import AdvancedSentimentAnalyzer
from src.services.database_service import DatabaseService

sentiment_api = Blueprint('sentiment_api', __name__)

@sentiment_api.route('/sentiment', methods=['POST'])
@jwt_required()
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text', '')
    analyzer = SentimentAnalyzer()
    sentiment = analyzer.analyze_sentiment(text)
    
    # Save sentiment to database
    db_service = DatabaseService()
    db_service.insert_sentiment(text, sentiment)
    
    return jsonify({'text': text, 'sentiment': sentiment})

@sentiment_api.route('/advanced_sentiment', methods=['POST'])
@jwt_required()
def analyze_advanced_sentiment():
    data = request.get_json()
    text = data.get('text', '')
    analyzer = AdvancedSentimentAnalyzer()
    result = analyzer.analyze_sentiment(text)
    
    # Save advanced sentiment to database
    db_service = DatabaseService()
    db_service.insert_sentiment(result['original_text'], result['sentiment'])
    
    return jsonify(result)

@sentiment_api.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username == "testuser" and password == "testpassword":
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"msg": "Bad username or password"}), 401
