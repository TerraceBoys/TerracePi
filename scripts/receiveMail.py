__author__ = 'branden'

import imaplib
import email
import time
import traceback

import People
import insulter
import helpDesk
import sendSMS
import personPicker
from scripts import alertHandler
import matrixControl


username = 'terraceraspberrysms@gmail.com'
password = 'TerraceRaspberryPi'
alerts = {}

# Emails must be sent in the following format
# subject: times
# body: 14:45   (this is an example time. times are military format)


def main():
    global mail, ssl 
    ssl = False
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(username, password)
        mail.list()
        while True:
            handle_mail()
            if ssl:
                break
            time.sleep(1)
        time.sleep(15)
        mail.logout()
        main()
    except:
        print "Error in receiveMail"
        print traceback.print_exc()
        time.sleep(15)
        mail.logout()
        main()


# Reads all incoming mail
def handle_mail():
    global mail, ssl
    try:
        mail.select("inbox")  # connect to updated inbox.

        # Read emails that are unread
        result, data = mail.search(None, '(UNSEEN)')

        ids = data[0]  # data is a list.
        id_list = ids.split()  # ids is a space separated string
        oldest_email_id = id_list[0]  # get the oldest unread email

        result, data = mail.fetch(oldest_email_id, "(RFC822)")  # Fetch the email body for the given ID (RFC822)
        raw_email = data[0][1]  # Raw text of the whole email Body

        email_message = email.message_from_string(raw_email)
        from_addr = email_message['From']  # Get complete from address
        sender = from_addr.split(' ', 1)[0].replace("\"", '')  # Format from address into just first name
        email_body = get_body(email_message)  # Get only the email body
        subject = email_message['Subject'].lower()

        # Send Custom Alert
        if subject == "alert":
            info = alertHandler.prepare_alert(str.split(email_body))
            # Station, direction, time, distance
            if alertHandler.check_alert_format(sender, info):
                People.add_alert(sender, info[0], info[1], info[2], int(info[3]))
                print "New Custom Alert From: " + from_addr + " set to " + email_body
        # Send Insult
        elif subject == "insult":
            info = str.split(email_body)
            for i in info:
                print "New Insult From: " + from_addr + " sending to " + i
            insulter.send_insult(sender, info)
        # Send Help Information
        elif subject == "help":
            print "New Help Request From: " + from_addr
            helpDesk.send_help(sender)
        # Send Times of stop
        elif subject == "times":
            print "New Time Request From: " + from_addr
            info = str.split(email_body)
            sendSMS.send_times(sender, *info)
        # Select a random person
        elif subject == "pick":
            print "New Person Pick From: " + from_addr
            info = str.split(email_body)
            personPicker.pick_person(sender, info)
        elif subject == "led":
            print "New LED Messsage From: " + from_addr
            info = str.split(email_body)
            message = ' '.join(info)
            matrixControl.pending_Text.append(message)
    except IndexError:
        return
    except:
        ssl = True
        return
        


# Gets the email body
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


# Gets rid of email signature
def trim_body(email_body):
    result = ""
    for letter in range(len(email_body)):
        if email_body[letter] == "\n":
            return result
        else:
            result += email_body[letter]


if __name__ == "__main__":
    main()