from api_docs.spec import spec
from piScan.schemas import device


spec.components.schema("Device", schema=device.DeviceSchema)
