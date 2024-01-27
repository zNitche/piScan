from flask import Flask
import os
from config import Config


def register_blueprints(app):
    from piScan.blueprints.main.routes import main

    app.register_blueprint(main, url_prefix="/api")


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=False)

    app.secret_key = os.urandom(25)
    app.config.from_object(config_class)

    with app.app_context():
        register_blueprints(app)

        return app
