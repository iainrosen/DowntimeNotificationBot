import os
import time
import telepot
import sqlite3
import dbget
import socket
token = dbget.readval("*", "api")
bot = telepot.Bot(token)
lastMsg = 1
hname = socket.gethostname()
starttext = '''Welcome to Downtime!
Before you start, put your server in registration mode by typing "downtime-cli register". Then, tap here -> /register'''
helptext = '''Available Commands:
/register           Register with Downtime Server
/getupdates         Get updates on the server with aptitude
/help               View this helptext
/status             View the Downtime Server status
/restart [x]        Restart a specified service
/whoami             View your userid
'''
def sendmsg(userid, message):
    try:
        token = dbget.readval("*", "api")
        bot = telepot.Bot(token)
        bot.sendMessage(userid, message)
        return 0
    except:
        return 1
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
    elif text == "/getupdates" and priv == True:
        sendmsg(usrid, "Searching for updates...")
        os.system("python3 /usr/bin/downtime/update-notf.py force &")
    elif text == "/doupdates" and priv == True:
        sendmsg(usrid, "Executing updates on " + hname)
        os.system("apt upgrade -y &")
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
    return updateid, 0, 0

userid = dbget.readval("*", "authusers")
msg = "Downtime on " + hname + " is starting by systemd."
sendmsg(userid, msg)
while True:
    try:
        message = bot.getUpdates(offset=lastMsg)
        if message != []:
            updateid, usrid, text = parseMsg(message)
            lastMsg = updateid + 1
            if usrid != 0:
                #process the message
                process(usrid, text)
        time.sleep(1)
    except:
        continue #ignore and restart
