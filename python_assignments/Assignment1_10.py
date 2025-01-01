
def CheckLen(str):

    length = len(str)
    return length

def main():
    name = ""
    ret = 0

    print("Enter your name :")
    name = input()

    ret = CheckLen(name)
    print("Length is : ",ret)


if __name__ == "__main__":
    main()