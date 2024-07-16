# src/controllers/home_controller.py
from flask import Blueprint, render_template, redirect, url_for
from flask_jwt_extended import jwt_required

home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/')
def home_page():
    return redirect(url_for('main.auth.login'))

@home_blueprint.route('/input')
@jwt_required()
def input_page():
    return render_template('index.html')

@home_blueprint.route('/advanced')
@jwt_required()
def advanced_page():
    return render_template('advanced_sentiment.html')

@home_blueprint.route('/trends')
@jwt_required()
def trends_page():
    return render_template('trends.html')