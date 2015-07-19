__author__ = 'Terrace Boiz'

import sendSMS, mbtaJsonParse, People
from collections import defaultdict


def decide_route(name):
    person = People.personGrab(name)
    temp_dict = defaultdict(list)
    mbtaJsonParse.popDict(temp_dict, north, 'Green Line E')
    for time in temp_dict['Northbound']:
        if 100 < time < 300:
            m, s = mbtaTimeDisplay.secsToMins(time)
            time_display = mbtaTimeDisplay.timeHandler(m, s)
            msg = 'Get off at North Station - Green Line comes in ' + time_display
            sendSMS.send(msg, person)
            return
    msg = 'Get off at Community Station'
    sendSMS.send(msg, person)
    
    
    