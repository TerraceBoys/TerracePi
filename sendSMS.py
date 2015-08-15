__author__ = 'Terrace Boiz'

import smtplib
import datetime
import os
import platform
import traceback
from collections import defaultdict

import mbtaTimeDisplay
import People
from scripts import mbtaJsonParse


username = 'terraceraspberrySMS'
password = 'TerraceRaspberryPi'
fromaddr = 'terraceraspberrySMS@gmail.com'


# Login to email client and send message
def send(msg, person):
    server = smtplib.SMTP()
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
    except:
        print("Error logging-in to email client. Trying again")
        print traceback.print_exc()
        send(msg, person)
    r = msg.replace("\n", " ")
    print 'Sending message: ' + '"' + r + '"' + ' to ' + person.name
    server.sendmail(fromaddr, person.number, msg)
    log_sms(person.name, msg)
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


# Sends a custom alert one time to specified person
def send_custom_sms(person, next_train):
    global sendCustom
    sendCustom = True
    run_alert(next_train, person)
    print "Custom alert sent to: " + person.name
    sendCustom = False


# Send sms only once
@run_once
def run_alert(next_train, person):
    m, s = mbtaTimeDisplay.secs_to_mins(next_train)
    time = str(m) + 'mins and ' + str(s) + 'seconds'
    msg = 'Time To Leave bro. Train comes in ' + time
    send(msg, person)


def send_times(name, station, direction=None):
    temp = defaultdict(list)
    mbtaJsonParse.pop_dict(temp, station)
    person = People.person_grab(name)
    msg = ""
    if direction == 'Northbound':
        msg += mbtaTimeDisplay.pop_north(temp, station)
    elif direction == 'Southbound':
        msg += mbtaTimeDisplay.pop_south(temp, station)
    else:
        msg += mbtaTimeDisplay.pop_north(temp, station)
        msg += mbtaTimeDisplay.pop_south(temp, station)
    send(msg, person)


# ################ TIME AND DAY CHECKS ###########################

# Check time of the day if text message should be sent
def time_check(h_min, m_min, h_max, m_max):
    now = datetime.datetime.now().time()
    lower = datetime.time(hour=h_min, minute=m_min)
    upper = datetime.time(hour=h_max, minute=m_max)
    return lower <= now <= upper


# Check day of the week if text message should be sent
def day_check(days):
    today = datetime.date.today().weekday()
    for d in days:
        if d == today:
            return True
    return False


# ##################### SMS LOG #################################
def log_sms(name, msg):
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

