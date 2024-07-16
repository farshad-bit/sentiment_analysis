# app.py
from flask import Flask, redirect, url_for
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from src.config import Config
from src.controllers.routes import main_blueprint
from src.api.sentiment_api import sentiment_api

app = Flask(__name__, template_folder='src/views/templates', static_folder='src/views/static')
app.config.from_object(Config)
jwt = JWTManager(app)
CORS(app, supports_credentials=True)

app.register_blueprint(main_blueprint)
app.register_blueprint(sentiment_api, url_prefix='/api')

@app.route('/')
def index():
    return redirect(url_for('main.auth.login'))

if __name__ == '__main__':
    app.run(debug=True)
