from marshmallow import Schema, fields, validate


class NewDeviceSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=2, max=50))
    device_id = fields.String(required=True, validate=validate.Length(min=2, max=100))
