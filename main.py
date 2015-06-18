__author__ = 'Terrace Boiz'

import mbtaJsonParse
import Weather
import receiveMail
import baseball
import alertHandler
import Queue
import threading

standard = [mbtaJsonParse, Weather, receiveMail, alertHandler]
baseball = [baseball, alertHandler, receiveMail]

pi_mode = standard

q = Queue.Queue()

def runMain(q, file):
    q.put(file.main())

if __name__ == "__main__":

    for f in standard:
        t = threading.Thread(target=runMain, args = (q, f))
        t.daemon = True
        t.start()

    s = q.get()
    print s




