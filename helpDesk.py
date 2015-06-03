__author__ = 'branden'


import sendSMS, People

#Send help information to specified person
def send_Help(sender):
    for p in People.allPeople:
        if p.name == sender:
            helpInfo = "Terrace Raspberry Pi Help:\n\nTo create custom alert:\nSubject: alert\nBody: Station Direction time distance\n\n" \
                       "To send an Insult:\n" \
                       "Subject: insult\n" \
                       "Body: Name"
            sendSMS.send(helpInfo, p)
