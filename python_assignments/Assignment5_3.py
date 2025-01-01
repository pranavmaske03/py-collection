

def Pattern(frequency):

    if(frequency != 0):
        print(frequency,end="\t")
        frequency = frequency - 1
        Pattern(frequency)


def main():
    value = 0

    print("Enter frequency :")
    value = int(input())

    Pattern(value)
    print()

if __name__ == "__main__":
    main()