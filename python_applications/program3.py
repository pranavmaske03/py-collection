
class DigitX:
    
    def __init__(self,no):
        self.No1 = no
    
    def CheckDigit(self):
        iDigit = 0
        temp = self.No1
    
        while(temp != 0):
            iDigit = temp % 10
            if iDigit == 7:
                break
            temp = (int)(temp / 10)
        
        if iDigit == 7:
            return True
        else:
            return False

def main():
    value = 0

    print("Enter number : ")
    value = int(input())

    obj = DigitX(value)
    
    ret = obj.CheckDigit()
    if ret == True:
        print("7 is present...")
    else:
        print("7 is not present")


if __name__ == "__main__":
    main()