from flask import Blueprint, request, Response, abort, jsonify
from marshmallow.exceptions import ValidationError
from piScan.models import ScanFormat
from piScan.schemas.scan_format import ScanFormatSchema
from piScan import db


scan_formats_bp = Blueprint("scan_formats", __name__)


@scan_formats_bp.route("/", methods=["GET"])
def get_scan_formats():
    schema = ScanFormatSchema(many=True)
    formats = schema.dump(db.session.query(ScanFormat).all())

    return formats


@scan_formats_bp.route("/", methods=["POST"])
def add_scan_format():
    try:
        schema = ScanFormatSchema().load(request.get_json())
        device = ScanFormat(**schema)

        db.session.add(device)
        db.session.commit()

        return Response(status=201)

    except ValidationError as e:
        return jsonify(error=str(e)), 400


@scan_formats_bp.route("/<uuid>", methods=["GET"])
def get_scan_format(uuid):
    format = db.session.query(ScanFormat).filter_by(uuid=uuid).first()

    if not format:
        abort(404)

    schema = ScanFormatSchema()

    return schema.dump(format)


@scan_formats_bp.route("/<uuid>", methods=["DELETE"])
def remove_scan_format(uuid):
    format = db.session.query(ScanFormat).filter_by(uuid=uuid).first()

    if not format:
        abort(404)

    db.session.delete(format)
    db.session.commit()

    return Response(status=200)
