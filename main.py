__author__ = 'Terrace Boiz'

import threading
import time
import server

import mbtaJsonParse
import weather
import receiveMail
import alertHandler


files = [
    (mbtaJsonParse, 15),
    (weather, 30),
    (receiveMail, 15),
    (alertHandler, 1)
]


def run_main(thread_file, delay, event):
    thread_file.setup()
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
    server.main()

    try:
        while 1:
            time.sleep(.1)
    except KeyboardInterrupt:
        print "Attempting to close threads..."
        run_event.clear()
        for t in thread_list:
            t.join()
        print "Threads successfully closed"