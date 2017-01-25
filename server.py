import controller
import baseball
from thread2 import Thread
from flask import Flask
from rgbmatrix import Adafruit_RGBmatrix

matrix = Adafruit_RGBmatrix(32, 2)
app = Flask(__name__)
t = None
c = controller

@app.route("/mbta")
def switch_mbta():
    run_thread(c.setup_run)
    return "Maybe no error"

@app.route("/baseball")
def switch_baseball():
    c.kill_threads()
    run_thread(baseball.main)
    return "SHould be baseball"

@app.route("/baseball/kill")
def kill_baseball():
    global t 
    if t and t.isAlive():
        t.terminate()
        t.join()
    return "Baseball killed?"    

@app.route("/mbta/kill")
def kill_mbta():
    print "Prep kill"
    c.kill_threads()
    print "Post controller call"
    global t
    if t and t.isAlive(): 
       t.terminate()
       t.join()
    print "post terminate"
    print "Post join"
    return "Hopefully kill"

def run_thread(f):
    matrix.Clear()
    switch = Thread(target = f, args=(matrix,))
    switch.start()
    global t
    if t and t.isAlive(): 
        t.terminate()
    t = switch

def main():
    run_thread(c.setup_run)
    app.run(host='0.0.0.0', port=8080)

main()
