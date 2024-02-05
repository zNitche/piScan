from marshmallow import Schema, fields, validate


class DeviceSchema(Schema):
    class Meta:
        dump_only = ["uuid"]

    uuid = fields.String()
    name = fields.String(validate=validate.Length(min=2, max=50))
    device_id = fields.String(validate=validate.Length(min=2, max=100))
