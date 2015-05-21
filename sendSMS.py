__author__ = 'Terrace Boiz'

import smtplib
import time
import datetime
import mbtaJsonParse

username = 'terraceraspberrySMS'
password = 'TerraceRaspberryPi'
fromaddr = 'terraceraspberrySMS@gmail.com'
brian  = '5086889360@vtext.com'
branden = '6039655776@vtext.com'
ray = '6318977618@txt.att.net'



#Login to email client and send message
def send(msg, toaddr):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
    except:
        print("Error logging-in to email client. Trying again")
        send(msg, toaddr)
    for t in toaddr:
        server.sendmail(fromaddr, t, msg)
    server.quit()


#So methods can run once a day
def run_once(f):
    def wrapper():
        if not wrapper.has_run:
            wrapper.has_run = True
            return f()
    wrapper.has_run = False
    return wrapper


################# ALERTS FOR BRANDEN ###########################

#Check to see if sms should be sent
def brandenAlert():
    if (datetime.datetime.now().time() >= datetime.time(hour=9, minute=30) and
            (mbtaJsonParse.schedule['Northbound'][0] < 250) and (mbtaJsonParse.schedule['Northbound'][0] > 180)):
        runBrandenAlert()

#Send sms only once
@run_once
def runBrandenAlert():
    msg = 'Time To Leave bro'
    to = [branden]
    send(msg, to)


################# ALERTS FOR BRIAN ###########################

#Check to see if sms should be sent
def brianAlert():
    if (datetime.datetime.now().time() >= datetime.time(hour=9, minute=30) and
            (mbtaJsonParse.schedule['Northbound'][0] < 250) and (mbtaJsonParse.schedule['Northbound'][0] > 180)):
        runBrandenAlert()

#Send sms only once
@run_once
def runBrianAlert():
    msg = 'Time To Leave bro'
    to = [brian]
    send(msg, to)


################# ALERTS FOR RAY ###########################

#Check to see if sms should be sent
def rayAlert():
    if (datetime.datetime.now().time() >= datetime.time(hour=7, minute=40) and
            (mbtaJsonParse.schedule['Northbound'][0] < 250) and (mbtaJsonParse.schedule['Northbound'][0] > 180)):
        runRayAlert()

#Send sms only once
@run_once
def runRayAlert():
    msg = 'Time To Leave bro'
    to = [ray]
    send(msg, to)