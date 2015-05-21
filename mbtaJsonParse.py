__author__ = 'Terrace Boiz'


import urllib
import json
import time
import datetime
import sendSMS
import os
import mbtaTimeDisplay
from collections import defaultdict

spacer = "-------------------------------------------"
access_key = 'MpYsZaqkKkG6p8WOeKHLqA'
train_url = 'http://realtime.mbta.com/developer/api/v2/predictionsbystop?api_key=' + access_key + '&stop=place-rcmnl&format=json'
schedule = defaultdict(list)


def main():
    try:
        while True:
            print spacer
            popDict()
            mbtaTimeDisplay.popNorth()
            mbtaTimeDisplay.popSouth()
            checkAlert()
            rayAlert()
            schedule.clear()
            print spacer
            time.sleep(15)
    except:
        print "Load Error mbta, Trying Again"
        time.sleep(15)
        main()



#Parse all Roxbury Crossing train arrival times
#Add all times to defaultdict (schedule)
def popDict():
    response = urllib.urlopen(train_url)
    train_data = json.loads(response.read().decode())
    print "Roxbury Crossing Train Schedule:\n"
    for x in range (len(train_data['mode']) - 1):
        if (train_data['mode'][x]['mode_name'] == 'Subway'):
            for y in range (len(train_data['mode'][x]['route'][0]['direction'])):
                for z in range (len(train_data['mode'][x]['route'][0]['direction'][y]['trip'])):
                    schedule[train_data['mode'][x]['route'][0]['direction'][y]['direction_name']].append(
                        int(train_data['mode'][x]['route'][0]['direction'][y]['trip'][z]['pre_away']))


def run_once(f):
    def wrapper():
        if not wrapper.has_run:
            wrapper.has_run = True
            return f()
    wrapper.has_run = False
    return wrapper

#Check to see if sms should be sent
def checkAlert():
    if (datetime.datetime.now().time() >= datetime.time(hour=9, minute=30) and
            (schedule['Northbound'][0] < 250) and (schedule['Northbound'][0] > 180)):
        runAlert()

#Send sms only once
@run_once
def runAlert():
    msg = 'Time To Leave bro'
    to = [sendSMS.branden, sendSMS.brian]
    sendSMS.send(msg, to)


#Check to see if sms should be sent
def rayAlert():
    if (datetime.datetime.now().time() >= datetime.time(hour=7, minute=40) and
            (schedule['Northbound'][0] < 250) and (schedule['Northbound'][0] > 180)):
        runRayAlert()

#Send sms only once
@run_once
def runRayAlert():
    msg = 'Time To Leave bro'
    to = [sendSMS.ray]
    sendSMS.send(msg, to)