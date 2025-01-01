import os

def main():
    print("Enter the name of file that you want to open for reading purpose : ")
    Fname = input()
    
    if os.path.exists(Fname):
        fobj = open(Fname,"r")
        print("File is sucessfully opened in write mode")
        
        Data = fobj.read(7)
        print(Data)

        fobj.close()

    else:
        print("Unable to open file as file in not present : ")

    
if __name__ == "__main__":
    main()