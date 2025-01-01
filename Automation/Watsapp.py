import pywhatkit
import csv
import time
import sys
import urllib.request as urllib2
import schedule

def is_connected():  
    try:
        urllib2.urlopen('http://www.youtube.com',timeout=1)
        return True
    except urllib2.URLError as err:
        return False

def Watsapp_Mesenger():

    connected = is_connected()

    if connected:
        file = open('WPData.csv','r')
        csvfile = csv.reader(file)

        message = "Hello bhai \n Maderchode kelya \n This is auto generated message \n Message says : Amar chutya"

        pywhatkit.sendwhatmsg_instantly('+919146997691',message,15,True,5)
        print("Message send successfully:")
    else:
        print("Internet is not connected :")

def main():
    print("----WATSAPP MESSAGE SENDER-----")
    print("Application name : "+sys.argv[0])

    if len(sys.argv) == 2:
        if (sys.argv[1] == "--h") or (sys.argv[1] == "--H"):
            print("This script is used to send emails")
            exit()
        
        if (sys.argv[1] == "--u") or (sys.argv[1] == "--U"):
            print("Usage : ApplicationName")
            exit()
    try:
        schedule.every(1).minutes.do(Watsapp_Mesenger)
        while True:
            schedule.run_pending()
            time.sleep(1)
                
    except Exception as eobj:
        print("Unable to send message due to : ",eobj)

if __name__ == "__main__":
    main()