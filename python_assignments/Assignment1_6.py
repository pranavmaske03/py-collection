
def CheckNum(No):

    if No == 0:
        print("Zero")
    elif No < 0:
        print("Negative Number")
    else:
        print("Positive Number")

def main():
    value = 0

    print("Enter number :")
    value = int(input())

    CheckNum(value)


if __name__ == "__main__":
    main()