
CheckEvenOdd = lambda no : no%2 == 0

def main(): 
    bRet = CheckEvenOdd(11)
    if(bRet == True):
        print("Even")
    else:
        print("Odd")

if __name__ == "__main__":
    main()