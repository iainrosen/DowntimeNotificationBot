import os
import time
import sys
import outgoing
import socket
import subprocess
hname = socket.gethostname()
netfail = 0
servicefail = 0
servicewatch = ["downtime", "apache2"] #add the services you want to watch here

while True:
    #check for server failures
    for i in servicewatch:
        checksvc = "systemctl is-active " + i
        if (subprocess.getoutput(checksvc)) == "inactive":
            print("Service Failed!")
    time.sleep(2)
