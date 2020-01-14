import os
import time
import sys
import serverauth
import sqlite3
import telepot
joinRunning = []
starttext = '''Welcome to Downtime!
Before you start, we need to register you with a new server. To do this, add your user id to the config file.
You can check your userid with /whoami'''
def sendmsg(userid, message):
    conn = sqlite3.connect("/usr/local/downtime/db/botconfig.db")
    c = conn.cursor()
    c.execute("SELECT * FROM api")
    token = c.fetchone()
    token = str(token[0])
    bot = telepot.Bot(token)
    bot.sendMessage(userid, message)
def process(usrid, text):
    if text[0] == "/":
        cmdType = True
    else:
        cmdType = False

    if text == "/start":
        sendmsg(usrid, starttext)
    elif text == "/help":
        sendmsg(usrid, "Good Luck!")
    elif text == "/whoami":
        msgSend = "Your User ID is: " + str(usrid)
        sendmsg(usrid, msgSend)
    else:
        sendmsg(usrid, "I don't understand that command yet. Try /help if you're lost.")
