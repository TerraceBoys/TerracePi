__author__ = 'Terrace Boiz'

import threading
import time

import mbtaJsonParse
import Weather
import receiveMail
import alertHandler
import server


files = [
    (mbtaJsonParse, 0),
    (Weather, 0),
    (receiveMail, 0),
    (alertHandler, 0),
    (server, 0)]


def run_main(thread_file, delay, event):
    while event.is_set():
        thread_file.main()
        time.sleep(delay)


if __name__ == "__main__":
    run_event = threading.Event()
    run_event.set()
    thread_list = []
    for f in files:
        t = threading.Thread(target=run_main, args=(f[0], f[1], run_event))
        thread_list.append(t)
        t.start()

    try:
        while 1:
            time.sleep(.1)
    except KeyboardInterrupt:
        print "Attempting to close threads..."
        run_event.clear()
        for t in thread_list:
            t.join()
        print "Threads successfully closed"