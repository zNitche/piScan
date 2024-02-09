from flask import Blueprint, render_template, send_file
from configs.config import Config


blueprint = Blueprint("docs", __name__, template_folder="templates", url_prefix="/docs")


@blueprint.route("/", methods=["GET"])
def swagger_ui():
    return render_template("/swagger_ui.html")


@blueprint.route("/schema", methods=["GET"])
def docs_schema():
    return send_file(Config.SWAGGER_SCHEMA_PATH)
