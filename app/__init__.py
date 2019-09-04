from flask import Flask
from app.routes import page

def create_app():
    app = Flask(__name__)

    app.secret_key = "random string here"
    
    app.register_blueprint(page)

    return app
