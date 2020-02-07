import os
import time
import telepot
import dbget
import socket
import subprocess
import dlog
versionid = "0.1.1"
dlog.info("Starting DowntimeBot...")
token = dbget.readval("*", "api")
bot = telepot.Bot(token)
lastMsg = 1
hname = socket.gethostname()
helptext = "Help text available at: https://github.com/iainrosen/DowntimeNotificationBot/blob/master/README.md"
def sendmsg(userid, message):
    try:
        token = dbget.readval("*", "api")
        bot = telepot.Bot(token)
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
        if priv is True:
            sendmsg(usrid, "Looks like you're already setup! Type /help for a list of available commands")
        else:
            sendmsg(usrid, "Hello from " + hname + "!")
    elif text == "/ping":
        sendmsg(usrid, hname+" is up!")
    elif text == "/register":
        if (dbget.readval("*", "authusers") != 1):
            dlog.warning("User initiated registration, but was already registered. Userid: " + str(usrid))
            sendmsg(usrid, "User already registered!")
            os.system("rm -rf /tmp/registration.downtime.lock")
            return 0
        if (os.path.exists("/tmp/registration.downtime.lock")) is True:
            dlog.info("Registering new user: " + str(usrid) + "...")
            cmd = "python3 /usr/bin/downtime/setup.py newuser " + str(usrid)
            os.system(cmd)
            os.system("rm -rf /tmp/registration.downtime.lock")
            sendmsg(usrid, "Registration Complete!")
            dlog.info("Registered " + str(usrid))
        else:
            dlog.warning("User attempted to register but registration was unavailable. Userid: "+str(usrid))
            sendmsg(usrid, "Registration Unavailable.")
    elif text == "/help":
        sendmsg(usrid, helptext)
    #priv commands
    elif text == "/status" and priv is True:
        stats = subprocess.getoutput("systemctl status downtime")
        sendmsg(usrid, stats)
    elif text == "/getupdates" and priv is True:
        sendmsg(usrid, "Searching for updates...")
        os.system("python3 /usr/bin/downtime/update-notf.py update &")
    elif text == "/doupdates" and priv is True:
        sendmsg(usrid, "Executing updates on " + hname)
        dlog.info("Executing updates as per command of user: " + str(usrid))
        os.system("python3 /usr/bin/downtime/update-notf.py upgrade &")
    elif "/restart" in text and priv is True:
        svstart = text.rsplit(' ')
        if svstart[1]:
            if svstart[1] == "downtime":
                sendmsg(usrid, "Downtime cannot restart itself.")
                return 0
            dlog.info(str(usrid) + " initiated restart of " + svstart[1] + ".")
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
        dlog.warning("User, " + str(usrid) + " attempted to access an unauthorized or unknown command.")
        sendmsg(usrid, "You might not be allowed to access that command yet.")
            


def parseMsg(message):
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
msg = "Downtime on " + hname + " started. Version " + versionid
sendmsg(userid, msg)
while True:
    try:
        message = bot.getUpdates(offset=lastMsg)
    except:
        message = bot.getUpdates()
    if message != []:
            updateid, usrid, text = parseMsg(message)
            lastMsg = updateid + 1
            if usrid != 0:
                #process the message
                process(usrid, text)
