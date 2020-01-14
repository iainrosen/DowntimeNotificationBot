import os
import time
import telepot
import sqlite3

def sendmsg(userid, message):
    conn = sqlite3.connect("/usr/local/downtime/db/botconfig.db")
    c = conn.cursor()
    c.execute("SELECT * FROM api")
    token = c.fetchone()
    token = str(token[0])
    bot = telepot.Bot(token)
    bot.sendMessage(userid, message)
def blast(serverid, message):
    conn = sqlite3.connect("/usr/local/downtime/db/botconfig.db")
    c = conn.cursor()
    c.execute("SELECT * FROM api")
    token = c.fetchone()
    token = str(token[0])
    bot = telepot.Bot(token)
    conn = sqlite3.connect("/usr/local/downtime/db/servers.db")
    c = conn.cursor()
    c.execute("SELECT * FROM authusers WHERE serverid=" + str(serverid))
    users = c.fetchall()
    print users
    print len(users)
    for i in range(len(users)):
        entry = users[i]
        userid = entry[0]
        if entry[2] == 1:
            try:
                bot.sendMessage(userid, message)
            except:
                print "Message Failure. Check UserID."
        else:
            print str(userid) + " not authorized"
