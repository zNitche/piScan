from marshmallow import Schema, fields


class ImageSchema(Schema):
    class Meta:
        dump_only = ["preview_url", "download_url", "thumbnail_url"]

    preview_url = fields.Url()
    thumbnail_url = fields.Url()
    download_url = fields.Url()
