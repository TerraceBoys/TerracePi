__author__ = 'Terrace Boiz'

import smtplib
import datetime
import os
import platform
import mbtaTimeDisplay, People, mbtaJsonParse
from collections import defaultdict


username = 'terraceraspberrySMS'
password = 'TerraceRaspberryPi'
fromaddr = 'terraceraspberrySMS@gmail.com'



#Login to email client and send message
def send(msg, person):
    server = smtplib.SMTP()
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
    except:
        print("Error logging-in to email client. Trying again")
        send(msg, person)
    r = msg.replace("\n", " ")
    print 'Sending message: ' + '"' + r + '"' + ' to ' + person.name
    server.sendmail(fromaddr, person.number, msg)
    logSMS(person.name, msg)
    server.quit()


# So methods can run once a day
def run_once(f):
    global sendCustom
    def wrapper(*args):
        if sendCustom:
            return f(*args)
        elif not wrapper.has_run:
            wrapper.has_run = True
            return f(*args)
    sendCustom = False
    wrapper.has_run = False
    return wrapper


#Sends a custom alert one time to specified person
def sendCustomSMS(person, nextTrain):
    global sendCustom
    sendCustom = True
    runAlert(nextTrain, person)
    sendCustom = False

# Send sms only once
@run_once
def runAlert(nextTrain, person):
    m, s = mbtaTimeDisplay.secsToMins(nextTrain)
    time = str(m) + 'mins and ' + str(s) + 'seconds'
    msg = 'Time To Leave bro. Train comes in ' + time
    send(msg, person)

def sendTimes(name, station, direction=None):
    temp = defaultdict(list)
    mbtaJsonParse.popDict(temp, station)
    person = People.personGrab(name)
    msg = ""
    if direction == 'Northbound':
        msg += mbtaTimeDisplay.popNorth(temp, station)
    elif direction == 'Southbound':
        msg += mbtaTimeDisplay.popSouth(temp, station)
    else:
        msg += mbtaTimeDisplay.popNorth(temp, station)
        msg += mbtaTimeDisplay.popSouth(temp, station)

    print 'got to the sending phase'
    send(msg, person)


################# TIME AND DAY CHECKS ###########################

#Check time of the day if text message should be sent
def timeCheck(hMin, mMin, hMax, mMax):
    now = datetime.datetime.now().time()
    lower = datetime.time(hour=hMin, minute=mMin)
    upper = datetime.time(hour=hMax, minute=mMax)
    return lower <= now <= upper

# Check day of the week if text message should be sent
def dayCheck(days):
    today = datetime.date.today().weekday()
    for d in days:
        if (d == today):
            return True
    return False

###################### SMS LOG #################################
def logSMS(name, msg):
    try:
        p = platform.uname()
    except:
        p = os.uname()

    if p[0] == 'Windows':
        path = 'C:/Users/Brian Cox/Desktop/smsLog.txt'
    elif p[0] == 'Linux' or p[0] == 'Linux2':
        path = '/home/pi/Desktop/smsLog.txt'
    elif p[0] == 'Darwin':
        path = '/Users/branden/Desktop/smsLog.txt'
    else:
        raise ValueError('Platform was not identified correctly')

    text_file = open(path, "a")
    today = datetime.datetime.now().strftime('%c')
    r = msg.replace("\n", " ")
    text_file.write(today + ": Sending " + name + ' - "' + r + '"' + "\n")
    text_file.close()

