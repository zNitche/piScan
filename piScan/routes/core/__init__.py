from flask import Blueprint, Response


core = Blueprint("core", __name__)


@core.route("/health-check", methods=["GET"])
def health_check():
    return Response(status=200)
