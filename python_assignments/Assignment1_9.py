
def DisplayEven(No):

    for i in range(1,No+1):
        if i % 2 == 0:
            print(i, end = "\t")
    print()

def main():
    value = 0

    print("Enter number :")
    value = int(input())

    DisplayEven(value)


if __name__ == "__main__":
    main()