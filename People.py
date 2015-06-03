__author__ = 'branden'


class customAlert:
    def __init__(self, station, direction, time, dist):
        self.station = station        #String: Station that the alert is for
        self.direction = direction    #String: Northbound/Southbound
        self.time = time              #String: Desired time to leave
        self.dist = dist              #Int: Distance from the train station (in minutes)

class Person:
    def __init__(self, name, number, dailyTimes, dailyDays, waitingOnDaily = True, alertInfo = None):
        self.name = name                     #String: Person's name
        self.number = number                 #String: Person's phone number
        self.dailyTimes = dailyTimes         #Array: Time window for Daily Alert
        self.dailyDays = dailyDays           #Array: The days of the week to send daily alert
        self.waitingOnDaily = waitingOnDaily #Boolean: True if they have not received a daily alert today
        self.alertInfo = alertInfo           #customAlert: Information about custom alert


weekdays = [0,1,2,3,4]
summerWeekdays = [0,1,2,3]

#People for custom and daily alerts
branden = Person('Branden', '6039655776@vtext.com', [9,30,10,0], summerWeekdays)
brian = Person('Brian', '5086889360@vtext.com', [9,30,10,0], summerWeekdays)
ray = Person('Raymond', '6318977618@txt.att.net', [7,40,8,20], weekdays)

allPeople = [branden, brian, ray]


#People just for insults
corinne = Person('Corinne', '7746446908@tmomail.net', None, None)
allison = Person('Allison', '8608037963@vtext.com', None, None)
mark = Person('Mark', '2018350105@vtext.com', None, None)
jj = Person('JJ', '2153017800@vtext.com', None, None)
allie = Person('Allie', '2019650132@txt.att.net', None, None)

insultPeople = [branden, brian, ray, corinne, allison, mark, jj, allie]


#Creates a custom alert from the fields given
#Called in receiveMail
def addAlert(name, station, direction, time, dist):
    alert = customAlert(station, direction, time, dist)
    for person in allPeople:
        if person.name == name:
            person.alertInfo = alert
            break

def personGrab(name):
    for person in allPeople:
        if person.name == name:
            return person