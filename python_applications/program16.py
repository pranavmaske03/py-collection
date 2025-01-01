
def CountEven(No):
    iDigit = 0
    count = 0

    while No != 0:
        iDigit = No % 10
        if iDigit % 2 == 0:
            count += 1
        No = (int)(No / 10)
    return count

def main():
    value = 0

    print("enter number :")
    value = int(input())

    print("Count of the even digits is : ",CountEven(value))

if __name__ == "__main__":
    main()