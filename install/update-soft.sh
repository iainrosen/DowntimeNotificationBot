#!/bin/bash
rm -rf /tmp/DowntimeUpdates
mkdir /tmp/DowntimeUpdates
cd /tmp/DowntimeUpdates
git clone git@github.com:iainrosen/DowntimeNotificationBot.git
cd DowntimeNotificationBot
bash install.run
