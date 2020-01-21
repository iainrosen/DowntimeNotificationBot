import os
import time
import telepot
import sqlite3
import dbget
import socket
import subprocess
import dlog
dlog.info("Starting DowntimeBot...")
token = dbget.readval("*", "api")
bot = telepot.Bot(token)
lastMsg = 1
hname = socket.gethostname()
starttext = '''Welcome to Downtime!
Before you start, put your server in registration mode by typing "downtime-cli register". Then, tap here -> /register'''
helptext = '''Available Commands:
/register           Register with Downtime Server
/getupdates         Get updates on the server with aptitude
/doupdates          Update the server's packages with aptitude
/help               View this helptext
/status             View the Downtime Server status
/restart [x]        Restart a specified service
/whoami             View your userid (DEPRICATED)
'''
def sendmsg(userid, message):
    try:
        token = dbget.readval("*", "api")
        bot = telepot.Bot(token)
        message = hname + ": " + message
        bot.sendMessage(userid, message)
        dlog.info("Sent message: " + message + "to userid: " + str(userid))
        return 0
    except:
        dlog.critical("Failed to send message to: " + str(userid) + ". Message was: " + message)
        return 1
def process(usrid, text):
    if str(usrid) == (dbget.readval("*", "authusers")):
        priv = True
        dlog.info("Recieved message: " + text + " from privileged user: " + str(usrid))
    else:
        priv = False
        dlog.info("Recieved message: " + text + " from unprivileged user: " + str(usrid))
    #nonpriv commands
    if text == "/start":
        sendmsg(usrid, starttext)
    elif text == ("/register " + hname):
        if (dbget.readval("*", "authusers") != 1):
            dlog.warning("User initiated registration, but was already registered. Userid: " + str(usrid))
            sendmsg(usrid, "User already registered!")
            os.system("rm -rf /tmp/registration.downtime.lock")
            return 0
        if (os.path.exists("/tmp/registration.downtime.lock")) == True:
            dlog.info("Registering new user: " + str(usrid) + "...")
            cmd = "python3 /usr/bin/downtime/setup.py newuser " + str(usrid)
            os.system(cmd)
            os.system("rm -rf /tmp/registration.downtime.lock")
            sendmsg(usrid, "Registration Complete!")
            dlog.info("Registered " + str(usrid))
        else:
            dlog.warning("User attempted to register but registration was unavailable. Userid: "+str(usrid))
            sendmsg(usrid, "Registration Unavailable.")
    elif text == ("/help " + hname):
        sendmsg(usrid, helptext)
    #priv commands
    elif text == "/status" and priv == True:
        stats = subprocess.getoutput("systemctl status downtime")
        sendmsg(usrid, stats)
    elif text == ("/getupdates " + hname) and priv == True:
        sendmsg(usrid, "Searching for updates...")
        os.system("python3 /usr/bin/downtime/update-notf.py force &")
    elif text == ("/doupdates " + hname) and priv == True:
        sendmsg(usrid, "Executing updates on " + hname)
        dlog.info("Executing updates as per command of user: ", str(usrid))
        os.system("apt upgrade -y &")
    elif "/restart" in text and priv == True:
        svstart = text.rsplit(' ')
        if svstart[1] == hname and svstart[2]:
            dlog.info(str(usrid) + " initiated restart of " + svstart[2] + ".")
            sendmsg(usrid, "Attempting to start " + svstart[1])
            cmd = "systemctl restart " + svstart[1]
            os.system(cmd)
            stats = subprocess.getoutput("systemctl is-active " + svstart[1])
            if stats == "active":
                dlog.info("Service restarted successfully")
                sendmsg(usrid, svstart[1] + " start complete.")
            else:
                dlog.warning("Service restart failed.")
                sendmsg(usrid, svstart[1] + " start failed.")
    else:
        if hname in text:
            dlog.warning("User, " + str(usrid) + " attempted to access an unauthorized or unknown command.")
            sendmsg(usrid, "You might not be allowed to access that command yet.")
def parseMsg(msg):
    parse = message[0]
    updateid = parse.get("update_id")
    lastMsg = updateid + 1
    messageDetails = parse.get("message")
    if messageDetails:
        #parse
        fromDetails = messageDetails.get("from")
        usrid = fromDetails.get("id")
        text = messageDetails.get("text")
        return updateid, usrid, text
    else:
        messageDetails = parse.get("edited_message")
        fromDetails = messageDetails.get("from")
        usrid = fromDetails.get("id")
        text = messageDetails.get("text")
        return updateid, usrid, text
    return updateid, 0, 0
userid = dbget.readval("*", "authusers")
msg = "Downtime on " + hname + " is starting by systemd."
sendmsg(userid, msg)
while True:
        message = bot.getUpdates(offset=lastMsg)
        if message != []:
            dlog.info("RAW MESSAGE DUMP: " + str(message))
            updateid, usrid, text = parseMsg(message)
            lastMsg = updateid + 1
            if usrid != 0:
                #process the message
                process(usrid, text)
        time.sleep(1)
