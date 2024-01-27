from marshmallow import Schema, fields


class DeviceSchema(Schema):
    name = fields.Str()
