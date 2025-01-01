import psutil

def DisplayProcess():
    print("List of running process are :")
    print("_________________________________________")
    for proc in psutil.process_iter(['pid','name','username']):
        print(proc.info)

    print("_________________________________________")

def main():
    DisplayProcess()

if __name__ == "__main__":
    main()