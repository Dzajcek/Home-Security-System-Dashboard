import psutil

def get_system_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    partitions = psutil.disk_partitions()
    disks_usage = {}
    for p in partitions:
        try:
            mountpoint = p.mountpoint
            usage = psutil.disk_usage(mountpoint).percent
            disks_usage[p.device] = usage
        except:
            continue
    

    return {"CPU": cpu_percent, "RAM": ram, "DISKS": disks_usage}

if __name__ == "__main__":
    info = get_system_info()
    print(info)