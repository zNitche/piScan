from flask import Blueprint
from piScan.models import Printer
from piScan.schemas.device import DeviceSchema
from piScan import db


devices = Blueprint("devices", __name__)


@devices.route("/", methods=["GET"])
def get_devices():
    schema = DeviceSchema(many=True)
    printers = schema.dump(db.session.query(Printer).all())

    return printers
