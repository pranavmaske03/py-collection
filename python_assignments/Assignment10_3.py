import os
import sys
import shutil

def DirectoryCopy(Dir_name,newDir_name):
    nexist = os.path.isdir(newDir_name)

    if nexist == False:
        os.mkdir(newDir_name)
        print("Directory created at runtime")

    flag = os.path.isabs(Dir_name)

    if flag == False:
        Dir_name = os.path.abspath(Dir_name)

    flag = os.path.isabs(newDir_name)
    
    if flag == False:
        newDir_name = os.path.abspath(newDir_name)
    
    exist = os.path.isdir(Dir_name)
   
    count = 0
    if exist == True:
        for foldername,subfoldername,filename in os.walk(Dir_name):
            for name in filename:
                try:
                    shutil.copy(os.path.join(foldername,name),os.path.join(newDir_name,name))
                    print("File copied : ",os.path.join(newDir_name,name))
                    count = count + 1
                except Exception as eobj:
                    print("Unable to copied due to : ",eobj)
        print(count," Files copied to "+newDir_name+" Directory")

def main():

    if len(sys.argv) == 2:
        if argv[1] == "--h" or argv[1] == "--H":
            print("This script is used to copy files from one directory to another :")
            exit()
        
        if argv[1] == "--u" or argv[1] == "--U":
            print("Usage of the script : ")
            print("Name_of_Directory  Name_of_Directory")

    if len(sys.argv) == 3:
        try:
            DirectoryCopy(sys.argv[1],sys.argv[2])
        except Exception as eobj:
            print("Unable to do task due to : ",eobj)
    
    else:
        print("Invalid option")
        print("Use --h to get help and use --u to get usage of application")
        exit()

if __name__ == "__main__":
    main()