from marshmallow import Schema, fields, validate
from piScan.schemas.image import ImageSchema
from piScan.schemas.image_details import ImageDetailsSchema


class ScanFileSchema(Schema):
    class Meta:
        dump_only = ["uuid", "created_at", "extension", "image", "details"]

    uuid = fields.String()
    name = fields.String(validate=validate.Length(min=0, max=100))
    extension = fields.String(validate=validate.Length(min=3, max=5))
    created_at = fields.DateTime()
    image = fields.Nested(ImageSchema)
    details = fields.Nested(ImageDetailsSchema)