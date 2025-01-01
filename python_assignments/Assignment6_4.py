import threading

def CheckCapital(string):
    print("capital alphabates of the string are :")
    for i in string:
        if i.isupper() == True:
            print(i)
    print(threading.current_thread())      


def CheckSmall(string):
    print("small alphabates of the string are : ")
    for i in string:
        if i.islower() == True:
            print(i)
    print(threading.current_thread())      


def CheckDigit(string):
    print("Digits of the string are :")
    for i in string:
        if i.isdigit() == True:
           print(i)
    print(threading.current_thread())


def main():
    
    string = ""

    print("Enter string : ")
    string = input()

    small = threading.Thread(target = CheckSmall,args = (string,))
    capital = threading.Thread(target = CheckCapital,args = (string,))
    digit = threading.Thread(target = CheckDigit,args = (string,))

    small.start()
    capital.start()
    digit.start()

if __name__ == "__main__":
    main()
