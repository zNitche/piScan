from flask import Flask
import os
from piscan.app_modules.redis_client import RedisClient
from piscan.app_modules.devices_processes_manager import DevicesProcessesManager
from piscan.database.db import Database
from config import Config


db = Database()
devices_processes_manager = DevicesProcessesManager()


def generate_docs():
    if Config.HOST_DOCS:
        swagger_json_path = Config.SWAGGER_SCHEMA_PATH

        if swagger_json_path and not os.path.exists(swagger_json_path):
            from generate_swagger_docs import generate

            generate()


def init_files_structure():
    paths = [
        Config.SCAN_FILES_DIR_PATH,
        Config.SCAN_FILES_THUMBNAILS_DIR_PATH
    ]

    for path in paths:
        if not os.path.exists(path):
            os.mkdir(path)


def register_blueprints(app):
    from piscan import routes

    app.register_blueprint(routes.core.blueprint)
    app.register_blueprint(routes.api.blueprint)

    if app.config["HOST_DOCS"]:
        app.register_blueprint(routes.docs.blueprint)


def init_modules(app):
    db.setup(app.config["DATABASE_URI"])
    db.create_all()

    redis_url = app.config["REDIS_URI"]
    redis_port = int(app.config["REDIS_PORT"])

    devices_processes_manager_cache_client = RedisClient(1)
    devices_processes_manager_cache_client.setup(redis_url, redis_port)

    devices_processes_manager.setup(devices_processes_manager_cache_client)


def create_app():
    app = Flask(__name__, instance_relative_config=False)

    app.secret_key = os.urandom(25)
    app.config.from_object(Config)

    init_modules(app)

    with app.app_context():
        register_blueprints(app)

        return app
