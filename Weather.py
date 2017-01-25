__author__ = 'Terrace Boiz'

import urllib
import json
import time
import traceback
import matrixControl

access_key = 'aceec2d6587b3b0c'
weather_url = 'http://api.wunderground.com/api/' + access_key + '/conditions/q/MA/Roxbury_Crossing.json'
spacer = "-------------------------------------------"


def main(matrix):
    try:
        while True:
            grab_weather()
            current_weather, color = weather_panel()
            matrixControl.set_weather(current_weather, color)
            matrixControl.main(matrix)
            for x in range(300):
                time.sleep(1)
    except SystemExit:
        print "Thread terminated"
    except IOError:
        print "Caught IOError while Loading Weather - Trying Again"
        print traceback.print_exc()
        time.sleep(600)
        main()
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
    return str(temperature), get_temp_color(temperature)


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


if __name__ == "__main__":
    main()
