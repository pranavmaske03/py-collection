import psutil
import sys
import os 
import time

def process_log():
    listprocess = []

    for proc in psutil.process_iter(['name','username','pid']):
        listprocess.append(proc.info)
    return listprocess

def create_log(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    file_name = os.path.join(dir_name,"Infosystems.txt")
   
    fd = open(file_name,'w')
    separator = "-"*80
    fd.write(separator+"\n")
    fd.write("Marvellous Process Log file")
    fd.write("Log file created at : "+time.ctime()+"\n")
    fd.write(separator+"\n")
    Arr = process_log()
    for data in Arr:
        fd.write("%s\n"%data)
    fd.write(separator+"\n")
    fd.close()
    

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script is used to display information of the process ")
            exit()
        
        if sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Usage : ApplicationName  Name_of_Process")
            exit()

        try:
            create_log(sys.argv[1])
        except Exception as eobj:
            print("Unable to do task due to : ",eobj)

if __name__ == "__main__":
    main()