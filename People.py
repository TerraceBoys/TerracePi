__author__ = 'branden'


class customAlert:
    def __init__(self, station, direction, time, dist):
        self.station = station  # String: Station that the alert is for
        self.direction = direction  # String: Northbound/Southbound
        self.time = time  # String: Desired time to leave
        self.dist = dist  # Int: Distance from the train station (in minutes)


class dailyAlert:
    def __init__(self, station, direction, time, days, dist):
        self.station = station  # String: Station
        self.direction = direction  # String: Northbound/Southbound
        self.time = time  # Array: Desired time window to leave
        self.days = days  # Array: Days to send the alert
        self.dist = dist  # Int: Distance from the train station (in minutes)


class Person:
    def __init__(self, name, number, dailyAlertInfo=None, waitingOnDaily=True, customAlertInfo=None):
        self.name = name  # String: Person's name
        self.number = number  # String: Person's phone number
        self.dailyAlertInfo = dailyAlertInfo  # dailyAlert: Information about daily alert
        self.waitingOnDaily = waitingOnDaily  # Boolean: True if they have not received a daily alert today
        self.customAlertInfo = customAlertInfo  # customAlert: Information about custom alert


# ############ DAILY ALERT INFO #######################

weekdays = [0, 1, 2, 3, 4]
summerWeekdays = [0, 1, 2, 3]

brandenDaily = dailyAlert('Roxbury', 'Northbound', [9, 30, 10, 0], summerWeekdays, 4)
brianDaily = dailyAlert('Roxbury', 'Northbound', [9, 30, 10, 0], summerWeekdays, 4)
rayDaily = dailyAlert('Roxbury', 'Northbound', [7, 50, 8, 30], weekdays, 4)

# #######  People for custom and daily alerts #######################

branden = Person('Branden', '6039655776@vtext.com', brandenDaily)
brian = Person('Brian', '5086889360@vtext.com', brianDaily)
ray = Person('Raymond', '6318977618@txt.att.net', rayDaily)

allPeople = [branden, brian, ray]


# #######  People just for insults ##############

corinne = Person('Corinne', '7746446908@tmomail.net')
allison = Person('Allison', '8608037963@vtext.com')
mark = Person('Mark', '2018350105@vtext.com')
jj = Person('JJ', '2153017800@vtext.com')
allie = Person('Allie', '2019650132@txt.att.net')

insultPeople = [branden, brian, ray, corinne, allison, mark, jj, allie]


# ################## PEOPLE METHODS ####################

# Creates a custom alert from the fields given
# Called in receiveMail
def add_alert(name, station, direction, time, dist):
    alert = customAlert(station, direction, time, dist)
    for person in allPeople:
        if person.name == name:
            person.customAlertInfo = alert
            break


def person_grab(name):
    for person in allPeople:
        if person.name == name:
            return person