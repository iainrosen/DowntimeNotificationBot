import subprocess
import os
import sys
import time
import dbget
import socket
import telepot
def sendmsg(userid, message):
    try:
        token = dbget.readval("*", "api")
        bot = telepot.Bot(token)
        bot.sendMessage(userid, message)
        return 0
    except:
        return 1
force = False
hname = socket.gethostname()
if sys.argv[1]:
    #cli mode
    if sys.argv[1] == "force":
        force = True
while True:
    ctime = time.strftime("%H%M")
    if str(ctime) == (dbget.readval("*", "timeint")) or force is True:
        os.system("aptitude update")
        updateslist = subprocess.getoutput("aptitude search '~U'")
        if updateslist != "":
            usrid = dbget.readval("*", "authusers")
            sendmsg(usrid, "Updates Available for " + hname)
            sendmsg(usrid, updateslist)
        if updateslist == "" and force is True:
            usrid = dbget.readval("*", "authusers")
            sendmsg(usrid, "No Updates Available for " + hname)
        time.sleep(60)
        if force is True:
            break
    else:
        time.sleep(30)
