import os

def main():
    print("Enter the file name :")
    Fname = input()

    if os.path.exists(Fname):
        print("File exist")
    else:
        print("Unable to locate file :")
        
if __name__ == "__main__":
    main()