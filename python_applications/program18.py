
class Pattern:
    def __init__(self,no1,no2):
        self.iRow = no1
        self.iCol = no2
    
    def DisplayPattern(self):
        i,j = 0,0

        for i in range(1,self.iRow+1):
            for j in range(1,self.iCol+1):
                print(i,end = "\t")
            print()

def main():
    value1 = 0
    value2 = 0

    print("enter number of rows :")
    value1 = int(input())

    print("Eter number of columns :")
    value2 = int(input())

    obj = Pattern(value1,value2)
    obj.DisplayPattern()

if __name__ == "__main__":
    main()