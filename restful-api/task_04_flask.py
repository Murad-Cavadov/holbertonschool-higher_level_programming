#!/usr/bin/python3
"""
Flask freymvorku ilə qurulmuş sadə RESTful API.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# İstifadəçiləri yaddaşda saxlamaq üçün lüğət
users = {}


@app.route("/")
def home():
    """Kök endpoint üçün xoş gəldin mesajı."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Sistemdəki bütün istifadəçi adlarının siyahısını qaytarır."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """API-nin vəziyyətini yoxlamaq üçün endpoint."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Verilən istifadəçi adına görə bütün məlumatları qaytarır."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Yeni istifadəçi əlavə edən POST endpointi."""
    # JSON-un düzgünlüyünü yoxlayırıq
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # İstifadəçini əlavə edirik
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
