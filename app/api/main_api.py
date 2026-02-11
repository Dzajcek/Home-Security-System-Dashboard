from fastapi import FastAPI, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from ..database.database import SessionLocal, save_system_info, save_devices_info
from ..database.models import SystemStat, NetworkDevice
from ..core.system_stats import get_system_info
from ..core.network_scanner import scanner

app = FastAPI()

def perform_full_scan():
    print("[LOG] Rozpoczynanie automatycznego zbierania danych...")
    sys_info = get_system_info()
    net_info = scanner()
    save_system_info(sys_info["CPU"], sys_info["RAM"], sys_info["DISKS"])
    save_devices_info(net_info)
    print("[LOG] Odswiezono dane.")

@app.get("/scan")
async def trigger_scan(background_tasks: BackgroundTasks):
    background_tasks.add_task(perform_full_scan)
    return {"message": "Skanowanie uruchomione w tle. Odswiez /stats lub /devices za chwile."}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/stats")
def read_stats(db: Session = Depends(get_db)):
    stats = db.query(SystemStat).all()
    return stats

@app.get("/devices")
def read_devices(db: Session = Depends(get_db)):
    devices = db.query(NetworkDevice).all()
    return devices

