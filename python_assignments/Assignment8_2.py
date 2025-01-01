
class BankAccount:
    ROI = 10.5

    def __init__(self,name,amount):
        self.Name = name
        self.Amount = amount
    
    def Deposite(self):
        value = 0
        print("Enter the amount to deposite :")
        value = int(input())
        self.Amount += value

    def Withdrow(self):
        value = 0
        print("Enter the amount to withdrow :")
        value = int(input())
        self.Amount -= value

    def CalculateIntrest(self):
        ret = 0
        ret = self.Amount * BankAccount.ROI
        return ret

    def Display(self):
        print("Name of the bank is : ",self.Name )
        print("Amount of the bank is : ",self.Amount)


def main():
    
    print("Enter the name of the bank :")
    name = input()
    print("Enter the amount in the bank : ")
    amount = int(input())

    obj1 = BankAccount(name,amount)
    obj1.Deposite()
    obj1.Withdrow()
    print("Intrest is : ",obj1.CalculateIntrest())
    obj1.Display()

if __name__ == "__main__":
    main()
