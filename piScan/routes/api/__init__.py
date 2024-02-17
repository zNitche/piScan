from flask import Blueprint

from .devices import blueprint as devices_bp
from .scan_formats import blueprint as scan_formats_bp
from .scan_files import blueprint as scan_files_bp


blueprint = Blueprint("api", __name__, url_prefix="/api")

blueprint.register_blueprint(devices_bp, url_prefix="/devices")
blueprint.register_blueprint(scan_formats_bp, url_prefix="/scan-formats")
blueprint.register_blueprint(scan_files_bp, url_prefix="/scan-files")
