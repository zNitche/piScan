from piScan.db import db_session
from flask import current_app


@current_app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
