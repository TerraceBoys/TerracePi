__author__ = 'branden'

import sendSMS
import People


# Send help information to specified person
def send_help(sender):
    for p in People.allPeople:
        if p.name == sender:
            help_info = "Terrace Raspberry Pi Help\n\n" \
                        "(To create a custom alert)\n" \
                        "Subject- alert\n" \
                        "Body- Station Direction time distance\n\n" \
                        "(To send an Insult)\n" \
                        "Subject- insult\n" \
                        "Body- Name"
            sendSMS.send(help_info, p)
