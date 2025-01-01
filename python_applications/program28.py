
def CheckString(strr):
    
    for char in strr:
        if(not char.isalpha()):
            return False
        elif(not char.isnumeric()):
            return False
    return True

def main():
    strr = ""   

    print("Enter string : ")
    strr = input()

    print(CheckString(strr))


if __name__ == "__main__":
    main()