from flask import Blueprint
from piScan.models import Printer
from piScan.schemas.device import DeviceSchema
from piScan import db


devices = Blueprint("devices", __name__)


@devices.route("/", methods=["GET"])
def get_devices():
    schema = DeviceSchema(many=True)

    with db.session() as session:
        printers = schema.dump(session.query(Printer).all())

    return printers
