def warning(msg):
    f = open('downtime.log', 'a')
    f.write('[WARNING] ' + msg)
    f.write("\n")
    f.close()
def info(msg):
    f = open('downtime.log', 'a')
    f.write('[INFO] ' + msg)
    f.write("\n")
    f.close()
def critical(msg):
    f = open('downtime.log', 'a')
    f.write('[CRITICAL] ' + msg)
    f.write("\n")
    f.close()
def error(msg):
    f = open('downtime.log', 'a')
    f.write('[ERROR] ' + msg)
    f.write("\n")
    f.close()
