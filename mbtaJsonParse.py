__author__ = 'Terrace Boiz'

import urllib
import json
import time
import traceback
import config
from collections import defaultdict

import matrixControl

train_url = 'http://realtime.mbta.com/developer/api/v2/predictionsbystop?api_key=' + config.MBTA_API_KEY + '&stop=place-'
schedule = defaultdict(list)
stationConverter = {'Forrest': 'forhl', 'Green': 'grnst', 'Stony': 'sbmnl', 'Jackson': 'jaksn', 'Roxbury': 'rcmnl',
                    'Ruggles': 'rugg', 'Mass': 'masta', 'Back': 'bbsta', 'Tufts': 'nemnl', 'Chinatown': 'chncl',
                    'Downtown': 'dwnxg', 'State': 'state', 'Haymarket': 'haecl', 'North': 'north', 'Community': 'ccmnl',
                    'Sullivan': 'sull', 'Wellington': 'welln', 'Malden': 'mlmnl', 'Oak': 'ogmnl'}


def main(matrix):
    try:
        while True:
            pop_dict(schedule, 'Roxbury')  # populate schedule dict
            matrixControl.set_mbta(schedule)
            matrixControl.main(matrix)
            for x in range(15):
                time.sleep(1)  # sleep
    except SystemExit:
        print "Thread terminated"
    except IOError:
        print "Caught IOError"
        print traceback.print_exc()
        time.sleep(15)
        main(matrix)
    except KeyError:
        print "Caught IOError"
        print traceback.print_exc()
        time.sleep(15)
        main(matrix)
    except ValueError:
        print traceback.print_exc()
        time.sleep(60)
        main(matrix)
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
        for x in range(len(train_data['mode'])):
            # If the mode is subway
            if train_data['mode'][x]['mode_name'] == 'Subway':
                # for each route
                for r in range(len(train_data['mode'][x]['route'])):
                    # if route name is orange line
                    if train_data['mode'][x]['route'][r]['route_name'] == 'Orange Line':
                        # for every direction
                        for y in range(len(train_data['mode'][x]['route'][r]['direction'])):
                            # For each train
                            for z in range(len(train_data['mode'][x]['route'][r]['direction'][y]['trip'])):
                                # add each train to the schedule dict -> schedule['direction'].append(pre_away)
                                current_dict[
                                    train_data['mode'][x]['route'][r]['direction'][y]['direction_name']].append(
                                    int(train_data['mode'][x]['route'][r]['direction'][y]['trip'][z]['pre_away']))
                break
