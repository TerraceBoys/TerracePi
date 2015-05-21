__author__ = 'Terrace Boiz'

import smtplib
import time
import datetime

username = 'terraceraspberrySMS'
password = 'TerraceRaspberryPi'
fromaddr = 'terraceraspberrySMS@gmail.com'
brian  = '5086889360@vtext.com'
branden = '6039655776@vtext.com'
ray = '6318977618@vtext.com'




def send(msg, toaddr):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
    except:
        print("Error logging in to email client. Trying again")
        send(msg, toaddr)
    for t in toaddr:
        server.sendmail(fromaddr, t, msg)
    server.quit()
