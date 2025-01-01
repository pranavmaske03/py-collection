
class Arithametic:
    def __init__(self,):
        self.value1 = 0
        self.value2 = 0
    
    def Accept(self):
        print("Enter first number :")
        self.value1 = int(input())
        self.value2 = int(input())
    
    def Addition(self):
        Ans = 0
        Ans = self.value1 + self.value2
        return Ans
    
    def Subtraction(self):
        Ans = 0
        Ans = self.value1 - self.value2
        return Ans
    
    def Multiplication(self):
        Ans = 0
        Ans = self.value1 * self.value2
        return Ans
    
    def Division(self):
        Ans = 0
        Ans = self.value1 / self.value2
        return Ans

def main():

    obj = Arithametic()
    obj.Accept()
    print("Addition is : ",obj.Addition())
    print("Substraction is : ",obj.Subtraction())
    print("Multiplication is : ",obj.Multiplication())
    print("Division is : ",obj.Division())

if __name__ == "__main__":
    main()