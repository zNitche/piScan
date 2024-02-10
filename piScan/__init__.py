from flask import Flask
import os
from piScan.app_modules.redis_client import RedisClient
from piScan.app_modules.devices_processes_manager import DevicesProcessesManager
from piScan.database.db import Database


APP_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

db = Database()
cache_client = RedisClient(0)
devices_processes_manager = DevicesProcessesManager()


def register_blueprints(app):
    from piScan import routes

    app.register_blueprint(routes.core.blueprint)
    app.register_blueprint(routes.api.blueprint)

    if app.config["HOST_DOCS"]:
        app.register_blueprint(routes.docs.blueprint)


def init_modules(app):
    db.setup(app.config["DATABASE_URI"])
    db.create_all()

    redis_url = app.config["REDIS_URI"]
    redis_port = int(app.config["REDIS_PORT"])

    cache_client.setup(redis_url, redis_port)

    devices_processes_manager_cache_client = RedisClient(1)
    devices_processes_manager_cache_client.setup(redis_url, redis_port)

    devices_processes_manager.setup(devices_processes_manager_cache_client)


def create_app(config_class=None):
    if not config_class:
        from configs.config import Config

        config_class = Config

    app = Flask(__name__, instance_relative_config=False)

    app.secret_key = os.urandom(25)
    app.config.from_object(config_class)

    init_modules(app)

    with app.app_context():
        register_blueprints(app)

        return app
