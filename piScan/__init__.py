from flask import Flask
import os
from config import Config
from piScan.app_modules.redis_client import RedisClient
from piScan.app_modules.processes_manager import ProcessesManager
from piScan.database.db import Database


db = Database()
cache_client = RedisClient(0)
processes_manager = ProcessesManager()


def register_blueprints(app):
    from piScan import routes

    app.register_blueprint(routes.core)
    app.register_blueprint(routes.api)

    if app.config["HOST_DOCS"]:
        app.register_blueprint(routes.docs)


def init_modules(app):
    db.setup(app.config["DATABASE_URI"])
    db.create_all()

    redis_url = app.config["REDIS_URI"]
    redis_port = int(app.config["REDIS_PORT"])

    cache_client.setup(redis_url, redis_port)

    processes_manager_cache_client = RedisClient(1)
    processes_manager_cache_client.setup(redis_url, redis_port)

    processes_manager.setup(processes_manager_cache_client)


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=False)

    app.secret_key = os.urandom(25)
    app.config.from_object(config_class)

    init_modules(app)

    with app.app_context():
        register_blueprints(app)

        return app
