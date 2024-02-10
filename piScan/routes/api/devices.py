from flask import Blueprint, request, Response, abort, jsonify, current_app
from marshmallow.exceptions import ValidationError
from piScan.models import Device, ScanFormat
from piScan.schemas.device import DeviceSchema
from piScan import db, exceptions
from piScan.utils import device_utils


blueprint = Blueprint("devices", __name__)


@blueprint.route("/", methods=["GET"])
def get_devices():
    schema = DeviceSchema(many=True)
    printers = schema.dump(db.session.query(Device).all())

    return printers


@blueprint.route("/", methods=["POST"])
def add_device():
    try:
        schema = DeviceSchema().load(request.get_json())
        device = Device(**schema)

        db.session.add(device)
        db.session.commit()

        return Response(status=201)

    except ValidationError as e:
        return jsonify(error=str(e)), 400


@blueprint.route("/<uuid>", methods=["GET"])
def get_device(uuid):
    device = db.session.query(Device).filter_by(uuid=uuid).first()

    if not device:
        abort(404)

    schema = DeviceSchema()
    dumped_device = schema.dump(device)

    return dumped_device


@blueprint.route("/<uuid>", methods=["DELETE"])
def remove_device(uuid):
    device = db.session.query(Device).filter_by(uuid=uuid).first()

    if not device:
        abort(404)

    db.session.delete(device)
    db.session.commit()

    return Response(status=200)


@blueprint.route("/<device_uuid>/format/<format_uuid>", methods=["POST"])
def add_scan_format_to_device(device_uuid, format_uuid):
    device = db.session.query(Device).filter_by(uuid=device_uuid).first()
    scan_format = db.session.query(ScanFormat).filter_by(uuid=format_uuid).first()

    if not device or not scan_format:
        abort(404)

    if scan_format not in device.scan_formats:
        device.scan_formats.append(scan_format)
        db.session.commit()

        return Response(status=200)

    abort(400)


@blueprint.route("/<device_uuid>/format/<format_uuid>", methods=["DELETE"])
def remove_scan_format_for_device(device_uuid, format_uuid):
    device = db.session.query(Device).filter_by(uuid=device_uuid).first()
    scan_format = db.session.query(ScanFormat).filter_by(uuid=format_uuid).first()

    if not device or not scan_format:
        abort(404)

    if scan_format in device.scan_formats:
        device.scan_formats.remove(scan_format)
        db.session.commit()

        return Response(status=200)

    abort(400)


@blueprint.route("/<uuid>/resolutions", methods=["POST"])
def add_scan_resolution_for_device(uuid):
    device = db.session.query(Device).filter_by(uuid=uuid).first()

    if not device:
        abort(404)

    try:
        device.resolutions = request.get_json()
        db.session.commit()

    except exceptions.ModelValidationError as e:
        return jsonify(error=str(e)), 400

    return Response(status=200)


@blueprint.route("/<uuid>/health-check", methods=["GET"])
def device_health_check(uuid):
    device = db.session.query(Device).filter_by(uuid=uuid).first()

    if not device:
        abort(404)

    is_available = device_utils.check_device_availability(device.device_id)

    return jsonify(is_available=is_available), 200


@blueprint.route("/<uuid>/scan", methods=["POST"])
def run_scan(uuid):
    device = db.session.query(Device).filter_by(uuid=uuid).first()

    if not device:
        abort(404)

    parameters = request.get_json()
    resolution = parameters.get("resolution")
    extension = parameters.get("extension")

    if resolution is None or extension is None:
        return jsonify(error="one of following parameters missing: resolution, extension"), 400

    scan_format = db.session.query(ScanFormat).filter_by(name=extension).first()

    if resolution not in device.resolutions or scan_format not in device.scan_formats:
        return jsonify(error="unsupported resolution or extension"), 400

    file_uuid = device_utils.perform_scan(device.device_id, current_app.config["SCAN_FILES_DIR_PATH"],
                                          extension, resolution)

    return Response(status=200 if file_uuid else 400)
