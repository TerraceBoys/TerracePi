#!/bin/sh

sleep 15

cd ~/Desktop/TerracePi

sudo pkill -9 python
sleep 2
git pull
sleep 5
sudo python main.py

