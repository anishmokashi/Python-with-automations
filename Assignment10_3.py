''' Please follow below rules while designing automation script as 

   * Accept input through command line or through file.
   * Display any message in log file instead of console.
   * For separate task define separate function.
   * For robustness handle every expected exception.
   * Perform validations before taking any action.
   * create user defined modules to store the funtionality.

'''

''' 
3.Design automation script which accept two directory names .Copy all files from first directory into second directory.
  Second directory should be created at run time.

  Usage : DirectoryCopy.py "Demo" "temp" 

  Demo is name of directory which is existing and contains files in it.
  We have to create new Directory as Temp and copy all files from Demo to Temp.
'''
from sys import *
import os
import shutil
def Copy_Files(old_Dir,new_Dir):
    
    
    if os.path.exists(old_Dir):
        os.mkdir(new_Dir)
     
        for file_name in (os.listdir(old_Dir)):
            old_f_path=os.path.join(old_Dir,file_name)
            new_f_path=os.path.join(new_Dir,file_name)
            shutil.copy(old_f_path,new_f_path)
    # shutil.copytree(old_Dir,new_Dir)#istead of above lines this method can also be used
    
    
    
    


def main():
    print("----------------Moving files--------------")
    print("Application name: "+argv[0])

    if(len(argv)!=3):
        print("Error : Invalid number of arguments")
        exit()
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory and display checksum of files")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory Extentsion")
        exit()

    
    
    try:
        Copy_Files(argv[1],argv[2])
        
        

    except ValueError:
        print("Error : Invalid datatype of input")


if __name__=="__main__":
    main()