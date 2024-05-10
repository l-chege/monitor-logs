import psutil
import logging
from datetime import datetime
import time

#Configure logging
logging.basicConfig(filename='system_monitor.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

def monitor_system():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent

    #Log the system resources data
    logging.info(f"CPU Usage: {cpu_percent}% | Memory Usage: {memory_percent}% | Disk Usage: {disk_percent}%")

def  main():
    while True:
        monitor_system()
        time.sleep(3600) #log data every hour (in secs)

if __name__ == '__main__':
    main()
