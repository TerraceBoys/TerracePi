__author__ = 'Terrace Boiz'

import Queue
import threading

import mbtaJsonParse
import Weather
import receiveMail
import alertHandler

files = [mbtaJsonParse, Weather, receiveMail, alertHandler]
q = Queue.Queue()


def run_main(q, file):
    q.put(file.main())

if __name__ == "__main__":
    for f in files:
        t = threading.Thread(target=run_main, args=(q, f))
        t.daemon = True
        t.start()

    s = q.get()
    print s



