from flask import Flask, render_template, Blueprint

page = Blueprint("page", __name__, template_folder="templates")


@page.route("/")
def index():
    return render_template("views/index.html")

