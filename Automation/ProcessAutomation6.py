import psutil
import time
import schedule
import os
import sys

def CreateLog(FolderName = "Marvellous"):

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    FileName = os.path.join(FolderName,"Marvellous%s.log"%(time.ctime()))

    fd = open(FileName,"a")
    separator = "-"*70

    fd.write(separator+"\n")
    fd.write("Marvellous Process Log"+"\n")
    fd.write("Log file created at : "+time.ctime()+"\n")
    fd.write(separator+"\n")

    Arr = GetProcessInfo()

    for data in Arr:
        fd.write("%s \n"%data)
    fd.write(separator+"\n")

    print("Log file is succefully created")
    fd.close()


def GetProcessInfo():
    listprocess = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            vms = proc.memory_info().vms / (1024 * 1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
                    pass

    return listprocess


def main():
    schedule.every(1).minutes.do(CreateLog)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()