from sqlalchemy import Column, Integer, String
from piScan.db import Base


class Printer(Base):
    __tablename__ = "printers"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
