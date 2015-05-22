__author__ = 'Terrace Boiz'

import smtplib
import datetime

username = 'terraceraspberrySMS'
password = 'TerraceRaspberryPi'
fromaddr = 'terraceraspberrySMS@gmail.com'
brian  = '5086889360@vtext.com'
branden = '6039655776@vtext.com'
ray = '6318977618@txt.att.net'

weekdays = [0,1,2,3,4]
summerWeekdays = [0,1,2,3]

rayTime = [7,40,8,20]
brianTime = [9,30,10,0]
brandenTime = [9,30,10,0]




#Login to email client and send message
def send(msg, toaddr):
    server = smtplib.SMTP()
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


# So methods can run once a day
def run_once(f):
    def wrapper():
        if not wrapper.has_run:
            wrapper.has_run = True
            return f()
    wrapper.has_run = False
    return wrapper


################# ALERTS FOR BRANDEN ###########################

# Check to see if sms should be sent
def brandenAlert(nextTrain):
    if (timeCheck(*brandenTime) and 180 < nextTrain < 250 and (dayCheck(summerWeekdays))):
        runBrandenAlert()

# Send sms only once
@run_once
def runBrandenAlert():
    msg = 'Time To Leave bro'
    to = [branden]
    print 'Sending Branden an Alert'
    send(msg, to)


################# ALERTS FOR BRIAN ###########################

#Check to see if sms should be sent
def brianAlert(nextTrain):
    if (timeCheck(*brianTime) and 180 < nextTrain < 250 and (dayCheck(summerWeekdays))):
        runBrianAlert()

# Send sms only once
@run_once
def runBrianAlert():
    msg = 'Time To Leave bro'
    to = [brian]
    print 'Sending Brian an Alert'
    send(msg, to)


################# ALERTS FOR RAY ###########################

# Check to see if sms should be sent
def rayAlert(nextTrain):
    if (timeCheck(*rayTime) and 180 < nextTrain < 250 and (dayCheck(weekdays))):
        runBrianAlert()

# Send sms only once
@run_once
def runRayAlert():
    msg = 'Time To Leave bro'
    to = [ray]
    print 'Sending Ray an Alert'
    send(msg, to)


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

