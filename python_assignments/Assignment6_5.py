import threading

def Display():
    print("Display in straight form :")
    for i in range(1,51):
        print(i)

def DisplayR():
    print("Display in reverse order : ")
    for i in range(50,0,-1):
        print(i)

def main():
   
    T1 = threading.Thread(target = Display)    
    T2 = threading.Thread(target = DisplayR)

    T1.start()
    T1.join()
    T2.start()
    T2.join()


if __name__ == "__main__":
    main()
