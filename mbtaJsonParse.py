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
            popDict()                    #populate schedule dict
            mbtaTimeDisplay.popNorth()   #print northbound times
            mbtaTimeDisplay.popSouth()   #print southbound times
            sendSMS.brandenAlert()       #check for branden alerts
            sendSMS.brianAlert()         #check for brian alerts
            sendSMS.rayAlert()           #check for ray alerts
            schedule.clear()             #clear schedule dict
            print spacer
            time.sleep(15)               #sleep
    except:
        print "Load Error for mbta, Trying Again"
        time.sleep(15)
        main()


#Parse all Roxbury Crossing train arrival times
#Add all times to defaultdict (schedule)
def popDict():
    response = urllib.urlopen(train_url)
    train_data = json.loads(response.read().decode())
    print "Roxbury Crossing Train Schedule:\n"
    #for all Roxbury train data
    for x in range (len(train_data['mode']) - 1):
        #If the mode is subway
        if (train_data['mode'][x]['mode_name'] == 'Subway'):
            #for each direction
            for y in range (len(train_data['mode'][x]['route'][0]['direction'])):
                #For each train
                for z in range (len(train_data['mode'][x]['route'][0]['direction'][y]['trip'])):
                    #add each train to the schedule dict -> schedule['direction'].append(pre_away)
                    schedule[train_data['mode'][x]['route'][0]['direction'][y]['direction_name']].append(
                        int(train_data['mode'][x]['route'][0]['direction'][y]['trip'][z]['pre_away']))

