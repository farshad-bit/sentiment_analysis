from flask import Blueprint, jsonify

home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/', methods=['GET'])
def home():
    return "Welcome to the Sentiment Analysis API", 200
