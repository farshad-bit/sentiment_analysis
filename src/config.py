# src/config.py
import os

class Config:
    # تولید یک کلید مخفی برای برنامه
    SECRET_KEY = os.urandom(24)
    
    # کلید مخفی برای JWT (توکن‌های وب JSON)
    JWT_SECRET_KEY = 'FgesP_Wx6yTOi8kNm0hX2JH0ZwvL-EuG'
    
    # مکان ذخیره توکن‌های JWT (در کوکی‌ها و هدرها)
    JWT_TOKEN_LOCATION = ['cookies', 'headers']
    
    # مسیر دسترسی کوکی‌های JWT
    JWT_ACCESS_COOKIE_PATH = '/'
    
    # آیا کوکی‌ها باید ایمن باشند (فقط از طریق HTTPS)
    JWT_COOKIE_SECURE = False
    
    # حفاظت از CSRF در کوکی‌های JWT
    JWT_COOKIE_CSRF_PROTECT = True
    
    # ذخیره توکن‌های CSRF در کوکی‌ها
    JWT_CSRF_IN_COOKIES = True
