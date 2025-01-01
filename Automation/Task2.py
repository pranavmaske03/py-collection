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
import sys

def process_log():
    listprocess = []

    for proc in psutil.process_iter(['name','username','pid']):
        listprocess.append(proc.info)
    return listprocess

def is_connected():
    
    try:
        urllib2.urlopen('http://www.youtube.com',timeout=1)
        return True
    except urllib2.URLError as err:
        return False

def MailSender(filename,time):

    try:
        fromaddr = "maskepranav99@gmail.com"
        toaddr = "pranavbmaske@gmail.com"

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr

        body = """
        Hello %s,
        Welcome to Marvellous Infosystems.
        Please find attached document which contains Log of Running process.
        Log file is created at : %s

        This is auto generated mail.

        Thanks & Regards,
        Pranav Bibhishan Maske
        """%(toaddr,time)

        Subject = """
        Marvellous Infosystems Process log generated at : %s
        """%(time)

        msg['Subject'] = Subject

        msg.attach(MIMEText(body,'plain'))

        attachment = open(filename,"rb")

        p = MIMEBase('application','octet-stream')

        p.set_payload((attachment).read())

        encoders.encode_base64(p)

        p.add_header('Content-Disposition',"attachment; filename = %s" %filename)

        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com',587)

        s.starttls()

        s.login(fromaddr,"khrrgticefafhcsp")

        text = msg.as_string()

        s.sendmail(fromaddr,toaddr,text)

        s.quit()

        print("Log file successfully sent through Mail")
    
    except Exception as E:
        print("Unable to send mail : ",E)

def create_log():
    exist = os.path.exists('Marvellous.log')

    if exist == False:
        fd = open('Marvellous.log','w')

    log_path = os.path.join('Marvellous.log')
   
    fd = open(log_path,'w')
    separator = "-"*80
    fd.write(separator+"\n")
    fd.write("Marvellous Process Log file \n")
    fd.write("Log file created at : "+time.ctime()+"\n")
    fd.write(separator+"\n")

    Arr = process_log()

    for data in Arr:
        fd.write("%s\n"%data)

    fd.write(separator+"\n")
    fd.close()
    print("Log file is successfully generated at location : %s"%(log_path))

    connected = is_connected()

    if connected:
        startTime = time.time()
        MailSender(log_path,time.ctime())
        endTime = time.time()
    
        print('Took %s seconds to send mail '%(endTime-startTime))
    else:
        print("There is no Internet connection")
    

def main():
    print("----Marvellous Process Logger-----")
    print("Application name : "+sys.argv[0])

    if len(sys.argv) == 2:
        if (sys.argv[1] == "--h") or (sys.argv[1] == "--H"):
            print("This script is used to send log record of running processes")
            exit()
        
        if (sys.argv[1] == "--u") or (sys.argv[1] == "--U"):
            print("Usage : ApplicationName")
            exit()
    
    try:
        create_log()
    except ValueError:
        print("Error : Invalid datatype of input")
    
    except Exception as E:
        print("Error : Invalid input :",E)

if __name__ == "__main__":
    main() 