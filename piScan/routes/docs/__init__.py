from flask import Blueprint, render_template, send_file
from config import Config
import os


docs = Blueprint("docs", __name__, template_folder="templates", url_prefix="/docs")


@docs.route("/", methods=["GET"])
def swagger_ui():
    return render_template("/swagger_ui.html")


@docs.route("/schema", methods=["GET"])
def docs_schema():
    return send_file(os.path.join(Config.CURRENT_DIR, "swagger.json"))
