import MarvellousNum

Arr = list()

def ListPrime(size):
    i = 0
    flag = False
    no = 0

    print("Enter the elements of the list : ")
    for i in range(size):
        no = int(input())
        bret = MarvellousNum.checkPrime(no)
        if(bret == True):
            Arr.append(no)


def Display():
    i = 0

    print("Prime elements are : ")
    for i in range(len(Arr)):
        print(Arr[i],end="\t")
    print()


def addPrime():
    Sum = 0

    for i in range(len(Arr)):
        Sum = Sum + Arr[i]
    return Sum

def main():
    size = 0

    print("Enter number of elements in list :")
    size = int(input())

    ListPrime(size)
    Display()

    ret = addPrime()
    print("Summation of the prime elements are : ",ret)


if __name__ == "__main__":
    main()