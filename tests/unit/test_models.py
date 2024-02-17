from piScan import models


def test_printer():
    name = "TestPrinter"
    printer = models.Device(name=name)

    assert printer.name == name
