__author__ = 'Terrace Boiz'


import sendSMS, People

#Send help information to specified person
def send_Help(sender):
    for p in People.allPeople:
        if p.name == sender:
            helpInfo = "Terrace Raspberry Pi Help\n\n" \
                       "(To create a custom alert)\n" \
                       "Subject- alert\n" \
                       "Body- Station Direction time distance\n\n" \
                       "(To send an Insult)\n" \
                       "Subject- insult\n" \
                       "Body- Name"
            sendSMS.send(helpInfo, p)
