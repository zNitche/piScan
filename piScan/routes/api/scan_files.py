from flask import Blueprint, request, Response, abort, jsonify, send_file
from marshmallow.exceptions import ValidationError
from piScan.models import ScanFile
from piScan.schemas.scan_file import ScanFileSchema
from piScan import db
from piScan.utils import files_utils

blueprint = Blueprint("scan_files", __name__)


@blueprint.route("/", methods=["GET"])
def get_scan_files():
    schema = ScanFileSchema(many=True)
    files = schema.dump(db.session.query(ScanFile).all())

    return files


@blueprint.route("/<uuid>", methods=["GET"])
def get_scan_file(uuid):
    file = db.session.query(ScanFile).filter_by(uuid=uuid).first()

    if not file:
        abort(404)

    schema = ScanFileSchema()

    return schema.dump(file)


@blueprint.route("/<uuid>/download", methods=["GET"])
def download_scan_file(uuid):
    file = db.session.query(ScanFile).filter_by(uuid=uuid).first()

    if not file:
        abort(404)

    file_name = f"{file.name if file.name else file.uuid}.{file.extension}"
    file_path = files_utils.get_path_to_file(file.uuid)

    return send_file(path_or_file=file_path, as_attachment=True, download_name=file_name)


@blueprint.route("/<uuid>/preview", methods=["GET"])
def get_scan_file_preview(uuid):
    file = db.session.query(ScanFile).filter_by(uuid=uuid).first()

    if not file:
        abort(404)

    file_path = files_utils.get_path_to_file(file.uuid)
    download_name = f"{file_path}.{file.extension}"

    return send_file(path_or_file=file_path, download_name=download_name,
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
