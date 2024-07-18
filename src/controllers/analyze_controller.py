# src/controllers/analyze_controller.py
# این فایل برای مسیریابی و مدیریت درخواست‌های مربوط به نمایش صفحه ورودی تحلیل احساسات است

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from src.models.sentiment_analyzer import SentimentAnalyzer
import logging

analyze_blueprint = Blueprint('analyze', __name__)

@analyze_blueprint.route('/api/sentiment', methods=['POST'])
@jwt_required()
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text', '')
    logging.info(f"Received text for analysis: {text}")  # اضافه کردن لاگ برای متنی که دریافت شده
    analyzer = SentimentAnalyzer()
    sentiment = analyzer.analyze_sentiment(text)
    logging.info(f"Sentiment result: {sentiment}")  # اضافه کردن لاگ برای نتیجه تحلیل احساسات
    return jsonify({'text': text, 'sentiment': sentiment})

