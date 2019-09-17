from flask import Flask,render_template,Blueprint, request, url_for, session, redirect, json, jsonify, make_response, flash
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
    if "/" in request.form["message"]:
        users.append({ "username": request.form["username"], "message": "Harmfull message" })
        return redirect(url_for("page.vuln_endpoint"))
    else:
        users.append({ "username": request.form["username"], "message": request.form["message"] })
        return redirect(url_for("page.vuln_endpoint"))

    return render_template("views/index.html")

# DELETE a user
# @page.route("/api/users/<id>", methods=["DELETE"])
# def delete_one_user(id):
#     for user in users:
#         if user["username"] == id:
#             users
#             return redirect(url_for("page.get_users"))

#     return jsonify({"error": "No user found" }), 400

# Vulnerable endpoint
@page.route("/vuln-endpoint")
def vuln_endpoint():
    api_url = requests.get("http://localhost:5000/api/users")
    data = json.loads(api_url.text)
    return render_template("views/vuln-endpoint.html", data=data)


@page.route("/what-is-xss")
def what_is_xss():
    return render_template("views/what-is-xss.html")

@page.route("/test")
def test():
    return render_template("views/test.html")