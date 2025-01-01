
def Factorial(No):
    iFact = 1

    for i in range(1,No+1):
        iFact = iFact * i 

    return iFact

def main():
    value = 0
    result = 0

    print("Enter number :")
    value = int(input())

    result = Factorial(value)
    print("Factorial is :",result)

if __name__ == "__main__":
    main()