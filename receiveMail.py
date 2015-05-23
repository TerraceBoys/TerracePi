__author__ = 'branden'


import imaplib
import email

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('terraceraspberrySMS@gmail.com', 'TerraceRaspberryPi')
mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("inbox") # connect to inbox.

result, data = mail.search(None, '(HEADER Subject "alert" UNSEEN)')


ids = result[len(result)-1] # data is a list.
id_list = ids.split() # ids is a space separated string
oldest_email_id = id_list[-1] # get the latest

result, data = mail.fetch(oldest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID

raw_email = result[0][1]# here's the body, which is raw text of the whole email
# including headers and alternate payloads


email_message = email.message_from_string(raw_email)

print email_message['To']

print email_message['From']



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

    print trim_body(body)


def trim_body(email_body):
    result = ""
    for letter in range (len(email_body)):
        if (email_body[letter] == "\n"):
            return result
        else:
            result += email_body[letter]

get_body(email_message)