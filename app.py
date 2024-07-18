# app.py
# این فایل نقطه ورود اصلی برنامه است. تنظیمات Flask، JWT، و CORS را انجام می‌دهد و بلوپرینت‌های مختلف را ثبت می‌کند.


from flask import Flask, redirect, url_for
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from src.config import Config
from src.controllers.routes import main_blueprint
from src.controllers.analyze_controller import analyze_blueprint
from src.controllers.trends_controller import trends_blueprint
from src.controllers.auth_controller import auth_blueprint
from src.controllers.advanced_controller import advanced_blueprint

app = Flask(__name__, template_folder='src/views/templates', static_folder='src/views/static')
app.config.from_object(Config)
jwt = JWTManager(app)
CORS(app, supports_credentials=True)

app.register_blueprint(main_blueprint)
app.register_blueprint(analyze_blueprint, url_prefix='/analyze')
app.register_blueprint(trends_blueprint, url_prefix='/trends')
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(advanced_blueprint, url_prefix='/advanced')

@app.route('/')
def index():
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)




