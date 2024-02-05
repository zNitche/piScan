from sqlalchemy import Column, Integer, String
from piScan.database.db import Base
import uuid


class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True)
    uuid = Column(String(32), unique=True, default=lambda: uuid.uuid4().hex)
    name = Column(String(50), unique=True)
    device_id = Column(String(100), unique=True)


class ScanFormat(Base):
    __tablename__ = "scan_formats"

    id = Column(Integer, primary_key=True)
    uuid = Column(String(32), unique=True, default=lambda: uuid.uuid4().hex)
    name = Column(String(5), unique=True)
