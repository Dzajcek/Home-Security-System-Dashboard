from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from .models import Base, SystemStat, DiskStat, NetworkDevice
from datetime import datetime

DATABASE_URL = "sqlite:///./data/monitor.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

def save_system_info(cpu: float, ram: float, disks: dict):
    db = SessionLocal()
    try:
        new_stat = SystemStat(cpu_usage=cpu, ram_usage=ram)
        db.add(new_stat)
        db.flush()

        for name, usage in disks.items():
            disk_entry = DiskStat(device_name=name, usage_percent=usage, system_stat_id=new_stat.id)
            db.add(disk_entry)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Blad zapisu do bazy: {e}")
    finally:
        db.close()

    db.commit()

def save_devices_info(devices_list: list):
    db = SessionLocal()
    try:
        for dev in devices_list:
            existing = db.query(NetworkDevice).filter(NetworkDevice.mac_address == dev['mac']).first()
            
            if existing:
                existing.ip_address = dev['ip']
                existing.last_seen = datetime.utcnow()
            else:
                new_dev = NetworkDevice(
                    mac_address=dev['mac'], 
                    ip_address=dev['ip']
                )
                db.add(new_dev)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Błąd zapisu urządzeń: {e}")
    finally:
        db.close()