#!/usr/bin/python3
"""A simple api with Flask"""
from flask import Flask, jsonify, request


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# In-memory storage for users
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Root endpoint
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Endpoint to return status
@app.route('/status')
def status():
    return "OK"

# Endpoint to return all usernames
@app.route('/data')
def get_usernames():
    usernames = list(users.keys())
    if usernames:
        return jsonify(usernames)
    return jsonify({"error": "Users not found"})

# Endpoint to return user data for a specific username
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return  {"error": "User not found"}

# Endpoint to add a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    if request.is_json:
        user_data = request.get_json()
        username = user_data.get('username')
        
        if not username:
            return jsonify({"error": "Username is required"}), 400
        
        if username in users:
            return jsonify({"error": "User already exists"}), 400

        users = {
            "username": user_data.get('username'),
            "name": user_data.get('name'),
            "age": user_data.get('age'),
            "city": user_data.get('city')
        }
        
        return jsonify({"message": "User added", "user": users})
    else:
        return jsonify({"error": "Invalid JSON"}), 400