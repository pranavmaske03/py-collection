from functools import reduce

Arr = list()

def Accept(size):
    i = 0
    no = 0

    print("Enter the elements of the list :")
    for i in range(size):
        no = int(input())
        Arr.append(no)

def CheckPrime(No):
    iCnt = 0
    flag = True
    
    for iCnt in range(2,(int)(No/2)+1):
        if No % iCnt == 0:
            flag = False
    return flag

def Increment(No):
    return No * 2

def Maximum(No1,No2):
    if No1 > No2:
        return No1
    else:
        return No2

def main():
    size = 0

    print("Enter the number of elements :")
    size = int(input())

    Accept(size)

    FArr = list(filter(CheckPrime,Arr))
    print("Data after filter activity : ",FArr)

    MArr = list(map(Increment,FArr))
    print("Data after map activity : ",MArr)

    ret = reduce(Maximum,MArr)
    print("Maximum number is : ",ret)

if __name__ == "__main__":
    main()