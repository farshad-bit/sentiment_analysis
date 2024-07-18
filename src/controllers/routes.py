# src/controllers/routes.py
# این فایل برای ثبت همه بلوپرینت‌های مختلف برنامه در یک بلوپرینت اصلی است

from flask import Blueprint
from src.controllers.home_controller import home_blueprint
from src.controllers.analyze_controller import analyze_blueprint
from src.controllers.trends_controller import trends_blueprint
from src.controllers.auth_controller import auth_blueprint
from src.controllers.advanced_controller import advanced_blueprint

main_blueprint = Blueprint('main', __name__)

main_blueprint.register_blueprint(home_blueprint, url_prefix='/home')
main_blueprint.register_blueprint(analyze_blueprint, url_prefix='/analyze')
main_blueprint.register_blueprint(trends_blueprint, url_prefix='/trends')
main_blueprint.register_blueprint(auth_blueprint, url_prefix='/auth')
main_blueprint.register_blueprint(advanced_blueprint, url_prefix='/advanced')


