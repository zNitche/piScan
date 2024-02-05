from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, mapped_column
from piScan.database.db import Base
import uuid

device_format = Table(
    "device_format",
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

    scan_formats = relationship("ScanFormat", secondary=device_format, backref="device")


class ScanFormat(Base):
    __tablename__ = "scan_formats"

    id = mapped_column(Integer, primary_key=True)
    uuid = Column(String(32), unique=True, default=lambda: uuid.uuid4().hex)
    name = Column(String(5), unique=True)
