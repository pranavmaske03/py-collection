
Arr = list()

def Accept(size):
    i = 0
    no = 0

    print("Enter elements of the list :")
    for i in range(size):
        no = int(input())
        Arr.append(no)


def Display():
    i = 0

    print("Elements of the list are :")
    for i in range(len(Arr)):
        print(Arr[i], end="\t")
    print()


def Maximum():
    i = 0
    iMax = Arr[i]

    for i in range(len(Arr)):
        if(iMax < Arr[i]):
            iMax = Arr[i]
    return iMax


def main():
    size = 0

    print("Enter number elements in list :")
    size = int(input())

    Accept(size)
    Display()

    ret = Maximum()
    print("Maximum element from list is : ",ret)


if __name__ == "__main__":
    main()