from functools import reduce

Arr = list()

# CheckNum = lambda No : (No > 70 and No <= 90)
# Increment = lambda No : No + 10
# Product = lambda No1,No2 : No1 * No2

def Accept(size):
    i = 0
    no = 0

    print("Enter the elements of the list :")
    for i in range(size):
        no = int(input())
        Arr.append(no)

def CheckNum(No):
    if((No > 70 and No <= 90)):
        return True
    else:
        return False

def Increment(No):
    Ans = 0
    Ans = No + 10
    return Ans
    
def Product(no1,no2):
    return no1*no2


def main():
    size = 0

    print("Enter the number of elements :")
    size = int(input())

    Accept(size)

    FArr = list(filter(CheckNum,Arr))
    print("Data after filter activity : ",FArr)

    MArr = list(map(Increment,FArr))
    print("Data after map activity : ",MArr)

    ret = reduce(Product,MArr)
    print("Product is : ",ret)

if __name__ == "__main__":
    main()