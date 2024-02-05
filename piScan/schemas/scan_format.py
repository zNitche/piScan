from marshmallow import Schema, fields, validate


class ScanFormatSchema(Schema):
    class Meta:
        dump_only = ["uuid"]

    uuid = fields.String()
    name = fields.String(validate=validate.Length(min=3, max=5))
