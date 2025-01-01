
class Demo:
    value = 11

    def __init__(self,no1,no2):
        print("Inside constructor :")
        self.No1 = no1
        self.No2 = no2
    
    def Fun(self):
        print("Inside Fun :")
        print("Value of No1 : ",self.No1)
        print("Value of No2 : ",self.No2)
    
    def Gun(self):
        print("Inside Gun :")
        print("Value of No1 : ",self.No1)
        print("Value of No2 : ",self.No2)

def main():
    value1 = 0
    value2 = 0

    print("Enter first number : ")
    value1 = int(input())

    print("Enter second number :")
    value2 = int(input())

    obj = Demo(value1,value2)
    
    obj.Fun()
    obj.Gun()

if __name__ == "__main__":
    main()