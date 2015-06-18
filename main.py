__author__ = 'Terrace Boiz'

import mbtaJsonParse
import Weather
import receiveMail
import alertHandler

import Queue
import threading

standard = [mbtaJsonParse, Weather, receiveMail, alertHandler]
baseball = [alertHandler, receiveMail]

pi_mode = standard

q = Queue.Queue()

def runMain(q, pi_mode):
    q.put(pi_mode.main())

if __name__ == "__main__":

    for f in pi_mode:
        t = threading.Thread(target=runMain, args = (q, f))
        t.daemon = True
        t.start()

    s = q.get()
    print s




