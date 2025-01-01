import os
import sys

def DirectoryRename(Dir_name,fis_Extention,sec_Extention):
    flag = os.path.isabs(Dir_name)

    if flag == False:
        Dir_name = os.path.abspath(Dir_name)

    exist = os.path.isdir(Dir_name)

    count = 0
    if exist == True:

        for foldername,subfoldername,filename in os.walk(Dir_name):
            for name in filename:
                if name.endswith(fis_Extention):
                    file_name,old_extension = os.path.splitext(os.path.join(foldername,name))
                    new_name = file_name + sec_Extention
                    count = count + 1
                try:
                    os.rename(os.path.join(foldername,name),new_name)
                    print("File changed with name : ",new_name)
                except Exception as eobj:
                    print("Unable to change due to : ",eobj)
        print(count,"Files extention changed from "+old_extension+" To "+sec_Extention)
    else:
        print("No such directory :")


def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script is used to change the extention of the file :")
            exit()
        
        if sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Usage of script : ")
            print("Name_of_Directory   Name_of_File_Extention   Name_of_Extention_To_Replace")
            exit()
    
    if len(sys.argv) == 4:
        try:
            DirectoryRename(sys.argv[1],sys.argv[2],sys.argv[3])
        except Exception as eobj:
            print("Unable to change extention due to : ",eobj)
    
    else:
        print("Invalid option")
        print("Use --h to get help and use --u to get usage of application")
        exit()

if __name__ == "__main__":
    main()