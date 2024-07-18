# src/api/sentiment_routes.py
# این فایل برای مسیریابی و مدیریت درخواست‌های مربوط به تحلیل احساسات است

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from src.models.sentiment_analyzer import SentimentAnalyzer
from src.services.database_service import DatabaseService

sentiment_api = Blueprint('sentiment_api', __name__)

@sentiment_api.route('/sentiment', methods=['POST'])
@jwt_required()
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text', '')
    analyzer = SentimentAnalyzer()
    sentiment = analyzer.analyze_sentiment(text)
    
    # ذخیره نتیجه تحلیل احساسات در دیتابیس
    db_service = DatabaseService()
    db_service.insert_sentiment(text, sentiment)
    
    return jsonify({'text': text, 'sentiment': sentiment})
