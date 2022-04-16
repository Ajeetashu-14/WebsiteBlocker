import time
from datetime import datetime as d
temp_host ="hosts"
host_path="C:\Windows\System32\drivers\etc\hosts"
ip="127.0.0.1"
site_list=[""]

while True:
    if d(d.now().year,d.now().month,d.now().day,22) < d.now() < d(d.now().year,d.now().month,d.now().day,23):
        print("working")
        with open(temp_host,'r+') as file:
            content=file.read()
            for site in site_list:
                if site in content:
                    pass
                else:
                    file.write(ip + " " + site + "\n")
    else:
        with open(temp_host,'r+') as file:
            content=file.readline()
            file.seek(0)
            for line in content:
                if not any(site in line for site in site_list):
                    file.write(line)
            file.truncate()
        print("fun time")
    time.sleep(5)