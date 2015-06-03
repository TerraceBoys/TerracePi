__author__ = 'branden'


class customAlert:
    def __init__(self, station, direction, time, dist):
        self.station = station
        self.direction = direction
        self.time = time
        self.dist = dist

class Person:
    def __init__(self, name, number, dailyTimes, dailyDays, waitingOnDaily = True, alertInfo = None):
        self.name = name                #Person's name
        self.number = number            #Person's phone number
        self.dailyTimes = dailyTimes    #Time window for Daily Alert (Array)
        self.dailyDays = dailyDays      #The days of the week to send daily alert
        self.waitingOnDaily = waitingOnDaily
        self.alertInfo = alertInfo      #Information about custom alert


weekdays = [0,1,2,3,4]
summerWeekdays = [0,1,2,3]

#Instances of people
branden = Person('Branden', '6039655776@vtext.com', [9,30,10,0], summerWeekdays)
brian = Person('Brian', '5086889360@vtext.com', [9,30,10,0], summerWeekdays)
ray = Person('Raymond', '6318977618@txt.att.net', [7,40,8,20], weekdays)
corinne = Person('Corinne', '7746446908@tmomail.net', None, None)
allison = Person('Allison', '8608037963@vtext.com', None, None)
mark = Person('Mark', '2018350105@vtext.com', None, None)
jj = Person('JJ', '2153017800@vtext.com', None, None)
allie = Person('Allie', '2019650132@txt.att.net', None, None)

allPeople = [branden, brian, ray]
insultPeople = [branden, brian, ray, corinne, allison, mark, jj, allie]


def addAlert(name, station, direction, time, dist):
    alert = customAlert(station, direction, time, dist)
    for person in allPeople:
        if person.name == name:
            person.alertInfo = alert
            break
