
def CheckPrime(No):
    
    for icnt in range(2,(int)(No/2)):
        if No % icnt == 0:
            break
    
    if icnt == (int)(No/2):
        return True
    else:
        return False

def main():
    value = 0

    print("Enter number :")
    value = int(input())

    bRet = CheckPrime(value)
    if bRet == True:
        print("Given number is prime...")
    else:
        print("NOT prime number...")

if __name == "__main__":
    main()

    