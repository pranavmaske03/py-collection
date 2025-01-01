
print("Demonstration of Object Orientation : ")

class Arithematic:
    def __init__(self,value1,value2):
        self.No1 = value1
        self.No2 = value2
        
    def Addition(self):
        Ans = self.No1 + self.No2
        return Ans
    
    def Substraction(self):
        Ans = self.No1 - self.No2
        return Ans

print("Enter first number : ")
A = int(input())

print("Enter second number : ")
B = int(input())

obj = Arithematic(A,B)

Ret = obj.Addition()
print("Addition is : ",Ret)

Ret = obj.Substraction()
print("Substraction is : ",Ret)