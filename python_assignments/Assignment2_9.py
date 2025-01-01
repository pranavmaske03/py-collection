
def CountDigit(No):
    iDigit = 0
    count = 0

    while(No != 0):
        iDigit = (int)(No % 10)
        count = count + 1
        No = (int)(No / 10)
    
    return count


def main():
    value = 0
    ret = 0

    print("Enter number :")
    value = int(input())

    ret = CountDigit(value)
    print("Count of the digits is : ",ret)


if __name__ == "__main__":
    main()