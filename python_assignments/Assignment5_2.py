
i = 1

def Pattern(frequency):
    global i 

    if(i <= frequency):
        print(i,end="\t")
        i = i + 1
        Pattern(frequency)


def main():
    value = 0

    print("Enter frequency :")
    value = int(input())

    Pattern(value)
    print()

if __name__ == "__main__":
    main()