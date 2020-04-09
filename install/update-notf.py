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
def update(cron):
    hname = socket.gethostname()
    usrid = dbget.readval("*", "authusers")
    os.system("aptitude update")
    updateslist = subprocess.getoutput("aptitude search '~U'")
    if updateslist != "":
        sendmsg(usrid, "Updates Available for " + hname)
        sendmsg(usrid, updateslist)
    if updateslist == "" and cron == False:
        sendmsg(usrid, "No updates available for " + hname)
def upgrade():
    hname = socket.gethostname()
    usrid = dbget.readval("*", "authusers")
    upgradeverb = subprocess.getoutput("aptitude upgrade -y")
    sendmsg(usrid, "Completed Updates: ")
    sendmsg(usrid, upgradeverb)
if sys.argv[1]:
    #cli mode
    if sys.argv[1] == "update":
        update(False)
    elif sys.argv[1] == "upgrade":
        upgrade()
    elif sys.argv[1] == "cronupdate":
        update(True)
else:
    print("update-notf.py didn't recieve any command-line parameters")