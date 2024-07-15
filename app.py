from flask import Flask
from src.api.sentiment_api import create_api
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    create_api(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
