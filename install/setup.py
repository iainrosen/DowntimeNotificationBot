import os
import sys
import time
import sqlite3
import dbget
def checkconf():
    if os.path.exists("/usr/bin/downtime/db/botconfig.db") == True:
        print(0)
        return 0
    else:
        print(1)
        return 1
def init(key):
    os.system("rm -rf /usr/bin/downtime/db/*")
    conn = sqlite3.connect("/usr/bin/downtime/db/botconfig.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE api
    (apikey text)''')
    c.execute('''CREATE TABLE authusers
    (userid text)''')
    insertCommand = "INSERT INTO api VALUES ('" + key + "')"
    c.execute(insertCommand)
    conn.commit()
    print(0)
    os.system("touch /usr/bin/downtime/db/services.watchlist")
    os.system("echo downtime >> /usr/bin/downtime/db/services.watchlist")
    return 0
def newuser(userid):
    if dbget.writeval(userid, "authusers") == 0:
        print(0)
        return 0
    else:
        print(1)
        return 1
try:
    if sys.argv[1] == "init":
        init(sys.argv[2])
    elif sys.argv[1] == "check":
        checkconf()
    elif sys.argv[1] == "newuser":
        newuser(sys.argv[2])
    else:
        print("Argument missing or not recognized.")
except(IndexError):
    raise Exception("Required argument missing.")
