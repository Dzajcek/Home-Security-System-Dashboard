# 🛡️ Home Security & System Dashboard

Narzędzie do monitorowania zasobów systemowych oraz analizy bezpieczeństwa sieci lokalnej.

## 🚀 O projekcie
Projekt łączy monitorowanie wydajności hosta z pasywnym i aktywnym skanowaniem sieci w celu wykrywania urządzeń. Budowany z naciskiem na architekturę, bezpieczeństwo danych i konteneryzację.

## 🛠️ Tech Stack
- **Język:** Python 3.12+
- **Biblioteki:** Scapy (Network), Psutil (System), Dotenv (Config)

## ⚙️ Uruchomienie
1. Zainstaluj wymagania: `pip install -r requirements.txt`
2. Skonfiguruj plik `.env` (użyj `.env.example` jako wzoru).
3. Uruchom skaner: `python app/core/network_scanner.py` (wymaga uprawnień admina).