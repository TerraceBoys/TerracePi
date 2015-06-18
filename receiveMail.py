__author__ = 'branden'


import imaplib
import email
import time
import pi_controller, People, insulter, helpDesk, sendSMS, personPicker, alertHandler, matrixControl, baseball



username = 'terraceraspberrysms@gmail.com'
password = 'TerraceRaspberryPi'
alerts = {}

#Emails must be sent in the following format
#subject: times
#body: 14:45   (this is an example time. times are military format)

def main():
    global mail
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(username, password)
        mail.list()
        while True:
            handleMail()
    except:
        print "Error in receiveMail"
        time.sleep(15)
        mail.logout()
        main()


#Reads all incoming mail
def handleMail():
    global mail
    try:
        mail.select("inbox") # connect to updated inbox.

        #Read emails that are unread
        result, data = mail.search(None, '(UNSEEN)')

        ids = data[0]                 # data is a list.
        id_list = ids.split()         # ids is a space separated string
        oldest_email_id = id_list[0]  # get the oldest unread email

        result, data = mail.fetch(oldest_email_id, "(RFC822)") #Fetch the email body for the given ID (RFC822)
        raw_email = data[0][1] #Raw text of the whole email Body

        email_message = email.message_from_string(raw_email)
        fromAddr = email_message['From']                        #Get complete from address
        sender = fromAddr.split(' ', 1)[0].replace("\"", '')    #Format from address into just first name
        emailBody = get_body(email_message)                     #Get only the email body
        subject = email_message['Subject'].lower()
        info = str.split(emailBody)
        pick_action(sender, fromAddr, subject, info)
    except:
        return


def pick_action(sender, fromAddr, subject, info):
    if pi_controller.pi_mode == pi_controller.standard:
        #Send Custom Alert
        if subject == "alert":
            info = alertHandler.prepareAlert(info)
            # Station, direction, time, distance
            if alertHandler.checkAlertFormat(sender, info):
                People.addAlert(sender, info[0], info[1], info[2], int(info[3]))
                print "New Custom Alert From: " + fromAddr
        #Send Insult
        elif subject == "insult":
            for i in info:
                print "New Insult From: " + fromAddr + " sending to " + i
            insulter.send_Insult(sender, info)
        #Send Help Information
        elif subject == "help":
            print "New Help Request From: " + fromAddr
            helpDesk.send_Help(sender)
        #Send Times of stop
        elif subject == "times":
            print "New Time Request From: " + fromAddr
            sendSMS.sendTimes(sender, *info)
        #Select a random person
        elif subject == "pick":
            print "New Person Pick From: " + fromAddr
            personPicker.pickPerson(sender, info)
        #Print message to led board
        elif subject == "led":
            print "New LED Messsage From: " + fromAddr
            message = ' '.join(info)
            matrixControl.pending_Text.append(message)
        #Start Baseball mode
        elif subject == "baseball":
            print "Entering baseball mode"
            baseball.init_game(info)
            pi_controller.pi_mode = pi_controller.baseball
    elif pi_controller.pi_mode == pi_controller.baseball:
        #Exit baseball mode
        if subject == "exit":
            pi_controller.pi_mode = pi_controller.standard
        #Exit baseball mode
        elif subject == "score":
            baseball.updateScore(info)


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