# src/api/advanced_sentiment_routes.py
# این فایل برای مسیریابی و مدیریت درخواست‌های مربوط به تحلیل پیشرفته احساسات است

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from src.models.advanced_sentiment_analyzer import AdvancedSentimentAnalyzer
from src.services.database_service import DatabaseService

advanced_sentiment_api = Blueprint('advanced_sentiment_api', __name__)

@advanced_sentiment_api.route('/advanced_sentiment', methods=['POST'])
@jwt_required()
def analyze_advanced_sentiment():
    data = request.get_json()
    text = data.get('text', '')
    analyzer = AdvancedSentimentAnalyzer()
    result = analyzer.analyze_sentiment(text)
    
    # ذخیره نتیجه تحلیل پیشرفته احساسات در دیتابیس
    db_service = DatabaseService()
    db_service.insert_sentiment(result['original_text'], result['sentiment'])
    
    return jsonify(result)
