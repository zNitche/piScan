from .api import blueprint
from .devices import blueprint as devices_bp
from .scan_formats import blueprint as scan_formats_bp


blueprint.register_blueprint(devices_bp, url_prefix="/devices")
blueprint.register_blueprint(scan_formats_bp, url_prefix="/scan-formats")
