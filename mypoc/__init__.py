import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']

    @app.route("/")
    def hello():
        return "Hello, World!"

    @app.route("/health")
    def health():
        return "OK"

    from mypoc import pet
    app.register_blueprint(pet.bp)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        return app
