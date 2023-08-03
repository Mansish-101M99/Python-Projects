# pip install psutil
import psutil

cpu = psutil.cpu_count()
print("cpu count : ",cpu)

while True:
    cpu_pcnt = psutil.cpu_percent(1)   # ------->> 1 as parameter shows usage percent per second
    print("Usage percent (now) :- ", cpu_pcnt)