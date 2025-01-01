
class Number:
    def __init__(self,value):
        self.No = value
    
    def CheckPrime(self):
        temp = self.No
        flag = True

        for i in range(2,temp+1):
            if temp % i == 0:
                flag = False
        return flag

    def SumFactor(self):
        temp = self.No
        sum = 0
        for i in range(1,((int)(temp/2)+1)):
            if((temp % i) == 0):
                sum += i 
        return sum

    def CheckPerfect(self):
        result = 0
        result = self.SumFactor()
        if(result == self.No):
            return True
        else:
            return False

    
    def Factors(self):
        temp = self.No
        for i in range(1,((int)(temp/2)+1)):
            if((temp % i) == 0):
                print(i)

def main():
    value = 0

    print("Enter number : ")
    value = int(input())

    obj = Number(value)
    
    bret = obj.CheckPrime()
    if(bret == True):
        print("Prime")
    else:
        print("NOT prime")
    
    bret = obj.CheckPerfect()
    if bret == True:
        print("Perfect")
    else:
        print("NOT Perfect")

    ret = obj.SumFactor()
    print("Summation of the factors is : ",ret)
    obj.Factors()

if __name__ == "__main__":
    main()