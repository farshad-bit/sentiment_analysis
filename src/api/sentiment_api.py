import sys
import os
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

# اضافه کردن مسیر پروژه به مسیرهای جستجوی Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.models.sentiment_analyzer import SentimentAnalyzer
from src.services.database_service import DatabaseService
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)

analyzer = SentimentAnalyzer()
db_service = DatabaseService()

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Sentiment Analysis API", 200

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@app.route('/api/sentiment', methods=['POST'])
@jwt_required()
def analyze_sentiment():
    text = request.json.get('text')
    if not text:
        return jsonify({"msg": "No text provided"}), 400
    sentiment = analyzer.analyze_sentiment(text)
    return jsonify(text=text, sentiment=sentiment), 200

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(debug=True)
