#!/bin/bash
rm -rf /tmp/DowntimeUpdates
mkdir /tmp/DowntimeUpdates
cd /tmp/DowntimeUpdates
echo "Downloading..."
git clone git@github.com:iainrosen/DowntimeNotificationBot.git &> /dev/null
cd DowntimeNotificationBot
bash install.run
