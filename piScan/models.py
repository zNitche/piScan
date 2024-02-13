from sqlalchemy import Column, Integer, String, Table, ForeignKey, DATETIME
from sqlalchemy.orm import relationship, mapped_column
from piScan.database.db import Base
from piScan import exceptions
import uuid
from datetime import datetime

device_to_format = Table(
    "device_to_format",
    Base.metadata,
    Column("device_id", ForeignKey("devices.id")),
    Column("format_id", ForeignKey("scan_formats.id")),
)


class Device(Base):
    __tablename__ = "devices"

    id = mapped_column(Integer, primary_key=True)
    uuid = Column(String(32), unique=True, default=lambda: uuid.uuid4().hex)
    name = Column(String(50), unique=True)
    device_id = Column(String(100), unique=True)
    _resolutions = Column("resolutions", String)

    scan_formats = relationship("ScanFormat", secondary=device_to_format, backref="device")

    @property
    def resolutions(self):
        items = self._resolutions.split(",") if self._resolutions else []

        return [int(item) for item in items]

    @resolutions.setter
    def resolutions(self, resolutions_list):
        is_valid = True if (isinstance(resolutions_list, list) and
                            all(isinstance(res, int) for res in resolutions_list)) else False

        if not is_valid:
            raise exceptions.ModelValidationError("resolutions validation error, "
                                                  "should be array of integers")

        self._resolutions = ",".join([str(elem) for elem in resolutions_list])


class ScanFormat(Base):
    __tablename__ = "scan_formats"

    id = mapped_column(Integer, primary_key=True)
    uuid = Column(String(32), unique=True, default=lambda: uuid.uuid4().hex)
    name = Column(String(5), unique=True)


class ScanFile(Base):
    __tablename__ = "scan_files"

    id = mapped_column(Integer, primary_key=True)
    uuid = Column(String(32), unique=True, default=lambda: uuid.uuid4().hex)
    name = Column(String(100))
    extension = Column(String(5))
    width = Column(Integer)
    height = Column(Integer)
    size = Column(Integer)
    created_at = Column(DATETIME, default=datetime.now)
