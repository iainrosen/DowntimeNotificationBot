#!/bin/bash
rm -rf /tmp/DowntimeUpdates
mkdir /tmp/DowntimeUpdates
cd /tmp/DowntimeUpdates
echo "Downloading..."
git clone https://github.com/iainrosen/DowntimeNotificationBot.git -b multi-server &> /dev/null
cd DowntimeNotificationBot
bash install.run
