import os
import sys

def main():
    
    if os.path.exists(sys.argv[1]):

        fobj = open(sys.argv[1],"r")
        data = fobj.read()
        
        aobj = open('Demo.txt',"w")
        aobj.write(data)

        fobj.close()
        aobj.close()

    else:
        print("Unable to locate file :")
        
if __name__ == "__main__":
    main()