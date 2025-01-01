import Arithmetic

def main():
    value1 = 0
    value2 = 0
    result = 0

    print("Enter first number :")
    value1 = int(input())

    print("Enter second number :")
    value2 = int(input())

    result = Arithmetic.Addition(value1,value2)
    print("Addition is : ",result)

    result = Arithmetic.Subtraction(value1,value2)
    print("Substraction is : ",result)

    result = Arithmetic.Multiplication(value1,value2)
    print("Multiplications is : ",result)

    result = Arithmetic.Division(value1,value2)
    print("Division is : ",result)

if __name__ == "__main__":
    main()