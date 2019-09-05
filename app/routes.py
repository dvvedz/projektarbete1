from flask import Flask,render_template,Blueprint, request, url_for, session, redirect, json, jsonify
import requests

page = Blueprint("page", __name__, template_folder="templates")

users = [
    {
        "username": "Oskar",
        "message": "Blah Blah Blah"
    },
    {
        "username": "Test1",
        "message": "Blah Blah Blah"
    },
    {
        "username": "Test2",
        "message": "Blah Blah Blah"
    }
]


@page.route("/")
def index():
    return render_template("views/index.html")


# GET -  All Users
@page.route("/api/users", methods=["GET"])
def get_users():
    return jsonify({"users": users})

# GET - One user
@page.route("/api/users/<id>")
def get_one_user(id):
    for user in users:
        if user["username"] == id:
            return jsonify({"user": user})

    return jsonify({"error": "No user found" }), 400

# POST - Create user
@page.route("/api/users", methods=["POST"])
def create_user():
    users.append({ "username": request.form["username"], "message": request.form["message"] })
    return redirect(url_for("page.index"))


# Vulnerable endpoint
@page.route("/vuln-endpoint")
def vuln_endopoint():
    api_url = requests.get("http://localhost:5000/api/users")
    data = json.loads(api_url.text)

    return render_template("views/vuln-endpoint.html", data=data)