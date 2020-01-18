import outgoing
import dbget
import socket
hname = socket.gethostname()
userid = dbget.readval("*", "authusers")
msg = "Downtime on " + hname + " is stopping by systemd."
outgoing.sendmsg(userid, msg)
