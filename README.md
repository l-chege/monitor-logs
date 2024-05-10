# System Resource Monitoring Script

- This project aims to develop a Python Script that monitors local system resources (CPU usage, memory usage and disk usage) and logs the info to a file every hour. 
- It automates the exection of the scrit using 'cron' on Unix-based system.

## Prerequisites
- Have Python 3.x installed

### Installation
1. Clone this repo to your local machine 

```bash
git clone https://github.com/your-username/your-repo.git
```
### Usage
1. Run python script:

```bash 
python system_monitor.py
```
2. Verify logs, check the 'system_monitor.log' file. It should contain logged data about CPU, memory and disk usage every hour.

### Automate Script Execution
- Using 'cron expression' on Unix-based systems.
