from marshmallow import Schema, fields, validate


class ConnectedDeviceInfoSchema(Schema):
    class Meta:
        dump_only = []

    name = fields.String(required=True, validate=validate.Length(min=2, max=50))
    device_id = fields.String(required=True, validate=validate.Length(min=2, max=100))
