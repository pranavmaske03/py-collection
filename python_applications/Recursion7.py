
i = 1

def DisplayR(no):
    global i

    if(no != 0):
        print(no)
        no = no - 1
        DisplayR(no)
    

def main():
    no = 0

    print("Enter frequency :")
    no = int(input())

    DisplayR(no)

if __name__ == "__main__":
    main()