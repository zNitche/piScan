from flask import Flask
import os
from config import Config
from piScan.database.db import init_db, db_engine
from piScan.database.migrations import init_migrations, migrate


def register_blueprints(app):
    root_prefix = app.config["ROOT_URL_PREFIX"]

    import piScan.blueprints.routes
    from piScan.blueprints.main.routes import main
    from piScan.blueprints.devices.routes import devices

    app.register_blueprint(main, url_prefix=f"{root_prefix}")
    app.register_blueprint(devices, url_prefix=f"{root_prefix}/devices")


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=False)

    app.secret_key = os.urandom(25)
    app.config.from_object(config_class)

    init_db()
    init_migrations(app.config, db_engine)
    migrate(app.config["MIGRATIONS_DIR_PATH"], db_engine)

    with app.app_context():
        register_blueprints(app)

        return app
