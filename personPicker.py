__author__ = 'branden'


import sendSMS, People
import random


#Picks a random person given a list of people
def pickPerson(sender, people):
    index = random.randint(0, len(people)-1)
    msg = "The Pi Gods Have Selected " + people[index]
    s = People.personGrab(sender)
    sendSMS.send(msg, s)