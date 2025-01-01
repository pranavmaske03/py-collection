
def Addition(No1,No2):

    Ans = 0
    Ans = No1 + No2
    return Ans

def main():

    value1 = 0
    value2 = 0

    print("Enter first number :")
    value1 = int(input())

    print("Enter second number :")
    value2 = int(input())

    Result = Addition(value1,value2)
    print("Addition is : ",Result)


if __name__ == "__main__":
    main()