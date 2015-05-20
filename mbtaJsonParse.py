__author__ = 'Terrace Boiz'


import urllib.request
import json
import time
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
            print(spacer)
            popDict()
            mbtaTimeDisplay.popNorth()
            mbtaTimeDisplay.popSouth()
            schedule.clear()
            # displayTime()
            print(spacer)
            time.sleep(15)
    except:
        print("Load Error, Trying Again")
        time.sleep(15)
        main()



#Parse all Roxbury Crossing train arrival times
#Add all times to defaultdict (schedule)
def popDict():
    response = urllib.request.urlopen(train_url)
    train_data = json.loads(response.read().decode())
    print ("Roxbury Crossing Train Schedule:\n")
    for x in range (len(train_data['mode']) - 1):
        if (train_data['mode'][x]['mode_name'] == 'Subway'):
            for y in range (len(train_data['mode'][x]['route'][0]['direction'])):
                for z in range (len(train_data['mode'][x]['route'][0]['direction'][y]['trip'])):
                    schedule[train_data['mode'][x]['route'][0]['direction'][y]['direction_name']].append(
                        int(train_data['mode'][x]['route'][0]['direction'][y]['trip'][z]['pre_away']))


