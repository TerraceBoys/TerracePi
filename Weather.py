__author__ = 'Terrace Boiz'

import urllib
import json
import traceback
import time

access_key = 'aceec2d6587b3b0c'
weather_url = 'http://api.wunderground.com/api/' + access_key + '/conditions/q/MA/Roxbury_Crossing.json'
spacer = "-------------------------------------------"


def setup():
    return


def main():
    try:
        grab_weather()
    except IOError:
        print "Caught IOError while Loading Weather - Trying Again"
        print traceback.print_exc()
    except:
        print "Caught unhandled exception in Weather.main"
        print traceback.print_exc()


def grab_weather():
    response = urllib.urlopen(weather_url)
    global weather_data
    weather_data = json.loads(response.read().decode())
    # print "Boston Weather:"
    # print weather_data['current_observation']['weather']
    # print weather_data['current_observation']['feelslike_f'] + " F"


def weather_panel():
    global weather_data
    temperature = int(float(weather_data['current_observation']['feelslike_f']))
    return str(temperature) + u"\u00b0", get_temp_color(temperature)


# Determine display color for temperature
def get_temp_color(temp):
    if temp >= 90:
        return 255, 0, 0
    elif temp >= 80:
        return 255, 50, 0
    elif temp >= 70:
        return 255, 100, 0
    elif temp >= 60:
        return 255, 150, 250
    else:
        return 0, 0, 255