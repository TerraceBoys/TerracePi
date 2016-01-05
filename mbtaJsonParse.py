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
            if train_data['mode'][mode]['mode_name'] == 'Subway':
                subway_routes = train_data['mode'][mode]
                # for each route
                for route in subway_routes:
                    # if route name is orange line
                    if subway_routes['route'][route]['route_name'] == 'Orange Line':
                        sort_trains(subway_routes['route'][route])
                        break
            

# Takes in all inbound and outbound trains and sorts them
def sort_trains(orange_line):
    # for each direction
    for direction in orange_line['direction']:
        in_or_out_trains = orange_line['direction'][direction]
        # For each train
        for train in in_or_out_trains['trip']:
            # add each train to the schedule dict -> schedule['direction'].append(pre_away)
            current_dict[in_or_out_trains['direction_name']].append(
                int(in_or_out_trains['trip'][train]['pre_away']))








