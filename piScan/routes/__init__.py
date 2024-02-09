from piScan import db
from flask import current_app

from piScan.routes import core
from piScan.routes import api
from piScan.routes import docs


@current_app.after_request
def after_request(response):
    return response


@current_app.teardown_appcontext
def teardown_appcontext(exception=None):
    db.close_session(exception=exception)
