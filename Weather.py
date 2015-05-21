__author__ = 'Terrace Boiz'

import urllib
import json
import time

weather_url = 'http://api.wunderground.com/api/aceec2d6587b3b0c/conditions/q/MA/Boston.json'
spacer = "-------------------------------------------"

def main():
    try:
        while True:
            print spacer
            grab_weather()
            print spacer
            time.sleep(15)
    except:
        print "Error Loading, Trying Again"
        time.sleep(15)
        main()


def grab_weather():
    response = urllib.urlopen(weather_url)
    weather_data = json.loads(response.read().decode())
    print "Boston Weather:\n"
    print weather_data['current_observation']['weather']
    print weather_data['current_observation']['feelslike_f'] + " F"



if __name__ == "__main__":
    main()