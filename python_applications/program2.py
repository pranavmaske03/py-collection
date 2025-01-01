
class Arithmetic:
    
    def __init__(self,no1,no2):
        self.No1 = no1
        self.No2 = no2

    def Addition(self):
        Ans = 0
        Ans = self.No1 + self.No2 
        return Ans
    
    def Substraction(self):
        Ans = 0
        Ans = self.No1 - self.No2 
        return Ans

def main():
    value1 = 0
    value2 = 0
    ret = 0

    print("Enter first number :")
    value1 = int(input())

    print("Enter second number :")
    value2 = int(input())

    obj = Arithmetic(value1,value2)

    ret = obj.Addition()
    print("Addition is : ",ret)

    ret = obj.Substraction()
    print("Substraction is : ",ret)
    
if __name__ == "__main__":
    main()