
def CheckNum(No):

    if No % 5 == 0:
        return True
    else:
        return False

def main():
    value = 0
    bRet = False

    print("Enter number :")
    value = int(input())

    bRet = CheckNum(value)
    print(bRet)


if __name__ == "__main__":
    main()