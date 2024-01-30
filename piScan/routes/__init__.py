from piScan import db
from flask import current_app

from piScan.routes.core import core
from piScan.routes.api import api
from piScan.routes.docs import docs


@current_app.teardown_appcontext
def teardown_appcontext(exception=None):
    db.close_session(exception=exception)
