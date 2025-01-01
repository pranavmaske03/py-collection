

def DisplayPattern(iRow,iCol):
    i = 0
    j = 0

    if iRow != iCol:
        print("Invalid Input")
        return
    
    for i in range(1,iRow+1):
        for j in range(1,iCol+1):
            print(j,end="\t")
        print()
    

def main():
    value1 = 0
    value2 = 0

    print("Enter number of rows :")
    value1 = int(input())

    print("Enter number of columns :")
    value2 = int(input())

    DisplayPattern(value1,value2)


if __name__ == "__main__":
    main()