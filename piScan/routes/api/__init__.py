from flask import Blueprint
from piScan.routes.api.core import core
from piScan.routes.api.devices import devices


api = Blueprint("api", __name__, url_prefix="/api")

api.register_blueprint(core)
api.register_blueprint(devices, url_prefix="/devices")
