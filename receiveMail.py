__author__ = 'branden'


import imaplib
import email
import time
import sendSMS, mbtaJsonParse

username = 'terraceraspberrySMS@gmail.com'
password = 'TerraceRaspberryPi'
alerts = {}

#Emails must be sent in the following format
#subject: times
#body: 14:45   (this is an example time. times are military format)

def main():
    try:
        while True:
            handleAlerts()
            handleMail()
    except:
        time.sleep(15)
        main()

#Handle custom alerts if they exist
def handleAlerts():
    for person in alerts:
        hrs, mins = alerts[person].split(':')
        hrs = int(hrs)
        mins = int(mins)
        if (sendSMS.timeCheck(*[hrs, mins, 23, 59])):
            for train in mbtaJsonParse.schedule['Northbound']:
                if (180 < train < 250):
                    sendSMS.sendCustomSMS(person)
                    print "Custom alert sent to: " + person
                    del alerts[person]
                    print person + " removed from custom alert list"



def handleMail():
    global fromAddr
    global emailBody
    fromAddr = ""
    emailBody = ""

    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(username, password)
    mail.list()
    mail.select("inbox") # connect to inbox.

    #Read emails that are unread and contain the subject "alert"
    result, data = mail.search(None, '(HEADER Subject "times" UNSEEN)')

    ids = data[0]                 # data is a list.
    id_list = ids.split()         # ids is a space separated string
    oldest_email_id = id_list[0]  # get the oldest

    result, data = mail.fetch(oldest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID

    raw_email = data[0][1]# here's the body, which is raw text of the whole email

    email_message = email.message_from_string(raw_email)
    print "got message"
    fromAddr = email_message['From']                        #get complete from address (e.g Branden Rodgers <branden@rodgersworld.com>)
    person = fromAddr.split(' ', 1)[0].replace("\"", '')    #Format from address into just first name
    emailBody = get_body(email_message)                     #Get only the time from the email body
    alerts[person] = emailBody                              #Enter into dict
    print "New Custom Alert From: " + fromAddr + " set to " + emailBody
    mail.logout()


#Gets the email body
def get_body(email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    body = ""
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                body += part.get_payload()
                break
    elif maintype == 'text':
        body += email_message_instance.get_payload()
    return trim_body(body)


#Gets rid of email signature
def trim_body(email_body):
    result = ""
    for letter in range (len(email_body)):
        if (email_body[letter] == "\n"):
            return result
        else:
            result += email_body[letter]


if __name__ == "__main__":
    main()