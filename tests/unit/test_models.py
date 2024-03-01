from piScan import models


def test_device():
    resolutions = [200, 400, 600]
    device = models.Device(name="TestPrinter", device_id="123")
    device.resolutions = resolutions

    assert resolutions == device.resolutions
