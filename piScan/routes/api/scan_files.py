from flask import Blueprint, request, Response, abort, jsonify, send_file, url_for
from marshmallow.exceptions import ValidationError
from piScan.models import ScanFile
from piScan.schemas.scan_file import ScanFileSchema
from piScan import db
from piScan.utils import files_utils
from piScan.services import scan_files_service

blueprint = Blueprint("scan_files", __name__)


@blueprint.route("/", methods=["GET"])
def get_scan_files():
    limit = request.args.get("limit") or 20
    offset = request.args.get("offset") or 0
    order_param = request.args.get("order")
    search_string = request.args.get("search") or ""

    order = order_param if order_param in ["desc", "asc"] else "desc"
    order_by = ScanFile.created_at

    schema = ScanFileSchema(many=True)
    files = (db.session.query(ScanFile)
             .order_by(order_by.desc() if order == "desc" else order_by.asc())
             .filter(ScanFile.name.contains(search_string))
             .limit(limit)
             .offset(offset))

    response_files = [scan_files_service.get_scan_file_with_details(file) for file in files]

    return schema.dump(response_files)


@blueprint.route("/<uuid>", methods=["GET"])
def get_scan_file(uuid):
    file = db.session.query(ScanFile).filter_by(uuid=uuid).first()

    if not file:
        abort(404)

    schema = ScanFileSchema()

    return schema.dump(scan_files_service.get_scan_file_with_details(file))


@blueprint.route("/<uuid>/download", methods=["GET"])
def download_scan_file(uuid):
    file = db.session.query(ScanFile).filter_by(uuid=uuid).first()

    if not file:
        abort(404)

    file_name = f"{file.name if file.name else file.uuid}.{file.extension}"
    file_path = files_utils.get_path_to_file(file.uuid)

    return send_file(path_or_file=file_path, as_attachment=True, download_name=file_name)


@blueprint.route("/<uuid>/preview", methods=["GET"])
def scan_file_preview(uuid):
    show_thumbnail_param = request.args.get("thumbnail")
    show_thumbnail = int(show_thumbnail_param) if show_thumbnail_param else None

    file = db.session.query(ScanFile).filter_by(uuid=uuid).first()

    if not file:
        abort(404)

    file_path = files_utils.get_path_to_file(file.uuid) if not show_thumbnail \
        else files_utils.get_path_to_thumbnail(file.uuid)

    file_name = f"{file_path}.{file.extension}"

    return send_file(path_or_file=file_path, download_name=file_name,
                     mimetype=f"image/{file.extension}", as_attachment=False)


@blueprint.route("/<uuid>", methods=["PUT"])
def update_scan_file(uuid):
    file = db.session.query(ScanFile).filter_by(uuid=uuid).first()

    if not file:
        abort(404)

    try:
        schema = ScanFileSchema().load(request.get_json())
        db.update_instance(file, schema)

        return Response(status=200)

    except ValidationError as e:
        return jsonify(error=str(e)), 400


@blueprint.route("/<uuid>", methods=["DELETE"])
def remove_scan_file(uuid):
    file = db.session.query(ScanFile).filter_by(uuid=uuid).first()

    if not file:
        abort(404)

    db.session.delete(file)
    db.session.commit()

    return Response(status=200)
