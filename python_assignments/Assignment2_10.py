
def sumDigits(No):
    iDigit = 0
    sum = 0

    while(No != 0):
        iDigit = (int)(No % 10)
        sum = sum + iDigit
        No = (int)(No / 10)
    
    return sum


def main():
    value = 0
    ret = 0

    print("Enter number :")
    value = int(input())

    ret = sumDigits(value)
    print("Sum of the digits is : ",ret)


if __name__ == "__main__":
    main()