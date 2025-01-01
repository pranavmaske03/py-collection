import os

def main():
    print("Enter the name of file that you want to open for writing purpose : ")
    Fname = input()
    
    if os.path.exists(Fname):
        fobj = open(Fname,"a")
        print("File is sucessfully opened in write mode")
        
        print("Enter data that you want to write in file")
        Data = input()
        fobj.write(Data)

        fobj.close()

    else:
        print("Unable to open file as file in not present : ")

    
if __name__ == "__main__":
    main()