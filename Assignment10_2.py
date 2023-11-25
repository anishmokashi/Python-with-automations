''' Please follow below rules while designing automation script as 

   * Accept input through command line or through file.
   * Display any message in log file instead of console.
   * For separate task define separate function.
   * For robustness handle every expected exception.
   * Perform validations before taking any action.
   * create user defined modules to store the funtionality.

'''

''' 
2.Design automation script which accept directory name and two file extensions from user.
  Rename all files with first file extension with the second file extension.

  Usage : DirectoryRename.py "Demo" ".txt" ".doc"

  Demo is name of directory and .txt is the extension that we want to search and rename with doc.
  After execution of this script each .txt file gets renamed as .doc.
'''
from sys import *
import os
def Rename_Files(Dir,old_extension,new_extension):
    
    for file_name in (os.listdir(Dir)):
        if file_name.endswith(old_extension):
            #check karaycha jar file apan enter kelelya extension chi asel tar if madhe jaycha
            
            old_file_path=os.path.join(Dir,file_name)
            #pahila folder name la file name extension sakat attach karaychi
            
            new_name=file_name.replace(old_extension,new_extension)
            #nantar replace method ni junya file extension la navin file extension ni replace karaycha 
            
            new_file_path=os.path.join(Dir,new_name)
            #navin replace kelela nav jodaycha directory la 
         
            os.rename(old_file_path,new_file_path)
            #os.rename(src,dest)
            #ani junya file path la navin file path ni replace karaycha

    
    
    


def main():
    print("----------------Renaming files--------------")
    print("Application name: "+argv[0])

    if(len(argv)!=4):
        print("Error : Invalid number of arguments")
        exit()
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory and display checksum of files")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory Extentsion")
        exit()

    
    
    try:
        Rename_Files(argv[1],argv[2],argv[3])
        
        

    except ValueError:
        print("Error : Invalid datatype of input")


if __name__=="__main__":
    main()