__author__ = 'branden'

import time
import traceback
from collections import defaultdict

import sendSMS
import mbtaJsonParse
import People


def main():
    try:
        while True:
            handle_custom_alerts()
            # handle_daily_alerts()
            time.sleep(15)
    except:
        print "Error in alertHandler"
        print traceback.print_exc()
        time.sleep(15)
        # main()


# ######################### CUSTOM ALERTS ##################################

# Handle custom alerts if they exist
def handle_custom_alerts():
    temp_dict = defaultdict(list)
    for person in People.allPeople:
        # If person has a pending custom alert
        if person.customAlertInfo is not None:
            hrs, mins = person.customAlertInfo.time.split(':')
            hrs = int(hrs)
            mins = int(mins)
            # If the current time is past the alert time
            if sendSMS.time_check(*[hrs, mins, 23, 59]):
                mbtaJsonParse.pop_dict(temp_dict, person.customAlertInfo.station)
                for nextTrain in temp_dict[person.customAlertInfo.direction]:
                    # If the next train is at the correct distance
                    if (person.customAlertInfo.dist * 60) < nextTrain < ((person.customAlertInfo.dist * 60) + 70):
                        sendSMS.send_custom_sms(person, nextTrain)
                        person.customAlertInfo = None
                        break


# Checks to see if emailed alerts are properly formatted
def check_alert_format(sender, email_info):
    if (email_info[0] in mbtaJsonParse.stationConverter) and \
            (email_info[1] == "Northbound" or email_info[1] == "Southbound") and \
            (":" in email_info[2]) and (0 < int(email_info[3]) < 60):
        return True
    else:
        msg = "Incorrect Alert Format. Please check spelling and try again"
        s = People.person_grab(sender)
        sendSMS.send(msg, s)
        return False


# Make sure station and direction are uppercase for custom alerts
def prepare_alert(email_info):
    email_info[0] = email_info[0].title()
    email_info[1] = email_info[1].title()
    return email_info


# ######################### DAILY ALERTS ###################################

# Check to see if sms should be sent for Daily Alert
def handle_daily_alerts():
    sendSMS.sendCustom = False
    temp_dict = defaultdict(list)
    for person in People.allPeople:
        if eligible_for_daily(person):
            mbtaJsonParse.pop_dict(temp_dict, person.dailyAlertInfo.station)
            for nextTrain in temp_dict[person.dailyAlertInfo.direction]:
                if (person.dailyAlertInfo.dist * 60) < nextTrain < ((person.dailyAlertInfo.dist * 60) + 70):
                    sendSMS.sendCustom = True
                    sendSMS.run_alert(nextTrain, person)
                    sendSMS.sendCustom = False
                    person.waitingOnDaily = False
                    break


# Determines if all daily alert criteria are met
# is it within the set time, has the person received an alert today yet, is it the right day
def eligible_for_daily(person):
    if (person.dailyAlertInfo is not None) and \
            (sendSMS.time_check(*person.dailyAlertInfo.time)) and \
            person.waitingOnDaily and \
            (sendSMS.day_check(person.dailyAlertInfo.days)):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
