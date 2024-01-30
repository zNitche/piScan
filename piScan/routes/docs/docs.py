from flask import Blueprint, render_template, send_file
from config import Config
import os


docs_bp = Blueprint("docs", __name__, template_folder="templates", url_prefix="/docs")


@docs_bp.route("/", methods=["GET"])
def swagger_ui():
    return render_template("/swagger_ui.html")


@docs_bp.route("/schema", methods=["GET"])
def docs_schema():
    return send_file(os.path.join(Config.CURRENT_DIR, "swagger.json"))
