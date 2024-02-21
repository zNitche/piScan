from marshmallow import Schema, fields


class DeviceOptionParametersSchema(Schema):
    name = fields.String()
    description = fields.String()


class DeviceOptionSchema(Schema):
    name = fields.String()
    parameters = fields.Nested(DeviceOptionParametersSchema, many=True)


class DeviceOptionsSchema(Schema):
    header = fields.String()
    options = fields.Nested(DeviceOptionSchema, many=True)
