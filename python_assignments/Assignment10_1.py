import os 
import sys

def DirectoryFileSearch(Dir_name,Extension):

    flag = os.path.isabs(Dir_name)

    if flag == False:
        Dir_name = os.path.abspath(Dir_name)
    
    exist = os.path.isdir(Dir_name)

    if exist == True:
        for foldername,subfoldername,filename in os.walk(Dir_name):
            for name in filename:
                if name.endswith(Extension):
                    print(name)
    else:
        print("No such Directory")



def main():

    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script is used to search the file with the given extension :")
            exit()
        
        if sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Usage of script : ")
            print("Name_of_Directory  Name_of_File_Extention")
            exit()

    if len(sys.argv) == 3:
        try:
            DirectoryFileSearch(sys.argv[1],sys.argv[2])
        except Exception as eobj:
            print("Unable to do task due to : ",eobj)
    
    else:
        print("Invalid option")
        print("Use --h to get help and use --u to get usage of application")
        exit()


if __name__ == "__main__":
    main()
