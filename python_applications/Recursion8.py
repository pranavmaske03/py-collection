
i = 1
iFact = 1

def Factorial(no):
    global i
    global iFact

    if(no >= 1):
        iFact = iFact * no 
        no = no - 1
        Factorial(no)
    return iFact
    

def main():
    no = 0

    print("Enter frequency :")
    no = int(input())

    ret = Factorial(no)
    print("Factorial is : ",ret)

if __name__ == "__main__":
    main()