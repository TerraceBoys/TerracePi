__author__ = 'Brian Cox'

import urllib2
import json
import sendSMS, People

insult_url = 'http://pleaseinsult.me/api?severity=random'

def main():
    print get_insult()


def get_insult():
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    response = opener.open(insult_url)
    insult_data = json.loads(response.read().decode())
    insult = insult_data['insult']
    return insult

def send_Insult(sender, recipient):
    insult = get_insult() + "\nLove,\n" + sender
    for r in recipient:
        for p in People.insultPeople:
            if p.name == r:
                sendSMS.send(insult, p)
                break

if __name__ == '__main__':
    main()