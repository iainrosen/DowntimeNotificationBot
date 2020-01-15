import os
import time
import sys
import outgoing
import socket
hname = socket.gethostname()
netfail = 0
servicefail = 0
servicewatch = [] #add the services you want to watch here

while True:
    #check for server failures
    for i in range(servicewatch):
        checksvc = "systemctl is-active " + servicewatch[i]
        if (os.Popen(checksvc).read) == "inactive":
            print("Service Failed!")
