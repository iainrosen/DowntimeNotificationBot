import os
import time
import telepot
import sqlite3
import dbget
def sendmsg(userid, message):
    token = dbget.readval("*", "api")
    bot = telepot.Bot(token)
    bot.sendMessage(userid, message)
