__author__ = 'Terrace Boiz'

import smtplib
import datetime
import sys
import mbtaTimeDisplay, People


username = 'terraceraspberrySMS'
password = 'TerraceRaspberryPi'
fromaddr = 'terraceraspberrySMS@gmail.com'



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
        print "sending message: " + msg + " to " + t
        server.sendmail(fromaddr, t, msg)
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
    to = [person.number]
    send(msg, to)
    logSMS(person.name)

################# DAILY ALERTS ###########################

# Check to see if sms should be sent for Daily Alert
def dailyAlert(nextTrain, person):
    global sendCustom
    sendCustom = False
    if person.waitingOnDaily:
        sendCustom = True
        if (timeCheck(*People.branden.dailyTimes) and 180 < nextTrain < 250 and dayCheck(People.branden.dailyDays)):
            runAlert(nextTrain, People.branden)
            sendCustom = False
            person.waitingOnDaily = False


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

def logSMS(name):
    today = datetime.datetime.now().strftime('%c')
    text_file = open('/home/pi/Desktop/smsLog.txt', "a")
    text_file.write(today + ": Sending " + name + " a text alert" + "\n")
    text_file.close()

