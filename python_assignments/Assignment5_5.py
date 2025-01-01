
iFact = 1
i = 0

def Factorial(No):
    global iFact
    global i 

    if No < 0:
        print("Invalid Number :")
        print("NOTE : please enter positive number :")
        return -1

    for i in range(1,No+1):
        iFact = iFact * i 
    return iFact


def main():
    value = 0

    print("Enter number :")
    value = int(input())

    ret = Factorial(value)

    if ret != -1:
        print("Result is : ",ret)

if __name__ == "__main__":
    main()