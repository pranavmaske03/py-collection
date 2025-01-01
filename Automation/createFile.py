import os

def main():
    print("Enter the name of file that ou want to create : ")
    Fname = input()

    open(Fname,"x")

    
if __name__ == "__main__":
    main()