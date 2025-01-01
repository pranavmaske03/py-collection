import threading

def EvenFact(No):
    sum = 0

    for i in range(1,(int)(No/2)+1):
        if ((No % i) == 0):
            if (i % 2) == 0:
                sum = sum + i 
    print(sum)

def OddFact(No):
    sum = 0

    for i in range(1,(int)(No/2)+1):
        if((No % i) != 0):
            if (i % 2) != 0:
                sum = sum + i 
    print(sum) 

def main():
    value = 0

    print("Enter number : ")
    value = int(input())

    T1 = threading.Thread(target = EvenFact,args = (value,))
    T2 = threading.Thread(target = OddFact,args = (value,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main : ")

if __name__ == "__main__":
    main()