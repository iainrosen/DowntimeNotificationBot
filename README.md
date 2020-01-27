# DowntimeNotificationBot

## Installation and Setup
A simple bash script is available to make git download and installation faster. On a Ubuntu or Debian-based OS, type:
```
wget https://iainrosen.me/update-soft.sh && sudo bash update-soft.sh
```
The installation script automatically installs or updates Downtime.

### Telegram Bot Tokens
To setup a new telegram bot, read the article here: https://core.telegram.org/bots

### Useful setup commands
Downtime includes a CLI to help you get up and running, as well as a setup script the reconfigure or verify Downtime's configuration.
To check if Downtime is setup correctly:
```
python3 /usr/bin/downtime/setup.py check
```
To install a new bot token:
```
python3 /usr/bin/downtime/setup.py init [token]
```
To manually add a new userid to the authorized_users database:
```
python3 /usr/bin/downtime/setup.py adduser [userid]
```
To change the time which Downtime notifies of updates:
```
python3 /usr/bin/downtime/setup.py setint [hhmm]
```

## User Registration
Downtime uses a CLI to make administration easier. To start the registration process, type:
```
downtime-cli register
```
This will open registration to any user for 30 seconds. To register a new user, open Telegram and navigate to the bot, then type:
```
/register [hname] (where hname is the server's hostname)
```
Downtime will confirm that the user is registered and the server will stop any other registrations from proceeding.
## Available Commands
```/help``` Displays a link to this page

```/register [hname]``` Attempts to register a user with the specified host

```/status [hname]``` Displays the status of the Downtime Service on a specified host

```/status all``` Displays the status of the Downtime Service on all servers connected to the Telegram bot

```/ping``` Pings all servers connected to the bot

```/getupdates [hname]``` Checks for updates on the specified host (Can take up to a minute)

```/doupdates [hname]``` Runs updates on all available packages on a specified host

```/restart [hname] [service]``` Attempts to restart a failed service on a specified host
