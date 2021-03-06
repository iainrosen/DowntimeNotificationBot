import time
import socket
import subprocess
import dbget
import telepot
def sendmsg(userid, message):
    try:
        token = dbget.readval("*", "api")
        bot = telepot.Bot(token)
        bot.sendMessage(userid, message)
        return 0
    except:
        return 1
userid = dbget.readval("*", "authusers")
hname = socket.gethostname()
netfail = 0
servicefail = 0
f = open("/usr/bin/downtime/db/services.watchlist", 'r')
watchlist = f.readlines()
f.close()
servicewatch = [x.replace('\n', '') for x in watchlist]
#add the services you want to watch here
failed = []
while True:
    #check for server failures
    for i in servicewatch:
        checksvc = "systemctl is-active " + i
        if (subprocess.getoutput(checksvc)) == "inactive" and i not in failed:
            failed.append(i)
            msg = "Service: " + i + " on " + hname + " has failed!"
            sendmsg(userid, msg)
        elif (subprocess.getoutput(checksvc)) != "inactive" and i in failed:
            msg = "Service: " + i + " on " + hname + " back active."
            sendmsg(userid, msg)
            failed.remove(i)
    time.sleep(2)
