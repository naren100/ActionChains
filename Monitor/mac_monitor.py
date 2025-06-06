import psutil
import time
import csv
import os
from datetime import datetime

def bytes_to_mb(b):
    return round(b / (1024 ** 2), 2)

def bytes_to_gb(b):
    return round(b / (1024 ** 3), 2)

CSV_FILE = "mac_monitor_log.csv"

# Write headers once if file doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "Timestamp", "CPU_Usage(%)", "Memory_Usage(%)", "Disk_Usage(%)",
            "Network_Sent(MB)", "Network_Recv(MB)", "Battery(%)", "Battery_Status"
        ])

try:
    while True:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        net = psutil.net_io_counters()
        battery_percent = ""
        battery_status = ""

        if hasattr(psutil, "sensors_battery"):
            battery = psutil.sensors_battery()
            if battery:
                battery_percent = battery.percent
                battery_status = "Plugged In" if battery.power_plugged else "On Battery"

        row = [
            timestamp,
            cpu,
            mem.percent,
            disk.percent,
            bytes_to_mb(net.bytes_sent),
            bytes_to_mb(net.bytes_recv),
            battery_percent,
            battery_status
        ]

        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)

        print(f"[{timestamp}] Logged system stats.")
        time.sleep(5)

except KeyboardInterrupt:
    print("\nMonitoring stopped.")




