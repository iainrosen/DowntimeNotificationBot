# DowntimeNotificationBot

## Installation and Setup
A simple bash script is available to make git download and installation faster. On a Ubuntu or Debian-based OS, type:
'''
wget https://iainrosen.me/update-soft.sh && sudo bash update-soft.sh
'''
The installation script automatically installs or updates Downtime.

### Telegram Bot Tokens
To setup a new telegram bot, read the article here: https://core.telegram.org/bots

### Useful setup commands
Downtime includes a CLI to help you get up and running, as well as a setup script the reconfigure or verify Downtime's configuration.
To check if Downtime is setup correctly:
'''
python3 /usr/bin/downtime/setup.py check
'''
To install a new bot token:
'''
python3 /usr/bin/downtime/setup.py init [token]
'''
To manually add a new userid to the authorized_users database:
'''
python3 /usr/bin/downtime/setup.py adduser [userid]
'''
To change the time which Downtime notifies of updates:
'''
python3 /usr/bin/downtime/setup.py setint [hhmm]
'''
