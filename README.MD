# 🛡️ Home Security & System Dashboard

Zaawansowane narzędzie do monitorowania zasobów systemowych oraz analizy bezpieczeństwa sieci lokalnej (ARP scanning) z interfejsem REST API.

## 🚀 Nowości w wersji 2.0 (Debian Edition)
- **REST API:** Dodano interfejs FastAPI do przeglądania danych w formacie JSON.
- **Trwała Retencja:** Pełna integracja z bazą SQLite przez SQLAlchemy (ORM).
- **Network History:** Śledzenie urządzeń w sieci z automatyczną aktualizacją czasu ostatniej aktywności (last seen).

## 🛠️ Tech Stack
- **Backend:** Python 3.12+ (Debian 12 optimized)
- **API Framework:** FastAPI + Uvicorn
- **Biblioteki:** Scapy (Network), Psutil (System)
- **Baza danych:** SQLite + SQLAlchemy

## 📂 Struktura Projektu
- `app/core/`: Silniki skanowania i zbierania statystyk.
- `app/database/`: Modele ORM i logika zapisu danych.
- `app/api/`: Endpointy FastAPI.
- `app/main.py`: Skrypt zbierający dane (wymaga sudo).



## ⚙️ Instalacja i Automatyzacja (Debian)

### 1. Środowisko wirtualne:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

### 1. Zmienne środowiskowe
Skopiuj plik `.env.example` do `.env` i uzupełnij dane:
`cp app/core/.env.example app/core/.env`

### 2. Automatyczny start (Systemd)
Aby projekt działał w tle i startował przy bootowaniu systemu:
1. Skopiuj konfigurację z `home_security.service.example` do `/etc/systemd/system/home_security.service`.
2. Przeładuj system: `sudo systemctl daemon-reload`.
3. Uruchom usługę: `sudo systemctl enable --now home_security`.

### 3. Monitoring
Sprawdź status usługi:
`sudo systemctl status home_security`