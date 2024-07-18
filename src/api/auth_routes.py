# src/api/auth_routes.py
# این فایل برای مسیریابی و مدیریت درخواست‌های مربوط به احراز هویت است

from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import create_access_token, unset_jwt_cookies
import datetime

auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username == "testuser" and password == "testpassword":
        access_token = create_access_token(identity=username)
        csrf_token = create_access_token(identity=username)  # برای توکن CSRF از همان توکن دسترسی استفاده می‌کنیم
        response = make_response(jsonify(access_token=access_token))
        response.set_cookie('access_token', access_token, httponly=True, samesite='Lax')
        response.set_cookie('csrf_access_token', csrf_token, httponly=True, samesite='Lax')
        
        # لاگ‌های دیباگ برای بررسی کوکی‌ها
        print(f"Access Token: {access_token}")
        print(f"CSRF Token: {csrf_token}")
        return response
    else:
        return jsonify({"msg": "Bad username or password"}), 401

@auth_api.route('/logout', methods=['POST'])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response
