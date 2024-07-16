# src/controllers/advanced_controller.py
from flask import Blueprint, render_template
from flask_jwt_extended import jwt_required

advanced_blueprint = Blueprint('advanced', __name__)

@advanced_blueprint.route('/')
@jwt_required()
def advanced_page():
    return render_template('advanced_sentiment.html')
