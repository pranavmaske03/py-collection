
Power = lambda No : No**2

def main():
    value = 0

    print("Enter the number :")
    value = int(input())

    ret = Power(value)
    print("Result is : ",ret)

if __name__ == "__main__":
    main()