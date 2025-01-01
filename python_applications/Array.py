
Arr = list()

def Accept(length):
    print("Enter the elements of the list")

    for i in range(length):
        no = int(input())
        Arr.append(no)


def Display():
    print("Elements of the array are :")

    for i in range(len(Arr)):
        print(Arr[i],end="\t")
    print()

def main():
    size = 0

    print("Enter number of elements :")
    size = int(input())

    Accept(size)
    Display()

if __name__ == "__main__":
    main()