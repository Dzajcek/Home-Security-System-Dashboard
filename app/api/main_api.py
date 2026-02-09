from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from ..database.database import SessionLocal
from ..database.models import SystemStat
from ..database.models import NetworkDevice

app = FastAPI()

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

