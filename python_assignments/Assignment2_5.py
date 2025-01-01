
def CheckPrime(No):
    i = 0
    Flag = False

    for i in range(2,((int)(No/2)+1)):
        if No % i == 0:
            Flag = True
            break

    return Flag

def main():
    value = 0
    result = 0
    bRet = False

    print("Enter number :")
    value = int(input())

    bRet = CheckPrime(value)

    if bRet == False:
        print("It is prime number :")
    else:
        print("It is NOT a prime number :")

if __name__ == "__main__":
    main()