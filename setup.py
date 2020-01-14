import os
import sys
import time
import sqlite3
if os.path.exists("/usr/bin/downtime/db/botconfig.db") == True and sys.argv[1] == "check":
    return 0
else:
    return 1
if sys.argv[1] == "init":
    os.system("rm -rf /usr/bin/downtime/db/*")
    conn = sqlite3.connect("/usr/bin/downtime/db/botconfig.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE api
    (apikey text)''')
    key = sys.argv[2]
    insertCommand = "INSERT INTO api VALUES ('" + key + "')"
    c.execute(insertCommand)
    conn.commit()
    return 0
