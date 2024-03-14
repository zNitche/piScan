from api_docs.spec import spec
from piScan.schemas import (device, scan_format, scan_file, device_options,
                            connected_device_info, image, image_details)


spec.components.schema("Device", schema=device.DeviceSchema)
# spec.components.schema("ScanFormat", schema=scan_format.ScanFormatSchema)
spec.components.schema("ScanFile", schema=scan_file.ScanFileSchema)
spec.components.schema("DeviceOptions", schema=device_options.DeviceOptionsSchema)
spec.components.schema("ConnectedDeviceInfoSchema", schema=connected_device_info.ConnectedDeviceInfoSchema)
# spec.components.schema("ImageSchema", schema=image.ImageSchema)
# spec.components.schema("ImageSchema", schema=image_details.ImageDetailsSchema)
