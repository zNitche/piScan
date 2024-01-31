from piScan import models


def test_printer():
    name = "TestPrinter"
    printer = models.Printer(name=name)

    assert printer.name == name
