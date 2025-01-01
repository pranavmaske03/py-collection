
Arr = list()

def Accept(size):
    i = 0
    no = 0

    print("Enter the elements of the list :")
    for i in range(size):
        no = int(input())
        Arr.append(no)


def Display():
    i = 0

    print("Elements of the list are :")
    for i in range(len(Arr)):
        print(Arr[i],end="\t")
    print()


def CountFreq(search):
    count = 0
    i = 0

    for i in range(len(Arr)):
        if(Arr[i] == search):
            count = count + 1
    return count


def main():
    size = 0
    value = 0

    print("Enter number of elements in list : ")
    size = int(input())

    Accept(size)
    Display()

    print("Enter the number to count frequency :")
    value = int(input())

    ret = CountFreq(value)
    print("Frequency of the ",value," is : ",ret)


if __name__ == "__main__":
    main()