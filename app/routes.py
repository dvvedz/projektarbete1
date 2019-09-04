from flask import (
    Flask,
    render_template,
    Blueprint, 
    request, 
    url_for, 
    session, 
    redirect, 
    json, 
    jsonify)

page = Blueprint("page", __name__, template_folder="templates")

users = [
    {
        "id": 1,
        "username": "Oskar",
        "message": "Blah Blah Blah"
    },
    {
        "id": 2,
        "username": "Test1",
        "message": "Blah Blah Blah"
    },
    {
        "id": 3,
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
@page.route("/api/users/<int:id>")
def get_one_user(id):
    for user in users:
        if user["id"] == id:
            return jsonify({"user": user})

    return jsonify({"error": "No user found" }), 400

