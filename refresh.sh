#!/bin/sh

timestamp=$(date +%s)
sleep 15

cd ~/Desktop/TerracePi

sudo pkill -9 python
sleep 2
git pull
sleep 5
echo $timestamp >> ../errors.txt
sudo python server.py 2>> ../errors.txt

