import os
import time
import telepot
import sqlite3
import msgprocess
import dbget
import outgoing
import socket
token = dbget.readval("*", "api")
bot = telepot.Bot(token)
lastMsg = 1
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
        return updateid, 0, 0
    return updateid, usrid, text
hname = socket.gethostname()
userid = dbget.readval("*", "authusers")
msg = "Downtime on " + hname + " is starting by systemd."
outgoing.sendmsg(userid, msg)
while True:
    try:
        message = bot.getUpdates(offset=lastMsg)
        if message != []:
            updateid, usrid, text = parseMsg(message)
            lastMsg = updateid + 1
            if usrid != 0:
                #process the message
                msgprocess.process(usrid, text)
        time.sleep(1)
    except:
        continue #ignore and restart
