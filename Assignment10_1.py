''' Please follow below rules while designing automation script as 

   * Accept input through command line or through file.
   * Display any message in log file instead of console.
   * For separate task define separate function.
   * For robustness handle every expected exception.
   * Perform validations before taking any action.
   * create user defined modules to store the funtionality.

'''

''' 
1.Design automation script which accept directory name and file extension from user.
  Display all files with that extension.

  Usage : DirectoryFileSearch.py "Demo.txt"

  Demo is name of directory and .txt is the extension that we want to search.
'''
from sys import *
import os
def Display_all_files_from_that_directory(dir_name):
    list=[]
    #je nav aahe te split karun ghetla . list chya first position madhe jya folder la access karaycha aahe tyacha nav and second madhe kuthlya 
    # extension chi file print krychiye 
    list.append(dir_name.split(".")[0])
    list.append(dir_name.split(".")[1])

    dir_name=list[0]
    Extension_of_file=list[1]


    for folder_name,sub_foldername,file_list in os.walk(dir_name):
        print("Current folder is :"+folder_name)
        for file in file_list:
            if(file.split(".")[1]==Extension_of_file):
                
                print(file)
            
    

    
    
    


def main():
    print("----------------Displaying files which particular extension--------------")
    print("Application name: "+argv[0])

    if(len(argv)!=2):
        print("Error : Invalid number of arguments")
        exit()
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory and display checksum of files")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory Extentsion")
        exit()

    
    Display_all_files_from_that_directory(argv[1])
    # try:
        
        
        

    # except ValueError:
    #     print("Error : Invalid datatype of input")


if __name__=="__main__":
    main()