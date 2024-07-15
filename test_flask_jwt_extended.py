try:
    from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
    print("flask_jwt_extended imported successfully!")
except ImportError as e:
    print(f"Error importing flask_jwt_extended: {e}")
