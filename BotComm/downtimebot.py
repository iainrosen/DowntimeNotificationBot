import os
import time
import telepot
import sqlite3
import msgprocess
conn = sqlite3.connect("/usr/bin/downtime/db/botconfig.db")
c = conn.cursor()
c.execute("SELECT * FROM api")
token = c.fetchone()
token = str(token[0])
bot = telepot.Bot(token)
lastMsg = 1
def parseMsg(msg):
    parse = message[0]
    updateid = parse.get("update_id")
    lastMsg = updateid + 1
    messageDetails = parse.get("message")
    fromDetails = messageDetails.get("from")
    usrid = fromDetails.get("id")
    text = messageDetails.get("text")
    return updateid, usrid, text
while True:
    message = bot.getUpdates(offset=lastMsg)
    if message != []:
        updateid, usrid, text = parseMsg(message)
        lastMsg = updateid + 1
        #process the message
        msgprocess.process(usrid, text)
    time.sleep(1)
