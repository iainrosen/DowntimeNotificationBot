import os
import time
import sys
import sqlite3
import telepot
import dbget
joinRunning = []
starttext = '''Welcome to Downtime!
Before you start, we need to register you with a new server. To do this, add your user id to the config file.
You can check your userid with /whoami'''
def sendmsg(userid, message):
    token = dbget.readval("*","api")
    bot = telepot.Bot(token)
    bot.sendMessage(userid, message)
def process(usrid, text):
    if usrid == (dbget.readval("*", "authusers")):
        priv = True
    else:
        priv = False
    #nonpriv commands
    if text == "/start":
        sendmsg(usrid, starttext)
    elif text == "/register":
        if os.path.exists("/tmp/registration.downtime.lock") == True:
            cmd = "python3 /usr/bin/downtime/setup.py newuser " + usrid
            os.system(cmd)
            os.system("rm -rf /tmp/registration.downtime.lock")
            sendmsg(usrid, "Registration Complete!")
        else:
            sendmsg(usrid, "Registration Unavailable.")
    elif text == "/help":
        sendmsg(usrid, "Good Luck!")
    elif text == "/whoami":
        msgSend = "Your User ID is: " + str(usrid)
        sendmsg(usrid, msgSend)
    #priv commands
    elif text == "/restart" and priv == True:
       sendmsg(usrid, "Attempting to restart services...")
       sendmsg(usrid, "Sorry this isn't implemented yet")
    else:
        sendmsg(usrid, "You might not be allowed to access that command yet.")
