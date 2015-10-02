__author__ = 'branden'

import random

import sendSMS
import People

# Picks a random person given a list of people
def pick_person(sender, people):
    index = random.randint(0, len(people)-1)
    msg = "The Pi Gods Have Selected " + people[index]
    s = People.person_grab(sender)
    sendSMS.send(msg, s)