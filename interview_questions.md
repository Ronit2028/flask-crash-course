# Interview Questions: Python Flask (Crash Course)

This document contains conceptual, theoretical interview questions and answers covering Flask web framework basics.

---

## ❓ Interview Questions & Answers

### 1. What is Flask, and why is it referred to as a "micro-framework"?
**Answer:**
Flask is a web framework written in Python. It is called a **micro-framework** because it does not require particular tools or libraries (like database abstraction layers, form validation, or third-party authentication templates). Flask keeps the core simple but extensible, letting developers choose their own database engine (SQLAlchemy, MongoEngine), form parsers, and architectural design patterns.

---

### 2. What is WSGI in the context of Python web development?
**Answer:**
**WSGI (Web Server Gateway Interface)** is a standardized interface between Python web applications (like Flask or Django) and web servers (like Nginx, Apache, Gunicorn, or uWSGI). It ensures that different web servers can interact with different Python web frameworks seamlessly.

---

### 3. How does routing work in Flask? What is a Python decorator?
**Answer:**
*   **Routing:** Flask maps URLs to Python functions using the `@app.route()` decorator. When a client makes an HTTP request to a URL, Flask calls the associated function and returns its output.
*   **Decorator:** A decorator is a structural design pattern in Python that wraps a function, modifying or extending its behavior without altering the function's code directly. In Flask, it registers the function with the application's internal URL routing table.

---

### 4. How do you parse different input request types (Query parameters, Form-data, and JSON payloads) in a Flask handler?
**Answer:**
You use the global `request` object imported from `flask`:
*   **Query String parameters:** Access via `request.args` (e.g., `request.args.get('name')`).
*   **HTML Form submission:** Access via `request.form` (e.g., `request.form.get('email')`).
*   **JSON payloads (API requests):** Access via `request.get_json()` (e.g., `data = request.get_json()`).

---

### 5. What does the `jsonify()` function do in Flask? How does it differ from returning a standard dictionary?
**Answer:**
*   **`jsonify()`** serializes data (like lists or dictionaries) into a JSON string and returns a `Response` object with the headers explicitly set to `Content-Type: application/json`.
*   In modern Flask versions (since 1.0), returning a standard Python dictionary from a route handler is automatically cast to JSON. However, using `jsonify()` is still preferred when you need to return JSON arrays, chain custom HTTP status codes, or customize the HTTP headers directly.

---

### 6. Why should you never use Flask's built-in development server in a production environment?
**Answer:**
Flask's built-in development server is single-threaded, not optimized for security, and lacks resource scaling capacity. If multiple concurrent requests hit the development server, it blocks execution and slows down dramatically. In production, you should always wrap your Flask application inside a production-ready WSGI container like **Gunicorn** or **uWSGI**, which handles connection pooling, worker thread spawning, and process scaling.
