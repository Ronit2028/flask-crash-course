# Python Flask Crash Course: Live-Coding Server Template
from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated in-memory database
items_db = [
    {"id": 1, "name": "Python Book"},
    {"id": 2, "name": "Flask Cheat Sheet"}
]

# TODO 1: Define a GET route '/' returning a simple plaintext welcome greeting
# @app.route('/')
# def welcome():
#     pass

# TODO 2: Define a GET route '/api/greet' that extracts query string parameter 'name'
#         If 'name' is present, return JSON { "message": "Hello, <name>!" }
#         If 'name' is missing, default to "Hello, Guest!"

# TODO 3: Define a POST route '/api/items' that accepts a JSON body containing { "name": string }
#         Parse payload using request.get_json()
#         If "name" is missing, return error status 400
#         If valid, append new item to items_db and return the item with status 201

# TODO 4: Define a GET route with dynamic variable rules '/api/items/<int:item_id>'
#         Search items_db for the item matching item_id
#         If found, return the item with status 200
#         If not found, return an error message with status 404

# TODO 5: Start the server on port 5000 in debug mode if script is run directly

if __name__ == '__main__':
    print("Flask Server template is waiting for live coding...")
