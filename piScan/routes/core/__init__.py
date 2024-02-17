from flask import Blueprint, Response


blueprint = Blueprint("core", __name__)


@blueprint.route("/health-check", methods=["GET"])
def health_check():
    return Response(status=200)
