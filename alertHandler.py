__author__ = 'branden'


import time
import sendSMS, mbtaJsonParse, People
from collections import defaultdict


def main():
    try:
        while True:
            handleAlerts()
            time.sleep(15)
    except:
        print "Error in alertHandler"
        time.sleep(15)
        main()


#Handle custom alerts if they exist
def handleAlerts():
    tempDict = defaultdict(list)
    for person in People.allPeople:
        #If person has a custom alert
        if person.alertInfo != None:
            hrs, mins = person.alertInfo.time.split(':')
            hrs = int(hrs)
            mins = int(mins)
            #If the current time is past the alert time
            if (sendSMS.timeCheck(*[hrs, mins, 23, 59])):
                mbtaJsonParse.popDict(tempDict, person.alertInfo.station)
                for nextTrain in tempDict[person.alertInfo.direction]:
                   #If the next train is at the correct distance
                   if ((person.alertInfo.dist * 60) < nextTrain < ((person.alertInfo.dist * 60) + 70)):
                        sendSMS.sendCustomSMS(person, nextTrain)
                        print "Custom alert sent to: " + person.name
                        person.alertInfo = None
                        tempDict.clear()
                        break



if __name__ == "__main__":
    main()