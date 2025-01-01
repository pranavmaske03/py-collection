
class Pattern:
    def __init__(self,no1,no2):
        self.iRow = no1
        self.iCol = no2
    
    def DisplayPattern(self):
        i = 0
        j = 0

        for i in range(self.iRow):
            for j in range(self.iCol):
                if i == j:
                    print("#",end = '\t')
                else:
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