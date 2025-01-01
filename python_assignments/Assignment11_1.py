import os
from sys import *
import hashlib

def Hashfile(path,blocksize = 1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def Directory_CheckSum(DirName):
    flag = os.path.isabs(DirName)

    if flag == False:
        DirName = os.path.abspath(DirName)
    
    exist = os.path.isdir(DirName)

    if exist == True:
        for directory,subdirs,filename in os.walk(DirName):
            for name in filename:
                path = os.path.join(directory,name)
                file_hash = Hashfile(path)
                print(path)
                print(file_hash)
    else:
        print("No such Directory")

def main():

    if len(argv) == 2:
        if argv[1] == "--h" or argv[1] == "--H":
            print("This script is used display checksum of the files :")
            exit()
        
        if argv[1] == "--u" or argv[1] == "--U":
            print("Usage of the Script")
            print("ApplicationName AbsolutePath_Of_Directory")
            exit() 
        
        try:
            Directory_CheckSum(argv[1])
        except Exception as eobj:
            print("Unable to find checksum due to : ",eobj)
    else:
        print("Invalid option")
        print("Use --h to get help and use --u to get usage of application")
        exit()

if __name__ == "__main__":
    main()