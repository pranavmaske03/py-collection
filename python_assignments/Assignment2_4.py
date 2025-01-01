
def sumFactor(No):
    sum = 0

    if No < 0:
        print("Invalid input :")
        return    

    for i in range(1,((int)(No/2)+1)):
        if No % i == 0:
            sum = sum + i

    return sum

def main():
    value = 0
    result = 0

    print("Enter number :")
    value = int(input())

    result = sumFactor(value)
    print("summation is :",result)

if __name__ == "__main__":
    main()