import subprocess
import os
import sys
import time
import dbget
import socket
import telepot
import sqlite3
def sendmsg(userid, message):
    try:
        token = dbget.readval("*", "api")
        bot = telepot.Bot(token)
        bot.sendMessage(userid, message)
        return 0
    except:
        return 1
force = False
climode = False
upgrade = False
hname = socket.gethostname()
if sys.argv[1]:
    climode = True
    if sys.argv[1] == "force":
        force = True
    if sys.argv[1] == "upgrade":
        upgrade = True
while climode = True:
    ctime = time.strftime("%H%M")
    if str(ctime) == (dbget.readval("*", "timeint")):
        os.system("aptitude update")
        updateslist = subprocess.getoutput("aptitude search '~U'")
        if updateslist != "":
            usrid = dbget.readval("*", "authusers")
            sendmsg(usrid, "Updates Available for " + hname)
            sendmsg(usrid, updateslist)
        if updateslist == "":
            usrid = dbget.readval("*", "authusers")
            sendmsg(usrid, "No Updates Available for " + hname)
        time.sleep(60)
        if force is True:
            break
    else:
        time.sleep(30)
if force is True or upgrade is True:
    os.system("aptitude update")
    updateslist = subprocess.getoutput("aptitude search '~U'")
    if updateslist != "" and upgrade is False:
        usrid = dbget.readval("*", "authusers")
        sendmsg(usrid, "Updates Available for " + hname)
        sendmsg(usrid, updateslist)
    if upgrade is True:
        usrid = dbget.readval("*", "authusers")
        upgradeverb = subprocess.getoutput("aptitude upgrade -y")
        sendmsg(usrid, "Completed Updates: ")
        sendmsg(usrid, upgradeverb)