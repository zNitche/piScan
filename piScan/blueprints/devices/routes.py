from flask import Blueprint, Response
from piScan.models import Printer


devices = Blueprint("devices", __name__)


@devices.route("/", methods=["GET"])
def get_devices():
    printers = Printer.query.all()

    return Response(status=200)
