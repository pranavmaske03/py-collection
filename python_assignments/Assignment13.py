import psutil
import sys
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
import hashlib

file_count = 0
duplicate_count = 0

def is_connected():
    
    try:
        urllib2.urlopen('http://www.youtube.com',timeout=1)
        return True
    except urllib2.URLError as err:
        return False

def MailSender(filename,time,receiver_mail):
    global file_count
    global duplicate_count

    try:
        fromaddr = "maskepranav99@gmail.com"
        toaddr = receiver_mail

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr

        body = """
        Hello %s,
        Welcome to MARVELLOUS INFOSYSTEMS.
        This is auto generated mail.

        Please find attached document which contains Log of Running process.
        Log file is created at : %s

        Total number of files scanned : %s
        Total number of duplicates found : %s

        Thanks & Regards,
        Pranav Maske
        """%(toaddr,time,file_count,duplicate_count)

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


def create_log(Arr,dir_name = "Marvellous"):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    
    log_path = os.path.join(dir_name,'duplicate%s.log'%(time.ctime()))

    fd = open(log_path,'w')
    separator = '-'*80
    fd.write(separator+"\n")        
    fd.write("Marvellous Process Log file to detect duplcates files \n")
    fd.write("Log file created at : "+time.ctime()+"\n")
    fd.write(separator+"\n")

    for data in Arr:
        fd.write("%s \n"%data)
    fd.write(separator+"\n")
    fd.close()

    print("Log file is successfully created at location : %s"%(log_path))

    connected = is_connected()

    if connected:
        startTime = time.time()
        MailSender(log_path,time.ctime(),sys.argv[3])
        endTime = time.time()
    
        print('Took %s seconds to send mail '%(endTime-startTime))
    else:
        print("There is no Internet connection")


def checksum(path,blocksize = 1024):
    afile = open(path,"rb")
    hasher = hashlib.md5()
    buffer = afile.read(blocksize)
    while len(buffer) > 0:
        hasher.update(buffer)
        buffer = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def FindDuplicate(dir_name):
    global file_count
    global duplicate_count

    flag = os.path.isabs(dir_name)

    if flag == False:
        dir_name = os.path.abspath(dir_name)
    
    exist = os.path.isdir(dir_name)
    dups = {}

    if exist == True:
        for dirs,subdirs,filename in os.walk(dir_name):
            for name in filename:
                path = os.path.join(dirs,name)
                file_hash = checksum(path)
                file_count += 1

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        
        results = list(filter(lambda x : len(x) > 1, dups.values()))
        Arr = []
        if len(results) > 0:           
            icnt = 0
            for result in results:
                for subresult in result:
                    icnt += 1
                    if icnt >= 2:
                        Arr.append(subresult)
                        duplicate_count += 1
                        os.remove(subresult)
                icnt = 0
        create_log(Arr)
    else:
        print("Invalid path")


def main():
    print("----Duplicate File Removal-----")
    print("File removing process is started.....")
    print("Application name : "+argv[0])

    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[0] == "--H":
            print("This script is used to create log files write duplicates files into that log file :")
            exit()
        
        if sys.argv[1] == "u" or sys.argv[1] == "--U":
            print("Usage : ApplicationName Name_of_Directory")
            exit()
    
    if len(sys.argv) == 4:
        try:
            schedule.every(int(argv[2])).minutes.do(FindDuplicate,sys.argv[1])
            while True:
                schedule.run_pending()
                time.sleep(1)

        except ValueError:
            print("Error : Invalid datatype of input")
        
        except Exception as E:
            print("Error : Invalid input :",E)

if __name__ == "__main__":
    main()
