import os
import time
import psutil
import smtplib
import urllib.request as urllib2
import schedule
from sys import *
import sys
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import csv
from datetime import datetime

def is_connected():
    
    try:
        urllib2.urlopen('http://www.youtube.com',timeout=1)
        return True
    except urllib2.URLError as err:
        return False

def MailSender(to_send):

    try:
        fromaddr = "maskepranav99@gmail.com"
        toaddr = to_send

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr

        body = """
        Hello %s,

        Happy birthday to you Brother.

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

        print("Email successfully send to : %s"%(to_send))
        print("Email sucessfylly send at time : %s"%(time.ctime()))
    
    except Exception as E:
        print("Unable to send mail : ",E)

def read_csv():

    connected = is_connected()
    
    if connected:
        today = datetime.now().day
        month = datetime.now().month

        file_name = 'Birthday.csv'
        with open(file_name, 'r') as csvFile:
            data = list(csv.reader(csvFile))

            for value in data:
                date_object = datetime.strptime(value[1], '%d:%m:%Y').date()
                if ((today == date_object.day) and (month == date_object.month)):
                    MailSender(value[0])
    else:
        print("Internet is not connected")

def main():
    print("----Marvellous Mail Sender-----")
    print("Scanning emails to send msg......")
    print("Application name : "+sys.argv[0])

    if len(sys.argv) == 2:
        if (sys.argv[1] == "--h") or (sys.argv[1] == "--H"):
            print("This script is used to send emails")
            exit()
        
        if (sys.argv[1] == "--u") or (sys.argv[1] == "--U"):
            print("Usage : ApplicationName")
            exit()
    
    try:
        schedule.every(1).days.at("00:00").do(read_csv)
        while True:
            schedule.run_pending()
            time.sleep(1)

    except ValueError:
        print("Error : Invalid datatype of input")
    
    except Exception as E:
        print("Error : Invalid input :",E)

if __name__ == "__main__":
    main()