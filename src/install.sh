#!/usr/bin/env bash

apt install python3 python3-pip hping3 curl -y
pip3 install -r requirements.txt
mkdir -p /usr/share/bot
cp * /usr/share/bot
cd /usr/share/bot
cp bot.service /lib/systemd/system
service bot start
systemctl enable bot
