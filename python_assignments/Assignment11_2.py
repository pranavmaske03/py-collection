import psutil
import sys
import os
import hashlib
import time

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

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        
        results = list(filter(lambda x : len(x) > 1, dups.values()))
        if len(results) > 0:           
            Arr = []
            icnt = 0
            for result in results:
                for subresult in result:
                    icnt += 1
                    if icnt >= 2:
                        Arr.append(subresult)
                icnt = 0
        create_log(Arr)
    else:
        print("Invalid path")

def create_log(Arr):
    if not os.path.exists("Log.txt"):
        fd = open('Log.txt','w')
    
    exist = os.path.exists('Log.txt')

    if exist:
        fd = open('Log.txt','w')
        separator = '-'*80
        fd.write(separator+"\n")        
        fd.write("Marvellous Process Log file to detect duplcates files \n")
        fd.write("Log file created at : "+time.ctime()+"\n")
        fd.write(separator+"\n")

        for data in Arr:
            fd.write("%s \n"%data)
        fd.write(separator+"\n")

    fd.close()


def main():

    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[0] == "--H":
            print("This script is used to create log files write duplicates files into that log file :")
            exit()
        
        if sys.argv[1] == "u" or sys.argv[1] == "--U":
            print("Usage : ApplicationName Name_of_Directory")
            exit()
        
        try:
            FindDuplicate(sys.argv[1])
            print("Creating Log file process successfully created :")
        except Exception as eobj:
            print("Unable to do task due to : ",eobj)

if __name__ == "__main__":
    main()
