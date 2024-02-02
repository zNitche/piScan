from marshmallow import Schema, fields, validate


class DeviceSchema(Schema):
    class Meta:
        dump_only = ["uuid"]

    uuid = fields.Str()
    name = fields.Str(validate=validate.Length(min=2, max=50))
    device_id = fields.Str(validate=validate.Length(min=2, max=100))
