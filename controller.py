import Queue
from thread2 import Thread

import mbtaJsonParse
import Weather
import matrixControl

files = [mbtaJsonParse, Weather, matrixControl]
q = Queue.Queue()
threads = []

def run_main(q, file, matrix):
    q.put(file.main(matrix))

def kill_threads():
    global threads
    for t in threads:
        if t and t.isAlive():
            t.terminate()
    threads = []

def setup_run(matrix):
    global threads
    for f in files:
        t = Thread(target=run_main, args=(q, f, matrix))
        t.daemon = True
        t.start()
        threads = threads + [t]
    s = q.get()

if __name__ == "__main__":
    setup_run(matrix)
