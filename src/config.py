# src/config.py
import os

class Config:
    SECRET_KEY = os.urandom(24)
    JWT_SECRET_KEY = 'FgesP_Wx6yTOi8kNm0hX2JH0ZwvL-EuG'
    JWT_TOKEN_LOCATION = ['cookies', 'headers']
    JWT_ACCESS_COOKIE_PATH = '/'
    JWT_COOKIE_SECURE = False
    JWT_COOKIE_CSRF_PROTECT = True
    JWT_CSRF_IN_COOKIES = True
