# src/controllers/auth_controller.py
from flask import Blueprint, request, jsonify, render_template, redirect, url_for, make_response
from flask_jwt_extended import create_access_token, set_access_cookies, get_csrf_token
import datetime
import logging

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    username = request.form.get('username')
    password = request.form.get('password')

    if username != 'admin' or password != 'admin':
        logging.error(f"Login failed for user: {username}")
        return jsonify({"msg": "Bad username or password"}), 401

    expires = datetime.timedelta(days=1)
    access_token = create_access_token(identity=username, expires_delta=expires)
    response = make_response(redirect(url_for('main.home.input_page')))
    set_access_cookies(response, access_token)
    response.set_cookie('csrf_access_token', get_csrf_token(access_token))
    return response
