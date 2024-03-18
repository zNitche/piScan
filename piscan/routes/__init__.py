from piscan import db
from flask import current_app

from piscan.routes import core
from piscan.routes import api
from piscan.routes import docs


@current_app.after_request
def after_request(response):
    # meant to be LAN only so we don't have to care about strict cors
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")

    return response


@current_app.teardown_appcontext
def teardown_appcontext(exception=None):
    db.close_session(exception=exception)
