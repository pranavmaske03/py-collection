
def Display(no):
    i = 0

    if(no <= 0):
        print("Invalid input")
        return 
        
    for i in range(no):
        print("Jay Ganesh...")

def main():
    value = 0
    value = int(input("Enter freqnency : "))
    Display(value)

if __name__ == "__main__":
    main()