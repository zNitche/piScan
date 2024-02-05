from flask import Blueprint, request, Response, abort, jsonify
from marshmallow.exceptions import ValidationError
from piScan.models import Device
from piScan.schemas.device import DeviceSchema
from piScan import db


devices_bp = Blueprint("devices", __name__)


@devices_bp.route("/", methods=["GET"])
def get_devices():
    schema = DeviceSchema(many=True)
    printers = schema.dump(db.session.query(Device).all())

    return printers


@devices_bp.route("/", methods=["POST"])
def add_device():
    try:
        schema = DeviceSchema().load(request.get_json())
        device = Device(**schema)

        db.session.add(device)
        db.session.commit()

        return Response(status=201)

    except ValidationError as e:
        return jsonify(error=str(e)), 400


@devices_bp.route("/<uuid>", methods=["GET"])
def get_device(uuid):
    device = db.session.query(Device).filter_by(uuid=uuid).first()

    if not device:
        abort(404)

    schema = DeviceSchema()
    dumped_device = schema.dump(device)

    return dumped_device


@devices_bp.route("/<uuid>", methods=["DELETE"])
def remove_device(uuid):
    device = db.session.query(Device).filter_by(uuid=uuid).first()

    if not device:
        abort(404)

    db.session.delete(device)
    db.session.commit()

    return Response(status=200)
