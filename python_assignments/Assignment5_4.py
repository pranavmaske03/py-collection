
def sumDigits(No):
    Sum = 0
    iDigit = 0

    if No < 0:
        print("Invalid Number :")
        print("NOTE : please enter positive number :")
        return -1

    while(No != 0):
        iDigit = No % 10
        Sum = Sum + iDigit
        No = (int)(No / 10)
    
    return Sum

def main():
    value = 0

    print("Enter number :")
    value = int(input())

    ret = sumDigits(value)

    if ret != -1:
        print("Summation is : ",ret)

if __name__ == "__main__":
    main()