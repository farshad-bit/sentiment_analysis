from flask import Blueprint
from src.controllers.home_controller import home_blueprint
from src.controllers.analyze_controller import analyze_blueprint
from src.controllers.trends_controller import trends_blueprint

main_blueprint = Blueprint('main', __name__)

main_blueprint.register_blueprint(home_blueprint)
main_blueprint.register_blueprint(analyze_blueprint)
main_blueprint.register_blueprint(trends_blueprint)
