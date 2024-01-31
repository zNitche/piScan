from piScan import db
from flask import current_app

from piScan.routes.core import core_bp
from piScan.routes.api import api_bp
from piScan.routes.docs import docs_bp


@current_app.after_request
def after_request(response):
    return response


@current_app.teardown_appcontext
def teardown_appcontext(exception=None):
    db.close_session(exception=exception)
