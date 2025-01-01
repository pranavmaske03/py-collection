
class NumberX:
    def __init__(self,no):
        self.No1 = no 
    
    def Factorial(self):
        Result = 1
        for i in range(1,self.No1+1):
            Result = Result * i 
        return Result
            
def main():
    value = 0

    print("Enter number : ")
    value = int(input())

    obj = NumberX(value)
    ret = obj.Factorial()

    print("Result is : ",ret)


if __name__ == "__main__":
    main()