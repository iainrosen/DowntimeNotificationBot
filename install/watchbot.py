import os
import time
import sys
import outgoing
import socket
import subprocess
import dbget
userid = dbget.readval("*", "authusers")
hname = socket.gethostname()
netfail = 0
servicefail = 0
servicewatch = ["downtime", "apache2"] #add the services you want to watch here
failed = []
while True:
    #check for server failures
    for i in servicewatch:
        checksvc = "systemctl is-active " + i
        if (subprocess.getoutput(checksvc)) == "inactive" and i not in failed:
            failed.append(i)
            msg = "Service: " + i + " on " + hname + " has failed!"
            outgoing.sendmsg(userid, msg)
        elif (subprocess.getoutput(checksvc)) != "inactive" and i in failed:
            failed.remove(i)
    time.sleep(2)
