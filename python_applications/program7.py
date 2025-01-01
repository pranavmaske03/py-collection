
class DigitX:
    def __init__(self,no):
        self.No1 = no
    
    def SumDigits(self):

        if self.No1 < 0:
            self.No1 = -self.No1
            
        sum,iDigit,temp = 0,0,self.No1

        while temp != 0:
            iDigit = temp % 10
            sum = sum + iDigit
            temp = (int)(temp/10)
        
        return sum

def main():
    value = 0

    print("Enter number :")
    value = int(input())

    obj = DigitX(value)
    ret = obj.SumDigits()

    print(ret)


if __name__ == "__main__":
    main()
