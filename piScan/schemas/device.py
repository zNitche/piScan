from marshmallow import Schema, fields, validate
from piScan.schemas.scan_format import ScanFormatSchema


class DeviceSchema(Schema):
    class Meta:
        dump_only = ["uuid", "scan_formats", "resolutions"]

    uuid = fields.String()
    name = fields.String(required=True, validate=validate.Length(min=2, max=50))
    device_id = fields.String(required=True, validate=validate.Length(min=2, max=100))
    resolutions = fields.List(fields.Number())

    scan_formats = fields.Nested(ScanFormatSchema, many=True)
