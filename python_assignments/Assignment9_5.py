import os

def main():

    count = 0

    print("Enter file name to read : ")
    Fname = input()

    if os.path.exists(Fname):
        fobj = open(Fname,"r")
        print("Enter string to search : ")
        key = input()

        data = fobj.read()

        for i in range(len(data)):
            if data[i:i+len(key)] == key:
                count = count+1

        print("Number of occuerence is : ",count)

        fobj.close()

    else:
        print("Unable to locate file")

if __name__ == "__main__":
    main()