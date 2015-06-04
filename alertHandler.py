__author__ = 'branden'


import time
import sendSMS, mbtaJsonParse, People
from collections import defaultdict


def main():
    while True:
        handleCustomAlerts()
        handleDailyAlerts()
        time.sleep(15)
    # except:
    #     print "Error in alertHandler"
    #     time.sleep(15)
    #     main()

############## CUSTOM ALERTS ##########################

#Handle custom alerts if they exist
def handleCustomAlerts():
    for person in People.allPeople:
        tempDict = defaultdict(list)
        #If person has a custom alert
        if person.customAlertInfo != None:
            hrs, mins = person.customAlertInfo.time.split(':')
            hrs = int(hrs)
            mins = int(mins)
            #If the current time is past the alert time
            if (sendSMS.timeCheck(*[hrs, mins, 23, 59])):
                mbtaJsonParse.popDict(tempDict, person.cutsomAlertInfo.station)
                for nextTrain in tempDict[person.customAlertInfo.direction]:
                   #If the next train is at the correct distance
                   if ((person.customAlertInfo.dist * 60) < nextTrain < ((person.customAlertInfo.dist * 60) + 70)):
                        sendSMS.sendCustomSMS(person, nextTrain)
                        print "Custom alert sent to: " + person.name
                        person.customAlertInfo = None
                        tempDict.clear()
                        break


############### DAILY ALERTS ###########################

# Check to see if sms should be sent for Daily Alert
def handleDailyAlerts():
    sendSMS.sendCustom = False
    for person in People.allPeople:
        tempDict = defaultdict(list)
        if person.dailyAlertInfo != None and (sendSMS.timeCheck(*person.dailyAlertInfo.time)):
            if person.waitingOnDaily:
                mbtaJsonParse.popDict(tempDict, person.dailyAlertInfo.station)
                for nextTrain in tempDict[person.dailyAlertInfo.direction]:
                    if ((person.dailyAlertInfo.dist * 60) < nextTrain < ((person.dailyAlertInfo.dist * 60) + 70)) and \
                            sendSMS.dayCheck(person.dailyAlertInfo.days):
                        sendSMS.sendCustom = True
                        sendSMS.runAlert(nextTrain, person)
                        sendSMS.sendCustom = False
                        person.waitingOnDaily = False
                        break


if __name__ == "__main__":
    main()