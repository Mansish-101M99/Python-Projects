# pip install - plyer, psutil
import time 
from plyer import notification
import psutil 

# This will work for Laptops

battery = psutil.sensors_battery()
pcnt = battery.percent

notification.notify(
    title="Battery percentage", message=str(pcnt)+"% battery remaining", timeout=20
)