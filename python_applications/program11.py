
class NumberX:
    Num = 0

    def __init__(self,value):
        NumberX.Num = value
    
    @classmethod
    def SumFactors(cls,No1):
        sum = 0

        for i in range(1,(int)(No1/2)+1):
            if No1 % i == 0:
                sum += i 
        return sum

    @classmethod
    def CheckPerfect(cls):
        Result = 0
        Result = NumberX.SumFactors(NumberX.Num)

        if Result == NumberX.Num:
            return True
        else:
            return False


def main():
    value = 0

    print("Enter number :")
    value = int(input())

    obj = NumberX(value)

    bRet = NumberX.CheckPerfect()
    if bRet == True:
        print("Number is perfect :")
    else:
        print("Number is not perefect :")


if __name__ == "__main__":
    main()