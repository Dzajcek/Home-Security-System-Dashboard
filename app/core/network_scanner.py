import scapy.all as scapy
from dotenv import load_dotenv
import os

def scanner():
    load_dotenv()
    SCAN_IP = os.getenv("SCAN_IP")

    arp_requests = scapy.ARP(pdst=SCAN_IP)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_requests

    clients_list = []

    answered_list = scapy.srp(packet, timeout=1, verbose=False)[0]
    for element in answered_list:
        device_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(device_info)

    return clients_list