import os

def main():
    print("Enter the file name to check in the Directory :")
    Fname = input()

    if os.path.exists(Fname):
        fobj = open(Fname,"r")

        data = fobj.read()
        print("Data from file is : ")
        print(data)
        
    else:
        print("Unable to locate file :")
        
if __name__ == "__main__":
    main()