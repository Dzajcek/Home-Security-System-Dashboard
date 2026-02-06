from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class SystemStat(Base):
    __tablename__ = "system_stats"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    cpu_usage = Column(Float, nullable=False)
    ram_usage = Column(Float, nullable=False)

    disks = relationship("DiskStat", back_populates="parent_stat")

class DiskStat(Base):
    __tablename__ = "disk_stats"

    id = Column(Integer, primary_key=True)
    system_stat_id = Column(Integer, ForeignKey("system_stats.id"))
    device_name = Column(String(50))
    usage_percent = Column(Float)

    parent_stat = relationship("SystemStat", back_populates="disks")

class NetworkDevice(Base):
    __tablename__ = "network_devices"

    id = Column(Integer, primary_key=True)
    mac_address = Column(String(17), unique=True)
    ip_address = Column(String(15))
    last_seen = Column(DateTime, default=datetime.utcnow)