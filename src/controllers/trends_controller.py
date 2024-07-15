from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.services.database_service import DatabaseService

trends_blueprint = Blueprint('trends', __name__)
db_service = DatabaseService()

@trends_blueprint.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

# این مسیر یک نمونه فرضی است
@trends_blueprint.route('/api/trends', methods=['GET'])
@jwt_required()
def get_trends():
    # فرض کنیم داده‌های مربوط به ترندها را از پایگاه داده می‌گیرید
    trends_data = db_service.get_trends_data()
    return jsonify(trends=trends_data), 200
