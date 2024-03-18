from marshmallow import Schema, fields


class ImageDetailsSchema(Schema):
    class Meta:
        dump_only = ["width", "height", "size"]

    width = fields.Integer()
    height = fields.Integer()
    size = fields.Integer()
