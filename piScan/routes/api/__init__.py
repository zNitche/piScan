from .api import api_bp
from .devices import devices_bp


api_bp.register_blueprint(devices_bp, url_prefix="/devices")
