

def DisplayString(strr):

    for i in range(len(strr)-1,-1,-1):
        if strr[i] != 's':
            print(strr[i])

    for char in reversed(strr):
        if char != 's':
            print(char)

def main():
    strr = ""   

    print("Enter string : ")
    strr = input()

    DisplayString(strr)


if __name__ == "__main__":
    main()