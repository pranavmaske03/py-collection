
def CheckPallindrome(No):
    iReverse,temp,iDigit = 0,No,0

    while temp != 0:
        iDigit = temp % 10
        iReverse = (iReverse * 10) + iDigit
        temp = (int)(temp / 10)

    if iReverse == No:
        return True
    else:
        return False

def main():
    value = 0

    print("enter number :")
    value = int(input())

    bRet = CheckPallindrome(value)
    if bRet == True:
        print(value," is pallindrome number ")
    else:
        print(value," is not pallindrome number ")

if __name__ == "__main__":
    main()