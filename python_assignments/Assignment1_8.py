
def DisplayPattern(No):

    for i in range(No):
        print("*",end = "\t")
    print()

def main():
    value = 0

    print("Enter number :")
    value = int(input())

    DisplayPattern(value)


if __name__ == "__main__":
    main()