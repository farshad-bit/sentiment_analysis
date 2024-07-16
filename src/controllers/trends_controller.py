# src/controllers/trends_controller.py
from flask import Blueprint, render_template, jsonify
from flask_jwt_extended import jwt_required
from src.models.trend_analyzer import plot_trends

trends_blueprint = Blueprint('trends', __name__)

@trends_blueprint.route('/')
@jwt_required()
def trends_page():
    return render_template('trends.html')

@trends_blueprint.route('/trends', methods=['GET'])
@jwt_required()
def get_trends():
    plot_trends()
    return jsonify({"msg": "Trends plotted successfully"})
