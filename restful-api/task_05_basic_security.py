#!/usr/bin/python3
"""
Basic Auth və JWT Auth ilə təhlükəsizlik tətbiq edilmiş Flask API.
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Təhlükəsizlik açarları
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['JWT_SECRET_KEY'] = 'your-jwt-secret-key'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# İstifadəçi bazası (yaddaşda)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# --- Basic Authentication Məntiqi ---

@auth.verify_password
def verify_password(username, password):
    """Basic Auth üçün parolu yoxlayır."""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Yalnız düzgün Basic Auth məlumatı olanlar üçün."""
    return "Basic Auth: Access Granted"

# --- JWT Authentication Məntiqi ---

@app.route('/login', methods=['POST'])
def login():
    """Giriş edib JWT tokeni almaq üçün endpoint."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get('username')
    password = data.get('password')

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Rol məlumatını tokenin içinə yerləşdiririk
        access_token = create_access_token(
            identity=username,
            additional_claims={"role": user['role']}
        )
        return jsonify(access_token=access_token)
    
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """Yalnız düzgün JWT tokeni olanlar üçün."""
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Yalnız 'admin' rolu olanlar üçün."""
    # Tokendən istifadəçinin kimliyini və əlavə məlumatları alırıq
    from flask_jwt_extended import get_jwt
    claims = get_jwt()
    
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    
    return "Admin Access: Granted"

# --- Custom JWT Error Handlers (401 qaytarmaq üçün) ---

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

if __name__ == "__main__":
    app.run()
