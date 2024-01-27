from flask import Blueprint
from piScan.models import Printer
from piScan.schemas.device import DeviceSchema


devices = Blueprint("devices", __name__)


@devices.route("/", methods=["GET"])
def get_devices():
    schema = DeviceSchema(many=True)
    printers = schema.dump(Printer.query.all())

    return printers
