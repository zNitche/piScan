from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from piScan.schemas import device


spec = APISpec(
    title="piScan",
    version="1.0.0",
    openapi_version="3.0.2",
    info=dict(description="API for piScan system"),
    plugins=[MarshmallowPlugin()]
)

spec.components.schema("Device", schema=device.DeviceSchema)


spec.path(
    path="/api/devices",
    operations=dict(
        get=dict(
            responses={
                "200": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "array",
                                "items": "Device"
                            }
                        }
                    }
                }
            }
        )
    ),
)
