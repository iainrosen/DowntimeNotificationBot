import outgoing
import dbget
import socket
hname = socket.gethostname()
userid = dbget.readval("*", "authusers")
msg = "Downtime on " + hname + " is stopping by systemd."
def sendmsg(userid, message):
    try:
        token = dbget.readval("*", "api")
        bot = telepot.Bot(token)
        message = hname + ": " + message
        bot.sendMessage(userid, message)
        dlog.info("Sent message: " + message + "to userid: " + str(userid))
        return 0
    except:
        dlog.critical("Failed to send message to: " + str(userid) + ". Message was: " + message)
        return 1
sendmsg(userid, msg)
