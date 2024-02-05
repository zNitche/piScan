from .api import api_bp
from .devices import devices_bp
from .scan_formats import scan_formats_bp


api_bp.register_blueprint(devices_bp, url_prefix="/devices")
api_bp.register_blueprint(scan_formats_bp, url_prefix="/scan-formats")
