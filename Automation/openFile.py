import os

def main():
    print("Enter the name of file that ou want to create : ")
    Fname = input()

    if os.path.exists(Fname):
        fobj = open(Fname,"r")
        print("File is sucessfully opened")
        print(fobj)
        
    else:
        print("Unable to open file as file in not present : ")

    
if __name__ == "__main__":
    main()