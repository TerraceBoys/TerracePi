__author__ = 'Terrace Boiz'

import urllib
import json
import time

access_key = 'aceec2d6587b3b0c'
weather_url = 'http://api.wunderground.com/api/' + access_key + '/conditions/q/MA/Boston.json'
spacer = "-------------------------------------------"

def main():
    try:
        while True:
            print spacer
            grab_weather()
            print spacer
            time.sleep(300)
    except (IOError):
        print "Error Loading Weather, Trying Again"
        time.sleep(600)
        main()


def grab_weather():
    response = urllib.urlopen(weather_url)
    weather_data = json.loads(response.read().decode())
    print "Boston Weather:\n"
    print weather_data['current_observation']['weather']
    print weather_data['current_observation']['feelslike_f'] + u"\u00b0"

def weatherPanel():
    response = urllib.urlopen(weather_url)
    weather_data = json.loads(response.read().decode())
    weather = int(weather_data['current_observation']['feelslike_f'])
    return  str(weather) + u"\u00b0"




if __name__ == "__main__":
    main()