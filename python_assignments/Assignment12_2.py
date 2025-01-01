import psutil
import sys

def ProcessInfo(proc_name):
    print("Information of the Process is : ")
    for proc in psutil.process_iter(['pid','name','username']):
        if proc.name() == proc_name:
            print(proc.info)

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script is used to display information of the process ")
            exit()
        
        if sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Usage : ApplicationName  Name_of_Process")
            exit()

        try:
            ProcessInfo(sys.argv[1])
        except Exception as eobj:
            print("Unable to do task due to : ",eobj)

if __name__ == "__main__":
    main()