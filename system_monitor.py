import psutil
import logging
import smtplib
from datetime import datetime
import time
import config
from config import *

#Configure logging
logging.basicConfig(filename='system_monitor.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# Define email otification function
def send_email(subject, message):
    sender_email = SENDER_EMAIL 
    receiver_email = RECIPIENT_EMAIL
    password = EMAIL_PASSWORD

    # create email message
    email_message = f"Subject: {subject}\n\n{message}"

    # send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, email_message)

# Mondify monitor_system to include alerting logic
def monitor_system():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent

    #Log the system resources data
    logging.info(f"CPU Usage: {cpu_percent}% | Memory Usage: {memory_percent}% | Disk Usage: {disk_percent}%")

    #Check thresholds and trigger alerts 
    if cpu_percent > CPU_THRESHOLD:
        send_email("High CPU Usage Alert", f"CPU Usage exceeded threshold: {cpu_percent}%")
    if memory_percent > MEMORY_THRESHOLD:
        send_email("High Memory Usage Alert", f"Memory Usage exceeded threshold: {memory_percent}%")
    if disk_percent > DISK_THRESHOLD:
        send_email("High Disk Usage Alert", f"Disk Usage exceeded threshold: {disk_percent}%")

def  main():
    while True:
        try:
            monitor_system()
            time.sleep(3600) #log data every hour (in secs)
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
    
if __name__ == '__main__':
    main()
