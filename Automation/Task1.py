import os
import time
import psutil
import smtplib
import urllib.request as urllib2
import schedule
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_connected():
    
    try:
        urllib2.urlopen('http://www.youtube.com',timeout=1)
        return True
    except urllib2.URLError as err:
        return False

def MailSender():    
    try:
        fromaddr = "maskepranav99@gmail.com"
        toaddr = "pranavbmaske@gmail.com"

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr

        body = """
        Hello %s,

        This is auto generated mail without Attachment.
        Task1 is complete.

        Thanks & Regards,
        Pranav Maske
        """%(toaddr)


        msg.attach(MIMEText(body,'plain'))

        Subject = """
        Auto Generated Mail at : %s
        """%(time.ctime())

        msg['Subject'] = Subject

        s = smtplib.SMTP('smtp.gmail.com',587)

        s.starttls()

        s.login(fromaddr,"khrrgticefafhcsp")

        text = msg.as_string()

        s.sendmail(fromaddr,toaddr,text)

        s.quit()

        print("Email successfully send.")
    
    except Exception as E:
        print("Unable to send mail : ",E)


def main():
    print("----AUTO MAIL SENDER-----")

    connected = is_connected()

    if connected:
        startTime = time.time()
        MailSender()
        endTime = time.time()
    
        print('Took %s seconds to send mail '%(endTime-startTime))
    else:
        print("There is no Internet connection")

if __name__ == "__main__":
    main()