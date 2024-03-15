from piScan import db
from flask import current_app

from piScan.routes import core
from piScan.routes import api
from piScan.routes import docs


@current_app.after_request
def after_request(response):
    # meant to be LAN only so we don't have to care about strict cors
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Methods", "GET,POST,PATCH,PUT,DELETE,OPTIONS")
    response.headers.add("Access-Control-Allow-Headers", "Origin,Content-Type")

    return response


@current_app.teardown_appcontext
def teardown_appcontext(exception=None):
    db.close_session(exception=exception)
