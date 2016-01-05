__author__ = 'Terrace Boiz'

import urllib
import json
import time
import traceback
from collections import defaultdict

import matrixControl


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
            pop_dict(schedule, 'Roxbury')  # populate schedule dict
            # mbtaTimeDisplay.popNorth(schedule)   #print northbound times
            # mbtaTimeDisplay.popSouth(schedule)   #print southbound times
            matrixControl.main()
            time.sleep(15)  # sleep
    except IOError:
        print "Caught IOError"
        print traceback.print_exc()
        time.sleep(15)
        main()
    except KeyError:
        print "Caught IOError"
        print traceback.print_exc()
        time.sleep(15)
        main()
    except:
        print "Caught Unhandled exception in mbtajsonparse main"
        print traceback.print_exc()


def get_station_json(station):
    response = urllib.urlopen(train_url + stationConverter[station] + '&format=json')
    train_data = json.loads(response.read().decode())
    return train_data


# Parse all Roxbury Crossing train arrival times
# Add all times to defaultdict (schedule)
def pop_dict(current_dict, station):
    train_data = get_station_json(station)
    current_dict.clear()
    if 'mode' in train_data:
        for mode in train_data['mode']:
            # If the mode is subway
            if mode['mode_name'] == 'Subway':
                # for each route
                for route in mode['route']:
                    # if route name is orange line
                    if route['route_id'] == 'Orange':
                        sort_trains(current_dict, route)
                        break
            

# Takes in all inbound and outbound trains and sorts them
def sort_trains(current_dict, orange_line):
    # for each direction
    for direction in orange_line['direction']:
        # For each train
        for trip in direction['trip']:
            # add each train to the schedule dict -> schedule['direction'].append(pre_away)
            current_dict[direction['direction_name']].append(
                int(trip['pre_away']))








