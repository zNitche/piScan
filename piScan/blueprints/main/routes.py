from flask import Blueprint, Response


main = Blueprint("main", __name__)


@main.route("/health-check", methods=["GET"])
def health_check():
    return Response(status=200)
