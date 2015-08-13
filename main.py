__author__ = 'Terrace Boiz'

import threading

import mbtaJsonParse
import Weather
import receiveMail
import alertHandler
import server


files = [mbtaJsonParse, Weather, receiveMail, alertHandler, server]


def run_main(thread_file):
    thread_file.main()

if __name__ == "__main__":
    for f in files:
        t = threading.Thread(target=run_main, args=f)
        t.daemon = True
        t.start()