import telepot
import sqlite3
def readval(value, table):
    try:
        conn = sqlite3.connect("/usr/bin/downtime/db/botconfig.db")
        c = conn.cursor()
        command = "SELECT " + value + " FROM " + table
        c.execute(command)
        configFetch = c.fetchone()
        return configFetch[0]
    except:
        return 1
def writeval(value, table):
    try:
        conn = sqlite3.connect("/usr/bin/downtime/db/botconfig.db")
        c = conn.cursor()
        command = "INSERT INTO " + table + " VALUES ('" + value + "')"
        c.execute(command)
        conn.commit()
        return 0
    except:
        return 1
