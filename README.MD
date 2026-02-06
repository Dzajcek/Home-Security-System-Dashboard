# 🛡️ Home Security & System Dashboard

Narzędzie do monitorowania zasobów systemowych oraz analizy bezpieczeństwa sieci lokalnej z trwałą retencją danych.

## 🚀 O projekcie
Projekt łączy monitorowanie wydajności hosta z aktywnym skanowaniem sieci ARP. Dane są gromadzone w relacyjnej bazie danych, co pozwala na późniejszą analizę incydentów i trendów wydajnościowych.

## 🛠️ Tech Stack
- **Język:** Python 3.12+
- **Biblioteki:** Scapy, Psutil, python-dotenv
- **Baza danych:** SQLite + SQLAlchemy (ORM)

## ⚙️ Uruchomienie
1. Zainstaluj wymagania: `pip install -r requirements.txt`
2. Skonfiguruj plik `.env` na podstawie `.env.example`.
3. Uruchom główną aplikację: `python app/main.py` (wymaga uprawnień administratora dla Scapy).