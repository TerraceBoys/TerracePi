__author__ = 'Brian Cox'


import json
import urllib.request
from pprint import pprint


url = "http://realtime.mbta.com/developer/api/v2/predictionsbystop?api_key=wX9NwuHnZU2ToO7GmGR9uw&stop=place-rcmnl&format=json"

response = urllib.request.urlopen(url)
jsonObj = json.loads(response.readall().decode())
first = jsonObj['mode'][0]['route'][0]

# with open(jsonObj) as data_file

print(jsonObj)
print(first)

