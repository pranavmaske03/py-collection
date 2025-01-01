
Arr = list()

def Accept(size):

    print("Enter elements of the list :")
    for i in range(size):
        no = int(input())
        Arr.append(no)

def Display():

    print("Elements of the list are : ")
    for i in range(len(Arr)):
        print(Arr[i],end="\t")
    print()

def Summation():
    Sum = 0

    for i in range(len(Arr)):
        Sum = Sum + Arr[i]
    return Sum

def main():
    size = 0
    
    print("Enter number of elements in the list : ")
    size = int(input())

    Accept(size)
    Display()
    ret = Summation()

    print("Summation is : ",ret)

if __name__ == "__main__":
    main()