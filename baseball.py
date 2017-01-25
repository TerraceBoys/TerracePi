#!.env/bin/python
import config
import urllib
import json
import time
import display

current_data = []

def main(matrix):
    global current_data
    first = True
    while True:
        try:
            response = urllib.urlopen(config.API_URL)
            data = json.loads(response.read())
            if first:
                display.drawIntro(matrix)
            if data != current_data or first:
                display.main(matrix, data)
            current_data = data
            first = False
        except Exception as e:
            print "Error fetching game state"
            print e
            break
        time.sleep(1)

if __name__ == "__main__":
    main()
