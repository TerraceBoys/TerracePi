__author__ = 'Terrace Boiz'


import urllib.request
import json
from collections import defaultdict

train_url = 'http://realtime.mbta.com/developer/api/v2/predictionsbystop?api_key=wX9NwuHnZU2ToO7GmGR9uw&stop=place-rcmnl&format=json'
response = urllib.request.urlopen(train_url);
train_data = json.loads(response.read().decode());

#Dict of all times
schedule = defaultdict(list)

#test 3 with defaultdict entry
print ("Roxbury Crossing Train Schedule\n\n")
for x in range (len(train_data['mode']) - 1):
    if (train_data['mode'][x]['mode_name'] == 'Subway'):
        for y in range (len(train_data['mode'][x]['route'][0]['direction'])):
            for z in range (len(train_data['mode'][x]['route'][0]['direction'][y]['trip'])):
                schedule[train_data['mode'][x]['route'][0]['direction'][y]['direction_name']].append(
                    int(train_data['mode'][x]['route'][0]['direction'][y]['trip'][z]['pre_away']))


print("Roxbury Crossing Schedule\n\n")
print("Northbound (Oak Grove)")
for x in range (len(schedule['Northbound'])):
    if (x == 0):
        m, s = divmod(schedule['Northbound'][x], 60)
        print ("Next Train: %02d:%02d" % (m, s))
    else:
        m, s = divmod(schedule['Northbound'][x], 60)
        print ("%02d:%02d" % (m, s))
print("\n")
print("Southbound (Forrest Hills)")
for x in range (len(schedule['Southbound'])):
    if (x == 0):
        m, s = divmod(schedule['Southbound'][x], 60)
        print ("Next Train: %02d:%02d" % (m, s))
    else:
        m, s = divmod(schedule['Southbound'][x], 60)
        print ("%02d:%02d" % (m, s))