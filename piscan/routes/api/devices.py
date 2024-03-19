from flask import Blueprint, request, Response, abort, jsonify
from marshmallow.exceptions import ValidationError
from piscan.models import Device, ScanFormat, ScanFile
from piscan.schemas.device import DeviceSchema
from piscan.schemas.connected_device_info import ConnectedDeviceInfoSchema
from piscan.schemas.new_device import NewDeviceSchema
from piscan import db, exceptions, devices_processes_manager
from piscan.utils import device_utils, images_utils

blueprint = Blueprint("devices", __name__)


@blueprint.route("/", methods=["GET"])
def get_devices():
    schema = DeviceSchema(many=True)
    printers = schema.dump(db.session.query(Device).all())

    return printers


@blueprint.route("/", methods=["POST"])
def add_device():
    try:
        schema = NewDeviceSchema().load(request.get_json())
        device = db.session.query(Device).filter_by(device_id=schema["device_id"]).first()

        if not device:
            device = Device(**schema)

            db.session.add(device)
            db.session.commit()

        return Response(status=200)

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


@blueprint.route("/<uuid>", methods=["PUT"])
def update_device(uuid):
    device = db.session.query(Device).filter_by(uuid=uuid).first()

    if not device:
        abort(404)

    try:
        schema = DeviceSchema().load(request.get_json())
        db.update_instance(device, schema)

        return Response(status=200)

    except ValidationError as e:
        return jsonify(error=str(e)), 400


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


@blueprint.route("/<uuid>/options", methods=["GET"])
def device_options(uuid):
    device = db.session.query(Device).filter_by(uuid=uuid).first()

    if not device:
        abort(404)

    options = device_utils.get_device_options(device.device_id)

    if options is None:
        return jsonify(error="device might be unavailable"), 500

    return options, 200


@blueprint.route("/<uuid>/scan/progress", methods=["GET"])
def scan_progress(uuid):
    device = db.session.query(Device).filter_by(uuid=uuid).first()

    if not device:
        abort(404)

    progress, is_running = devices_processes_manager.get_scan_progress_for_device(device.device_id)

    return jsonify(progress=progress, is_running=is_running), 200


@blueprint.route("/<uuid>/scan", methods=["POST"])
def run_scan(uuid):
    device = db.session.query(Device).filter_by(uuid=uuid).first()

    if not device:
        abort(404)

    parameters = request.get_json()

    file_name = parameters.get("file_name") or ""
    resolution = parameters.get("resolution")
    extension = parameters.get("extension")

    if resolution is None or extension is None:
        return jsonify(error="one of following parameters missing: resolution, extension"), 400

    scan_format = db.session.query(ScanFormat).filter_by(name=extension).first()

    if resolution not in device.resolutions or scan_format not in device.scan_formats:
        return jsonify(error="unsupported resolution or extension"), 400

    if devices_processes_manager.get_device_availability_state(device.device_id):
        devices_processes_manager.set_device_availability_state(device.device_id, False)
        update_progress_callback = devices_processes_manager.set_scan_progress_for_device

        file_uuid = device_utils.perform_scan(device.device_id, extension, resolution,
                                              update_progress_callback=update_progress_callback)

        devices_processes_manager.set_device_availability_state(device.device_id, True)

        if not file_uuid:
            abort(500)

        images_utils.create_thumbnail(file_uuid, extension)
        width, height, size = images_utils.get_file_details(file_uuid)

        file = ScanFile(uuid=file_uuid, name=file_name, extension=extension,
                        width=width, height=height, size=size)
        db.session.add(file)
        db.session.commit()

        return jsonify(file_uuid=file_uuid), 200

    else:
        return jsonify(error="device is currently unavailable"), 500


@blueprint.route("/list-connected", methods=["GET"])
def list_connected_devices():
    devices = device_utils.get_connected_devices()
    devices_ids_in_db = [device.device_id for device in db.session.query(Device).all()]

    for device in devices:
        device["is_added"] = device["device_id"] in devices_ids_in_db

    schema = ConnectedDeviceInfoSchema(many=True)

    return schema.dump(devices), 200
