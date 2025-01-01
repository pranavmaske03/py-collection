
class Pattern:
    def __init__(self,no1,no2):
        self.iRow = no1
        self.iCol = no2

    def DisplayPattern(self):
        i,j = 0,0

        for i in range(self.iRow):
            for j in range(i+1):
                print("*",end = "\t")
            print()
        
        for i in range(self.iRow,0,-1):          
            for j in range(i+1):
                print("*",end = "\t")
            print()

def main():
    value1 = 0
    value2 = 0

    print("Enter number of rows :")
    value1 = int(input())

    print("Enter number of columns :")
    value2 = int(input())

    obj = Pattern(value1,value2)
    obj.DisplayPattern()

if __name__ == "__main__":
    main()