__author__ = 'Terrace Boiz'


import urllib.request
import json
import time
import os
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
            popNorth()
            popSouth()
            schedule.clear()
            # displayTime()
            print(spacer)
            time.sleep(15)
    except:
        print("Load Error, Trying Again")
        time.sleep(15)
        main()



#Dict of all times


#test 3 with defaultdict entry
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



def popNorth():
    print("Northbound (Oak Grove)")
    for x in range (len(schedule['Northbound'])):
        if (x == 0):
            m, s = divmod(schedule['Northbound'][x], 60)
            print ("Next Train: %02d:%02d" % (m, s))
        else:
            m, s = divmod(schedule['Northbound'][x], 60)
            print ("%02d:%02d" % (m, s))
    print("\n")

def popSouth():
    print("Southbound (Forrest Hills)")
    for x in range (len(schedule['Southbound'])):
        if (x == 0):
            m, s = divmod(schedule['Southbound'][x], 60)
            print ("Next Train: %02d:%02d" % (m, s))
        else:
            m, s = divmod(schedule['Southbound'][x], 60)
            print ("%02d:%02d" % (m, s))

