import os
import sys

def main():

    if (os.path.exists(sys.argv[1])) and (os.path.exists(sys.argv[2])):

        file1 = open(sys.argv[1],"r")
        file2 = open(sys.argv[2],"r")

        data1 = file1.read()
        data2 = file2.read()

        if data1 == data2:
            print("Sucess")
        else:
            print("Failure")

        file1.close()
        file2.close()
        
    else:
        print("Unable to locate file :")

if __name__ == "__main__":
    main()