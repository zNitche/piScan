from piScan.routes.api.api import api
from piScan.routes.api.devices import devices


api.register_blueprint(devices, url_prefix="/devices")
