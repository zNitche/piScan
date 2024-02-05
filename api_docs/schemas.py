from api_docs.spec import spec
from piScan.schemas import device, scan_format


spec.components.schema("Device", schema=device.DeviceSchema)
# spec.components.schema("ScanFormat", schema=scan_format.ScanFormatSchema)
