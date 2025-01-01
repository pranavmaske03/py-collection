import psutil

def main():
    print("------------------------------------------------------------")
    print("List of running processes are :")
    print("------------------------------------------------------------")
    
    for proc in psutil.process_iter(['pid','name','username']):
        print(proc.info)
    print("-------------------------------------------------------------")

if __name__ == "__main__":
    main()