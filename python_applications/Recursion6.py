
i = 1

def DisplayR(no):
    global i

    if(i <= no):
        print(i)
        i = i + 1
        DisplayR(no)
    

def main():
    no = 0

    print("Enter frequency :")
    no = int(input())

    DisplayR(no)

if __name__ == "__main__":
    main()