from core.system_stats import get_system_info
from core.network_scanner import scanner
from database.database import init_db, save_system_info

def display():
    info = get_system_info()
    clients_list = scanner()

    print("-" * 30)
    print("STATYSTYKI SYSTEMU")
    print("-" * 30)
    for element, value in info.items():
        if isinstance(value, dict):
            print("=== Dyski ===")
            for disk, percent in value.items():
                print(f"{disk}: {percent}%")
            print("=============")
            continue
        print(f"{element}: {value}%")
        
    print("=== URZĄDZENIA W SIECI ===")
    for device in clients_list:
        print(f"IP: {device['ip']}, MAC: {device['mac']}")

    return info, clients_list

def main():
    init_db()

    info, devices = display()

    save_system_info(info["CPU"], info["RAM"], info["DISKS"])
    print("\nDane zostaly zapisane do bazy danych.")
if __name__ == "__main__":
    main()