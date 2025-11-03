import shutil
import logging
import schedule
import time

logging.basicConfig(filename='disk_usage.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
def check_disk():
    # print(dir(shutil))
    disk = shutil.disk_usage("/")
    logging.info(f"Disk usage: {disk}")

    per_used = (disk.total - disk.free) / disk.total * 100
    #print(f"Percentage of disk used: {per_used:.2f}%")
    if per_used > 70:
        logging.warning("Disk usage is above 70%%")
    elif per_used > 90:
        logging.critical("Disk usage is above 90%%")
    else:
        logging.info("Disk usage is normal.")
        
check_disk()

# Schedule the disk check every 10 seconds
schedule.every(10).seconds.do(check_disk)
while True:
    schedule.run_pending()
    time.sleep(1) 