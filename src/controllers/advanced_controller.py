# src/controllers/advanced_controller.py
# این فایل برای مسیریابی و مدیریت درخواست‌های مربوط به نمایش صفحه تحلیل پیشرفته احساسات است

from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import jwt_required
from src.models.advanced_sentiment_analyzer import AdvancedSentimentAnalyzer

advanced_blueprint = Blueprint('advanced', __name__)

@advanced_blueprint.route('/', methods=['GET'])
@jwt_required()
def advanced_page():
    return render_template('advanced_sentiment.html')

@advanced_blueprint.route('/analyze', methods=['POST'])
@jwt_required()
def analyze_advanced_sentiment():
    data = request.get_json()
    text = data.get('text', '')
    analyzer = AdvancedSentimentAnalyzer()
    result = analyzer.analyze_sentiment(text)
    return jsonify(result)
