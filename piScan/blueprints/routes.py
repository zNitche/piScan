from piScan import db
from flask import current_app


@current_app.teardown_appcontext
def teardown_appcontext(exception=None):
    db.close_session(exception=exception)
