from flask import Blueprint, Response


core_bp = Blueprint("core", __name__)


@core_bp.route("/health-check", methods=["GET"])
def health_check():
    return Response(status=200)
