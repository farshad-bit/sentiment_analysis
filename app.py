from flask import Flask
from src.controllers.routes import main_blueprint
from flask_wtf.csrf import CSRFProtect
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    csrf = CSRFProtect(app)
    app.register_blueprint(main_blueprint)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
