import subprocess
import os
import sys
import time
import dbget
import outgoing
import socket
hname = socket.gethostname()
while True:
    #wait for time to be 2am local
    ctime = time.strftime("%H%M")
    if str(ctime) == (dbget.readval("*", "timeint")):
        os.system("aptitude update")
        updateslist = subprocess.getoutput("aptitude search '~U'")
        if updateslist != "":
            usrid = dbget.readval("*", "authusers")
            outgoing.sendmsg(usrid, "Updates Available for " + hname)
            outgoing.sendmsg(usrid, updateslist)
        time.sleep(60)
    else:
        time.sleep(30)
