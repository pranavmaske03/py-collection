from functools import reduce

Arr = list()

def Accept(size):
    i = 0
    no = 0

    print("Enter the elements of the list :")
    for i in range(size):
        no = int(input())
        Arr.append(no)

def checkEven(No):
    if No % 2 == 0:
        return True
    else:
        return False
    
def Square(No):
    return No**2

def Summation(no1,no2):
    return no1 + no2

def main():
    size = 0

    print("Enter the number of elements :")
    size = int(input())

    Accept(size)

    FArr = list(filter(checkEven,Arr))
    print("Data after filter activity : ",FArr)

    MArr = list(map(Square,FArr))
    print("Data after map activity : ",MArr)

    ret = reduce(Summation,MArr)
    print("Additioin is : ",ret)

if __name__ == "__main__":
    main()