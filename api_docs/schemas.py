from api_docs.spec import spec
from piscan.schemas import (device, scan_format, scan_file, device_options,
                            connected_device_info, image, image_details, new_device)

spec.components.schema("Device", schema=device.DeviceSchema)
# spec.components.schema("ScanFormat", schema=scan_format.ScanFormatSchema)
spec.components.schema("ScanFile", schema=scan_file.ScanFileSchema)
spec.components.schema("DeviceOptions", schema=device_options.DeviceOptionsSchema)
spec.components.schema("ConnectedDeviceInfo", schema=connected_device_info.ConnectedDeviceInfoSchema)
# spec.components.schema("Image", schema=image.ImageSchema)
# spec.components.schema("ImageDetails", schema=image_details.ImageDetailsSchema)
spec.components.schema("NewDevice", schema=new_device.NewDeviceSchema)
