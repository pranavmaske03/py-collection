
class NumberX:
    def __init__(self,no):
        self.No1 = no 
    
    def DisplayFactors(self):
        
        for i in range(1,(int)(self.No1/2)+1):
            if self.No1 % i == 0:
                print(i)

def main():
    value = 0

    print("Enter number : ")
    value = int(input())

    obj = NumberX(value)
    obj.DisplayFactors()


if __name__ == "__main__":
    main()