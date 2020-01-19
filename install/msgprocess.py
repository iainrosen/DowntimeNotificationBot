import os
import time
import sys
import sqlite3
import telepot
import dbget
import subprocess
joinRunning = []
starttext = '''Welcome to Downtime!
Before you start, put your server in registration mode by typing "downtime-cli register". Then, tap here -> /register'''
helptext = '''Available Commands:
/register           Register with Downtime Server
/help               View this helptext
/status             View the Downtime Server status
/restart [service]  Restart a specified service
/whoami             View your userid
'''
def sendmsg(userid, message):
    token = dbget.readval("*","api")
    bot = telepot.Bot(token)
    bot.sendMessage(userid, message)
def process(usrid, text):
    if str(usrid) == (dbget.readval("*", "authusers")):
        priv = True
    else:
        priv = False
    #nonpriv commands
    if text == "/start":
        sendmsg(usrid, starttext)
    elif text == "/register":
        if (dbget.readval("*", "authusers") != 1):
            sendmsg(usrid, "User already registered!")
            os.system("rm -rf /tmp/registration.downtime.lock")
            exit()
        if (os.path.exists("/tmp/registration.downtime.lock")) == True:
            cmd = "python3 /usr/bin/downtime/setup.py newuser " + str(usrid)
            os.system(cmd)
            os.system("rm -rf /tmp/registration.downtime.lock")
            sendmsg(usrid, "Registration Complete!")
        else:
            sendmsg(usrid, "Registration Unavailable.")
    elif text == "/help":
        sendmsg(usrid, helptext)
    elif text == "/whoami":
        msgSend = "Your User ID is: " + str(usrid)
        sendmsg(usrid, msgSend)
    #priv commands
    elif text == "/status" and priv == True:
        stats = subprocess.getoutput("systemctl status downtime")
        sendmsg(usrid, stats)
    elif "/restart" in text and priv == True:
        svstart = text.rsplit(' ')
        sendmsg(usrid, "Attempting to start " + svstart[1])
        cmd = "systemctl start " + svstart[1]
        os.system(cmd)
        stats = subprocess.getoutput("systemctl is-active " + svstart[1])
        if stats == "active":
            sendmsg(usrid, svstart[1] + " start complete.")
        else:
            sendmsg(usrid, svstart[1] + " start failed.")
    else:
        sendmsg(usrid, "You might not be allowed to access that command yet.")
