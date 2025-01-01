
class DigitX:
    def __init__(self,no):
        self.No = no

    def CheckDigitFrequency(self,digit):
        iDigit,count,temp = 0,0,self.No

        while temp != 0:
            iDigit = temp % 10
            if iDigit == digit:
                count += 1
            temp = (int)(temp/10)

        return count


def main():
    value = 0
    digit = 0

    print("Enter number :")
    value = int(input())

    print("Enter the digit to count his frequency in number :")
    digit = int(input())

    obj = DigitX(value)
    ret = obj.CheckDigitFrequency(digit)
    print("Count of the digit si : ",ret)

if __name__ == "__main__":
    main()