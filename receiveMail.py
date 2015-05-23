__author__ = 'branden'


import imaplib
import email
import time
import sendSMS

username = 'terraceraspberrySMS@gmail.com'
password = 'TerraceRaspberryPi'


def main():
    try:
        while True:
            handleMail()
    except:
        print "No new mail"
        time.sleep(15)
        main()


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

    fromAddr = email_message['From']
    emailBody = get_body(email_message)
    print "New Email From: " + fromAddr
    print "Body: " + emailBody



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