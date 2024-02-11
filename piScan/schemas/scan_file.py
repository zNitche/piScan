from marshmallow import Schema, fields, validate


class ScanFileSchema(Schema):
    class Meta:
        dump_only = ["uuid", "created_at", "extension"]

    uuid = fields.String()
    name = fields.String(validate=validate.Length(min=0, max=100))
    extension = fields.String(validate=validate.Length(min=3, max=5))
    created_at = fields.DateTime()
