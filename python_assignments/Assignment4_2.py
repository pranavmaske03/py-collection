
Mult = lambda No1,No2 : No1*No2

def main():
    value1 = 0
    value2 = 0

    print("Enter the first number :")
    value1 = int(input())

    print("Enter the second number :")
    value2 = int(input())

    ret = Mult(value1,value2)
    print("Multiplication is : ",ret)

if __name__ == "__main__":
    main()