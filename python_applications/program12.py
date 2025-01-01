
def CountDigit(Num):
    iDigit,count = 0,0

    while Num != 0:
        iDigit = Num % 10
        if iDigit == 7:
            count += 1
        Num = (int)(Num / 10)
    return count

def main():
    value = 0

    print("Enter number :")
    value = int(input())

    ret = CountDigit(value)
    print("Count of the digit is : ",ret)

if __name__ == "__main__":
    main()