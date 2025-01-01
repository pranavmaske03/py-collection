import threading

Arr = list()

def Accept(size):
    i = 0
    no = 0

    print("Enter elements of the array :")
    for i in range(size):
        no = int(input())
        Arr.append(no)


def Display():
    print("Elements of the list are :")
    for i in Arr:
        print(i,end="\t")
    print()


def SumEven():
    sum  = 0

    for i in Arr:
        if i % 2 == 0:
            sum = sum + i 
    print(sum)


def SumOdd():
    sum = 0

    for i in Arr:
        if i % 2 != 0:
            sum = sum + i 
    print(sum)


def main():
    size  = 0

    print("Enter number of elements :")
    size = int(input())

    Accept(size)
    Display()

    T1 = threading.Thread(target = SumEven)    
    T2 = threading.Thread(target = SumOdd)

    T1.start()
    T2.start()


if __name__ == "__main__":
    main()
