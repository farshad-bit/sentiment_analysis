# src/controllers/trends_controller.py
from flask import Blueprint, render_template, jsonify
from flask_jwt_extended import jwt_required
from src.services.database_service import get_trends

trends_blueprint = Blueprint('trends', __name__)

@trends_blueprint.route('/')
@jwt_required()
def trends_page():
    return render_template('trends.html')

@trends_blueprint.route('/data', methods=['GET'])
@jwt_required()
def fetch_trends():
    trends = get_trends()
    return jsonify(trends)
