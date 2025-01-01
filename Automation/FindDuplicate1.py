from Duplicate_Module import *
 
def PrintDuplicate(dict1):
    results = filterX(CountLength,dict1)

    if len(results) > 0:
        print("Duplicates found : ")

        print("The following files are identical")

        icnt = 0
        for result in results:
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    print('\t\t%s'%subresult)
            icnt = 0
    else:
        print("No duplicate files found")


def main():
    print("--------------------------------------------")

    print("Application name : "+argv[0])

    if(len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if(argv[1] == "--h") or (argv[1] == "--H"):
        print("This script is used to traverse specific directory and display checksum of files")
        exit()
    
    if(argv[1] == "--u") or (argv[1] == "--U"):
        print("Usage : ApplicationName AbsolutePath_Of_Directory")
        exit()    

    try:
        arr = {}
        arr = FindDuplicate(argv[1])
        PrintDuplicate(arr)

    except ValueError:
        print("Error : Invalid datatype of input")
    except Exception as E:
        print("Error : Invalid input ",E)

if __name__ == "__main__":
    main()