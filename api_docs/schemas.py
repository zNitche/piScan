from api_docs.spec import spec
from piScan.schemas import device, scan_format, scan_file, device_options


spec.components.schema("Device", schema=device.DeviceSchema)
# spec.components.schema("ScanFormat", schema=scan_format.ScanFormatSchema)
spec.components.schema("ScanFile", schema=scan_file.ScanFileSchema)
spec.components.schema("DeviceOptions", schema=device_options.DeviceOptionsSchema)
