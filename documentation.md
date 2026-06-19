# Python Flask: Foundations & Web Routing

## 📖 Key Concepts

1. **What is Flask?**: Flask is a lightweight **micro-framework** for Python. Unlike Django, it does not come with a built-in database ORM, form validation, or user authentication. It provides the bare minimum required to route requests, parse inputs, and return responses, leaving all architectural choices to the developer.
2. **WSGI (Web Server Gateway Interface)**: A standardized specification for Python web applications to communicate with web servers (like Apache or Nginx). Flask is a WSGI application.
3. **Decorator Routing**: Flask uses Python decorators (`@app.route()`) to map URL paths to specific handler functions.
4. **Request Context**: Flask uses a thread-safe local object `request` to access incoming request parameters:
   - `request.args`: Accesses URL query parameters (e.g., `/search?term=python`).
   - `request.form`: Accesses body payload sent via standard HTML form-data.
   - `request.get_json()`: Parses and retrieves incoming JSON payloads.
5. **JSON Responses**: Return structured JSON objects to client apps using Flask's native `jsonify()` function or by returning standard Python dictionaries (which Flask automatically serializes to JSON in modern versions).

---

## 💻 Code Snippets

### A Basic Flask API Server
```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Basic Route (GET)
@app.route('/')
def home():
    return "Welcome to Flask Crash Course!"

# Dynamic Route Parameter
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Simulated database fetch
    user_profile = {"id": user_id, "username": f"user_{user_id}", "status": "active"}
    return jsonify(user_profile), 200

# POST Request with JSON Body
@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Name field is required"}), 400
        
    new_item = {
        "id": 101,
        "name": data['name'],
        "status": "Created"
    }
    return jsonify(new_item), 201

if __name__ == '__main__':
    # Run server in debug mode on port 5000
    app.run(debug=True, port=5000)
```
