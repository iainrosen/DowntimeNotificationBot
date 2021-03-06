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

```/register``` Attempts to register a user

```/status``` Displays the status of the Downtime Service

```/ping``` Pings all servers connected to the bot

```/getupdates``` Checks for updates (Can take up to a minute)

```/doupdates``` Runs updates on all available packages on a specified host

```/restart [service]``` Attempts to restart a failed service

## A note about multi-server functionality
The latest version of Downtime no longer supports multi-server functionality due to limitations with the telegram API.
