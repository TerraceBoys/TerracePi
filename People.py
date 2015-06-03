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

allPeople = [branden, brian, ray]


def addAlert(name, station, direction, time, dist):
    alert = customAlert(station, direction, time, dist)
    for person in allPeople:
        if person.name == name:
            person.alertInfo = alert
            break
