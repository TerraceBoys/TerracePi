__author__ = 'Terrace Boiz'


import urllib
import json
import time
import mbtaTimeDisplay
from collections import defaultdict


spacer = "-------------------------------------------"
access_key = 'MpYsZaqkKkG6p8WOeKHLqA'
train_url = 'http://realtime.mbta.com/developer/api/v2/predictionsbystop?api_key=' + access_key + '&stop=place-'
schedule = defaultdict(list)
stationConverter = {'Forrest': 'forhl', 'Green': 'grnst', 'Stony': 'sbmnl', 'Jackson': 'jaksn', 'Roxbury': 'rcmnl',
                    'Ruggles': 'rugg', 'Mass': 'masta', 'Back': 'bbsta', 'Tufts': 'nemnl', 'Chinatown': 'chncl',
                    'Downtown': 'dwnxg', 'State': 'state', 'Haymarket': 'haecl', 'North': 'north', 'Community': 'ccmnl',
                    'Sullivan': 'sull', 'Wellington': 'welln', 'Malden': 'mlmnl', 'Oak': 'ogmnl'}

def main():
    try:
        while True:
            print spacer
            popDict(schedule, 'Roxbury')         #populate schedule dict
            mbtaTimeDisplay.popNorth(schedule)   #print northbound times
            mbtaTimeDisplay.popSouth(schedule)   #print southbound times
            print spacer
            time.sleep(15)               #sleep
            schedule.clear()             #clear schedule dict
    except (IOError):
        print "Load Error for mbta, Trying Again"
        time.sleep(15)
        main()


def getStationJSON(station):
    response = urllib.urlopen(train_url + stationConverter[station] + '&format=json')
    train_data = json.loads(response.read().decode())
    return train_data


#Parse all Roxbury Crossing train arrival times
#Add all times to defaultdict (schedule)
def popDict(currentDict, station):
    train_data = getStationJSON(station)
    if (len(train_data) > 1):
        for x in range (len(train_data['mode'])):
            #If the mode is subway
            if (train_data['mode'][x]['mode_name'] == 'Subway'):
                #for each route
                for r in range (len(train_data['mode'][x]['route'])):
                    #if route name is orange line
                    if (train_data['mode'][x]['route'][r]['route_name'] == 'Orange Line'):
                        #for every direction
                        for y in range (len(train_data['mode'][x]['route'][r]['direction'])):
                            #For each train
                            for z in range (len(train_data['mode'][x]['route'][r]['direction'][y]['trip'])):
                                #add each train to the schedule dict -> schedule['direction'].append(pre_away)
                                currentDict[train_data['mode'][x]['route'][r]['direction'][y]['direction_name']].append(
                                int(train_data['mode'][x]['route'][r]['direction'][y]['trip'][z]['pre_away']))
                break




