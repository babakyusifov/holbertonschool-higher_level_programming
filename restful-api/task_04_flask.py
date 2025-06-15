from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}
@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    user = list(users)
    return jsonify(user)

@app.post("/add_user")
def add():
    data = request.json
    user = {"username": data.get("username"), "name": data.get("name"), "age": data.get("age"), "city": data.get("city")}

    if user["username"] is None:
        return {"error":"Username is required"}, 400
    users[data.get("username")] = user
    return jsonify({'message': 'User added', 'user': user}), 201

@app.route("/users/<username>")
def user(username):
    if username is None:
        return jsonify({'error': 'Username is required'}), 400

    if users.get(username) is None:
        return {"error": "User not found"}, 404
    return jsonify(users.get(username)), 200

@app.route("/status")
def status():
    return "OK"

app.run()
