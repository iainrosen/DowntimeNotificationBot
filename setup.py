import os
import sys
import time
import sqlite3
def checkconf():
    if os.path.exists("/usr/bin/downtime/db/botconfig.db") == True:
        return 0
    else:
        return 1
def init(key):
    os.system("rm -rf /usr/bin/downtime/db/*")
    conn = sqlite3.connect("/usr/bin/downtime/db/botconfig.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE api
    (apikey text)''')
    insertCommand = "INSERT INTO api VALUES ('" + key + "')"
    c.execute(insertCommand)
    conn.commit()
    return 0
if sys.argv[1] == "init":
    init(sys.agrv[2])
elif sys.argv[1] == "check":
    checkconf()
else:
    print("Argument missing or not recognized.")
