iCnt = 1
iFact = 1

def Factorial(No):
    global iFact
    global iCnt

    if iCnt <= No:
        iFact = iFact * iCnt
        iCnt = iCnt + 1
        Factorial(No)
    return iFact

def main():
    value = 0

    print("enter number :")
    value = int(input())

    print("Factorial is : ",Factorial(value))

if __name__ == "__main__":
    main()