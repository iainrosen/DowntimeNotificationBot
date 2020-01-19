import subprocess
import os
import sys
import time
import dbget
import outgoing
import socket
force = False
hname = socket.gethostname()
if sys.argv[1]:
    #cli mode
    if sys.argv[1] == "force":
        force = True
while True:
    #wait for time to be 2am local
    ctime = time.strftime("%H%M")
    if str(ctime) == (dbget.readval("*", "timeint")) or force == True:
        os.system("aptitude update")
        updateslist = subprocess.getoutput("aptitude search '~U'")
        if updateslist != "":
            usrid = dbget.readval("*", "authusers")
            outgoing.sendmsg(usrid, "Updates Available for " + hname)
            outgoing.sendmsg(usrid, updateslist)
        if updateslist == "" and force == True:
            usrid = dbget.readval("*", "authusers")
            outgoing.sendmsg(usrid, "No Updates Available for " + hname)
        time.sleep(60)
        if force == True:
            break
    else:
        time.sleep(30)
